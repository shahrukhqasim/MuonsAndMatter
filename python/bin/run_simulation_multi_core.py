import gzip
import json
import pickle
import time

import numpy as np
from muon_slabs import simulate_muon, initialize, collect, kill_secondary_tracks
from lib.reference_designs.params_design_8 import get_design
import multiprocessing as mp


def run_test(workload, params):
    if type(workload) is tuple:
        workload = workload[0]

    z_bias = 50
    detector = get_design(params = params,z_bias=z_bias)
    detector['limits']['minimum_kinetic_energy'] =  0.1 # GeV
    detector['limits']['max_step_length'] = 0.05 # 5 cm
    # detector['store_all'] = True
    detector = json.dumps(detector)

    initialize(np.random.randint(256), np.random.randint(256), np.random.randint(256), np.random.randint(256),
               detector)


    # set_field_value(1,0,0)
    # set_kill_momenta(65)
    kill_secondary_tracks(False)
    px,py,pz,x,y,z,charge = workload.T

    #charge = np.random.randint(2, size=len(px))
    #charge[charge == 0] = -1

    # print(px.shape, py.shape, pz.shape, charge.shape)
    zpos = -17


    muon_data = []
    for i in range(len(px)):
        simulate_muon(px[i], py[i], pz[i], int(charge[i]), x[i],y[i], zpos)
        data = collect()
        muon_data += [[data['px'][-1], data['py'][-1], data['pz'][-1],data['x'][-1], data['y'][-1], data['z'][-1]]]
    muon_data = np.asarray(muon_data)
    print(data.keys())
    return muon_data

DEF_INPUT_FILE = 'data/inputs.pkl'#'data/oliver_data_enriched.pkl'
def main(tag:str,
         cores:int = 4, 
         params = None, 
         input_file = DEF_INPUT_FILE,
         n_muons:int = 0):
    with gzip.open(input_file, 'rb') as f:
        data = pickle.load(f)
    np.random.shuffle(data)
    if 0<n_muons<=data.shape[0]:
        data = data[:n_muons]

    if isinstance(params,str):
        params_file = params
        params = []
        with open(params_file, 'r') as file:
            for line in file:
                params.append(float(line.strip()))
    if len(params)==42:
        params = np.insert(params,0,[70.0, 170.0])
        params = np.insert(params,8,[40.0, 40.0, 150.0, 150.0, 2.0, 2.0, 80.0, 80.0, 150.0, 150.0, 2.0, 2.0])


    data = data[0:cores*int(len(data) / cores)]
    
    division = int(len(data) / cores)

    # print(f"Workloads for each core: {workloads}")

    workloads = []
    for i in range(cores):
        workloads.append(data[i * division:(i + 1) * division, :])

    t1 = time.time()
    with mp.Pool(cores) as pool:
        # Use starmap to pass multiple arguments
        result = pool.starmap(run_test, [(workload,params) for workload in workloads])
    t2 = time.time()

    all_results = []

    for i, rr in enumerate(result):
        resulting_data = rr
        all_results += [resulting_data]

    print(f"Workload of {division} samples spread over {cores} cores took {t2 - t1:.2f} seconds.")
    all_results = np.concatenate(all_results, axis=0)
    with gzip.open(f'data/results_{tag}.pkl', 'wb') as f:
        pickle.dump(all_results, f)

import argparse
DEF_PARAMS = [208.0, 207.0, 281.0, 248.0, 305.0, 242.0, 72.0, 51.0, 29.0, 46.0, 10.0, 7.0, 54.0, 38.0, 46.0, 192.0, 14.0, 9.0, 10.0, 31.0, 35.0, 31.0, 51.0, 11.0, 3.0, 32.0, 54.0, 24.0, 8.0, 8.0, 22.0, 32.0, 209.0, 35.0, 8.0, 13.0, 33.0, 77.0, 85.0, 241.0, 9.0, 26.0]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, default=0)
    parser.add_argument("-c", type=int, default=45)
    parser.add_argument("-f", type=str, default=DEF_INPUT_FILE)
    parser.add_argument("-tag", type=str, default='geant4')
    parser.add_argument("-params", nargs='+', default=DEF_PARAMS)
    args = parser.parse_args()
    main(args.tag,cores = args.c,params=list(args.params),n_muons = args.n,input_file = args.f)