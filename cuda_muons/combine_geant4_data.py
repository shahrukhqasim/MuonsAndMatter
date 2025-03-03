import os
import gzip
import pickle
import numpy as np
from tqdm import tqdm


def load_pickled_data(file_path):
    """Loads data from a gzipped pickle file."""
    with gzip.open(file_path, 'rb') as f:
        data = pickle.load(f)
    return data


def concatenate_results(data_list):
    """Concatenates data from multiple dictionaries."""
    concatenated_data = {
        'initial_momenta': np.concatenate([data['initial_momenta'] for data in data_list]),
        'px': np.concatenate([data['px'] for data in data_list]),
        'py': np.concatenate([data['py'] for data in data_list]),
        'pz': np.concatenate([data['pz'] for data in data_list]),
        'x': np.concatenate([data['x'] for data in data_list]),
        'y': np.concatenate([data['y'] for data in data_list]),
        'z': np.concatenate([data['z'] for data in data_list]),
        'step_length': np.concatenate([data['step_length'] for data in data_list]),
    }
    return concatenated_data


def save_combined_data(file_path, data):
    """Saves concatenated data into a gzipped pickle file."""
    with gzip.open(file_path, 'wb') as f:
        pickle.dump(data, f)


def main(folder_path):
    # Collect all .pkl files in the specified folder
    pkl_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.pkl')]

    all_data = [load_pickled_data(file) for file in tqdm(pkl_files, desc="Loading data files")]

    # Concatenate all data
    combined_data = concatenate_results(all_data)

    # Save combined data to joined.pklj
    output_file = os.path.join(folder_path, 'joined.pklj')
    save_combined_data(output_file, combined_data)
    print(f"Combined data saved to {output_file}")

# Example usage
folder_path = 'data/data_batch_3/'  # Replace with your actual folder path
main(folder_path)

