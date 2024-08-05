
import json
import numpy as np
from muon_slabs import simulate_muon, initialize, collect, kill_secondary_tracks
from lib.reference_designs.params_design_8 import get_design

def run(muons, phi, z_bias=50, return_weight = False):
    if type(muons) is tuple:
        muons = muons[0]

    detector = get_design(params = phi,z_bias=z_bias)
    
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

