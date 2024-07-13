import time

import numpy as np
import matplotlib.pyplot as plt
from muon_slabs import add, simulate_muon, initialize, collect, set_field_value, set_kill_momenta, kill_secondary_tracks
from tqdm import tqdm
import pickle



# Add function test
print(add(1,2))

# Initialize muon simulation
initialize(0, 4, 4, 5)

# set_field_value(0,0,0)
set_kill_momenta(65)
kill_secondary_tracks(True)



load_old = False
pickle_file = '../../data/muon_data.pkl'

if load_old:
    # Load old data from pickle file
    try:
        with open(pickle_file, 'rb') as f:
            muon_data = pickle.load(f)
        print("Old data loaded successfully.")
    except FileNotFoundError:
        print("No existing data found. Running new simulations...")
        load_old = False  # If file not found, proceed to run simulations
else:
    times = []
    # Generate all muons and collect their data
    muon_data = []
    for _ in tqdm(range(10)):
        t1 = time.time()
        for _ in range(100):
            simulate_muon(0, 70, 0, 1, 0, 0, 0)
            data = collect()
            muon_data.append(data)
        print("Took ", time.time() - t1, "seconds")
        times += [time.time() - t1]

    # Dump muon_data to a pickle file
    with open(pickle_file, 'wb') as f:
        pickle.dump(muon_data, f)
    print("New data generated and saved successfully.")

    print(times)

0/0
# Plot all muons in the same plot but in different colors
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

colors = plt.cm.get_cmap('tab10', 10)  # Get a colormap with 10 colors

for i, data in enumerate(muon_data):
    x = data['x']
    y = data['y']
    z = data['z']
    ax.scatter(x, y, z, s=0.3, color=colors(i), label=f'Muon {i+1}')
    print(x)
    print(y)
    print(z)

# Set labels and title
ax.set_xlabel('X Coordinate (m)')
ax.set_ylabel('Y Coordinate (m)')
ax.set_zlabel('Z Coordinate (m)')
ax.set_title('3D Scatter Plot of Muon Simulation Data')

# Add legend
# ax.legend()

# Show plot
plt.show()


# plt.hist(data['step_length'])
# plt.show()

exit()


# for i in range(len(muon_data)):


# Extract px, py, pz values using list comprehensions and convert them to numpy arrays

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


# Create subplots
# fig, axes = plt.subplots(2, 2, figsize=(8, 3))


# axes = [axes[0][0], axes[0][1], axes[1][0], axes[1][1]]

# # Plot histograms
# axes[0].hist(px_combined, bins=30, color='b', alpha=0.7)
# axes[0].set_title('Histogram of dpx values')
# axes[0].set_xlabel('dpx')
# axes[0].set_ylabel('Frequency')
# axes[0].set_yscale('log')
#
# axes[1].hist(py_combined, bins=30, color='g', alpha=0.7)
# axes[1].set_title('Histogram of dpy values')
# axes[1].set_xlabel('dpy')
# axes[1].set_ylabel('Frequency')
# axes[1].set_yscale('log')
#
# axes[2].hist(pz_combined, bins=30, color='r', alpha=0.7)
# axes[2].set_title('Histogram of dpz values')
# axes[2].set_xlabel('dpz')
# axes[2].set_ylabel('Frequency')
# axes[2].set_yscale('log')
#
#
# axes[3].hist(p_mag_combined, bins=30, color='r', alpha=0.7)
# axes[3].set_title('Histogram of dp values')
# axes[3].set_xlabel('dp')
# axes[3].set_ylabel('Frequency')
# axes[3].set_yscale('log')
#
# # Adjust layout
# plt.tight_layout()
#
# # Show plot
# plt.show()


# fig, ax = plt.subplots()
# ax.hist(p_mag_combined, bins=30, color='r', alpha=0.7, label='Starting momenta = 70 GeV\nTracked until 65 (or lower)')
# ax.set_xlabel(r'$\delta_{\mathrm{step}} |P|$ [GeV]')
# ax.set_ylabel('Freq. (arb.)')
# ax.legend()
# ax.set_yscale('log')
# plt.savefig('delta_p_dist.pdf')
# plt.show()
#
#
#
#
# # Create logarithmically spaced bins
# bins = np.logspace(np.log10(min(step_length_values_combined)), np.log10(max(step_length_values_combined)), 100)
#
# fig, ax = plt.subplots()
# ax.hist(step_length_values_combined, bins=bins, color='r', alpha=0.7)
# ax.set_xscale('log')  # Set the x-axis to log scale
# ax.set_xlabel(r'Step length (m)')
# ax.set_ylabel(r'Freq. (arb.)')
# plt.savefig('step_length_dist.pdf')
# plt.show()

# fig, ax = plt.subplots()
# ax.hist(num_muon_steps, bins=60, color='r', alpha=0.7)
# ax.set_xlabel(r'Num steps')
# ax.set_ylabel(r'Fre. (arb.)')
# plt.savefig('num_steps_dist.pdf')
# plt.show()

