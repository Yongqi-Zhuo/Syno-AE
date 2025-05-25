/* Loops -1: Forward Kernel */
for (int i_0 = 0; i_0 < N; i_0++) {
    for (int i_1 = 0; i_1 < C_out; i_1++) {
        for (int i_2 = 0; i_2 < H; i_2++) {
            for (int i_3 = 0; i_3 < H; i_3++) {
                float temp_ri_2 = 0;
                for (int ri_2 = 0; ri_2 < k_1; ri_2++) {
                    float temp_ri_1 = 0;
                    for (int ri_1 = 0; ri_1 < C_in; ri_1++) {
                        float temp_ri_0 = 0;
                        for (int ri_0 = 0; ri_0 < s; ri_0++) {
                            temp_ri_0 += in_0[i_0, ri_1, (i_3 + 1) % H, restrict((((i_2 * s + ri_0 + 1) % s*H) / (s) + ri_2) - (k_1) / 2, 0, H)] * in_1[i_1, ri_2, (i_2 * s + ri_0 + 1) % s*H % s, ri_1];
                        }
                        temp_ri_1 += temp_ri_0;
                    }
                    temp_ri_2 += temp_ri_1;
                }
                out[i_0, i_1, i_2, i_3] = temp_ri_2;
            }
        }
    }
}
/* Loops 0: Backward Kernel for Input 0 */
for (int i_0 = 0; i_0 < N; i_0++) {
    for (int i_1 = 0; i_1 < C_in; i_1++) {
        for (int i_2 = 0; i_2 < H; i_2++) {
            for (int i_3 = 0; i_3 < H; i_3++) {
                float temp_ri_2 = 0;
                for (int ri_2 = 0; ri_2 < C_out; ri_2++) {
                    float temp_ri_1 = 0;
                    for (int ri_1 = 0; ri_1 < k_1; ri_1++) {
                        float temp_ri_0 = 0;
                        for (int ri_0 = 0; ri_0 < s; ri_0++) {
                            temp_ri_0 += in_1[ri_2, ri_1, ri_0, i_1] * grad_out[i_0, ri_2, (((restrict(i_3 - ri_1 + (k_1) / 2, 0, H) * s + ri_0) - 1) % s*H) / (s), (i_2 - 1) % H];
                        }
                        temp_ri_1 += temp_ri_0;
                    }
                    temp_ri_2 += temp_ri_1;
                }
                grad_in_0[i_0, i_1, i_2, i_3] = temp_ri_2;
            }
        }
    }
}
/* Loops 1: Backward Kernel for Input 1 */
for (int i_0 = 0; i_0 < C_out; i_0++) {
    for (int i_1 = 0; i_1 < k_1; i_1++) {
        for (int i_2 = 0; i_2 < s; i_2++) {
            for (int i_3 = 0; i_3 < C_in; i_3++) {
                float temp_ri_2 = 0;
                for (int ri_2 = 0; ri_2 < N; ri_2++) {
                    float temp_ri_1 = 0;
                    for (int ri_1 = 0; ri_1 < H; ri_1++) {
                        float temp_ri_0 = 0;
                        for (int ri_0 = 0; ri_0 < H; ri_0++) {
                            temp_ri_0 += in_0[ri_2, i_3, ri_1, ri_0] * grad_out[ri_2, i_0, (((restrict(ri_0 - i_1 + (k_1) / 2, 0, H) * s + i_2) - 1) % s*H) / (s), (ri_1 - 1) % H];
                        }
                        temp_ri_1 += temp_ri_0;
                    }
                    temp_ri_2 += temp_ri_1;
                }
                grad_in_1[i_0, i_1, i_2, i_3] = temp_ri_2;
            }
        }
    }
}
