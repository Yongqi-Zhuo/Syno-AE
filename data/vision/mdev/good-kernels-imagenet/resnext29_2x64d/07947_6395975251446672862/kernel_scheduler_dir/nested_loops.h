/* Loops -1: Forward Kernel */
for (int i_0 = 0; i_0 < N; i_0++) {
    for (int i_1 = 0; i_1 < C_out; i_1++) {
        for (int i_2 = 0; i_2 < H; i_2++) {
            for (int i_3 = 0; i_3 < H; i_3++) {
                float temp_ri_3 = 0;
                for (int ri_3 = 0; ri_3 < g^-1*s^-1*C_in; ri_3++) {
                    float temp_ri_2 = 0;
                    for (int ri_2 = 0; ri_2 < k_1; ri_2++) {
                        float temp_ri_1 = 0;
                        for (int ri_1 = 0; ri_1 < g*s; ri_1++) {
                            float temp_ri_0 = 0;
                            for (int ri_0 = 0; ri_0 < k_1; ri_0++) {
                                temp_ri_0 += in_0[i_0, ri_1 * g^-1*s^-1*C_in + ri_3, (restrict((i_2 + ri_0) - (k_1) / 2, 0, H) + 1) % H, restrict((i_3 + ri_2) - (k_1) / 2, 0, H)] * in_1[i_1 % g^-1*C_out, ri_1, ri_0] * in_2[i_1 / (g^-1*C_out), ri_3, ri_2];
                            }
                            temp_ri_1 += temp_ri_0;
                        }
                        temp_ri_2 += temp_ri_1;
                    }
                    temp_ri_3 += temp_ri_2;
                }
                out[i_0, i_1, i_2, i_3] = temp_ri_3;
            }
        }
    }
}
/* Loops 0: Backward Kernel for Input 0 */
for (int i_0 = 0; i_0 < N; i_0++) {
    for (int i_1 = 0; i_1 < C_in; i_1++) {
        for (int i_2 = 0; i_2 < H; i_2++) {
            for (int i_3 = 0; i_3 < H; i_3++) {
                float temp_ri_3 = 0;
                for (int ri_3 = 0; ri_3 < g; ri_3++) {
                    float temp_ri_2 = 0;
                    for (int ri_2 = 0; ri_2 < k_1; ri_2++) {
                        float temp_ri_1 = 0;
                        for (int ri_1 = 0; ri_1 < g^-1*C_out; ri_1++) {
                            float temp_ri_0 = 0;
                            for (int ri_0 = 0; ri_0 < k_1; ri_0++) {
                                temp_ri_0 += in_1[ri_1, i_1 / (g^-1*s^-1*C_in), ri_0] * in_2[ri_3, i_1 % g^-1*s^-1*C_in, ri_2] * grad_out[i_0, ri_3 * g^-1*C_out + ri_1, restrict((i_2 - 1) % H - ri_0 + (k_1) / 2, 0, H), restrict(i_3 - ri_2 + (k_1) / 2, 0, H)];
                            }
                            temp_ri_1 += temp_ri_0;
                        }
                        temp_ri_2 += temp_ri_1;
                    }
                    temp_ri_3 += temp_ri_2;
                }
                grad_in_0[i_0, i_1, i_2, i_3] = temp_ri_3;
            }
        }
    }
}
/* Loops 1: Backward Kernel for Input 1 */
for (int i_0 = 0; i_0 < g^-1*C_out; i_0++) {
    for (int i_1 = 0; i_1 < g*s; i_1++) {
        for (int i_2 = 0; i_2 < k_1; i_2++) {
            float temp_ri_5 = 0;
            for (int ri_5 = 0; ri_5 < g; ri_5++) {
                float temp_ri_4 = 0;
                for (int ri_4 = 0; ri_4 < g^-1*s^-1*C_in; ri_4++) {
                    float temp_ri_3 = 0;
                    for (int ri_3 = 0; ri_3 < k_1; ri_3++) {
                        float temp_ri_2 = 0;
                        for (int ri_2 = 0; ri_2 < N; ri_2++) {
                            float temp_ri_1 = 0;
                            for (int ri_1 = 0; ri_1 < H; ri_1++) {
                                float temp_ri_0 = 0;
                                for (int ri_0 = 0; ri_0 < H; ri_0++) {
                                    temp_ri_0 += in_0[ri_2, i_1 * g^-1*s^-1*C_in + ri_4, ri_1, ri_0] * in_2[ri_5, ri_4, ri_3] * grad_out[ri_2, ri_5 * g^-1*C_out + i_0, restrict((ri_1 - 1) % H - i_2 + (k_1) / 2, 0, H), restrict(ri_0 - ri_3 + (k_1) / 2, 0, H)];
                                }
                                temp_ri_1 += temp_ri_0;
                            }
                            temp_ri_2 += temp_ri_1;
                        }
                        temp_ri_3 += temp_ri_2;
                    }
                    temp_ri_4 += temp_ri_3;
                }
                temp_ri_5 += temp_ri_4;
            }
            grad_in_1[i_0, i_1, i_2] = temp_ri_5;
        }
    }
}
/* Loops 2: Backward Kernel for Input 2 */
for (int i_0 = 0; i_0 < g; i_0++) {
    for (int i_1 = 0; i_1 < g^-1*s^-1*C_in; i_1++) {
        for (int i_2 = 0; i_2 < k_1; i_2++) {
            float temp_ri_5 = 0;
            for (int ri_5 = 0; ri_5 < g^-1*C_out; ri_5++) {
                float temp_ri_4 = 0;
                for (int ri_4 = 0; ri_4 < g*s; ri_4++) {
                    float temp_ri_3 = 0;
                    for (int ri_3 = 0; ri_3 < k_1; ri_3++) {
                        float temp_ri_2 = 0;
                        for (int ri_2 = 0; ri_2 < N; ri_2++) {
                            float temp_ri_1 = 0;
                            for (int ri_1 = 0; ri_1 < H; ri_1++) {
                                float temp_ri_0 = 0;
                                for (int ri_0 = 0; ri_0 < H; ri_0++) {
                                    temp_ri_0 += in_0[ri_2, ri_4 * g^-1*s^-1*C_in + i_1, ri_1, ri_0] * in_1[ri_5, ri_4, ri_3] * grad_out[ri_2, i_0 * g^-1*C_out + ri_5, restrict((ri_1 - 1) % H - ri_3 + (k_1) / 2, 0, H), restrict(ri_0 - i_2 + (k_1) / 2, 0, H)];
                                }
                                temp_ri_1 += temp_ri_0;
                            }
                            temp_ri_2 += temp_ri_1;
                        }
                        temp_ri_3 += temp_ri_2;
                    }
                    temp_ri_4 += temp_ri_3;
                }
                temp_ri_5 += temp_ri_4;
            }
            grad_in_2[i_0, i_1, i_2] = temp_ri_5;
        }
    }
}
