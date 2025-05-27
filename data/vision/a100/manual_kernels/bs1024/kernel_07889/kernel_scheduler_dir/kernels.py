import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x55aeb9090398 [label="Sum", shape=box];
    reduce_0x55aeb90902e0 [label="Sum", shape=box];
    reduce_0x55aeb90902f8 [label="Sum", shape=box];
    reduce_0x55aeb9090450 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x55aeb43a1900 [label="N", shape=none];
        interface_0_out_0x55aeb637c590 [label="C_out", shape=none];
        interface_0_out_0x55aeb908ff90 [label="H", shape=none];
        interface_0_out_0x55aeb9090f10 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x55aeb9090398;
        reduce_0x55aeb90902e0;
        reduce_0x55aeb90902f8;
        reduce_0x55aeb9090450;
        interface_0_out_0x55aeb43a1900;
        interface_0_out_0x55aeb637c590;
        interface_0_out_0x55aeb908ff90;
        interface_0_out_0x55aeb9090f10;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55aeb43a1900 [label="N", shape=none];
        interface_0_in_0x55aeb433e510 [label="g", shape=none];
        interface_0_in_0x55aeb433e470 [label="k_1", shape=none];
        interface_0_in_0x55aeb908ff90 [label="H", shape=none];
        interface_0_in_0x55aeb433e4c0 [label="k_1", shape=none];
        interface_0_in_0x55aeb9090f10 [label="H", shape=none];
        interface_0_in_0x55aeb433e560 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x55aeb433e438 [label="C_out", shape=none];
        interface_0_in_0x55aeb433e528 [label="g", shape=none];
        interface_0_in_0x55aeb433e488 [label="k_1", shape=none];
        interface_0_in_0x55aeb433e4d8 [label="k_1", shape=none];
        interface_0_in_0x55aeb433e578 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55aeb43a1900;
        interface_0_in_0x55aeb433e510;
        interface_0_in_0x55aeb433e470;
        interface_0_in_0x55aeb908ff90;
        interface_0_in_0x55aeb433e4c0;
        interface_0_in_0x55aeb9090f10;
        interface_0_in_0x55aeb433e560;
        interface_0_in_0x55aeb433e438;
        interface_0_in_0x55aeb433e528;
        interface_0_in_0x55aeb433e488;
        interface_0_in_0x55aeb433e4d8;
        interface_0_in_0x55aeb433e578;
    }
    // Op's.
    op_0x55aeb433e400 [label="Share"];
    op_0x55aeb433e450 [label="Share"];
    op_0x55aeb433e4a0 [label="Share"];
    op_0x55aeb433e4f0 [label="Share"];
    op_0x55aeb433e540 [label="Share"];
    op_0x55aeb9090f58 [label="Expand"];
    // Dimension's.
    op_0x55aeb9090f58 -> op_0x55aeb433e400 [label="C_out"];
    interface_0_in_0x55aeb433e438 -> op_0x55aeb433e400 [label="C_out"];
    interface_0_in_0x55aeb433e470 -> op_0x55aeb433e450 [label="k_1"];
    interface_0_in_0x55aeb433e488 -> op_0x55aeb433e450 [label="k_1"];
    interface_0_in_0x55aeb433e4c0 -> op_0x55aeb433e4a0 [label="k_1"];
    interface_0_in_0x55aeb433e4d8 -> op_0x55aeb433e4a0 [label="k_1"];
    interface_0_in_0x55aeb433e510 -> op_0x55aeb433e4f0 [label="g"];
    interface_0_in_0x55aeb433e528 -> op_0x55aeb433e4f0 [label="g"];
    interface_0_in_0x55aeb433e560 -> op_0x55aeb433e540 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x55aeb433e578 -> op_0x55aeb433e540 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x55aeb43a1900 -> interface_0_out_0x55aeb43a1900 [label="N"];
    op_0x55aeb433e400 -> interface_0_out_0x55aeb637c590 [label="C_out"];
    interface_0_in_0x55aeb908ff90 -> interface_0_out_0x55aeb908ff90 [label="H"];
    op_0x55aeb433e450 -> reduce_0x55aeb90902e0 [label="k_1"];
    op_0x55aeb433e4a0 -> reduce_0x55aeb90902f8 [label="k_1"];
    op_0x55aeb433e4f0 -> reduce_0x55aeb9090398 [label="g"];
    op_0x55aeb433e540 -> reduce_0x55aeb9090450 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x55aeb9090f10 -> interface_0_out_0x55aeb9090f10 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55aeb43a1900 [label="N", shape=none];
        interface_1_out_0x55aeb433e510 [label="g", shape=none];
        interface_1_out_0x55aeb433e470 [label="k_1", shape=none];
        interface_1_out_0x55aeb908ff90 [label="H", shape=none];
        interface_1_out_0x55aeb433e4c0 [label="k_1", shape=none];
        interface_1_out_0x55aeb9090f10 [label="H", shape=none];
        interface_1_out_0x55aeb433e560 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x55aeb43a1900;
        interface_1_out_0x55aeb433e510;
        interface_1_out_0x55aeb433e470;
        interface_1_out_0x55aeb908ff90;
        interface_1_out_0x55aeb433e4c0;
        interface_1_out_0x55aeb9090f10;
        interface_1_out_0x55aeb433e560;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55aeb43a1900 [label="N", shape=none];
        interface_1_in_0x55aeb433e510 [label="g", shape=none];
        interface_1_in_0x55aeb9092568 [label="H", shape=none];
        interface_1_in_0x55aeb433e4c0 [label="k_1", shape=none];
        interface_1_in_0x55aeb9090f10 [label="H", shape=none];
        interface_1_in_0x55aeb433e560 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55aeb43a1900;
        interface_1_in_0x55aeb433e510;
        interface_1_in_0x55aeb9092568;
        interface_1_in_0x55aeb433e4c0;
        interface_1_in_0x55aeb9090f10;
        interface_1_in_0x55aeb433e560;
    }
    // Op's.
    op_0x55aeb9092540 [label="Unfold"];
    // Dimension's.
    op_0x55aeb9092540 -> interface_1_out_0x55aeb433e470 [label="k_1"];
    interface_1_in_0x55aeb433e4c0 -> interface_1_out_0x55aeb433e4c0 [label="k_1"];
    interface_1_in_0x55aeb433e510 -> interface_1_out_0x55aeb433e510 [label="g"];
    interface_1_in_0x55aeb433e560 -> interface_1_out_0x55aeb433e560 [label="g^-1*s^-1*C_out"];
    interface_1_in_0x55aeb43a1900 -> interface_1_out_0x55aeb43a1900 [label="N"];
    op_0x55aeb9092540 -> interface_1_out_0x55aeb908ff90 [label="H"];
    interface_1_in_0x55aeb9090f10 -> interface_1_out_0x55aeb9090f10 [label="H"];
    interface_1_in_0x55aeb9092568 -> op_0x55aeb9092540 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x55aeb9090228 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55aeb43a1900 [label="N", shape=none];
        interface_2_out_0x55aeb433e510 [label="g", shape=none];
        interface_2_out_0x55aeb9092568 [label="H", shape=none];
        interface_2_out_0x55aeb433e4c0 [label="k_1", shape=none];
        interface_2_out_0x55aeb9090f10 [label="H", shape=none];
        interface_2_out_0x55aeb433e560 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x55aeb9090228;
        interface_2_out_0x55aeb43a1900;
        interface_2_out_0x55aeb433e510;
        interface_2_out_0x55aeb9092568;
        interface_2_out_0x55aeb433e4c0;
        interface_2_out_0x55aeb9090f10;
        interface_2_out_0x55aeb433e560;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55aeb43a1900 [label="N", shape=none];
        interface_2_in_0x55aeb9093240 [label="C_in", shape=none];
        interface_2_in_0x55aeb9092568 [label="H", shape=none];
        interface_2_in_0x55aeb433e4c0 [label="k_1", shape=none];
        interface_2_in_0x55aeb9090f10 [label="H", shape=none];
        interface_2_in_0x55aeb433e560 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55aeb43a1900;
        interface_2_in_0x55aeb9093240;
        interface_2_in_0x55aeb9092568;
        interface_2_in_0x55aeb433e4c0;
        interface_2_in_0x55aeb9090f10;
        interface_2_in_0x55aeb433e560;
    }
    // Op's.
    op_0x55aeb9093200 [label="Split"];
    // Dimension's.
    interface_2_in_0x55aeb433e4c0 -> interface_2_out_0x55aeb433e4c0 [label="k_1"];
    op_0x55aeb9093200 -> interface_2_out_0x55aeb433e510 [label="g"];
    interface_2_in_0x55aeb433e560 -> interface_2_out_0x55aeb433e560 [label="g^-1*s^-1*C_out"];
    interface_2_in_0x55aeb43a1900 -> interface_2_out_0x55aeb43a1900 [label="N"];
    op_0x55aeb9093200 -> reduce_0x55aeb9090228 [label="g^-1*C_in"];
    interface_2_in_0x55aeb9090f10 -> interface_2_out_0x55aeb9090f10 [label="H"];
    interface_2_in_0x55aeb9092568 -> interface_2_out_0x55aeb9092568 [label="H"];
    interface_2_in_0x55aeb9093240 -> op_0x55aeb9093200 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55aeb43a1900 [label="N", shape=none];
        interface_3_out_0x55aeb9093240 [label="C_in", shape=none];
        interface_3_out_0x55aeb9092568 [label="H", shape=none];
        interface_3_out_0x55aeb433e4c0 [label="k_1", shape=none];
        interface_3_out_0x55aeb9090f10 [label="H", shape=none];
        interface_3_out_0x55aeb433e560 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x55aeb43a1900;
        interface_3_out_0x55aeb9093240;
        interface_3_out_0x55aeb9092568;
        interface_3_out_0x55aeb433e4c0;
        interface_3_out_0x55aeb9090f10;
        interface_3_out_0x55aeb433e560;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55aeb43a1900 [label="N", shape=none];
        interface_3_in_0x55aeb433e600 [label="C_in", shape=none];
        interface_3_in_0x55aeb9092568 [label="H", shape=none];
        interface_3_in_0x55aeb433e5b0 [label="k_1", shape=none];
        interface_3_in_0x55aeb9090f10 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x55aeb433e618 [label="C_in", shape=none];
        interface_3_in_0x55aeb433e5c8 [label="k_1", shape=none];
        interface_3_in_0x55aeb433e668 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55aeb43a1900;
        interface_3_in_0x55aeb433e600;
        interface_3_in_0x55aeb9092568;
        interface_3_in_0x55aeb433e5b0;
        interface_3_in_0x55aeb9090f10;
        interface_3_in_0x55aeb433e618;
        interface_3_in_0x55aeb433e5c8;
        interface_3_in_0x55aeb433e668;
    }
    // Op's.
    op_0x55aeb433e590 [label="Share"];
    op_0x55aeb433e5e0 [label="Share"];
    op_0x55aeb433e630 [label="Share"];
    op_0x55aeb9090f78 [label="Expand"];
    // Dimension's.
    op_0x55aeb433e590 -> interface_3_out_0x55aeb433e4c0 [label="k_1"];
    op_0x55aeb433e630 -> interface_3_out_0x55aeb433e560 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x55aeb433e5b0 -> op_0x55aeb433e590 [label="k_1"];
    interface_3_in_0x55aeb433e5c8 -> op_0x55aeb433e590 [label="k_1"];
    interface_3_in_0x55aeb433e600 -> op_0x55aeb433e5e0 [label="C_in"];
    interface_3_in_0x55aeb433e618 -> op_0x55aeb433e5e0 [label="C_in"];
    op_0x55aeb9090f78 -> op_0x55aeb433e630 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x55aeb433e668 -> op_0x55aeb433e630 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x55aeb43a1900 -> interface_3_out_0x55aeb43a1900 [label="N"];
    interface_3_in_0x55aeb9090f10 -> interface_3_out_0x55aeb9090f10 [label="H"];
    interface_3_in_0x55aeb9092568 -> interface_3_out_0x55aeb9092568 [label="H"];
    op_0x55aeb433e5e0 -> interface_3_out_0x55aeb9093240 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x55aeb43a1900 [label="N", shape=none];
        interface_4_out_0x55aeb433e600 [label="C_in", shape=none];
        interface_4_out_0x55aeb9092568 [label="H", shape=none];
        interface_4_out_0x55aeb433e5b0 [label="k_1", shape=none];
        interface_4_out_0x55aeb9090f10 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x55aeb43a1900;
        interface_4_out_0x55aeb433e600;
        interface_4_out_0x55aeb9092568;
        interface_4_out_0x55aeb433e5b0;
        interface_4_out_0x55aeb9090f10;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x55aeb43a1900 [label="N", shape=none];
        interface_4_in_0x55aeb433e600 [label="C_in", shape=none];
        interface_4_in_0x55aeb9092568 [label="H", shape=none];
        interface_4_in_0x55aeb90925a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x55aeb43a1900;
        interface_4_in_0x55aeb433e600;
        interface_4_in_0x55aeb9092568;
        interface_4_in_0x55aeb90925a8;
    }
    // Op's.
    op_0x55aeb9092580 [label="Unfold"];
    // Dimension's.
    op_0x55aeb9092580 -> interface_4_out_0x55aeb433e5b0 [label="k_1"];
    interface_4_in_0x55aeb433e600 -> interface_4_out_0x55aeb433e600 [label="C_in"];
    interface_4_in_0x55aeb43a1900 -> interface_4_out_0x55aeb43a1900 [label="N"];
    op_0x55aeb9092580 -> interface_4_out_0x55aeb9090f10 [label="H"];
    interface_4_in_0x55aeb9092568 -> interface_4_out_0x55aeb9092568 [label="H"];
    interface_4_in_0x55aeb90925a8 -> op_0x55aeb9092580 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x55aeb43a1900 [label="N", shape=none];
    interface_5_out_0x55aeb433e600 [label="C_in", shape=none];
    interface_5_out_0x55aeb9092568 [label="H", shape=none];
    interface_5_out_0x55aeb90925a8 [label="H", shape=none];
}

interface_5_out_0x55aeb43a1900 -> interface_4_in_0x55aeb43a1900;
interface_5_out_0x55aeb433e600 -> interface_4_in_0x55aeb433e600;
interface_5_out_0x55aeb9092568 -> interface_4_in_0x55aeb9092568;
interface_5_out_0x55aeb90925a8 -> interface_4_in_0x55aeb90925a8;

interface_4_out_0x55aeb43a1900 -> interface_3_in_0x55aeb43a1900;
interface_4_out_0x55aeb433e600 -> interface_3_in_0x55aeb433e600;
interface_4_out_0x55aeb9092568 -> interface_3_in_0x55aeb9092568;
interface_4_out_0x55aeb433e5b0 -> interface_3_in_0x55aeb433e5b0;
interface_4_out_0x55aeb9090f10 -> interface_3_in_0x55aeb9090f10;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x55aeb433e618 [label="C_in", shape=none];
    interface_6_out_0x55aeb433e5c8 [label="k_1", shape=none];
    interface_6_out_0x55aeb433e668 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x55aeb433e618 -> interface_3_in_0x55aeb433e618;
interface_6_out_0x55aeb433e5c8 -> interface_3_in_0x55aeb433e5c8;
interface_6_out_0x55aeb433e668 -> interface_3_in_0x55aeb433e668;

interface_3_out_0x55aeb43a1900 -> interface_2_in_0x55aeb43a1900;
interface_3_out_0x55aeb9093240 -> interface_2_in_0x55aeb9093240;
interface_3_out_0x55aeb9092568 -> interface_2_in_0x55aeb9092568;
interface_3_out_0x55aeb433e4c0 -> interface_2_in_0x55aeb433e4c0;
interface_3_out_0x55aeb9090f10 -> interface_2_in_0x55aeb9090f10;
interface_3_out_0x55aeb433e560 -> interface_2_in_0x55aeb433e560;

interface_2_out_0x55aeb43a1900 -> interface_1_in_0x55aeb43a1900;
interface_2_out_0x55aeb433e510 -> interface_1_in_0x55aeb433e510;
interface_2_out_0x55aeb9092568 -> interface_1_in_0x55aeb9092568;
interface_2_out_0x55aeb433e4c0 -> interface_1_in_0x55aeb433e4c0;
interface_2_out_0x55aeb9090f10 -> interface_1_in_0x55aeb9090f10;
interface_2_out_0x55aeb433e560 -> interface_1_in_0x55aeb433e560;

interface_1_out_0x55aeb43a1900 -> interface_0_in_0x55aeb43a1900;
interface_1_out_0x55aeb433e510 -> interface_0_in_0x55aeb433e510;
interface_1_out_0x55aeb433e470 -> interface_0_in_0x55aeb433e470;
interface_1_out_0x55aeb908ff90 -> interface_0_in_0x55aeb908ff90;
interface_1_out_0x55aeb433e4c0 -> interface_0_in_0x55aeb433e4c0;
interface_1_out_0x55aeb9090f10 -> interface_0_in_0x55aeb9090f10;
interface_1_out_0x55aeb433e560 -> interface_0_in_0x55aeb433e560;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x55aeb433e438 [label="C_out", shape=none];
    interface_7_out_0x55aeb433e528 [label="g", shape=none];
    interface_7_out_0x55aeb433e488 [label="k_1", shape=none];
    interface_7_out_0x55aeb433e4d8 [label="k_1", shape=none];
    interface_7_out_0x55aeb433e578 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x55aeb433e438 -> interface_0_in_0x55aeb433e438;
interface_7_out_0x55aeb433e528 -> interface_0_in_0x55aeb433e528;
interface_7_out_0x55aeb433e488 -> interface_0_in_0x55aeb433e488;
interface_7_out_0x55aeb433e4d8 -> interface_0_in_0x55aeb433e4d8;
interface_7_out_0x55aeb433e578 -> interface_0_in_0x55aeb433e578;

{
    rank = same;
    interface_5_out_0x55aeb43a1900;
    interface_5_out_0x55aeb433e600;
    interface_5_out_0x55aeb9092568;
    interface_5_out_0x55aeb90925a8;
    interface_7_out_0x55aeb433e438;
    interface_7_out_0x55aeb433e528;
    interface_7_out_0x55aeb433e488;
    interface_7_out_0x55aeb433e4d8;
    interface_7_out_0x55aeb433e578;
    interface_6_out_0x55aeb433e618;
    interface_6_out_0x55aeb433e5c8;
    interface_6_out_0x55aeb433e668;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x55aeb43a1900 [label="N", shape=none];
    interface_8_in_0x55aeb637c590 [label="C_out", shape=none];
    interface_8_in_0x55aeb908ff90 [label="H", shape=none];
    interface_8_in_0x55aeb9090f10 [label="H", shape=none];
}
interface_0_out_0x55aeb43a1900 -> interface_8_in_0x55aeb43a1900;
interface_0_out_0x55aeb637c590 -> interface_8_in_0x55aeb637c590;
interface_0_out_0x55aeb908ff90 -> interface_8_in_0x55aeb908ff90;
interface_0_out_0x55aeb9090f10 -> interface_8_in_0x55aeb9090f10;

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

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1024, 3584, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 56, 3, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnim, jik -> ljnimk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 2, 56, 3, 56, 1, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 32, 56, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 56, 3, 56, 1, ))

		# Perform contraction.
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1024, 1792, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnim, jik -> ljnimk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 2, 28, 3, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 32, 28, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 28, 3, 28, 2, ))

		# Perform contraction.
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1024, 3584, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnim, jik -> ljnimk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 4, 28, 3, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 32, 28, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 28, 3, 28, 2, ))

		# Perform contraction.
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1024, 1792, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnim, jik -> ljnimk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 4, 14, 3, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 32, 14, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 14, 3, 14, 4, ))

		# Perform contraction.
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1024, 3584, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 256, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnim, jik -> ljnimk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 8, 14, 3, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 32, 14, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 14, 3, 14, 4, ))

		# Perform contraction.
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1024, 1792, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 256, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnim, jik -> ljnimk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 8, 7, 3, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 32, 7, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 7, 3, 7, 8, ))

		# Perform contraction.
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

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

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1024, 3584, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 512, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("ljnim, jik -> ljnimk", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 16, 7, 3, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 32, 7, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 7, 3, 7, 8, ))

		# Perform contraction.
		t_7 = torch.einsum("nljokpm, iljkm -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

