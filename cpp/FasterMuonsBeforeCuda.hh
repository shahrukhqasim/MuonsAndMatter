//
// Created by Shah Rukh Qasim on 08.11.2024.
//

#ifndef MUON_SHIELD_FASTERMUONSBEFORECUDA_HH
#define MUON_SHIELD_FASTERMUONSBEFORECUDA_HH

void cuda_test_propagate_muons_k(float* muon_data_positions,
                                 float* muon_data_momenta,
                                 const float* hist_2d_probability_table,
                                 const int* hist_2d_alias_table,
                                 const float* hist_2d_step_length_vs_mag_all_probability_table,
                                 const int* hist_2d_step_length_vs_mag_all_alias_table,
                                 const float* hist_step_length_probability_table,
                                 const int* hist_step_length_alias_table,
                                 const float* hist_2d_bin_centers_first_dim,
                                 const float* hist_2d_bin_centers_second_dim,
                                 const float* hist_2d_bin_widths_first_dim,
                                 const float* hist_2d_bin_widths_second_dim,
                                 const float kill_at,
                                 const int N,
                                 const int H_2d,
                                 const int H_step_length);

#endif //MUON_SHIELD_FASTERMUONSBEFORECUDA_HH
