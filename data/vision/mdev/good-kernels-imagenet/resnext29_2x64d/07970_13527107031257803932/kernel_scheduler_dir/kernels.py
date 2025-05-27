import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x55d1b69697c0 [label="N", shape=none];
        interface_0_out_0x55d1b69697e8 [label="C_out", shape=none];
        interface_0_out_0x55d1b6969810 [label="H", shape=none];
        interface_0_out_0x55d1b6969838 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55d1b69697c0;
        interface_0_out_0x55d1b69697e8;
        interface_0_out_0x55d1b6969810;
        interface_0_out_0x55d1b6969838;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55d1b69697c0 [label="N", shape=none];
        interface_0_in_0x55d1ce270300 [label="g", shape=none];
        interface_0_in_0x55d1ce270318 [label="g^-1*C_out", shape=none];
        interface_0_in_0x55d1b6969810 [label="H", shape=none];
        interface_0_in_0x55d1b6969838 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55d1b69697c0;
        interface_0_in_0x55d1ce270300;
        interface_0_in_0x55d1ce270318;
        interface_0_in_0x55d1b6969810;
        interface_0_in_0x55d1b6969838;
    }
    // Op's.
    op_0x55d1ce2702c0 [label="Merge"];
    // Dimension's.
    interface_0_in_0x55d1b69697c0 -> interface_0_out_0x55d1b69697c0 [label="N"];
    op_0x55d1ce2702c0 -> interface_0_out_0x55d1b69697e8 [label="C_out"];
    interface_0_in_0x55d1b6969810 -> interface_0_out_0x55d1b6969810 [label="H"];
    interface_0_in_0x55d1b6969838 -> interface_0_out_0x55d1b6969838 [label="H"];
    interface_0_in_0x55d1ce270300 -> op_0x55d1ce2702c0 [label="g"];
    interface_0_in_0x55d1ce270318 -> op_0x55d1ce2702c0 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f2690007720 [label="Sum", shape=box];
    reduce_0x7f2690003a98 [label="Sum", shape=box];
    reduce_0x7f2690003ab0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55d1b69697c0 [label="N", shape=none];
        interface_1_out_0x55d1ce270300 [label="g", shape=none];
        interface_1_out_0x55d1ce270318 [label="g^-1*C_out", shape=none];
        interface_1_out_0x55d1b6969810 [label="H", shape=none];
        interface_1_out_0x55d1b6969838 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f2690007720;
        reduce_0x7f2690003a98;
        reduce_0x7f2690003ab0;
        interface_1_out_0x55d1b69697c0;
        interface_1_out_0x55d1ce270300;
        interface_1_out_0x55d1ce270318;
        interface_1_out_0x55d1b6969810;
        interface_1_out_0x55d1b6969838;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55d1b69697c0 [label="N", shape=none];
        interface_1_in_0x55d1ce270318 [label="g^-1*C_out", shape=none];
        interface_1_in_0x55d1ce264cf0 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x55d1ce264d90 [label="k_1", shape=none];
        interface_1_in_0x55d1b6969810 [label="H", shape=none];
        interface_1_in_0x55d1ce264de0 [label="k_1", shape=none];
        interface_1_in_0x55d1b6969838 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55d1ce264e48 [label="g", shape=none];
        interface_1_in_0x55d1ce264d08 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x55d1ce264da8 [label="k_1", shape=none];
        interface_1_in_0x55d1ce264df8 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55d1b69697c0;
        interface_1_in_0x55d1ce270318;
        interface_1_in_0x55d1ce264cf0;
        interface_1_in_0x55d1ce264d90;
        interface_1_in_0x55d1b6969810;
        interface_1_in_0x55d1ce264de0;
        interface_1_in_0x55d1b6969838;
        interface_1_in_0x55d1ce264e48;
        interface_1_in_0x55d1ce264d08;
        interface_1_in_0x55d1ce264da8;
        interface_1_in_0x55d1ce264df8;
    }
    // Op's.
    op_0x55d1ce264cd0 [label="Share"];
    op_0x55d1ce264d70 [label="Share"];
    op_0x55d1ce264dc0 [label="Share"];
    op_0x55d1ce264e10 [label="Share"];
    op_0x55d1ce265178 [label="Expand"];
    // Dimension's.
    interface_1_in_0x55d1b69697c0 -> interface_1_out_0x55d1b69697c0 [label="N"];
    interface_1_in_0x55d1b6969810 -> interface_1_out_0x55d1b6969810 [label="H"];
    interface_1_in_0x55d1b6969838 -> interface_1_out_0x55d1b6969838 [label="H"];
    interface_1_in_0x55d1ce264cf0 -> op_0x55d1ce264cd0 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x55d1ce264d08 -> op_0x55d1ce264cd0 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x55d1ce264d90 -> op_0x55d1ce264d70 [label="k_1"];
    interface_1_in_0x55d1ce264da8 -> op_0x55d1ce264d70 [label="k_1"];
    interface_1_in_0x55d1ce264de0 -> op_0x55d1ce264dc0 [label="k_1"];
    interface_1_in_0x55d1ce264df8 -> op_0x55d1ce264dc0 [label="k_1"];
    op_0x55d1ce265178 -> op_0x55d1ce264e10 [label="g"];
    interface_1_in_0x55d1ce264e48 -> op_0x55d1ce264e10 [label="g"];
    op_0x55d1ce264e10 -> interface_1_out_0x55d1ce270300 [label="g"];
    interface_1_in_0x55d1ce270318 -> interface_1_out_0x55d1ce270318 [label="g^-1*C_out"];
    op_0x55d1ce264d70 -> reduce_0x7f2690003a98 [label="k_1"];
    op_0x55d1ce264dc0 -> reduce_0x7f2690003ab0 [label="k_1"];
    op_0x55d1ce264cd0 -> reduce_0x7f2690007720 [label="g^-1*s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55d1b69697c0 [label="N", shape=none];
        interface_2_out_0x55d1ce270318 [label="g^-1*C_out", shape=none];
        interface_2_out_0x55d1ce264cf0 [label="g^-1*s^-1*C_in", shape=none];
        interface_2_out_0x55d1ce264d90 [label="k_1", shape=none];
        interface_2_out_0x55d1b6969810 [label="H", shape=none];
        interface_2_out_0x55d1ce264de0 [label="k_1", shape=none];
        interface_2_out_0x55d1b6969838 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x55d1b69697c0;
        interface_2_out_0x55d1ce270318;
        interface_2_out_0x55d1ce264cf0;
        interface_2_out_0x55d1ce264d90;
        interface_2_out_0x55d1b6969810;
        interface_2_out_0x55d1ce264de0;
        interface_2_out_0x55d1b6969838;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55d1b69697c0 [label="N", shape=none];
        interface_2_in_0x55d1ce270318 [label="g^-1*C_out", shape=none];
        interface_2_in_0x55d1ce264cf0 [label="g^-1*s^-1*C_in", shape=none];
        interface_2_in_0x55d1ce286568 [label="H", shape=none];
        interface_2_in_0x55d1ce264de0 [label="k_1", shape=none];
        interface_2_in_0x55d1b6969838 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55d1b69697c0;
        interface_2_in_0x55d1ce270318;
        interface_2_in_0x55d1ce264cf0;
        interface_2_in_0x55d1ce286568;
        interface_2_in_0x55d1ce264de0;
        interface_2_in_0x55d1b6969838;
    }
    // Op's.
    op_0x55d1ce286540 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x55d1b69697c0 -> interface_2_out_0x55d1b69697c0 [label="N"];
    op_0x55d1ce286540 -> interface_2_out_0x55d1b6969810 [label="H"];
    interface_2_in_0x55d1b6969838 -> interface_2_out_0x55d1b6969838 [label="H"];
    interface_2_in_0x55d1ce264cf0 -> interface_2_out_0x55d1ce264cf0 [label="g^-1*s^-1*C_in"];
    op_0x55d1ce286540 -> interface_2_out_0x55d1ce264d90 [label="k_1"];
    interface_2_in_0x55d1ce264de0 -> interface_2_out_0x55d1ce264de0 [label="k_1"];
    interface_2_in_0x55d1ce270318 -> interface_2_out_0x55d1ce270318 [label="g^-1*C_out"];
    interface_2_in_0x55d1ce286568 -> op_0x55d1ce286540 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7f2690004f10 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55d1b69697c0 [label="N", shape=none];
        interface_3_out_0x55d1ce270318 [label="g^-1*C_out", shape=none];
        interface_3_out_0x55d1ce264cf0 [label="g^-1*s^-1*C_in", shape=none];
        interface_3_out_0x55d1ce286568 [label="H", shape=none];
        interface_3_out_0x55d1ce264de0 [label="k_1", shape=none];
        interface_3_out_0x55d1b6969838 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f2690004f10;
        interface_3_out_0x55d1b69697c0;
        interface_3_out_0x55d1ce270318;
        interface_3_out_0x55d1ce264cf0;
        interface_3_out_0x55d1ce286568;
        interface_3_out_0x55d1ce264de0;
        interface_3_out_0x55d1b6969838;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55d1b69697c0 [label="N", shape=none];
        interface_3_in_0x55d1ce2650b0 [label="g*s", shape=none];
        interface_3_in_0x55d1ce264cf0 [label="g^-1*s^-1*C_in", shape=none];
        interface_3_in_0x55d1ce286568 [label="H", shape=none];
        interface_3_in_0x55d1ce265010 [label="k_1", shape=none];
        interface_3_in_0x55d1b6969838 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x55d1ce265078 [label="g^-1*C_out", shape=none];
        interface_3_in_0x55d1ce2650c8 [label="g*s", shape=none];
        interface_3_in_0x55d1ce265028 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55d1b69697c0;
        interface_3_in_0x55d1ce2650b0;
        interface_3_in_0x55d1ce264cf0;
        interface_3_in_0x55d1ce286568;
        interface_3_in_0x55d1ce265010;
        interface_3_in_0x55d1b6969838;
        interface_3_in_0x55d1ce265078;
        interface_3_in_0x55d1ce2650c8;
        interface_3_in_0x55d1ce265028;
    }
    // Op's.
    op_0x55d1ce264ff0 [label="Share"];
    op_0x55d1ce265040 [label="Share"];
    op_0x55d1ce265090 [label="Share"];
    op_0x55d1ce2651d8 [label="Expand"];
    // Dimension's.
    interface_3_in_0x55d1b69697c0 -> interface_3_out_0x55d1b69697c0 [label="N"];
    interface_3_in_0x55d1b6969838 -> interface_3_out_0x55d1b6969838 [label="H"];
    interface_3_in_0x55d1ce264cf0 -> interface_3_out_0x55d1ce264cf0 [label="g^-1*s^-1*C_in"];
    op_0x55d1ce264ff0 -> interface_3_out_0x55d1ce264de0 [label="k_1"];
    interface_3_in_0x55d1ce265010 -> op_0x55d1ce264ff0 [label="k_1"];
    interface_3_in_0x55d1ce265028 -> op_0x55d1ce264ff0 [label="k_1"];
    op_0x55d1ce2651d8 -> op_0x55d1ce265040 [label="g^-1*C_out"];
    interface_3_in_0x55d1ce265078 -> op_0x55d1ce265040 [label="g^-1*C_out"];
    interface_3_in_0x55d1ce2650b0 -> op_0x55d1ce265090 [label="g*s"];
    interface_3_in_0x55d1ce2650c8 -> op_0x55d1ce265090 [label="g*s"];
    op_0x55d1ce265040 -> interface_3_out_0x55d1ce270318 [label="g^-1*C_out"];
    interface_3_in_0x55d1ce286568 -> interface_3_out_0x55d1ce286568 [label="H"];
    op_0x55d1ce265090 -> reduce_0x7f2690004f10 [label="g*s"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x55d1b69697c0 [label="N", shape=none];
        interface_4_out_0x55d1ce2650b0 [label="g*s", shape=none];
        interface_4_out_0x55d1ce264cf0 [label="g^-1*s^-1*C_in", shape=none];
        interface_4_out_0x55d1ce286568 [label="H", shape=none];
        interface_4_out_0x55d1ce265010 [label="k_1", shape=none];
        interface_4_out_0x55d1b6969838 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x55d1b69697c0;
        interface_4_out_0x55d1ce2650b0;
        interface_4_out_0x55d1ce264cf0;
        interface_4_out_0x55d1ce286568;
        interface_4_out_0x55d1ce265010;
        interface_4_out_0x55d1b6969838;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x55d1b69697c0 [label="N", shape=none];
        interface_4_in_0x55d1ce2a5be0 [label="C_in", shape=none];
        interface_4_in_0x55d1ce286568 [label="H", shape=none];
        interface_4_in_0x55d1ce2865e8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x55d1b69697c0;
        interface_4_in_0x55d1ce2a5be0;
        interface_4_in_0x55d1ce286568;
        interface_4_in_0x55d1ce2865e8;
    }
    // Op's.
    op_0x55d1ce2865c0 [label="Unfold"];
    op_0x55d1ce2a5ba0 [label="Split"];
    // Dimension's.
    interface_4_in_0x55d1b69697c0 -> interface_4_out_0x55d1b69697c0 [label="N"];
    op_0x55d1ce2865c0 -> interface_4_out_0x55d1b6969838 [label="H"];
    op_0x55d1ce2a5ba0 -> interface_4_out_0x55d1ce264cf0 [label="g^-1*s^-1*C_in"];
    op_0x55d1ce2865c0 -> interface_4_out_0x55d1ce265010 [label="k_1"];
    op_0x55d1ce2a5ba0 -> interface_4_out_0x55d1ce2650b0 [label="g*s"];
    interface_4_in_0x55d1ce286568 -> interface_4_out_0x55d1ce286568 [label="H"];
    interface_4_in_0x55d1ce2865e8 -> op_0x55d1ce2865c0 [label="H"];
    interface_4_in_0x55d1ce2a5be0 -> op_0x55d1ce2a5ba0 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x55d1b69697c0 [label="N", shape=none];
    interface_5_out_0x55d1ce2a5be0 [label="C_in", shape=none];
    interface_5_out_0x55d1ce286568 [label="H", shape=none];
    interface_5_out_0x55d1ce2865e8 [label="H", shape=none];
}

interface_5_out_0x55d1b69697c0 -> interface_4_in_0x55d1b69697c0;
interface_5_out_0x55d1ce2a5be0 -> interface_4_in_0x55d1ce2a5be0;
interface_5_out_0x55d1ce286568 -> interface_4_in_0x55d1ce286568;
interface_5_out_0x55d1ce2865e8 -> interface_4_in_0x55d1ce2865e8;

interface_4_out_0x55d1b69697c0 -> interface_3_in_0x55d1b69697c0;
interface_4_out_0x55d1ce2650b0 -> interface_3_in_0x55d1ce2650b0;
interface_4_out_0x55d1ce264cf0 -> interface_3_in_0x55d1ce264cf0;
interface_4_out_0x55d1ce286568 -> interface_3_in_0x55d1ce286568;
interface_4_out_0x55d1ce265010 -> interface_3_in_0x55d1ce265010;
interface_4_out_0x55d1b6969838 -> interface_3_in_0x55d1b6969838;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x55d1ce265078 [label="g^-1*C_out", shape=none];
    interface_6_out_0x55d1ce2650c8 [label="g*s", shape=none];
    interface_6_out_0x55d1ce265028 [label="k_1", shape=none];
}

interface_6_out_0x55d1ce265078 -> interface_3_in_0x55d1ce265078;
interface_6_out_0x55d1ce2650c8 -> interface_3_in_0x55d1ce2650c8;
interface_6_out_0x55d1ce265028 -> interface_3_in_0x55d1ce265028;

interface_3_out_0x55d1b69697c0 -> interface_2_in_0x55d1b69697c0;
interface_3_out_0x55d1ce270318 -> interface_2_in_0x55d1ce270318;
interface_3_out_0x55d1ce264cf0 -> interface_2_in_0x55d1ce264cf0;
interface_3_out_0x55d1ce286568 -> interface_2_in_0x55d1ce286568;
interface_3_out_0x55d1ce264de0 -> interface_2_in_0x55d1ce264de0;
interface_3_out_0x55d1b6969838 -> interface_2_in_0x55d1b6969838;

interface_2_out_0x55d1b69697c0 -> interface_1_in_0x55d1b69697c0;
interface_2_out_0x55d1ce270318 -> interface_1_in_0x55d1ce270318;
interface_2_out_0x55d1ce264cf0 -> interface_1_in_0x55d1ce264cf0;
interface_2_out_0x55d1ce264d90 -> interface_1_in_0x55d1ce264d90;
interface_2_out_0x55d1b6969810 -> interface_1_in_0x55d1b6969810;
interface_2_out_0x55d1ce264de0 -> interface_1_in_0x55d1ce264de0;
interface_2_out_0x55d1b6969838 -> interface_1_in_0x55d1b6969838;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x55d1ce264e48 [label="g", shape=none];
    interface_7_out_0x55d1ce264d08 [label="g^-1*s^-1*C_in", shape=none];
    interface_7_out_0x55d1ce264da8 [label="k_1", shape=none];
    interface_7_out_0x55d1ce264df8 [label="k_1", shape=none];
}

interface_7_out_0x55d1ce264e48 -> interface_1_in_0x55d1ce264e48;
interface_7_out_0x55d1ce264d08 -> interface_1_in_0x55d1ce264d08;
interface_7_out_0x55d1ce264da8 -> interface_1_in_0x55d1ce264da8;
interface_7_out_0x55d1ce264df8 -> interface_1_in_0x55d1ce264df8;

interface_1_out_0x55d1b69697c0 -> interface_0_in_0x55d1b69697c0;
interface_1_out_0x55d1ce270300 -> interface_0_in_0x55d1ce270300;
interface_1_out_0x55d1ce270318 -> interface_0_in_0x55d1ce270318;
interface_1_out_0x55d1b6969810 -> interface_0_in_0x55d1b6969810;
interface_1_out_0x55d1b6969838 -> interface_0_in_0x55d1b6969838;

{
    rank = same;
    interface_5_out_0x55d1b69697c0;
    interface_5_out_0x55d1ce2a5be0;
    interface_5_out_0x55d1ce286568;
    interface_5_out_0x55d1ce2865e8;
    interface_7_out_0x55d1ce264e48;
    interface_7_out_0x55d1ce264d08;
    interface_7_out_0x55d1ce264da8;
    interface_7_out_0x55d1ce264df8;
    interface_6_out_0x55d1ce265078;
    interface_6_out_0x55d1ce2650c8;
    interface_6_out_0x55d1ce265028;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x55d1b69697c0 [label="N", shape=none];
    interface_8_in_0x55d1b69697e8 [label="C_out", shape=none];
    interface_8_in_0x55d1b6969810 [label="H", shape=none];
    interface_8_in_0x55d1b6969838 [label="H", shape=none];
}
interface_0_out_0x55d1b69697c0 -> interface_8_in_0x55d1b69697c0;
interface_0_out_0x55d1b69697e8 -> interface_8_in_0x55d1b69697e8;
interface_0_out_0x55d1b6969810 -> interface_8_in_0x55d1b6969810;
interface_0_out_0x55d1b6969838 -> interface_8_in_0x55d1b6969838;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 2, 3, 3]),
			torch.randn([4, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split7156f2737a83a060 -> [g*s]@Sharedc15ce1c9326f917, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (1, 64, 2, 56, 56, ))

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 7168, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 2, 56, 3, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("lknoim, jki -> ljnoim", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_5 = torch.reshape(t_5, (1, 8, 56, 168, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (1, 4, 2, 3, 56, 3, 56, ))

		# Perform contraction.
		t_6 = torch.einsum("mpijnko, lijk -> mlpno", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 128, 56, 56, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 4, 3, 3]),
			torch.randn([8, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split7156f2737a83a060 -> [g*s]@Sharedc15ce1c9326f917, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (1, 64, 4, 28, 28, ))

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 7168, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 4, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("lknoim, jki -> ljnoim", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_5 = torch.reshape(t_5, (1, 32, 28, 84, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (1, 8, 4, 3, 28, 3, 28, ))

		# Perform contraction.
		t_6 = torch.einsum("mpijnko, lijk -> mlpno", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 256, 28, 28, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 8, 3, 3]),
			torch.randn([16, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split7156f2737a83a060 -> [g*s]@Sharedc15ce1c9326f917, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (1, 64, 8, 14, 14, ))

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 7168, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 8, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("lknoim, jki -> ljnoim", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_5 = torch.reshape(t_5, (1, 128, 14, 42, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (1, 16, 8, 3, 14, 3, 14, ))

		# Perform contraction.
		t_6 = torch.einsum("mpijnko, lijk -> mlpno", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 512, 14, 14, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 16, 3, 3]),
			torch.randn([32, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split7156f2737a83a060 -> [g*s]@Sharedc15ce1c9326f917, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (1, 64, 16, 7, 7, ))

		# [H]@Unfold90ae9d8acef524e0 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share63a88e0da5dce9dc
		t_3 = torch.reshape(t_3, (1, 7168, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 16, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("lknoim, jki -> ljnoim", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_5 = torch.reshape(t_5, (1, 512, 7, 21, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (1, 32, 16, 3, 7, 3, 7, ))

		# Perform contraction.
		t_6 = torch.einsum("mpijnko, lijk -> mlpno", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 1024, 7, 7, ))

		# No need to crop the output tensor.
		y = t_7

		return y

