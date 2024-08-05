
import json
import numpy as np
from muon_slabs import simulate_muon, initialize, collect, kill_secondary_tracks
from lib.ship_muon_shield import get_design_from_params

def run(muons, phi, z_bias=50, return_weight = False):
    if type(muons) is tuple:
        muons = muons[0]

    detector = get_design_from_params(params = phi,z_bias=z_bias,force_remove_magnetic_field=False)
    
    detector['limits']['minimum_kinetic_energy'] =  0.1 # GeV
    detector['limits']['max_step_length'] = 0.05 # 5 cm
    # detector['store_all'] = True
    detector = json.dumps(detector)

    output_data = initialize(np.random.randint(256), np.random.randint(256), np.random.randint(256), np.random.randint(256), detector)
    output_data = json.loads(output_data)
    print("Detector weight: %f grams or %f tonnes "%(output_data['weight_total'], output_data['weight_total'] / 1E6))

    # set_field_value(1,0,0)
    # set_kill_momenta(65)
    kill_secondary_tracks(False)
    px,py,pz,x,y,z,charge = muons.T

    muon_data = []
    for i in range(len(px)):
        simulate_muon(px[i], py[i], pz[i], int(charge[i]), x[i],y[i], z[i])
        data = collect()
        muon_data += [[data['px'][-1], data['py'][-1], data['pz'][-1],data['x'][-1], data['y'][-1], data['z'][-1]]]
    muon_data = np.asarray(muon_data)
    if return_weight: return muon_data, output_data['weight_total']
    else: return muon_data

DEF_PARAMS = [208.0, 207.0, 281.0, 248.0, 305.0, 242.0, 72.0, 51.0, 29.0, 46.0, 10.0, 7.0, 54.0, 38.0, 46.0, 192.0, 14.0, 9.0, 10.0, 31.0, 35.0, 31.0, 51.0, 11.0, 3.0, 32.0, 54.0, 24.0, 8.0, 8.0, 22.0, 32.0, 209.0, 35.0, 8.0, 13.0, 33.0, 77.0, 85.0, 241.0, 9.0, 26.0]
DEF_INPUT_FILE = 'data/inputs.pkl'#'data/oliver_data_enriched.pkl'
if __name__ == '__main__':
    import argparse
    import gzip
    import pickle
    import time
    import multiprocessing as mp
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, default=0)
    parser.add_argument("-c", type=int, default=45)
    parser.add_argument("-f", type=str, default=DEF_INPUT_FILE)
    parser.add_argument("-tag", type=str, default='geant4')
    parser.add_argument("-params", nargs='+', default=DEF_PARAMS)
    args = parser.parse_args()
    tag = args.tag
    cores = args.c
    params=list(args.params)
    n_muons = args.n
    input_file = args.f

    with gzip.open(input_file, 'rb') as f:
        data = pickle.load(f)
    np.random.shuffle(data)
    if 0<n_muons<=data.shape[0]:
        data = data[:n_muons]
        cores = min(cores,n_muons)
    data = data[0:cores*int(len(data) / cores)]
    data[:,5] = 17*np.ones_like(data[:,5]) #how to pass correctly the z data?
    division = int(len(data) / cores)

    workloads = []
    for i in range(cores):
        workloads.append(data[i * division:(i + 1) * division, :])

    t1 = time.time()
    with mp.Pool(cores) as pool:
        result = pool.starmap(run, [(workload,params,50,True) for workload in workloads])
    t2 = time.time()

    all_results = []
    for i, rr in enumerate(result):
        resulting_data,weight = rr
        all_results += [resulting_data]

    print(f"Workload of {division} samples spread over {cores} cores took {t2 - t1:.2f} seconds.")
    all_results = np.concatenate(all_results, axis=0)
    with gzip.open(f'data/results_{tag}.pkl', 'wb') as f:
        pickle.dump(all_results, f)

