import json
import time

import argh
import numpy as np
from tqdm import tqdm
from lib.matplotlib_settings import *
import csv
import lib.reference_designs.params_design_9 as design_9
import lib.gigantic_sphere as sphere_design
from muon_slabs import simulate_muon, initialize, collect, set_field_value, kill_secondary_tracks
from lib.timelib import convert_seconds





def run_test(kill_secondary, num_tests, num_muons, momenta_value):
    kill_secondary_tracks(kill_secondary)

    times = []
    # Generate all muons and collect their data
    # muon_data = []
    for _ in tqdm(range(num_tests)):
        t1 = time.time()
        for _ in range(num_muons):
            # t2 = time.time()
            simulate_muon(0, 0, momenta_value, 1, 0, 0, -20)
            # print("Took ", time.time() - t2, "seconds")
            data = collect()
            # muon_data.append(data)
        times += [time.time() - t1]

    return np.array(times)

def run_test_given_momenta_values(kill_secondary, num_tests, momenta_values):
    kill_secondary_tracks(kill_secondary)

    times = []
    # Generate all muons and collect their data
    # muon_data = []
    for _ in tqdm(range(num_tests)):
        t1 = time.time()
        for momenta_value in momenta_values:
            print(momenta_value)
            simulate_muon(0, 0, momenta_value, 1, 0, 0, -20)
            data = collect()
            # muon_data.append(data)
        # print("Took ", time.time() - t1, "seconds")
        times += [time.time() - t1]

    return np.array(times)


def main(sphere=False, kill_secondary_tracks=True):
    if sphere:
        detector = sphere_design.get_design()
    else:
        detector = design_9.get_design()

    detector['limits']['minimum_kinetic_energy'] = 0.5 # GeV
    detector['limits']['max_step_length'] = 0.05 # 5 cm

    detector['limits']['minimum_kinetic_energy'] =  0.5 # GeV
    detector['limits']['max_step_length'] = 0.05 # 5 cm
    # detector['limits']['minimum_kinetic_energy'] =  -1#0.5 # GeV
    # detector['limits']['max_step_length'] = -1#0.05 # 5 cm

    file_path = 'data/momentums_positions.csv'

    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row if your CSV has headers

        my_rows = []
        for row in csv_reader:
            print(row)
            my_rows.append(row)

        px = np.array([float(row[1]) for row in my_rows])
        py = np.array([float(row[2]) for row in my_rows])
        pz = np.array([float(row[3]) for row in my_rows])

        p_mag = np.sqrt(px**2 + py**2 + pz**2)
    # Add function test

    t1 = time.time()



    # Initialize muon simulation
    initialize(0, 4, 4, 5, json.dumps(detector))

    if sphere:
        set_field_value(1,0,0)

    simulate_muon(0, 5, 0, 1, 0, 0, 0)  # The first step takes longer so we just flush it out
    print("Took", time.time() - t1, "seconds")

    # 0/0

    for i in range(10):
        simulate_muon(0, 70, 0, 1, 0, 0, 0) # The first step takes longer so we just flush it out


    load_old = False
    pickle_file = '../../data/muon_data.pkl'

    # Define the parameters
    kill_secondary = False
    num_tests = 4
    num_muons = 25
    momenta_values = range(1, 161, 10)

    # Store the means for each momenta value
    mean_times = []
    mean_times_kill_secondary = []

    for momenta in momenta_values:
        results = run_test(False, num_tests, num_muons, momenta)
        mean_time = np.mean(results) / num_muons
        mean_times.append(mean_time)

        results = run_test(True, num_tests, num_muons, momenta)
        mean_time = np.mean(results) / num_muons
        mean_times_kill_secondary.append(mean_time)

    # Plot the results
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(momenta_values, mean_times, marker='o', linestyle='-', color='b', label="Secondaries not killed")
    ax.plot(momenta_values, mean_times_kill_secondary, marker='o', linestyle='-', color='r', label="Secondaries killed")
    ax.set_yscale('log')
    ax.set_title('Mean Time Taken as a Function of Momenta [%s]'%('Sphere' if sphere else 'Muon Shield Design 9'))
    ax.set_xlabel('Momenta [GeV]')
    ax.set_ylabel('Simulation time (seconds)')
    ax.legend()

    ax.grid(which='major', linewidth=0.75, linestyle='-', color='0.75')
    plt.grid(which='minor', linewidth=0.5, linestyle=':', color='0.75')

    ax.minorticks_on()
    ax.set_ylim(0.0001, 0.1)

    # Add a text box
    additional_info = "Step limits:\nmin kinetic energy: %.2f [GeV]\nmax step size: %.2f [cm]"%(detector['limits']['minimum_kinetic_energy'], detector['limits']['max_step_length']*(1 if detector['limits']['max_step_length']<=0 else 100))  # replace with your additional information
    props = dict(boxstyle='round', facecolor='white', alpha=0.5)
    ax.text(0.45, 0.55, additional_info, transform=ax.transAxes, fontsize=12,
            verticalalignment='top', bbox=props)

    plt.savefig('plots/time_fo_momentum.pdf')
    plt.show()

    cached_strs = []
    num_tests = 3

    results_collected = []
    kill_secondary = True
    results = run_test_given_momenta_values(kill_secondary, num_tests, p_mag)
    seconds_ = np.mean(results) / len(p_mag)
    seconds_for_full = seconds_ * 10**5 * 4.5
    str = ("Same dist: kill_secondary=%d took %f seconds (%s for 10**5 * 4.5)"%(kill_secondary, seconds_, (convert_seconds(seconds_for_full))))
    cached_strs.append(str)

    results_collected = []
    kill_secondary = False
    results = run_test_given_momenta_values(kill_secondary, num_tests, p_mag)
    seconds_ = np.mean(results) / len(p_mag)
    seconds_for_full = seconds_ * 10**5 * 4.5
    str = ("Same dist: kill_secondary=%d took %f seconds (%s for 10**5 * 4.5)"%(kill_secondary, seconds_, (convert_seconds(seconds_for_full))))
    cached_strs.append(str)

    results_collected = []
    num_tests = 3
    num_muons = 40
    kill_secondary = False
    momenta_value = 70
    results = run_test(kill_secondary, num_tests, num_muons, momenta_value)
    results_collected.append((momenta_value, kill_secondary, results))


    kill_secondary = True
    momenta_value = 70
    results = run_test(kill_secondary, num_tests, num_muons, momenta_value)
    results_collected.append((momenta_value, kill_secondary, results))


    kill_secondary = False
    momenta_value = 20
    results = run_test(kill_secondary, num_tests, num_muons, momenta_value)
    results_collected.append((momenta_value, kill_secondary, results))

    kill_secondary = True
    momenta_value = 20
    results = run_test(kill_secondary, num_tests, num_muons, momenta_value)
    results_collected.append((momenta_value, kill_secondary, results))
    #
    #
    for momenta_value, kill_secondary, results in results_collected:
        seconds = np.mean(results) / num_muons
        seconds_for_full = seconds * 10**5 * 4.5

        print("Momenta=%f GeV and kill_secondary=%d took %f seconds (%s for 10**5 * 4.5)"%(momenta_value, kill_secondary, seconds, (convert_seconds(seconds_for_full))))

    for str in cached_strs:
        print(str)


if __name__ == '__main__':
    argh.dispatch_command(main)