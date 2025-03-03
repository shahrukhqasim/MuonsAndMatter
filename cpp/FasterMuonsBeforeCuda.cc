//
// Created by Shah Rukh Qasim on 08.11.2024.
//

#include "FasterMuonsBeforeCuda.hh"
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <random>


int get_first_bin(int num) {
    if (num < 10 || num > 200) {
        // If the number is out of the range 10-200, return -1 as an indicator
        return -1;
    }

    // Calculate the range index
    int index = (num - 10) / 10;

    return index;
}

// Helper function to compute the dot product of two vectors
float dotProduct(const float a[3], const float b[3]) {
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
}

// Helper function to compute the cross product of two vectors
void crossProduct(const float a[3], const float b[3], float result[3]) {
    result[0] = a[1] * b[2] - a[2] * b[1];
    result[1] = a[2] * b[0] - a[0] * b[2];
    result[2] = a[0] * b[1] - a[1] * b[0];
}

// Helper function to compute the norm of a vector
float norm(const float v[3]) {
    return sqrt(dotProduct(v, v));
}

// Helper function to normalize a vector
void normalize(const float v[3], float result[3]) {
    float v_norm = norm(v);
//     if (v_norm == 0) {
//         printf("Error: Vector cannot be zero vector.\n");
//         return; // Or handle as desired in CUDA (e.g., return default unit vector)
//     }
    result[0] = v[0] / v_norm;
    result[1] = v[1] / v_norm;
    result[2] = v[2] / v_norm;
}

// Function to rotate a vector delta_P to align with the direction of P
void rotateVector(const float P_unit[3], const float delta_P[3], const float P[3], float P_new[3]) {
    // Define the z-axis unit vector
    float z_axis[3] = {0, 0, 1};

    // Calculate the rotation axis (cross product of z-axis and P_unit)
    float rotation_axis[3];
    crossProduct(z_axis, P_unit, rotation_axis);
    float rotation_axis_norm = norm(rotation_axis);

     // Check if rotation is needed
     if (rotation_axis_norm == 0) {
         // P is aligned with z-axis; no rotation is needed
         P_new[0] = P[0] + delta_P[0];
         P_new[1] = P[1] + delta_P[1];
         P_new[2] = P[2] + delta_P[2];
         return;
     }

    // Normalize the rotation axis
    normalize(rotation_axis, rotation_axis);

    // Calculate the rotation angle
    float cos_theta = dotProduct(z_axis, P_unit);
    float theta = acos(cos_theta);

    // Construct the rotation matrix using Rodrigues' rotation formula
    float K[3][3] = {
            {0, -rotation_axis[2], rotation_axis[1]},
            {rotation_axis[2], 0, -rotation_axis[0]},
            {-rotation_axis[1], rotation_axis[0], 0}
    };

    float R[3][3];
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            R[i][j] = (i == j ? 1 : 0) +
                      sin(theta) * K[i][j] +
                      (1 - cos_theta) * (K[i][0] * K[0][j] + K[i][1] * K[1][j] + K[i][2] * K[2][j]);
        }
    }

    // Rotate delta_P using the rotation matrix
    float delta_P_rotated[3] = {
            R[0][0] * delta_P[0] + R[0][1] * delta_P[1] + R[0][2] * delta_P[2],
            R[1][0] * delta_P[0] + R[1][1] * delta_P[1] + R[1][2] * delta_P[2],
            R[2][0] * delta_P[0] + R[2][1] * delta_P[1] + R[2][2] * delta_P[2]
    };


    // Update P by adding the rotated delta_P to get the new position
    P_new[0] = P[0] + delta_P_rotated[0];
    P_new[1] = P[1] + delta_P_rotated[1];
    P_new[2] = P[2] + delta_P_rotated[2];
}

int get_fancy_log_bin(float num) {
    // Check if the number is within the expected range
    if (num < -22.0f || num > 0.0f) {
        // If the number is out of range, return -1 as an indicator
        return -1;
    }

    // Calculate the bin index for a uniform distribution from -22 to 0 in 100 bins
    int index = static_cast<int>((num + 22.0f) / 0.22f);

    // Ensure the index is within the range [0, 99]
    if (index < 0) index = 0;
    else if (index > 99) index = 99;

    return index;
}



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
                               const int H_step_length) {
    // Set up random number generation with C++11 <random> library
    std::random_device rd;  // Obtain a random seed from the hardware
    std::mt19937 gen(rd()); // Seed the generator with the random device

    // Define the range for uniform real distribution [0.0, 1.0]
    std::uniform_real_distribution<float> dist_float(0.0f, 1.0f);

    // Define a function to generate random integers from 0 to N-1
    auto get_random_int = [&gen](int N) {
        std::uniform_int_distribution<int> dist_int(0, N - 1);
        return dist_int(gen);
    };

    for (int idx = 0; idx < N; idx++) {
//        std::cout<<"I: "<< idx<<std::endl;
        int offset = idx * 3;
        float delta_P[3] = {0,0,-1};
        float output[3] = {0, 0, 0};

        float *muon_data_momenta_this = muon_data_momenta + offset;
        float *muon_data_positions_this = muon_data_positions + offset;


        for (int step = 0; step < 500; step++) {
            float mag_P = norm(muon_data_momenta_this);

            // Normalize P to get the direction unit vector
            float P_unit[3];
            normalize(muon_data_momenta_this, P_unit);

            int hist_idx = get_first_bin((int)mag_P);
            if (hist_idx==-1)
                break;

            if (kill_at != -1 and mag_P < kill_at)
                break;

            // 2. Generate a uniform random number in [0, 1] for sampling from CDF
            float rand_value = dist_float(gen);
            int bin_idx;
            int tbin = get_random_int(H_2d);
            if (rand_value < hist_2d_probability_table[tbin+hist_idx*H_2d])
                bin_idx = tbin;
            else
                bin_idx =  hist_2d_alias_table[tbin+hist_idx*H_2d];

            float bin_value_first_dim = hist_2d_bin_centers_first_dim[bin_idx]; // Initialize bin_value at the bin center
            float bin_jitter_first_dim = (dist_float(gen) - 0.5f) * hist_2d_bin_widths_first_dim[bin_idx]; // Calculate jitter in range [-bin_width/2, bin_width/2]
            bin_value_first_dim += bin_jitter_first_dim; // Apply jitter to the bin value

            float bin_value_second_dim = hist_2d_bin_centers_second_dim[bin_idx]; // Initialize bin_value at the bin center
            float bin_jitter_second_dim = (dist_float(gen) - 0.5f) * hist_2d_bin_widths_second_dim[bin_idx]; // Calculate jitter in range [-bin_width/2, bin_width/2]
            bin_value_second_dim += bin_jitter_second_dim; // Apply jitter to the bin value

            float delta = mag_P * exp(bin_value_first_dim);

            float delta_second_dim = mag_P * exp(bin_value_second_dim);

            float phi = dist_float(gen) * 2 * M_PI;

            // Convert polar coordinates to Cartesian coordinates
            float x = delta_second_dim * cos(phi);
            float y = delta_second_dim * sin(phi);

            delta_P[0] = x;
            delta_P[1] = -y;
            delta_P[2] = -delta;

            rotateVector(P_unit, delta_P, muon_data_momenta_this, output);

            if (sqrt(output[0]*output[0] + output[1]*output[1] + output[2]*output[2]) > 90.00) {
                std::cout<<"Error "<<x<<" "<<y<<" "<<delta<<" "<<bin_value_second_dim<<" "<<bin_value_first_dim<<" "<<bin_idx<<std::endl;
                std::cout<<"C "<<muon_data_momenta_this[0]<<" "<<muon_data_momenta_this[1]<<" "<<muon_data_momenta_this[2]<<" "<<delta<<" "<<delta_second_dim<<std::endl<<std::endl;
            }

            muon_data_momenta_this[0] = output[0];
            muon_data_momenta_this[1] = output[1];
            muon_data_momenta_this[2] = output[2];

            // Now thep position propagation
            rand_value = dist_float(gen);
            tbin = get_random_int(H_step_length);

            int log_bin = get_fancy_log_bin(log(sqrt(delta*delta + x*x + y*y) / mag_P));

//            std::cout<<"delta mag: "<<sqrt(delta*delta + x*x + y*y)<<std::endl;
//            std::cout<<"mag_P: "<<mag_P<<std::endl;
//            std::cout<<"log(...): "<<log(sqrt(delta*delta + x*x + y*y) / mag_P)<<std::endl;
//            std::cout<<"log bin: "<<log_bin<<std::endl;
//            std::cout<<"hist_idx: "<<hist_idx<<std::endl;
//            std::cout<<"H_2d: "<<H_2d<<std::endl;
//            std::cout<<"H_step_length: "<<H_step_length<<std::endl;
//            std::cout<<"tbin: "<<tbin<<std::endl;
//            std::cout<<"tbin + log_bin*H_step_length+hist_idx*H_2d: "<<tbin + log_bin*H_step_length+hist_idx*H_2d<<std::endl;
//            std::cout<<"hist_2d_step_length_vs_mag_all_probability_table[...]: "<<hist_2d_step_length_vs_mag_all_probability_table[tbin + log_bin*H_step_length+hist_idx*H_2d]<<std::endl;
//            std::cout<<"rand value: "<<rand_value<<std::endl;
//            std::cout<<"hist_2d_step_length_vs_mag_all_alias_table[tbin + log_bin*H_step_length+hist_idx*H_2d]: "<<hist_2d_step_length_vs_mag_all_alias_table[tbin + log_bin*H_step_length+hist_idx*H_2d]<<std::endl;
//            std::cout<<std::endl;


            if (rand_value < hist_2d_step_length_vs_mag_all_probability_table[tbin + log_bin*H_step_length+hist_idx*H_2d])
                bin_idx = tbin;
            else
                bin_idx =  hist_2d_step_length_vs_mag_all_alias_table[tbin + log_bin*H_step_length+hist_idx*H_2d];

            // This is for testing only:
//            if (rand_value < hist_2d_step_length_vs_mag_all_probability_table[tbin+hist_idx*H_step_length])
//                bin_idx = tbin;
//            else
//                bin_idx =  hist_2d_step_length_vs_mag_all_alias_table[tbin+hist_idx*H_step_length];

            // This is with 1D histogram
//            if (rand_value < hist_step_length_probability_table[tbin+hist_idx*H_step_length])
//                bin_idx = tbin;
//            else
//                bin_idx =  hist_step_length_alias_table[tbin+hist_idx*H_step_length];

            // TODO: This should be separately passed but the binning is the same so we use the second dimension of the 2D hist
            float bin_value_step_length = hist_2d_bin_centers_second_dim[bin_idx]; // Initialize bin_value at the bin center
            float bin_jitter_step_length = (dist_float(gen) - 0.5f) * hist_2d_bin_widths_second_dim[bin_idx]; // Calculate jitter in range [-bin_width/2, bin_width/2]
            bin_value_step_length += bin_jitter_step_length; // Apply jitter to the bin value

            float step_length_sampled = exp(bin_value_step_length);

//            std::cout<<"SS: "<<step_length_sampled<<std::endl;
            muon_data_positions_this[0] += step_length_sampled * P_unit[0];
            muon_data_positions_this[1] += step_length_sampled * P_unit[1];
            muon_data_positions_this[2] += step_length_sampled * P_unit[2];
        }
    }
}