
import json
import numpy as np
from muon_slabs import simulate_muon, initialize, collect, kill_secondary_tracks
from lib.reference_designs.params_design_9 import *
from time import time
import gzip
import pickle
import argparse
import multiprocessing as mp


def run_test(workload,xy = 'gaussian',random_charge = True):
    if type(workload) is tuple:
        workload = workload[0]
    print('SHAPE:',workload.shape)
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
    px,py,pz = workload.T
    #px = workload[:, 0]
    #py = workload[:, 1]
    #pz = workload[:, 2]
    if random_charge:
        charge = np.random.randint(2, size=len(px))
        charge[charge == 0] = -1
    else: charge = 13*np.ones_like(px)

    # print(px.shape, py.shape, pz.shape, charge.shape)
    zpos = -17


    #muon_data = []
    start = time()
    for i in range(len(px)):
        if xy == 'gaussian':
            simulate_muon(px[i], py[i], pz[i], charge[i], np.random.normal(0, 0.005), np.random.normal(0, 0.005), zpos)
        elif xy == 'zero':
            simulate_muon(px[i], py[i], pz[i], charge[i], 0, 0, zpos)
        #data = collect()
        #muon_data += [[data['px'][-1], data['py'][-1], data['pz'][-1]]]
    end = time()

    #muon_data = np.array(muon_data)
    #return muon_data
    return end-start

def main(data,cores: int = 4,xy = 'gaussian',random_charge = True, n=0):
    if 0<n<=data.shape[0]:
        data = data[:n]

    data = data[0:cores*int(len(data) / cores)]
    
    division = int(len(data) / cores)

    # print(f"Workloads for each core: {workloads}")

    workloads = []
    for i in range(cores):
        workloads.append(data[i * division:(i + 1) * division, :])

    t1 = time()
    with mp.Pool(cores) as pool:
        # Use starmap to pass multiple arguments
        result = pool.starmap(run_test, [(workload,xy,random_charge) for workload in workloads])
    t2 = time()
    for i, rr in enumerate(result):
        elapsed_time = rr
        print(f"Worker {i+1} took {elapsed_time:.2f} seconds.")

    print(f"Workload of {division} samples spread over {cores} cores took {t2 - t1:.2f} seconds.")
    return t2 - t1

import csv

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=0)
    parser.add_argument("--c", type=int, default=45)
    parser.add_argument("--tag", type=str, default='geant4')
    parser.add_argument("--xy", type=str, default='gaussian')
    parser.add_argument("--fix_charge",dest = 'random_charge', action='store_false')
    args = parser.parse_args()
    c = min(args.n,args.c) if args.n>0 else args.c
    with gzip.open('data/oliver_data_enriched.pkl', 'rb') as f:
        data = pickle.load(f)
    np.random.shuffle(data)
    d_time = main(data,c,args.xy,args.random_charge)
    #with open(f'n_events_time_{args.tag}.csv', mode='a', newline='') as file:
    #    writer = csv.writer(file)
    #    writer.writerow([args.n, d_time])