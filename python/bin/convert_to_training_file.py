import gzip
import pickle
import numpy as np


pickle_file = '../../data/muon_data_energy_loss.pkl'

try:
    with gzip.open(pickle_file, 'rb') as f:
        muon_data = pickle.load(f)
    print("Old data loaded successfully.")
except FileNotFoundError:
    print("No existing data found. Running new simulations...")
    load_old = False  # If file not found, proceed to run simulations




for muon in muon_data:
    muon['p_mag'] = np.sqrt(muon['px']**2 + muon['py']**2 + muon['pz']**2)


px_values = np.concatenate([muon['px'][0:-1] for muon in muon_data])[:, np.newaxis]
py_values = np.concatenate([muon['py'][0:-1] for muon in muon_data])[:, np.newaxis]
pz_values = np.concatenate([muon['pz'][0:-1]  for muon in muon_data])[:, np.newaxis]
px_loss_values = np.concatenate([muon['px'][0:-1] - muon['px'][1:] for muon in muon_data])[:, np.newaxis]
py_loss_values = np.concatenate([muon['py'][0:-1] - muon['py'][1:] for muon in muon_data])[:, np.newaxis]
pz_loss_values = np.concatenate([muon['pz'][0:-1] - muon['pz'][1:] for muon in muon_data])[:, np.newaxis]

px_next_values = np.concatenate([muon['px'][1:] for muon in muon_data])[:, np.newaxis]
py_next_values = np.concatenate([muon['py'][1:] for muon in muon_data])[:, np.newaxis]
pz_next_values = np.concatenate([muon['pz'][1:] for muon in muon_data])[:, np.newaxis]
step_length_values = np.concatenate([muon['step_length'] for muon in muon_data])[:, np.newaxis]


to_save  = {
    'px': px_values,
    'py': py_values,
    'pz': pz_values,
    'px_next': px_next_values,
    'py_next': py_next_values,
    'pz_next': pz_next_values,
    'px_loss': px_loss_values,
    'py_loss': py_loss_values,
    'pz_loss': pz_loss_values,
    'step_length': step_length_values,
}

with gzip.open('../../data/output.pkl', 'wb') as f:
    pickle.dump(to_save, f)
