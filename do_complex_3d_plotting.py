import json

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from muon_slabs import add, simulate_muon, initialize, collect, set_field_value, set_kill_momenta, kill_secondary_tracks
from magnet_params.params_design_8 import *
# from magnet_paramsX import *
import time
from tqdm import tqdm

def convert_seconds(seconds):
    if seconds < 60:
        return f"{seconds} seconds"
    elif seconds < 3600:
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return f"{minutes} minutes and {remaining_seconds} seconds"
    else:
        hours = seconds // 3600
        remaining_seconds = seconds % 3600
        minutes = remaining_seconds // 60
        remaining_seconds = remaining_seconds % 60
        return f"{hours} hours, {minutes} minutes and {remaining_seconds} seconds"


bias = 50 # meter

magnets_2 = []
for mag in magnets:
    mag['dz'] = mag['dz']/100.
    mag['z_center'] = mag['z_center']/100. + bias
    components_2 = mag['components']
    print(components_2)
    components_2 = [{'corners': (np.array(x['corners']) / 100.).tolist(),
                     'field': (x['field'][0]/mag_unit, x['field'][1]/mag_unit, x['field'][2]/mag_unit)} for x in components_2]
    mag['components'] = components_2
    mag['material'] = 'G4_Fe'
    mag['fieldX'] = 0.
    mag['fieldY'] = 0.
    mag['fieldZ'] = 0.
    magnets_2.append(mag)
magnets = magnets_2

print(json.dumps(magnets))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


detector = {
    "worldPositionX": 0, "worldPositionY": 0, "worldPositionZ": 0, "worldSizeX": 11, "worldSizeY": 11, "worldSizeZ": 50,
    'magnets': magnets
}

initialize(np.random.randint(256), np.random.randint(256), np.random.randint(256), np.random.randint(256), 1, json.dumps(detector))

# set_field_value(1,0,0)
# set_kill_momenta(65)
kill_secondary_tracks(True)

muon_data = []
for i in range(10):
    charge = np.random.randint(2)
    if charge == 0:
        charge = -1
    # momenta = np.maximum(10., np.random.normal(40.,10.))
    # momenta = -momenta
    print(charge)
    simulate_muon(0, 0, 50, charge, np.random.normal(0, 0.05), np.random.normal(0, 0.05), -10)
    data = collect()
    muon_data += [data]
#
# 0/0

with open('data/gdetector.json', 'w') as f:
    json.dump(detector, f)

for mag in magnets:
    z1 = -mag['dz']
    z2 = +mag['dz']

    for i, component in enumerate(mag['components']):
        # if i < 2:
        #     continue


        the_dat = component['corners']
        field = component['field']
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
        ax.scatter3D(corners[:, 0], corners[:, 1], corners[:, 2], color='b', s=0.04)

        # # Plot the points
        # ax.scatter(corners[:,2], corners[:,0], corners[:,1], c='r', marker='o', alpha=0.6, s=0.02)
        #
        # # Connect the points with lines to form the shape
        # for i in range(len(corners)):
        #     for j in range(i+1, len(corners)):
        #         ax.plot([corners[i,2], corners[j,2]], [corners[i,0], corners[j,0]], [corners[i,1], corners[j,1]], 'b-', alpha=0.2)
        # break

# ax.set_xlim(-300, 300)
# ax.set_ylim(-300, 300)
# ax.set_zlim(-300, 300)

colors = plt.cm.get_cmap('tab10', 10)  # Get a colormap with 10 colors
for i, data in enumerate(muon_data):
    x = data['x']
    y = data['y']
    z = data['z']
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

ax.set_xlim(-30+bias, -60+bias)
ax.set_ylim(-15, 15)
ax.set_zlim(-15, 15)

# Adjust the view angle and zoom level
# ax.view_init(elev=20., azim=30)  # Adjust elevation and azimuth
# ax.dist = 6 # Smaller values zoom in, larger values zoom out

ax.set_xlabel('Z (m)')
ax.set_ylabel('X (m)')
ax.set_zlabel('Y (m)')

plt.show()


def run_test(kill_secondary, num_tests, num_muons, momenta_value):
    kill_secondary_tracks(kill_secondary)

    times = []
    # Generate all muons and collect their data
    # muon_data = []
    for _ in tqdm(range(num_tests)):
        t1 = time.time()
        for _ in range(num_muons):
            # t2 = time.time()
            # simulate_muon(0, momenta_value, 0, 1, 0, 0, 0)
            charge = 1
            simulate_muon(0, 0, momenta_value, charge, np.random.normal(0, 0.05), np.random.normal(0, 0.05), -10)
            # print("Took ", time.time() - t2, "seconds")
            # muon_data.append(data)
        times += [time.time() - t1]

    return np.array(times)


results_collected = []
num_tests = 3
num_muons = 40
kill_secondary = False
momenta_value = 70
results = run_test(kill_secondary, num_tests, num_muons, momenta_value)
results_collected.append((momenta_value, kill_secondary, results))


kill_secondary = True
momenta_value = 70
results = run_test(kill_secondary, num_tests, num_muons, momenta_value)
results_collected.append((momenta_value, kill_secondary, results))


kill_secondary = False
momenta_value = 20
results = run_test(kill_secondary, num_tests, num_muons, momenta_value)
results_collected.append((momenta_value, kill_secondary, results))

kill_secondary = True
momenta_value = 20
results = run_test(kill_secondary, num_tests, num_muons, momenta_value)
results_collected.append((momenta_value, kill_secondary, results))
#
#
for momenta_value, kill_secondary, results in results_collected:
    seconds = np.mean(results) / num_muons
    seconds_for_full = seconds * 10**5 * 4.5

    print("Momenta=%f GeV and kill_secondary=%d took %f seconds (%s for 10**5 * 4.5)"%(momenta_value, kill_secondary, seconds, (convert_seconds(seconds_for_full))))
