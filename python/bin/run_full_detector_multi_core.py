import gzip
import json
import pickle
import time

import numpy as np
from muon_slabs import simulate_muon, initialize, collect, kill_secondary_tracks
from lib.reference_designs.params_design_9 import *
import multiprocessing as mp
import argh


def run_test(workload):
    z_bias = 50
    detector = get_design(z_bias=z_bias)

    initialize(np.random.randint(256), np.random.randint(256), np.random.randint(256), np.random.randint(256), 1,
               json.dumps(detector))

    # set_field_value(1,0,0)
    # set_kill_momenta(65)
    kill_secondary_tracks(False)
    mu_x = 0.012490037246296857
    std_x = 0.38902328901819816
    mu_y = -0.006776601713250063
    std_y = 0.3802085587089302
    lambda_z = 14.289589025683886
    if type(N_samples) is tuple:
        N_samples = N_samples[0]

    px = np.random.normal(mu_x, std_x, N_samples)
    py = np.random.normal(mu_y, std_y, N_samples)
    pz = np.random.exponential(lambda_z, N_samples)

    charge = np.random.randint(2, size=N_samples)
    charge[charge == 0] = -1

    # print(px.shape, py.shape, pz.shape, charge.shape)

    muon_data = []
    for i in range(N_samples):
        simulate_muon(px[i], py[i], pz[i], charge[i], np.random.normal(0, 0.05)*0, np.random.normal(0, 0.05)*0, -20)
        data = collect()
        muon_data += [data]


def worker(N_samples):
    run_test(N_samples)

def main(cores: int = 4, N_samples: int = 1000000):
    samples_per_core = N_samples // cores
    remainder = N_samples % cores
    # workloads = [samples_per_core] * cores

    # Distribute any remainder among the cores
    # for i in range(remainder):
    #     workloads[i] += 1

    print("Ignoring N samples")
    with gzip.open('data/oliver_data_enriched.pkl', 'rb') as f:
        data = pickle.load(f)

    data = data[0:cores*int(len(data) / cores)]
    division = int(len(data) / cores)

    # print(f"Workloads for each core: {workloads}")

    workloads = []
    for i in range(cores):
        workloads.append(data[i * division:(i + 1) * division, :])


    t1 = time.time()
    with mp.Pool(cores) as pool:
        # Use starmap to pass multiple arguments
        pool.map(worker, [(workload,) for workload in workloads])
    t2 = time.time()
    print(f"Workload of {N_samples} samples spread over {cores} cores took {t2 - t1:.2f} seconds.")

if __name__ == '__main__':
    argh.dispatch_command(main)