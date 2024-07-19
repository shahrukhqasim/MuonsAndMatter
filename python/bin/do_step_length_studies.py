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


m = 1000.

with open('data/gdetector.json', 'w') as f:
    json.dump(detector, f)

detector["step_length"] = 0.001 * m
# detector["step_length"] = -1
initialize(np.random.randint(256), np.random.randint(256), np.random.randint(256), np.random.randint(256), json.dumps(detector))

# set_field_value(1,0,0)
# set_kill_momenta(65)
kill_secondary_tracks(True)
const = False

muon_data = []

N_samples = 100

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
    # print("X", data['step_length'])
    muon_data += [data]


all_my_data = np.concatenate([m['step_length'] for m in muon_data], axis=0)


def plot_histogram(data, log_x=False, bins=50):
    if log_x:
        # Manual binning for log scale on x-axis
        min_data = np.min(data[data > 0])  # Avoid log(0)
        max_data = np.max(data)
        bins = np.logspace(np.log10(min_data), np.log10(max_data), bins)
    else:
        bins = np.linspace(np.min(data), np.max(data), bins)

    plt.hist(data, bins=bins)
    if log_x:
        plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Step Length (m)')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()

# Example usage:
plot_histogram(all_my_data, log_x=True)