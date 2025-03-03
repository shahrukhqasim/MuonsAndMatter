import os.path
import time

import numpy as np
import pickle
import gzip
import torch

from lib.helpers_cuda_muons import get_sample_arb8s
from matplotlib.colors import LogNorm
if os.path.exists('/disk/users/sqasim'):
    import faster_muons_torch
    server = True
else:
    from muon_slabs import cuda_test_propagate_muons
    server = False

import tensorflow as tf
from tqdm import tqdm

def alias_setup(histogram):
    N = histogram.shape[0]
    n = histogram.shape[1]
    prob_table = np.zeros_like(histogram)
    alias_table = np.zeros(histogram.shape, np.int32)

    # Normalize probabilities and scale by n
    normalized_prob = histogram*n

    for j in range(N):
        small = []
        large = []

        # Separate bins into small and large
        for i, p in enumerate(normalized_prob[j]):
            if p < 1:
                small.append(i)
            else:
                large.append(i)

        # Distribute probabilities between small and large bins
        while small and large:
            small_bin = small.pop()
            large_bin = large.pop()

            prob_table[j][small_bin] = normalized_prob[j][small_bin]
            alias_table[j][small_bin] = large_bin

            # Adjust the large bin's probability
            normalized_prob[j][large_bin] = (normalized_prob[j][large_bin] +
                                          normalized_prob[j][small_bin] - 1)
            if normalized_prob[j][large_bin] < 1:
                small.append(large_bin)
            else:
                large.append(large_bin)

        # Fill remaining bins
        for remaining in large + small:
            prob_table[j][remaining] = 1
            alias_table[j][remaining] = remaining

    return prob_table, alias_table

# np.concatenate((a[:, np.newaxis]*1 + 0*a[np.newaxis, :], a[np.newaxis,:] + 0*a[:, np.newaxis]), axis=1)
# a[:, np.newaxis]*1 + 0*a[np.newaxis, :]
# a[np.newaxis, :]*1 + 0*a[:, np.newaxis]

def propagate_muons_with_cuda(
    muons_positions,
    muons_momenta,
    hist_2d_probability_table,
    hist_2d_alias_table,
    hist_2d_step_length_vs_mag_all_probability_table,
    hist_2d_step_length_vs_mag_all_alias_table,
    hist_step_lengths_probability_table,
    hist_step_lengths_alias_table,
    hist_2d_bin_centers_first_dim,
    hist_2d_bin_centers_second_dim,
    hist_2d_bin_widths_first_dim,
    hist_2d_bin_widths_second_dim,
    kill_at=-1,
    num_steps=100,
    seed=1234,
):

    # Convert inputs to CUDA tensors
    muons_positions_cuda = torch.from_numpy(muons_positions).float().cuda()
    muons_momenta_cuda = torch.from_numpy(muons_momenta).float().cuda()
    hist_2d_probability_table_cuda = torch.from_numpy(hist_2d_probability_table).float().cuda()
    hist_2d_alias_table_cuda = torch.from_numpy(hist_2d_alias_table).int().cuda()
    hist_2d_step_length_vs_mag_all_probability_table_cuda = torch.from_numpy(hist_2d_step_length_vs_mag_all_probability_table).float().cuda()
    hist_2d_step_length_vs_mag_all_alias_table_cuda = torch.from_numpy(hist_2d_step_length_vs_mag_all_alias_table).int().cuda()
    hist_step_lengths_probability_table_cuda = torch.from_numpy(hist_step_lengths_probability_table).float().cuda()
    hist_step_lengths_alias_table_cuda = torch.from_numpy(hist_step_lengths_alias_table).int().cuda()
    hist_2d_bin_centers_first_dim_cuda = torch.from_numpy(hist_2d_bin_centers_first_dim).float().cuda()
    hist_2d_bin_centers_second_dim_cuda = torch.from_numpy(hist_2d_bin_centers_second_dim).float().cuda()
    hist_2d_bin_widths_first_dim_cuda = torch.from_numpy(hist_2d_bin_widths_first_dim).float().cuda()
    hist_2d_bin_widths_second_dim_cuda = torch.from_numpy(hist_2d_bin_widths_second_dim).float().cuda()

    magnetic_field = torch.zeros((100,100,1000, 3), dtype=torch.float32).cuda()
    magnetic_field[:, :, :, 1] = 1.0
    magnetic_field_ranges = torch.from_numpy(np.array([-100, 100, -100, 100, -300, 300])).float().cpu()

    arb8s = get_sample_arb8s()
    print(arb8s.shape)
    0/0



    t1 = time.time()
    # Call the function
    faster_muons_torch.propagate_muons_with_alias_sampling(
        muons_positions_cuda,
        muons_momenta_cuda,
        hist_2d_probability_table_cuda,
        hist_2d_alias_table_cuda,
        hist_2d_step_length_vs_mag_all_probability_table_cuda,
        hist_2d_step_length_vs_mag_all_alias_table_cuda,
        hist_step_lengths_probability_table_cuda,
        hist_step_lengths_alias_table_cuda,
        hist_2d_bin_centers_first_dim_cuda,
        hist_2d_bin_centers_second_dim_cuda,
        hist_2d_bin_widths_first_dim_cuda,
        hist_2d_bin_widths_second_dim_cuda,
        magnetic_field,
        magnetic_field_ranges,
        kill_at,
        num_steps,
        seed
    )
    torch.cuda.synchronize()
    print("Took", time.time() - t1, "seconds for %.2e muons and %d steps." % (len(muons_positions_cuda), num_steps))

    # Convert results back to numpy arrays and return
    return muons_positions_cuda.cpu().numpy(), muons_momenta_cuda.cpu().numpy()

def main():
    # with open('plots/hists_a/hists_n.pkl', 'rb') as f:
    #     stored_hist_data = pickle.load(f)
    with gzip.open('data/multi/out/combined_histograms.pkl', 'rb') as f:
        stored_hist_data = pickle.load(f)
    energy_segmentation = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

    edges_full = stored_hist_data['edges_dpz']
    centers_full = (edges_full[:-1] + edges_full[1:]) / 2
    widths_full = edges_full[1:] - edges_full[:-1]

    hist_2d_bin_centers_first_dim = (centers_full[:, np.newaxis] * 1 + 0 * centers_full[np.newaxis, :]).flatten()
    hist_2d_bin_centers_second_dim = (centers_full[np.newaxis, :] * 1 + 0 * centers_full[:, np.newaxis]).flatten()

    hist_2d_bin_widths_first_dim = (widths_full[:, np.newaxis] * 1 + 0 * widths_full[np.newaxis, :]).flatten()
    hist_2d_bin_widths_second_dim = (widths_full[np.newaxis, :] * 1 + 0 * centers_full[:, np.newaxis]).flatten()

    hist_2d_step_length_vs_mag_all = stored_hist_data['hist_mag_x_step_length']
    hist_2d_step_length_vs_mag_all = hist_2d_step_length_vs_mag_all.reshape((19,100,100))



    # hist_2d_step_length_vs_mag_all = np.transpose(hist_2d_step_length_vs_mag_all, (0, 2, 1)).copy()

    # hist_2d_step_length_vs_mag_all = np.sum(hist_2d_step_length_vs_mag_all, axis=1)
    hist_step_lengths_all = stored_hist_data['hist_step_length']
    hist_2d_step_length_vs_mag_all = hist_2d_step_length_vs_mag_all.reshape((-1, 100))


    hist_2d_step_length_vs_mag_all = np.array(hist_2d_step_length_vs_mag_all) / np.sum(hist_2d_step_length_vs_mag_all, axis=1, keepdims=True)
    hist_2d_step_length_vs_mag_all_probability_table, hist_2d_step_length_vs_mag_all_alias_table = alias_setup(hist_2d_step_length_vs_mag_all)


    # Some bug in the binning process or in g4...
    hist_2d_all = stored_hist_data['hist_dpz_x_transverse'].reshape((-1))
    for i in range(19*100*100):
        if i%100 == 99:
            hist_2d_all[i]=0.0

    hist_2d_all = hist_2d_all.reshape((-1,100*100))

    hist_2d_all = np.array(hist_2d_all) / np.sum(hist_2d_all, axis=1, keepdims=True)
    hist_step_lengths_all = np.array(hist_step_lengths_all) / np.sum(hist_step_lengths_all, axis=1, keepdims=True)

    hist_2d_probability_table, hist_2d_alias_table = alias_setup(hist_2d_all)
    hist_step_lengths_probability_table, hist_step_lengths_alias_table = alias_setup(hist_step_lengths_all)

    momenta_all = []
    positions_all = []
    for i in tqdm(range(1)):
        muons_positions = np.array([[0,0,0]]) * np.ones((500*100000,1))
        # muons_positions = np.array([[0,0,0]]) * np.ones((1*10,1))
        muons_positions = muons_positions.astype(np.float32)

        muons_momenta = np.array([[0.,0.,170.]]) * np.ones((500*100000,1))
        # muons_momenta = np.array([[0.,0,170.]]) * np.ones((1*10,1))
        muons_momenta = muons_momenta.astype(np.float32)

        if server:
            muons_positions, muons_momenta = propagate_muons_with_cuda (
                muons_positions,
                muons_momenta,
                hist_2d_probability_table,
                hist_2d_alias_table,
                hist_2d_step_length_vs_mag_all_probability_table,
                hist_2d_step_length_vs_mag_all_alias_table,
                # hist_step_lengths_probability_table,
                # hist_step_lengths_alias_table,
                hist_step_lengths_probability_table,
                hist_step_lengths_alias_table,
                hist_2d_bin_centers_first_dim,
                hist_2d_bin_centers_second_dim,
                hist_2d_bin_widths_first_dim,
                hist_2d_bin_widths_second_dim,
                -1,
                500,
                200
            )

            momenta_all = muons_momenta
            positions_all = muons_positions

            # print("Num unique", np.unique(momenta_all.flatten()).size)
            # 0/0
        else:
            cuda_test_propagate_muons (
                muons_positions,
                muons_momenta,
                hist_2d_probability_table,
                hist_2d_alias_table,
                hist_2d_step_length_vs_mag_all_probability_table,
                hist_2d_step_length_vs_mag_all_alias_table,
                # hist_step_lengths_probability_table,
                # hist_step_lengths_alias_table,
                hist_step_lengths_probability_table,
                hist_step_lengths_alias_table,
                hist_2d_bin_centers_first_dim,
                hist_2d_bin_centers_second_dim,
                hist_2d_bin_widths_first_dim,
                hist_2d_bin_widths_second_dim,
                -1,
            )

            for m in muons_momenta:
                momenta_all.append(m*1.0)
            for m in muons_positions:
                positions_all.append(m*1.0)

        # 0/0

    # 0/0
    momenta_all = np.array(momenta_all)
    positions_all = np.array(positions_all)
    # print(momenta_all.shape)
    my_dict = {
        'px': momenta_all[:,0],
        'py': momenta_all[:,1],
        'pz': momenta_all[:,2],
        'x': positions_all[:,0],
        'y': positions_all[:,1],
        'z': positions_all[:,2]
    }


    if len(momenta_all) > 1000:
        print("Writing out now...")
        with gzip.open('data/data/cuda_muons_data.pkl', 'wb') as f:
            pickle.dump(my_dict, f)
        print("Success.")

    # plt.hist(desired_all)
    # plt.yscale('log')
    # plt.show()

if __name__ == '__main__':
    main()