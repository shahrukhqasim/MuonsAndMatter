import gzip
import pickle
import numpy as np
# import matplotlib.pyplot as plt
from lib.matplotlib_settings import *

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
step_length_values = np.concatenate([muon['step_length'] for muon in muon_data])[:, np.newaxis]


to_save  = {
    'px': px_values,
    'py': py_values,
    'pz': pz_values,
    'px_loss': px_loss_values,
    'py_loss': py_loss_values,
    'pz_loss': pz_loss_values,
    'step_length': step_length_values,
}

# px_values = [muon['px'][0:-1] - muon['px'][1:] for muon in muon_data]
# py_values = [muon['py'][0:-1] - muon['py'][1:] for muon in muon_data]
# pz_values = [muon['pz'][0:-1] - muon['pz'][1:] for muon in muon_data]


p_mag_values = [(muon['p_mag'][0:-1]) for muon in muon_data]
p_mag_loss_values = [(muon['p_mag'][0:-1] - muon['p_mag'][1:]) for muon in muon_data]
num_muon_steps = [len(muon['p_mag']) for muon in muon_data]


p_mag_loss_combined = np.concatenate(p_mag_loss_values)
p_mag_combined = np.concatenate(p_mag_values)


p_mag_loss_percent_combined = p_mag_loss_combined / p_mag_combined
# y_bins = np.concatenate((np.linspace(0, 0.1, 101), np.linspace(0.1, 1, 10)[1:]))

# # Plotting the 2D histogram
# plt.figure(figsize=(10, 6))
# plt.hist2d(p_mag_combined, p_mag_loss_percent_combined, bins=[30, 30], cmap='Blues', norm=LogNorm())
# plt.colorbar(label='Counts')
#
# plt.xlabel('Magnitude (Mag)')
# plt.ylabel('Loss')
# plt.title('2D Histogram of Loss vs Magnitude')
#
# plt.show()


# Define the ranges
ranges = [
    (5, 10),
    (20, 25),
    (70, 75),
    (100, 105),
    (150, 155),
    (190, 195)
]

# Create subplots
fig, axes = plt.subplots(2, 3, figsize=(10, 6))
axes = [item for sublist in axes for item in sublist]


# Plot data for each range
for i, (low, high) in enumerate(ranges):
    ax = axes[i]
    mask = (p_mag_combined >= low) & (p_mag_combined <= high)
    ax.hist( p_mag_loss_percent_combined[mask], bins=30, color='r', alpha=0.7, label='')
    ax.set_yscale('log')
    ax.set_title('$%.f~$GeV < $|P|$ < $%.f~$GeV'%(low, high))
    ax.set_xlabel(r'$\frac{\delta_{\mathrm{step}}|P|}{|P|}$ [GeV]')
    ax.set_ylabel('Frequency')

# Adjust layout and show the plot
plt.tight_layout()
plt.savefig('muon_energy_losses.pdf')
plt.show()