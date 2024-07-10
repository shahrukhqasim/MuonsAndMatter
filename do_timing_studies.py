import time

import numpy as np
import matplotlib.pyplot as plt
from muon_slabs import add, simulate_muon, initialize, collect, set_field_value, set_kill_momenta, kill_secondary_tracks
from tqdm import tqdm
import pickle
import csv


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
print(add(1,2))

# Initialize muon simulation
initialize(0, 4, 4, 5)

set_field_value(1,0,0)
set_kill_momenta(65)
kill_secondary_tracks(True)
for i in range(10):
    simulate_muon(0, 70, 0, 1, 0, 0, 0) # The first step takes longer so we just flush it out

def convert_seconds(seconds):
    if seconds < 60:
        return f"{seconds} seconds"
    elif seconds < 3600:
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return f"{minutes} minutes and {remaining_seconds} seconds"
    else:
        hours = seconds // 3600
        remaining_seconds = seconds % 3600
        minutes = remaining_seconds // 60
        remaining_seconds = remaining_seconds % 60
        return f"{hours} hours, {minutes} minutes and {remaining_seconds} seconds"



load_old = False
pickle_file = 'muon_data.pkl'


def run_test(kill_secondary, num_tests, num_muons, momenta_value):
    kill_secondary_tracks(kill_secondary)

    times = []
    # Generate all muons and collect their data
    # muon_data = []
    for _ in tqdm(range(num_tests)):
        t1 = time.time()
        for _ in range(num_muons):
            simulate_muon(0, momenta_value, 0, 1, 0, 0, 0)
            data = collect()
            # muon_data.append(data)
        # print("Took ", time.time() - t1, "seconds")
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
            simulate_muon(0, momenta_value, 0, 1, 0, 0, 0)
            data = collect()
            # muon_data.append(data)
        # print("Took ", time.time() - t1, "seconds")
        times += [time.time() - t1]

    return np.array(times)


num_tests = 3

results_collected = []
kill_secondary = True
results = run_test_given_momenta_values(kill_secondary, num_tests, p_mag)
seconds = np.mean(results) / len(p_mag)
seconds_for_full = seconds * 10**5 * 4.5
print("Same dist: kill_secondary=%d took %f seconds (%s for 10**5 * 4.5)"%(kill_secondary, seconds, (convert_seconds(seconds_for_full))))

num_tests = 3
num_muons = 100
# kill_secondary = False
# momenta_value = 70
# results = run_test(kill_secondary, num_tests, num_muons, momenta_value)
# results_collected.append((momenta_value, kill_secondary, results))
#
#
# kill_secondary = True
# momenta_value = 70
# results = run_test(kill_secondary, num_tests, num_muons, momenta_value)
# results_collected.append((momenta_value, kill_secondary, results))
#
#
# kill_secondary = False
# momenta_value = 20
# results = run_test(kill_secondary, num_tests, num_muons, momenta_value)
# results_collected.append((momenta_value, kill_secondary, results))
#
# kill_secondary = True
# momenta_value = 20
# results = run_test(kill_secondary, num_tests, num_muons, momenta_value)
# results_collected.append((momenta_value, kill_secondary, results))
#
#
# for momenta_value, kill_secondary, results in results_collected:
#     seconds = np.mean(results) / num_muons
#     seconds_for_full = seconds * 10**5 * 4.5
#
#     print("Momenta=%f GeV and kill_secondary=%d took %f seconds (%s for 10**5 * 4.5)"%(momenta_value, kill_secondary, seconds, (convert_seconds(seconds_for_full))))


