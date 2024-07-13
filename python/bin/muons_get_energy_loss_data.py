import time

import numpy as np
import matplotlib.pyplot as plt
from muon_slabs import add, simulate_muon, initialize, collect, set_field_value, set_kill_momenta, kill_secondary_tracks
from tqdm import tqdm
import pickle
import gzip

def random_vector_of_magnitude_p(p, num_vectors=1):
    """
    Generate random vectors of magnitude p in random directions in 3D.

    Parameters:
    - p: Magnitude of the vectors
    - num_vectors: Number of vectors to generate (default is 1)

    Returns:
    - vectors: An array of shape (num_vectors, 3) containing the random vectors
    """
    # Generate random points on the unit sphere using spherical coordinates
    theta = np.random.uniform(0, 2 * np.pi, num_vectors)
    phi = np.arccos(1 - 2 * np.random.uniform(0, 1, num_vectors))

    # Convert spherical coordinates to Cartesian coordinates
    x = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(phi)

    # Stack the coordinates into a single array
    unit_vectors = np.stack((x, y, z), axis=-1)

    # Scale by the desired magnitude
    vectors = p * unit_vectors

    return vectors


# Add function test
print(add(1,2))
# Initialize muon simulation
initialize(0, 4, 4, 4)
kill_secondary_tracks(True)
set_kill_momenta(65) # No use here



num_sims = 200000
initial_momenta_vectors = random_vector_of_magnitude_p(1, num_sims)



load_old = False
pickle_file = '../../data/muon_data_energy_loss.pkl'

if load_old:
    # Load old data from pickle file
    try:
        with gzip.open(pickle_file, 'rb') as f:
            muon_data = pickle.load(f)
        print("Old data loaded successfully.")
    except FileNotFoundError:
        print("No existing data found. Running new simulations...")
        load_old = False  # If file not found, proceed to run simulations
else:
    # Generate all muons and collect their data
    muon_data = []
    for i in tqdm(range(num_sims)):
        p = np.random.uniform(4, 200)
        set_kill_momenta(p-1)
        simulate_muon(initial_momenta_vectors[i][0]*p, initial_momenta_vectors[i][1]*p, initial_momenta_vectors[i][2]*p, 1, 0, 0, 0)
        data = collect()
        muon_data.append(data)

    # Dump muon_data to a pickle file
    with gzip.open(pickle_file, 'wb') as f:
        pickle.dump(muon_data, f)
    print("New data generated and saved successfully.")



for muon in muon_data:
    muon['p_mag'] = np.sqrt(muon['px']**2 + muon['py']**2 + muon['pz']**2)


px_values = [muon['px'][0:-1] - muon['px'][1:] for muon in muon_data]
py_values = [muon['py'][0:-1] - muon['py'][1:] for muon in muon_data]
pz_values = [muon['pz'][0:-1] - muon['pz'][1:] for muon in muon_data]
p_mag_values = [(muon['p_mag'][0:-1] - muon['p_mag'][1:]) for muon in muon_data]
num_muon_steps = [len(muon['p_mag']) for muon in muon_data]


step_length_values = [muon['step_length'] for muon in muon_data]

# Concatenate these arrays along the appropriate axis (if needed, e.g., combining multiple lists)
px_combined = np.concatenate(px_values)
py_combined = np.concatenate(py_values)
pz_combined = np.concatenate(pz_values)
p_mag_combined = np.concatenate(p_mag_values)
step_length_values_combined = np.concatenate(step_length_values)

fig, ax = plt.subplots()
ax.hist(p_mag_combined, bins=30, color='r', alpha=0.7, label='')
ax.set_xlabel(r'$\delta_{\mathrm{step}} |P|$ [GeV]')
ax.set_ylabel('Freq. (arb.)')
ax.legend()
ax.set_yscale('log')
plt.savefig('delta_p_dist.pdf')
plt.show()