import gzip
import json

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from muon_slabs import simulate_muon, initialize, collect, kill_secondary_tracks
from lib.magnet_params.params_design_9 import *
# from magnet_paramsX import *
import time
from tqdm import tqdm
import pickle


z_bias = 50
detector = get_design(z_bias=z_bias, force_remove_magnetic_field=False)

with gzip.open('data/oliver_data_enriched_from_design_9.pkl', 'rb') as f:
# with gzip.open('data/oliver_data_enriched.pkl', 'rb') as f:
    data = pickle.load(f)

px = data[:, 0]
py = data[:, 1]
pz = data[:, 2]
pt = np.sqrt(px ** 2 + py ** 2)
p_mag = np.sqrt(px ** 2 + py ** 2 + pz ** 2)
filt = np.logical_and(pt < 1, p_mag > 15)
px = px[filt]*0
py = py[filt]*0
pz = pz[filt]*0+100



with open('data/gdetector.json', 'w') as f:
    json.dump(detector, f)

detector["max_step_length"] = 0.05
initialize(np.random.randint(256), np.random.randint(256), np.random.randint(256), np.random.randint(256), json.dumps(detector))

# set_field_value(1,0,0)
# set_kill_momenta(65)
kill_secondary_tracks(True)
const = False

muon_data = []

N_samples = 50

mu_x = 0.012490037246296857
std_x = 0.38902328901819816
mu_y = -0.006776601713250063
std_y = 0.3802085587089302
lambda_z = 14.289589025683886
if type(N_samples) is tuple:
    N_samples = N_samples[0]

# px = np.random.normal(mu_x, std_x, N_samples)
# py = np.random.normal(mu_y, std_y, N_samples)
# pz = np.random.exponential(lambda_z, N_samples)

zpos = -20

charge = np.random.randint(2, size=N_samples)
charge[charge == 0] = -1


for i in range(N_samples):
    if const:
        charge = np.random.randint(2)
        if charge == 0:
            charge = -1
        print(charge)
        simulate_muon(0, 0, 20, charge, np.random.normal(0, 0.05), np.random.normal(0, 0.05), zpos)
    else:
        simulate_muon(px[i], py[i], pz[i], charge[i], np.random.normal(0, 0.05), np.random.normal(0, 0.05), zpos)
    data = collect()
    print("X", data['step_length'])
    muon_data += [data]
#
# 0/0


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

magnets = detector['magnets']

for mag in magnets:
    z1 = -mag['dz']
    z2 = +mag['dz']

    for i, component in enumerate(mag['components']):
        the_dat = component['corners']
        field = component['field']
        col = 'purple'
        if field[0] < 0:
            col = 'red'
        elif field[0] > 0:
            col = 'red'
        elif field[1] < 0:
            col = 'green'
        elif field[1] > 0:
            col = 'green'
        elif field[2] < 0:
            col = 'blue'
        elif field[2] > 0:
            col = 'blue'
        corners = np.array(
            [
                [the_dat[0], the_dat[1], z1], [the_dat[2], the_dat[3], z1], [the_dat[4], the_dat[5], z1], [the_dat[6], the_dat[7], z1],
                [the_dat[0 + 8], the_dat[1 + 8], z2], [the_dat[2 + 8], the_dat[3 + 8], z2], [the_dat[4 + 8], the_dat[5 + 8], z2], [the_dat[6 + 8], the_dat[7 + 8], z2],
             ]
        )

        corners[:, 2] += mag['z_center']
        corners = np.array([[c[2], c[0], c[1]] for c in corners])

        # Define the 12 edges connecting the corners
        edges = [[corners[j] for j in [0, 1, 2, 3]],
                 [corners[j] for j in [4, 5, 6, 7]],
                 [corners[j] for j in [0, 1, 5, 4]],
                 [corners[j] for j in [2, 3, 7, 6]],
                 [corners[j] for j in [0, 3, 7, 4]],
                 [corners[j] for j in [1, 2, 6, 5]]]

        # # Plot the edges
        ax.add_collection3d(Poly3DCollection(edges, facecolors=col, linewidths=0.07, edgecolors='r', alpha=.25))
        #
        # # Scatter plot of the corners
        # ax.scatter3D(corners[:, 0], corners[:, 1], corners[:, 2], color='b', s=0.04)

colors = plt.cm.get_cmap('tab10', 10)  # Get a colormap with 10 colors
for i, data in enumerate(muon_data):
    x = data['x']
    y = data['y']
    z = data['z']
    print(len(x))
    # Check if the number of items is more than 20
    if len(x) > 20:
        # Calculate the step size for downsampling
        step = len(x) // 20
        # Select elements at regular intervals
        x = x[::step][:20]
        y = y[::step][:20]
        z = z[::step][:20]

    # print(data)

    ax.plot(z, x, y, color=colors(i), label=f'Muon {i + 1}')

ax.set_xlim(-30+z_bias, -70+z_bias)
ax.set_ylim(-20, 20)
ax.set_zlim(-20, 20)

# Adjust the view angle and zoom level
# ax.view_init(elev=20., azim=30)  # Adjust elevation and azimuth
# ax.dist = 6 # Smaller values zoom in, larger values zoom out

ax.set_xlabel('Z (m)')
ax.set_ylabel('X (m)')
ax.set_zlabel('Y (m)')

fig.tight_layout()
plt.show()

