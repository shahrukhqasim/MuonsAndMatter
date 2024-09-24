
import numpy as np
import os
from run_simulation import run, split_array
import sys
PROJECTS_DIR = os.getenv('PROJECTS_DIR')
sys.path.insert(1, os.path.join(PROJECTS_DIR,'BlackBoxOptimization/src'))
from problems import ShipMuonShieldCluster

def extract_number_from_string(s):
    number_str = ''
    for char in s:
        if char.isdigit(): 
            number_str += char
    return int(number_str)

def run(phi,inputs_dir:str,outputs_dir:str, cores:int = 384,sensitive_film_params = 57, input_dist:float=0.045,z_bias = 50, seed = 1):
    SHIP = ShipMuonShieldCluster(cores = cores,
                 loss_with_weight = False,
                 manager_ip='34.65.198.159',
                 port=444,
                 seed = seed)
    n_muons_total = 0
    n_hits_total = 0
    all_results = {}
    for name in os.listdir():
        print('FILE:', name)
        with gzip.open(os.path.join(inputs_dir,name), 'rb') as f:
            factor = pickle.load(f)[:,-1]
        SHIP.n_samples = factor.shape[0]
        n_muons = factor.sum()
        n_muons_total += n_muons
        n_hits = SHIP(phi)
        n_hits_total += n_hits
        all_results[extract_number_from_string(name)] = (n_muons,n_hits)
        with gzip.open(os.path.join(outputs_dir,f'num_muons_hits.pkl'), "wb") as f:
            pickle.dump(all_results, f)
        print('N MUONS: ', n_muons)
        print('N_HITS: ', n_hits)
    return n_muons_total,n_hits_total


INPUTS_DIR = '/home/hep/lprate/projects/MuonsAndMatter/data/full_sample'
if __name__ == '__main__':
    import argparse
    import gzip
    import pickle
    import time
    import multiprocessing as mp
    from lib.reference_designs.params import sc_v6
    parser = argparse.ArgumentParser()
    parser.add_argument("--c", type=int, default=45)
    parser.add_argument("-seed", type=int, default=None)
    parser.add_argument("-input_dir", type=str, default=INPUTS_DIR)
    parser.add_argument("--p","-params", type='str', default=sc_v6)
    parser.add_argument("--z", type=float, default=None)
    parser.add_argument("--sens_plane", type=float, default=57)
    parser.add_argument("-full_sample", action = 'store_true')
    parser.add_argument("-concatenate", action = 'store_true')
    args = parser.parse_args()
    
    if isinstance(args.params,str):
        with open(args.params, 'r') as file:
            params = []
            for line in file:
                number = float(line.strip())
                params.append(number)
    
    z_bias = 50
    input_dist = args.z
    sensitive_film_params = {'dz': 0.01, 'dx': 6, 'dy': 10, 'position':args.sens_plane}


    
    t1 = time.time()
    n_muons,n_hits = run(params,args.inputs_dir,args.outputs_dir, 
        cores = args.c,sensitive_film_params = sensitive_film_params,
        seed = args.seed, input_dist=args.z,z_bias = z_bias)
    t2 = time.time()
    print(f'INPUT MUONS: {n_muons}')
    print(f'TOTAL TIME: {(t2-t1):.3f}')
    print(f'HITS: {n_hits}')
    print(f'Muons survival rate:: {n_hits/n_muons}')