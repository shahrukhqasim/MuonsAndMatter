import gzip
import json

import numpy as np
import matplotlib.pyplot as plt
 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from muon_slabs import simulate_muon, initialize, collect, kill_secondary_tracks, collect_from_sensitive
from lib.reference_designs.params_design_9 import get_design as get_design_9
from lib.reference_designs.params_design_8 import get_design as get_design_8
from lib.reference_designs.params_design_8_ref import get_design as get_design_8_ref
from lib.reference_designs.params import *
# from magnet_paramsX import *
import time
from lib.ship_muon_shield import get_design_from_params
from tqdm import tqdm
import pickle
import argh
from plot_magnet import plot_magnet
from copy import deepcopy

def main(design = 100, output_file='plots/detector_visualization.png', params=None,
          sensitive_film_position:float = 57, fSC_mag:bool = True):
    design = int(design)
    assert design in {100, 9, 8}

    z_bias = 50
    if design == 100:
        if params is None:
            params = sc_v6
        elif isinstance(params,str):
            with open(params, 'r') as file:
                params = []
                for line in file:
                    number = float(line.strip())
                    params.append(number)
            
        if len(params)==42: #shield might have 14 fixed parameters
            params = np.insert(params,0,[70.0, 170.0])
            params = np.insert(params,8,[40.0, 40.0, 150.0, 150.0, 2.0, 2.0, 80.0, 80.0, 150.0, 150.0, 2.0, 2.0])
    

        detector = get_design_from_params(params, z_bias=z_bias, force_remove_magnetic_field=False, fSC_mag=fSC_mag)
    elif design == 9:
        detector = get_design_9(z_bias=z_bias, force_remove_magnetic_field=False)
    elif design == 8:
        # Design 8 is built directly from the parameters and using similar code, shield optimizations can be performed
        detector = get_design_8(z_bias=z_bias, force_remove_magnetic_field=False)

    # with gzip.open('data/oliver_data_enriched_from_design_9.pkl', 'rb') as f:
    with gzip.open('data/inputs.pkl', 'rb') as f:
        data = pickle.load(f)
    px = data[:, 0]
    py = data[:, 1]
    pz = data[:, 2]
    #z = data[:, 5]
    #z += 25

    with open('data/gdetector.json', 'w') as f:
        json.dump(detector, f)

    detector['limits']["max_step_length"] = 0.05 # meter
    detector['limits']["minimum_kinetic_energy"] = 0.1 # GeV
    detector["store_primary"] = True # If you place a sensitive film, you can also set this to False because you can
                                     # get all the hits at the sensitive film.
    detector["store_all"] = False

    sensitive_film_params:dict = {'dz': 0.01, 'dx': 10, 'dy': 15, 'position':sensitive_film_position}
    for k,v in sensitive_film_params.items():
        if k=='position': detector['sensitive_film']['z_center'] += v
        else: detector['sensitive_film'][k] = v

    # detector["store_all"] = True
    output_data = initialize(np.random.randint(256), np.random.randint(256), np.random.randint(256), np.random.randint(256), json.dumps(detector))
    output_data = json.loads(output_data)
    print("Detector weight: %f kilograms or %f tonnes "%(output_data['weight_total'], output_data['weight_total'] / 1E3))


    # set_field_value(1,0,0)
    # set_kill_momenta(65)
    kill_secondary_tracks(True)
    const = False

    muon_data = []
    muon_data_sensitive = []

    N_samples = 50

    mu_x = 0.012490037246296857
    std_x = 0.38902328901819816
    mu_y = -0.006776601713250063
    std_y = 0.3802085587089302
    lambda_z = 14.289589025683886
    if type(N_samples) is tuple:
        N_samples = N_samples[0]

    zpos = 0.045
    zpos = detector['magnets'][0]['z_center'] - detector['magnets'][0]['dz'] - zpos
    
    charge = np.random.randint(2, size=N_samples)
    charge[charge == 0] = -1

    def simulate_muon_(muon_data, muon_data_sensitive, *args):
        simulate_muon(*args)
        data = collect()
        if muon_data_sensitive is not None:
            data_sensitive = collect_from_sensitive()
            muon_data_sensitive += [data_sensitive]
        muon_data += [data]
    simulate_muon_(muon_data, muon_data_sensitive, 0, 0, 100, 1, 0, 0, zpos)
    simulate_muon_(muon_data, muon_data_sensitive,  0, 0, np.max(pz), 1, np.random.normal(0, 0.4), np.random.normal(0, 0.4), zpos)
    simulate_muon_(muon_data, muon_data_sensitive, np.max(py), np.max(py), pz[np.argmax(px)], 1, np.random.normal(0, 0.4), np.random.normal(0, 0.4), zpos)

    dz = 0
    for n,i in enumerate(detector['magnets']):
        #print('components', i['components'])
        print('Magnet ', n)
        try:
            print('DX = ', i['dx'])
            print('DY = ', i['dy'])
        except: pass
        print('DZ = ', i['dz']*2)
        print('Z center = ', i['z_center'])
        print('Z in ', [i['z_center']-i['dz'],i['z_center']+i['dz']])
        dz+=i['dz']*2
    print('Total Magnets Length:', dz)
    print('Total Magnets Length real:', detector['magnets'][-1]['z_center']+detector['magnets'][-1]['dz'] - (detector['magnets'][0]['z_center']-detector['magnets'][0]['dz']))
    plot_magnet(detector, output_file,
                muon_data, z_bias,sensitive_film_position)
    return output_data['weight_total']


if __name__ == '__main__':
    from multiprocessing import Pool
    from matplotlib.animation import FuncAnimation
    import os
    def GetBounds(zGap:float = 1.):
        magnet_lengths = [(170 + zGap, 300 + zGap)] * 6  
        dX_bounds = [(10, 100)] * 2
        dY_bounds = [(20, 200)] * 2 
        gap_bounds = [(2, 70)] * 2 
        bounds = magnet_lengths + 6*(dX_bounds + dY_bounds + gap_bounds)
        return np.array(bounds).T
    num_frames = 10
    SC_mag = False
    
    min_bound,max_bound = GetBounds()
    relevant_parameters = range(len(sc_v6))
    for p in relevant_parameters:
        out_dir = f'plots/params/param_{p}'
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        weight = []
        phi_range = np.linspace(min_bound[p],max_bound[p],num_frames)
        for phi in phi_range:
            params = deepcopy(baseline)#sc_v6)
            params[p] = phi
            name = os.path.join(out_dir,f'param_{p}_{phi:.0f}.png')
            with Pool(1) as pool:
                w= pool.starmap(main, [(100, name, params,3, SC_mag)])
            weight.append(w)
            #main(output_file=f'plots/params/param_{p}_{phi}.png', params=params, sensitive_film_position= 3)
        plt.plot(phi_range,weight)
        plt.xlabel(f'Param {p}')
        plt.ylabel('Weight [kg]')
        plt.grid()
        plt.savefig(os.path.join(out_dir,f'weight_{p}'))
        plt.close()
        def update(frame):
            ax.clear()  # Clear the previous frame
            phi = phi_range[frame]
            img = plt.imread(os.path.join(out_dir,f'param_{p}_{phi:.0f}.png'))  # Read the current frame
            ax.imshow(img, aspect='auto')
            ax.axis('off')  # Hide axes
        fig, ax = plt.subplots()
        fig.tight_layout()
        ani = FuncAnimation(fig, update, frames=num_frames, repeat=True)
        ani.save(os.path.join(out_dir,f'animation_{p}.gif'), writer='pillow', fps=20)

    main(params=sc_v6,sensitive_film_position=5)#argh.dispatch_command(main)

