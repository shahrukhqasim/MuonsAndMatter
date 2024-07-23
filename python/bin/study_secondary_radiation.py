import gzip
import json
import pickle
import numpy as np
from matplotlib.colors import LogNorm
from muon_slabs import simulate_muon, initialize, collect, kill_secondary_tracks
from numba import jit
from numba.typed import List, Dict
from tqdm import tqdm
from lib.reference_designs.params_design_9 import get_design
import matplotlib.pyplot as plt
import time
from lib.matplotlib_settings import *
import multiprocessing as mp
import argh

@jit(nopython=True)
def find_unique_indices_last(track_id)->Dict[int, int]:
    result = Dict()
    for i in range(len(track_id)):
        result[track_id[i]] = i

    return result


def run_test(workload):
    if type(workload) is tuple:
        workload = workload[0]

    z_bias = 50
    detector = get_design(z_bias=z_bias)
    detector['limits']['minimum_kinetic_energy'] =  0.1 # GeV
    detector['limits']['max_step_length'] = 0.05 # 5 cm
    detector['store_all'] = False
    detector = json.dumps(detector)


    initialize(np.random.randint(256), np.random.randint(256), np.random.randint(256), np.random.randint(256),
               detector)

    px = workload[:, 0]
    py = workload[:, 1]
    pz = workload[:, 2]
    zpos = -17

    charge = np.random.randint(2, size=len(px))

    result_px = []
    result_py = []
    result_pz = []
    result_z = []
    for i in tqdm(range(len(px))):
        simulate_muon(px[i], py[i], pz[i], charge[i], np.random.normal(0, 0.005), np.random.normal(0, 0.005), zpos)
        new_data = collect()

        indices = find_unique_indices_last(new_data['track_id'])
        # 0/0
        for k,v in indices.items():
            # print(new_data['px'].shape, v)
            result_px += [new_data['px'][v]]
            result_py += [new_data['py'][v]]
            result_pz += [new_data['pz'][v]]
            result_z += [new_data['z'][v]]

        # new_data is a dict, containing numpy arrays. The keys are as follows, px, py, pz, x, y, z, trackId
        # can  you finish the code so all px, py, pz, x, y, z are selected but for unique values of trackId such that


    result_px = np.array(result_px)
    result_py = np.array(result_py)
    result_pz = np.array(result_pz)
    result_z = np.array(result_z)


    return result_px, result_py, result_pz, result_z


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
    # data = data[0:4000]
    data = data[0:cores*int(len(data) / cores)]
    division = int(len(data) / cores)
    # data = data[0:10000]

    workloads = []
    for i in range(cores):
        workloads.append(data[i * division:(i + 1) * division, :])


    t1 = time.time()
    with mp.Pool(cores) as pool:
        # Use starmap to pass multiple arguments
        result = pool.map(worker, [(workload,) for workload in workloads])
    t2 = time.time()

    result_px = []
    result_py = []
    result_pz = []
    result_z = []

    for i, rr in enumerate(result):
        elapsed_time, resulting_data = rr
        px, py, pz, z = resulting_data
        result_px += [px]
        result_py += [py]
        result_pz += [pz]
        result_z += [z]

        # all_results += [resulting_data]
        print(f"Worker {i+1} took {elapsed_time:.2f} seconds.")

    result_px = np.concatenate(result_px, axis=0)
    result_py = np.concatenate(result_py, axis=0)
    result_pz = np.concatenate(result_pz, axis=0)

    # Calculating the magnitude
    p_mag = np.sqrt(result_px**2 + result_py**2 + result_pz**2)
    pt = np.sqrt(result_px**2 + result_py**2)

    filt = p_mag > 1
    p_mag = p_mag[filt]
    pt = pt[filt]

    # Create a 2D histogram
    plt.figure(figsize=(10, 7))
    plt.hist2d(p_mag, pt, bins=50, cmap='viridis', norm=LogNorm())

    # Add color bar
    plt.colorbar(label='Counts')

    # Add labels and title
    plt.xlabel('$|P|$ [GeV]')
    plt.ylabel('$P_t$ [GeV]')
    plt.title('2D Histogram of Magnitude vs Transverse Momentum')
    plt.savefig('plots/secondary_radiation.png')

    # Show plot
    plt.show()


if __name__ == '__main__':
    a = np.array([0,0,0,1,1,1,2,2,2,2,1,2,4,4,2])
    print(find_unique_indices_last(a))
    argh.dispatch_command(main)