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
    if type(workload) is tuple:
        workload = workload[0]

    z_bias = 50
    detector = get_design(z_bias=z_bias)
    detector['limits']['minimum_kinetic_energy'] =  0.1 # GeV
    detector['limits']['max_step_length'] = 0.05 # 5 cm
    # detector['store_all'] = True
    detector = json.dumps(detector)


    initialize(np.random.randint(256), np.random.randint(256), np.random.randint(256), np.random.randint(256),
               detector)


    # set_field_value(1,0,0)
    # set_kill_momenta(65)
    kill_secondary_tracks(False)
    px = workload[:, 0]
    py = workload[:, 1]
    pz = workload[:, 2]

    charge = np.random.randint(2, size=len(px))
    charge[charge == 0] = -1

    # print(px.shape, py.shape, pz.shape, charge.shape)
    zpos = -17


    muon_data = []
    for i in range(len(px)):
        simulate_muon(px[i], py[i], pz[i], charge[i], np.random.normal(0, 0.005), np.random.normal(0, 0.005), zpos)
        data = collect()
        muon_data += [[data['px'][-1], data['py'][-1], data['pz'][-1]]]

    muon_data = np.array(muon_data)
    return muon_data


def worker(N_samples):
    start_time = time.time()
    resulting_data = run_test(N_samples)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, resulting_data


def main(cores: int = 4):
    with gzip.open('data/oliver_data_enriched.pkl', 'rb') as f:
        data = pickle.load(f)

    np.random.shuffle(data)

    division = int(len(data) / (cores-1)) #cores-1 so it does not throw away some samples
    workloads = []
    for i in range(cores-1):
        workloads.append(data[i * division:(i + 1) * division, :])
    workloads.append(data[(i + 1) * division:, :])

    t1 = time.time()
    with mp.Pool(cores) as pool:
        # Use starmap to pass multiple arguments
        result = pool.map(worker, [(workload,) for workload in workloads])
    t2 = time.time()

    all_results = []

    for i, rr in enumerate(result):
        elapsed_time, resulting_data = rr
        all_results += [resulting_data]
        print(f"Worker {i+1} took {elapsed_time:.2f} seconds.")

    print(f"Workload of {division} samples spread over {cores} cores took {t2 - t1:.2f} seconds.")
    all_results = np.concatenate(all_results, axis=0)
    print(all_results.shape)
    with gzip.open('data/oliver_data_enriched_from_design_9.pkl', 'wb') as f:
        pickle.dump(all_results, f)

if __name__ == '__main__':
    argh.dispatch_command(main)