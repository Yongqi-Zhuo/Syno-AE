import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x556a8bff0a98 [label="Sum", shape=box];
    reduce_0x556a8bff09f8 [label="Sum", shape=box];
    reduce_0x556a8bff0a10 [label="Sum", shape=box];
    reduce_0x556a8bff0b50 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x556a8c18af90 [label="N", shape=none];
        interface_0_out_0x7f28ac000b60 [label="C_out", shape=none];
        interface_0_out_0x7f28a4000b60 [label="H", shape=none];
        interface_0_out_0x7f2728000b60 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x556a8bff0a98;
        reduce_0x556a8bff09f8;
        reduce_0x556a8bff0a10;
        reduce_0x556a8bff0b50;
        interface_0_out_0x556a8c18af90;
        interface_0_out_0x7f28ac000b60;
        interface_0_out_0x7f28a4000b60;
        interface_0_out_0x7f2728000b60;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x556a8c18af90 [label="N", shape=none];
        interface_0_in_0x556a8bff1610 [label="g", shape=none];
        interface_0_in_0x556a8bff1570 [label="k_1", shape=none];
        interface_0_in_0x7f28a4000b60 [label="H", shape=none];
        interface_0_in_0x556a8bff15c0 [label="k_1", shape=none];
        interface_0_in_0x7f2728000b60 [label="H", shape=none];
        interface_0_in_0x556a8bff1660 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x556a8bff1538 [label="C_out", shape=none];
        interface_0_in_0x556a8bff1628 [label="g", shape=none];
        interface_0_in_0x556a8bff1588 [label="k_1", shape=none];
        interface_0_in_0x556a8bff15d8 [label="k_1", shape=none];
        interface_0_in_0x556a8bff1678 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x556a8c18af90;
        interface_0_in_0x556a8bff1610;
        interface_0_in_0x556a8bff1570;
        interface_0_in_0x7f28a4000b60;
        interface_0_in_0x556a8bff15c0;
        interface_0_in_0x7f2728000b60;
        interface_0_in_0x556a8bff1660;
        interface_0_in_0x556a8bff1538;
        interface_0_in_0x556a8bff1628;
        interface_0_in_0x556a8bff1588;
        interface_0_in_0x556a8bff15d8;
        interface_0_in_0x556a8bff1678;
    }
    // Op's.
    op_0x556a8bff1500 [label="Share"];
    op_0x556a8bff1550 [label="Share"];
    op_0x556a8bff15a0 [label="Share"];
    op_0x556a8bff15f0 [label="Share"];
    op_0x556a8bff1640 [label="Share"];
    op_0x556a8c17ee18 [label="Expand"];
    // Dimension's.
    op_0x556a8bff1550 -> reduce_0x556a8bff09f8 [label="k_1"];
    op_0x556a8bff15a0 -> reduce_0x556a8bff0a10 [label="k_1"];
    op_0x556a8bff15f0 -> reduce_0x556a8bff0a98 [label="g"];
    op_0x556a8bff1640 -> reduce_0x556a8bff0b50 [label="g^-1*s^-1*C_out"];
    op_0x556a8c17ee18 -> op_0x556a8bff1500 [label="C_out"];
    interface_0_in_0x556a8bff1538 -> op_0x556a8bff1500 [label="C_out"];
    interface_0_in_0x556a8bff1570 -> op_0x556a8bff1550 [label="k_1"];
    interface_0_in_0x556a8bff1588 -> op_0x556a8bff1550 [label="k_1"];
    interface_0_in_0x556a8bff15c0 -> op_0x556a8bff15a0 [label="k_1"];
    interface_0_in_0x556a8bff15d8 -> op_0x556a8bff15a0 [label="k_1"];
    interface_0_in_0x556a8bff1610 -> op_0x556a8bff15f0 [label="g"];
    interface_0_in_0x556a8bff1628 -> op_0x556a8bff15f0 [label="g"];
    interface_0_in_0x556a8bff1660 -> op_0x556a8bff1640 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x556a8bff1678 -> op_0x556a8bff1640 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x556a8c18af90 -> interface_0_out_0x556a8c18af90 [label="N"];
    interface_0_in_0x7f2728000b60 -> interface_0_out_0x7f2728000b60 [label="H"];
    interface_0_in_0x7f28a4000b60 -> interface_0_out_0x7f28a4000b60 [label="H"];
    op_0x556a8bff1500 -> interface_0_out_0x7f28ac000b60 [label="C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x556a8c18af90 [label="N", shape=none];
        interface_1_out_0x556a8bff1610 [label="g", shape=none];
        interface_1_out_0x556a8bff1570 [label="k_1", shape=none];
        interface_1_out_0x7f28a4000b60 [label="H", shape=none];
        interface_1_out_0x556a8bff15c0 [label="k_1", shape=none];
        interface_1_out_0x7f2728000b60 [label="H", shape=none];
        interface_1_out_0x556a8bff1660 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x556a8c18af90;
        interface_1_out_0x556a8bff1610;
        interface_1_out_0x556a8bff1570;
        interface_1_out_0x7f28a4000b60;
        interface_1_out_0x556a8bff15c0;
        interface_1_out_0x7f2728000b60;
        interface_1_out_0x556a8bff1660;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x556a8c18af90 [label="N", shape=none];
        interface_1_in_0x556a8bff1610 [label="g", shape=none];
        interface_1_in_0x556a8bea9728 [label="H", shape=none];
        interface_1_in_0x556a8bea9768 [label="H", shape=none];
        interface_1_in_0x556a8bff1660 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x556a8c18af90;
        interface_1_in_0x556a8bff1610;
        interface_1_in_0x556a8bea9728;
        interface_1_in_0x556a8bea9768;
        interface_1_in_0x556a8bff1660;
    }
    // Op's.
    op_0x556a8bea9700 [label="Unfold"];
    op_0x556a8bea9740 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x556a8bea9728 -> op_0x556a8bea9700 [label="H"];
    interface_1_in_0x556a8bea9768 -> op_0x556a8bea9740 [label="H"];
    op_0x556a8bea9700 -> interface_1_out_0x556a8bff1570 [label="k_1"];
    op_0x556a8bea9740 -> interface_1_out_0x556a8bff15c0 [label="k_1"];
    interface_1_in_0x556a8bff1610 -> interface_1_out_0x556a8bff1610 [label="g"];
    interface_1_in_0x556a8bff1660 -> interface_1_out_0x556a8bff1660 [label="g^-1*s^-1*C_out"];
    interface_1_in_0x556a8c18af90 -> interface_1_out_0x556a8c18af90 [label="N"];
    op_0x556a8bea9740 -> interface_1_out_0x7f2728000b60 [label="H"];
    op_0x556a8bea9700 -> interface_1_out_0x7f28a4000b60 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x556a8bff0928 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x556a8c18af90 [label="N", shape=none];
        interface_2_out_0x556a8bff1610 [label="g", shape=none];
        interface_2_out_0x556a8bea9728 [label="H", shape=none];
        interface_2_out_0x556a8bea9768 [label="H", shape=none];
        interface_2_out_0x556a8bff1660 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x556a8bff0928;
        interface_2_out_0x556a8c18af90;
        interface_2_out_0x556a8bff1610;
        interface_2_out_0x556a8bea9728;
        interface_2_out_0x556a8bea9768;
        interface_2_out_0x556a8bff1660;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x556a8c18af90 [label="N", shape=none];
        interface_2_in_0x556a8c04fa40 [label="C_in", shape=none];
        interface_2_in_0x556a8bea9728 [label="H", shape=none];
        interface_2_in_0x556a8bea9768 [label="H", shape=none];
        interface_2_in_0x556a8bff1660 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x556a8c18af90;
        interface_2_in_0x556a8c04fa40;
        interface_2_in_0x556a8bea9728;
        interface_2_in_0x556a8bea9768;
        interface_2_in_0x556a8bff1660;
    }
    // Op's.
    op_0x556a8c04fa00 [label="Split"];
    // Dimension's.
    interface_2_in_0x556a8bea9728 -> interface_2_out_0x556a8bea9728 [label="H"];
    interface_2_in_0x556a8bea9768 -> interface_2_out_0x556a8bea9768 [label="H"];
    op_0x556a8c04fa00 -> reduce_0x556a8bff0928 [label="g^-1*C_in"];
    op_0x556a8c04fa00 -> interface_2_out_0x556a8bff1610 [label="g"];
    interface_2_in_0x556a8bff1660 -> interface_2_out_0x556a8bff1660 [label="g^-1*s^-1*C_out"];
    interface_2_in_0x556a8c04fa40 -> op_0x556a8c04fa00 [label="C_in"];
    interface_2_in_0x556a8c18af90 -> interface_2_out_0x556a8c18af90 [label="N"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x556a8bff09e0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x556a8c18af90 [label="N", shape=none];
        interface_3_out_0x556a8c04fa40 [label="C_in", shape=none];
        interface_3_out_0x556a8bea9728 [label="H", shape=none];
        interface_3_out_0x556a8bea9768 [label="H", shape=none];
        interface_3_out_0x556a8bff1660 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x556a8bff09e0;
        interface_3_out_0x556a8c18af90;
        interface_3_out_0x556a8c04fa40;
        interface_3_out_0x556a8bea9728;
        interface_3_out_0x556a8bea9768;
        interface_3_out_0x556a8bff1660;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x556a8c18af90 [label="N", shape=none];
        interface_3_in_0x556a8bff1700 [label="C_in", shape=none];
        interface_3_in_0x556a8bea9728 [label="H", shape=none];
        interface_3_in_0x556a8bff16b0 [label="k_1", shape=none];
        interface_3_in_0x556a8bea9768 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x556a8bff1718 [label="C_in", shape=none];
        interface_3_in_0x556a8bff16c8 [label="k_1", shape=none];
        interface_3_in_0x556a8bff1768 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x556a8c18af90;
        interface_3_in_0x556a8bff1700;
        interface_3_in_0x556a8bea9728;
        interface_3_in_0x556a8bff16b0;
        interface_3_in_0x556a8bea9768;
        interface_3_in_0x556a8bff1718;
        interface_3_in_0x556a8bff16c8;
        interface_3_in_0x556a8bff1768;
    }
    // Op's.
    op_0x556a8bff1690 [label="Share"];
    op_0x556a8bff16e0 [label="Share"];
    op_0x556a8bff1730 [label="Share"];
    op_0x556a8c17ee38 [label="Expand"];
    // Dimension's.
    interface_3_in_0x556a8bea9728 -> interface_3_out_0x556a8bea9728 [label="H"];
    interface_3_in_0x556a8bea9768 -> interface_3_out_0x556a8bea9768 [label="H"];
    op_0x556a8bff1690 -> reduce_0x556a8bff09e0 [label="k_1"];
    op_0x556a8bff1730 -> interface_3_out_0x556a8bff1660 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x556a8bff16b0 -> op_0x556a8bff1690 [label="k_1"];
    interface_3_in_0x556a8bff16c8 -> op_0x556a8bff1690 [label="k_1"];
    interface_3_in_0x556a8bff1700 -> op_0x556a8bff16e0 [label="C_in"];
    interface_3_in_0x556a8bff1718 -> op_0x556a8bff16e0 [label="C_in"];
    op_0x556a8c17ee38 -> op_0x556a8bff1730 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x556a8bff1768 -> op_0x556a8bff1730 [label="g^-1*s^-1*C_out"];
    op_0x556a8bff16e0 -> interface_3_out_0x556a8c04fa40 [label="C_in"];
    interface_3_in_0x556a8c18af90 -> interface_3_out_0x556a8c18af90 [label="N"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x556a8c18af90 [label="N", shape=none];
        interface_4_out_0x556a8bff1700 [label="C_in", shape=none];
        interface_4_out_0x556a8bea9728 [label="H", shape=none];
        interface_4_out_0x556a8bff16b0 [label="k_1", shape=none];
        interface_4_out_0x556a8bea9768 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x556a8c18af90;
        interface_4_out_0x556a8bff1700;
        interface_4_out_0x556a8bea9728;
        interface_4_out_0x556a8bff16b0;
        interface_4_out_0x556a8bea9768;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x556a8c18af90 [label="N", shape=none];
        interface_4_in_0x556a8bff1700 [label="C_in", shape=none];
        interface_4_in_0x556a8bea9728 [label="H", shape=none];
        interface_4_in_0x556a8bea97a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x556a8c18af90;
        interface_4_in_0x556a8bff1700;
        interface_4_in_0x556a8bea9728;
        interface_4_in_0x556a8bea97a8;
    }
    // Op's.
    op_0x556a8bea9780 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x556a8bea9728 -> interface_4_out_0x556a8bea9728 [label="H"];
    op_0x556a8bea9780 -> interface_4_out_0x556a8bea9768 [label="H"];
    interface_4_in_0x556a8bea97a8 -> op_0x556a8bea9780 [label="H"];
    op_0x556a8bea9780 -> interface_4_out_0x556a8bff16b0 [label="k_1"];
    interface_4_in_0x556a8bff1700 -> interface_4_out_0x556a8bff1700 [label="C_in"];
    interface_4_in_0x556a8c18af90 -> interface_4_out_0x556a8c18af90 [label="N"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x556a8c18af90 [label="N", shape=none];
    interface_5_out_0x556a8bff1700 [label="C_in", shape=none];
    interface_5_out_0x556a8bea9728 [label="H", shape=none];
    interface_5_out_0x556a8bea97a8 [label="H", shape=none];
}

interface_5_out_0x556a8c18af90 -> interface_4_in_0x556a8c18af90;
interface_5_out_0x556a8bff1700 -> interface_4_in_0x556a8bff1700;
interface_5_out_0x556a8bea9728 -> interface_4_in_0x556a8bea9728;
interface_5_out_0x556a8bea97a8 -> interface_4_in_0x556a8bea97a8;

interface_4_out_0x556a8c18af90 -> interface_3_in_0x556a8c18af90;
interface_4_out_0x556a8bff1700 -> interface_3_in_0x556a8bff1700;
interface_4_out_0x556a8bea9728 -> interface_3_in_0x556a8bea9728;
interface_4_out_0x556a8bff16b0 -> interface_3_in_0x556a8bff16b0;
interface_4_out_0x556a8bea9768 -> interface_3_in_0x556a8bea9768;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x556a8bff1718 [label="C_in", shape=none];
    interface_6_out_0x556a8bff16c8 [label="k_1", shape=none];
    interface_6_out_0x556a8bff1768 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x556a8bff1718 -> interface_3_in_0x556a8bff1718;
interface_6_out_0x556a8bff16c8 -> interface_3_in_0x556a8bff16c8;
interface_6_out_0x556a8bff1768 -> interface_3_in_0x556a8bff1768;

interface_3_out_0x556a8c18af90 -> interface_2_in_0x556a8c18af90;
interface_3_out_0x556a8c04fa40 -> interface_2_in_0x556a8c04fa40;
interface_3_out_0x556a8bea9728 -> interface_2_in_0x556a8bea9728;
interface_3_out_0x556a8bea9768 -> interface_2_in_0x556a8bea9768;
interface_3_out_0x556a8bff1660 -> interface_2_in_0x556a8bff1660;

interface_2_out_0x556a8c18af90 -> interface_1_in_0x556a8c18af90;
interface_2_out_0x556a8bff1610 -> interface_1_in_0x556a8bff1610;
interface_2_out_0x556a8bea9728 -> interface_1_in_0x556a8bea9728;
interface_2_out_0x556a8bea9768 -> interface_1_in_0x556a8bea9768;
interface_2_out_0x556a8bff1660 -> interface_1_in_0x556a8bff1660;

interface_1_out_0x556a8c18af90 -> interface_0_in_0x556a8c18af90;
interface_1_out_0x556a8bff1610 -> interface_0_in_0x556a8bff1610;
interface_1_out_0x556a8bff1570 -> interface_0_in_0x556a8bff1570;
interface_1_out_0x7f28a4000b60 -> interface_0_in_0x7f28a4000b60;
interface_1_out_0x556a8bff15c0 -> interface_0_in_0x556a8bff15c0;
interface_1_out_0x7f2728000b60 -> interface_0_in_0x7f2728000b60;
interface_1_out_0x556a8bff1660 -> interface_0_in_0x556a8bff1660;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x556a8bff1538 [label="C_out", shape=none];
    interface_7_out_0x556a8bff1628 [label="g", shape=none];
    interface_7_out_0x556a8bff1588 [label="k_1", shape=none];
    interface_7_out_0x556a8bff15d8 [label="k_1", shape=none];
    interface_7_out_0x556a8bff1678 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x556a8bff1538 -> interface_0_in_0x556a8bff1538;
interface_7_out_0x556a8bff1628 -> interface_0_in_0x556a8bff1628;
interface_7_out_0x556a8bff1588 -> interface_0_in_0x556a8bff1588;
interface_7_out_0x556a8bff15d8 -> interface_0_in_0x556a8bff15d8;
interface_7_out_0x556a8bff1678 -> interface_0_in_0x556a8bff1678;

{
    rank = same;
    interface_5_out_0x556a8c18af90;
    interface_5_out_0x556a8bff1700;
    interface_5_out_0x556a8bea9728;
    interface_5_out_0x556a8bea97a8;
    interface_7_out_0x556a8bff1538;
    interface_7_out_0x556a8bff1628;
    interface_7_out_0x556a8bff1588;
    interface_7_out_0x556a8bff15d8;
    interface_7_out_0x556a8bff1678;
    interface_6_out_0x556a8bff1718;
    interface_6_out_0x556a8bff16c8;
    interface_6_out_0x556a8bff1768;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x556a8c18af90 [label="N", shape=none];
    interface_8_in_0x7f28ac000b60 [label="C_out", shape=none];
    interface_8_in_0x7f28a4000b60 [label="H", shape=none];
    interface_8_in_0x7f2728000b60 [label="H", shape=none];
}
interface_0_out_0x556a8c18af90 -> interface_8_in_0x556a8c18af90;
interface_0_out_0x7f28ac000b60 -> interface_8_in_0x7f28ac000b60;
interface_0_out_0x7f28a4000b60 -> interface_8_in_0x7f28a4000b60;
interface_0_out_0x7f2728000b60 -> interface_8_in_0x7f2728000b60;

}

"""
class kernel_manual_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 32, 3, 3, 1]),
			torch.randn([64, 3, 1]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold22f5584eb7a8b416 -> [H]@Unfolde73c9e24012bc66d, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (128, 3584, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 56, 3, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 2, 56, 56, 1, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (128, 32, 56, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 56, 56, 1, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (128, 5376, 56, 1, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 56, 3, 56, 1, ))

		# Perform contraction.
		t_7 = torch.einsum("nljpkom, iljkm -> nipo", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_manual_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 32, 3, 3, 2]),
			torch.randn([64, 3, 2]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold22f5584eb7a8b416 -> [H]@Unfolde73c9e24012bc66d, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (128, 1792, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 2, 28, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (128, 32, 28, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 28, 28, 2, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (128, 2688, 28, 2, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 28, 3, 28, 2, ))

		# Perform contraction.
		t_7 = torch.einsum("nljpkom, iljkm -> nipo", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_manual_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 32, 3, 3, 2]),
			torch.randn([128, 3, 2]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold22f5584eb7a8b416 -> [H]@Unfolde73c9e24012bc66d, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (128, 3584, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 128, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 4, 28, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (128, 32, 28, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 28, 28, 2, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (128, 2688, 28, 2, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 28, 3, 28, 2, ))

		# Perform contraction.
		t_7 = torch.einsum("nljpkom, iljkm -> nipo", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_manual_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 32, 3, 3, 4]),
			torch.randn([128, 3, 4]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold22f5584eb7a8b416 -> [H]@Unfolde73c9e24012bc66d, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (128, 1792, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 128, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 4, 14, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (128, 32, 14, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 14, 14, 4, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (128, 1344, 14, 4, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 14, 3, 14, 4, ))

		# Perform contraction.
		t_7 = torch.einsum("nljpkom, iljkm -> nipo", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_manual_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 32, 3, 3, 4]),
			torch.randn([256, 3, 4]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold22f5584eb7a8b416 -> [H]@Unfolde73c9e24012bc66d, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (128, 3584, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 256, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 8, 14, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (128, 32, 14, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 14, 14, 4, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (128, 1344, 14, 4, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 14, 3, 14, 4, ))

		# Perform contraction.
		t_7 = torch.einsum("nljpkom, iljkm -> nipo", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_manual_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 32, 3, 3, 8]),
			torch.randn([256, 3, 8]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold22f5584eb7a8b416 -> [H]@Unfolde73c9e24012bc66d, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (128, 1792, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 256, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 8, 7, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (128, 32, 7, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 7, 7, 8, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (128, 672, 7, 8, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 7, 3, 7, 8, ))

		# Perform contraction.
		t_7 = torch.einsum("nljpkom, iljkm -> nipo", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_manual_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 32, 3, 3, 8]),
			torch.randn([512, 3, 8]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold22f5584eb7a8b416 -> [H]@Unfolde73c9e24012bc66d, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (128, 3584, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 512, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("njlim, jik -> njlmk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 16, 7, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (128, 32, 7, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 7, 7, 8, ))

		# [H]@Unfolde73c9e24012bc66d -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share20826c8af74ae67f
		t_6 = torch.reshape(t_6, (128, 672, 7, 8, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 7, 3, 7, 8, ))

		# Perform contraction.
		t_7 = torch.einsum("nljpkom, iljkm -> nipo", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

