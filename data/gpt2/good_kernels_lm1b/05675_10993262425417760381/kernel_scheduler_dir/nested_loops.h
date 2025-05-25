/* Loops -1: Forward Kernel */
for (int i_0 = 0; i_0 < N; i_0++) {
    for (int i_1 = 0; i_1 < seq_len; i_1++) {
        for (int i_2 = 0; i_2 < t*H_in; i_2++) {
            float temp_ri_0 = 0;
            for (int ri_0 = 0; ri_0 < k_1^-1*H_in; ri_0++) {
                temp_ri_0 += in_0[i_0, i_1, (i_2 % k_1^-3*t^-1*H_in) / (k_1^-4*t^-1*H_in) * k_1^-1*H_in + ri_0] * in_1[i_2 / (k_1^-3*t^-1*H_in), ri_0, i_2 % k_1^-3*t^-1*H_in % k_1^-4*t^-1*H_in];
            }
            out[i_0, i_1, i_2] = temp_ri_0;
        }
    }
}
/* Loops 0: Backward Kernel for Input 0 */
for (int i_0 = 0; i_0 < N; i_0++) {
    for (int i_1 = 0; i_1 < seq_len; i_1++) {
        for (int i_2 = 0; i_2 < H_in; i_2++) {
            float temp_ri_1 = 0;
            for (int ri_1 = 0; ri_1 < k_1^3*t^2; ri_1++) {
                float temp_ri_0 = 0;
                for (int ri_0 = 0; ri_0 < k_1^-4*t^-1*H_in; ri_0++) {
                    temp_ri_0 += in_1[ri_1, i_2 % k_1^-1*H_in, ri_0] * grad_out[i_0, i_1, ri_1 * k_1^-3*t^-1*H_in + i_2 / (k_1^-1*H_in) * k_1^-4*t^-1*H_in + ri_0];
                }
                temp_ri_1 += temp_ri_0;
            }
            grad_in_0[i_0, i_1, i_2] = temp_ri_1;
        }
    }
}
/* Loops 1: Backward Kernel for Input 1 */
for (int i_0 = 0; i_0 < k_1^3*t^2; i_0++) {
    for (int i_1 = 0; i_1 < k_1^-1*H_in; i_1++) {
        for (int i_2 = 0; i_2 < k_1^-4*t^-1*H_in; i_2++) {
            float temp_ri_2 = 0;
            for (int ri_2 = 0; ri_2 < N; ri_2++) {
                float temp_ri_1 = 0;
                for (int ri_1 = 0; ri_1 < seq_len; ri_1++) {
                    float temp_ri_0 = 0;
                    for (int ri_0 = 0; ri_0 < k_1; ri_0++) {
                        temp_ri_0 += in_0[ri_2, ri_1, ri_0 * k_1^-1*H_in + i_1] * grad_out[ri_2, ri_1, i_0 * k_1^-3*t^-1*H_in + ri_0 * k_1^-4*t^-1*H_in + i_2];
                    }
                    temp_ri_1 += temp_ri_0;
                }
                temp_ri_2 += temp_ri_1;
            }
            grad_in_1[i_0, i_1, i_2] = temp_ri_2;
        }
    }
}
