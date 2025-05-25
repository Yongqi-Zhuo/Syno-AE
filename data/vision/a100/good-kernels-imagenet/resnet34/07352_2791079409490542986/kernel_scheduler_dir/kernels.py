import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7fc218001928 [label="Sum", shape=box];
    reduce_0x7fc218001a98 [label="Sum", shape=box];
    reduce_0x7fc218001ab0 [label="Sum", shape=box];
    reduce_0x7fc218009288 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x5569250421b0 [label="N", shape=none];
        interface_0_out_0x5569250421d8 [label="C_out", shape=none];
        interface_0_out_0x556925042200 [label="H", shape=none];
        interface_0_out_0x556925042228 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc218001928;
        reduce_0x7fc218001a98;
        reduce_0x7fc218001ab0;
        reduce_0x7fc218009288;
        interface_0_out_0x5569250421b0;
        interface_0_out_0x5569250421d8;
        interface_0_out_0x556925042200;
        interface_0_out_0x556925042228;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5569250421b0 [label="N", shape=none];
        interface_0_in_0x55691eaf9e40 [label="g", shape=none];
        interface_0_in_0x556925042200 [label="H", shape=none];
        interface_0_in_0x55691eaf9e90 [label="k_1", shape=none];
        interface_0_in_0x556925042228 [label="H", shape=none];
        interface_0_in_0x55691eaf9f30 [label="k_1", shape=none];
        interface_0_in_0x55691eaf9ee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x55691eaf9e58 [label="g", shape=none];
        interface_0_in_0x55691eaf9ea8 [label="k_1", shape=none];
        interface_0_in_0x55691eaf9f48 [label="k_1", shape=none];
        interface_0_in_0x55691eaf9db8 [label="C_out", shape=none];
        interface_0_in_0x55691eaf9ef8 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5569250421b0;
        interface_0_in_0x55691eaf9e40;
        interface_0_in_0x556925042200;
        interface_0_in_0x55691eaf9e90;
        interface_0_in_0x556925042228;
        interface_0_in_0x55691eaf9f30;
        interface_0_in_0x55691eaf9ee0;
        interface_0_in_0x55691eaf9e58;
        interface_0_in_0x55691eaf9ea8;
        interface_0_in_0x55691eaf9f48;
        interface_0_in_0x55691eaf9db8;
        interface_0_in_0x55691eaf9ef8;
    }
    // Op's.
    op_0x55691ea6b578 [label="Expand"];
    op_0x55691eaf9d80 [label="Share"];
    op_0x55691eaf9e20 [label="Share"];
    op_0x55691eaf9e70 [label="Share"];
    op_0x55691eaf9ec0 [label="Share"];
    op_0x55691eaf9f10 [label="Share"];
    // Dimension's.
    op_0x55691ea6b578 -> op_0x55691eaf9d80 [label="C_out"];
    interface_0_in_0x55691eaf9db8 -> op_0x55691eaf9d80 [label="C_out"];
    interface_0_in_0x55691eaf9e40 -> op_0x55691eaf9e20 [label="g"];
    interface_0_in_0x55691eaf9e58 -> op_0x55691eaf9e20 [label="g"];
    interface_0_in_0x55691eaf9e90 -> op_0x55691eaf9e70 [label="k_1"];
    interface_0_in_0x55691eaf9ea8 -> op_0x55691eaf9e70 [label="k_1"];
    interface_0_in_0x55691eaf9ee0 -> op_0x55691eaf9ec0 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x55691eaf9ef8 -> op_0x55691eaf9ec0 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x55691eaf9f30 -> op_0x55691eaf9f10 [label="k_1"];
    interface_0_in_0x55691eaf9f48 -> op_0x55691eaf9f10 [label="k_1"];
    interface_0_in_0x5569250421b0 -> interface_0_out_0x5569250421b0 [label="N"];
    op_0x55691eaf9d80 -> interface_0_out_0x5569250421d8 [label="C_out"];
    interface_0_in_0x556925042200 -> interface_0_out_0x556925042200 [label="H"];
    interface_0_in_0x556925042228 -> interface_0_out_0x556925042228 [label="H"];
    op_0x55691eaf9e20 -> reduce_0x7fc218001928 [label="g"];
    op_0x55691eaf9e70 -> reduce_0x7fc218001a98 [label="k_1"];
    op_0x55691eaf9f10 -> reduce_0x7fc218001ab0 [label="k_1"];
    op_0x55691eaf9ec0 -> reduce_0x7fc218009288 [label="g^-1*s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5569250421b0 [label="N", shape=none];
        interface_1_out_0x55691eaf9e40 [label="g", shape=none];
        interface_1_out_0x556925042200 [label="H", shape=none];
        interface_1_out_0x55691eaf9e90 [label="k_1", shape=none];
        interface_1_out_0x556925042228 [label="H", shape=none];
        interface_1_out_0x55691eaf9f30 [label="k_1", shape=none];
        interface_1_out_0x55691eaf9ee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x5569250421b0;
        interface_1_out_0x55691eaf9e40;
        interface_1_out_0x556925042200;
        interface_1_out_0x55691eaf9e90;
        interface_1_out_0x556925042228;
        interface_1_out_0x55691eaf9f30;
        interface_1_out_0x55691eaf9ee0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5569250421b0 [label="N", shape=none];
        interface_1_in_0x55691eaf9e40 [label="g", shape=none];
        interface_1_in_0x55691ea9dae8 [label="H", shape=none];
        interface_1_in_0x556925042228 [label="H", shape=none];
        interface_1_in_0x55691eaf9f30 [label="k_1", shape=none];
        interface_1_in_0x55691eaf9ee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5569250421b0;
        interface_1_in_0x55691eaf9e40;
        interface_1_in_0x55691ea9dae8;
        interface_1_in_0x556925042228;
        interface_1_in_0x55691eaf9f30;
        interface_1_in_0x55691eaf9ee0;
    }
    // Op's.
    op_0x55691ea9dac0 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x55691ea9dae8 -> op_0x55691ea9dac0 [label="H"];
    interface_1_in_0x55691eaf9e40 -> interface_1_out_0x55691eaf9e40 [label="g"];
    op_0x55691ea9dac0 -> interface_1_out_0x55691eaf9e90 [label="k_1"];
    interface_1_in_0x55691eaf9ee0 -> interface_1_out_0x55691eaf9ee0 [label="g^-1*s^-1*C_out"];
    interface_1_in_0x55691eaf9f30 -> interface_1_out_0x55691eaf9f30 [label="k_1"];
    interface_1_in_0x5569250421b0 -> interface_1_out_0x5569250421b0 [label="N"];
    op_0x55691ea9dac0 -> interface_1_out_0x556925042200 [label="H"];
    interface_1_in_0x556925042228 -> interface_1_out_0x556925042228 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7fc218005a90 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5569250421b0 [label="N", shape=none];
        interface_2_out_0x55691eaf9e40 [label="g", shape=none];
        interface_2_out_0x55691ea9dae8 [label="H", shape=none];
        interface_2_out_0x556925042228 [label="H", shape=none];
        interface_2_out_0x55691eaf9f30 [label="k_1", shape=none];
        interface_2_out_0x55691eaf9ee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc218005a90;
        interface_2_out_0x5569250421b0;
        interface_2_out_0x55691eaf9e40;
        interface_2_out_0x55691ea9dae8;
        interface_2_out_0x556925042228;
        interface_2_out_0x55691eaf9f30;
        interface_2_out_0x55691eaf9ee0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5569250421b0 [label="N", shape=none];
        interface_2_in_0x55691eaa1e40 [label="C_in", shape=none];
        interface_2_in_0x55691ea9dae8 [label="H", shape=none];
        interface_2_in_0x556925042228 [label="H", shape=none];
        interface_2_in_0x55691eaf9f30 [label="k_1", shape=none];
        interface_2_in_0x55691eaf9ee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5569250421b0;
        interface_2_in_0x55691eaa1e40;
        interface_2_in_0x55691ea9dae8;
        interface_2_in_0x556925042228;
        interface_2_in_0x55691eaf9f30;
        interface_2_in_0x55691eaf9ee0;
    }
    // Op's.
    op_0x55691eaa1e00 [label="Split"];
    // Dimension's.
    interface_2_in_0x55691ea9dae8 -> interface_2_out_0x55691ea9dae8 [label="H"];
    interface_2_in_0x55691eaa1e40 -> op_0x55691eaa1e00 [label="C_in"];
    op_0x55691eaa1e00 -> interface_2_out_0x55691eaf9e40 [label="g"];
    interface_2_in_0x55691eaf9ee0 -> interface_2_out_0x55691eaf9ee0 [label="g^-1*s^-1*C_out"];
    interface_2_in_0x55691eaf9f30 -> interface_2_out_0x55691eaf9f30 [label="k_1"];
    interface_2_in_0x5569250421b0 -> interface_2_out_0x5569250421b0 [label="N"];
    interface_2_in_0x556925042228 -> interface_2_out_0x556925042228 [label="H"];
    op_0x55691eaa1e00 -> reduce_0x7fc218005a90 [label="g^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5569250421b0 [label="N", shape=none];
        interface_3_out_0x55691eaa1e40 [label="C_in", shape=none];
        interface_3_out_0x55691ea9dae8 [label="H", shape=none];
        interface_3_out_0x556925042228 [label="H", shape=none];
        interface_3_out_0x55691eaf9f30 [label="k_1", shape=none];
        interface_3_out_0x55691eaf9ee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5569250421b0;
        interface_3_out_0x55691eaa1e40;
        interface_3_out_0x55691ea9dae8;
        interface_3_out_0x556925042228;
        interface_3_out_0x55691eaf9f30;
        interface_3_out_0x55691eaf9ee0;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5569250421b0 [label="N", shape=none];
        interface_3_in_0x55691eafa110 [label="C_in", shape=none];
        interface_3_in_0x55691ea9dae8 [label="H", shape=none];
        interface_3_in_0x556925042228 [label="H", shape=none];
        interface_3_in_0x55691eab0860 [label="k_1", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x55691eafa128 [label="C_in", shape=none];
        interface_3_in_0x55691eab0878 [label="k_1", shape=none];
        interface_3_in_0x55691eaf9f98 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5569250421b0;
        interface_3_in_0x55691eafa110;
        interface_3_in_0x55691ea9dae8;
        interface_3_in_0x556925042228;
        interface_3_in_0x55691eab0860;
        interface_3_in_0x55691eafa128;
        interface_3_in_0x55691eab0878;
        interface_3_in_0x55691eaf9f98;
    }
    // Op's.
    op_0x55691ea6b598 [label="Expand"];
    op_0x55691eab0840 [label="Share"];
    op_0x55691eaf9f60 [label="Share"];
    op_0x55691eafa0f0 [label="Share"];
    // Dimension's.
    interface_3_in_0x55691ea9dae8 -> interface_3_out_0x55691ea9dae8 [label="H"];
    op_0x55691eafa0f0 -> interface_3_out_0x55691eaa1e40 [label="C_in"];
    interface_3_in_0x55691eab0860 -> op_0x55691eab0840 [label="k_1"];
    interface_3_in_0x55691eab0878 -> op_0x55691eab0840 [label="k_1"];
    op_0x55691eaf9f60 -> interface_3_out_0x55691eaf9ee0 [label="g^-1*s^-1*C_out"];
    op_0x55691eab0840 -> interface_3_out_0x55691eaf9f30 [label="k_1"];
    op_0x55691ea6b598 -> op_0x55691eaf9f60 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x55691eaf9f98 -> op_0x55691eaf9f60 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x55691eafa110 -> op_0x55691eafa0f0 [label="C_in"];
    interface_3_in_0x55691eafa128 -> op_0x55691eafa0f0 [label="C_in"];
    interface_3_in_0x5569250421b0 -> interface_3_out_0x5569250421b0 [label="N"];
    interface_3_in_0x556925042228 -> interface_3_out_0x556925042228 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x5569250421b0 [label="N", shape=none];
        interface_4_out_0x55691eafa110 [label="C_in", shape=none];
        interface_4_out_0x55691ea9dae8 [label="H", shape=none];
        interface_4_out_0x556925042228 [label="H", shape=none];
        interface_4_out_0x55691eab0860 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x5569250421b0;
        interface_4_out_0x55691eafa110;
        interface_4_out_0x55691ea9dae8;
        interface_4_out_0x556925042228;
        interface_4_out_0x55691eab0860;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x5569250421b0 [label="N", shape=none];
        interface_4_in_0x55691eafa110 [label="C_in", shape=none];
        interface_4_in_0x55691ea9dae8 [label="H", shape=none];
        interface_4_in_0x55691ea9dce8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x5569250421b0;
        interface_4_in_0x55691eafa110;
        interface_4_in_0x55691ea9dae8;
        interface_4_in_0x55691ea9dce8;
    }
    // Op's.
    op_0x55691ea9dcc0 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x55691ea9dae8 -> interface_4_out_0x55691ea9dae8 [label="H"];
    interface_4_in_0x55691ea9dce8 -> op_0x55691ea9dcc0 [label="H"];
    op_0x55691ea9dcc0 -> interface_4_out_0x55691eab0860 [label="k_1"];
    interface_4_in_0x55691eafa110 -> interface_4_out_0x55691eafa110 [label="C_in"];
    interface_4_in_0x5569250421b0 -> interface_4_out_0x5569250421b0 [label="N"];
    op_0x55691ea9dcc0 -> interface_4_out_0x556925042228 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x5569250421b0 [label="N", shape=none];
    interface_5_out_0x55691eafa110 [label="C_in", shape=none];
    interface_5_out_0x55691ea9dae8 [label="H", shape=none];
    interface_5_out_0x55691ea9dce8 [label="H", shape=none];
}

interface_5_out_0x5569250421b0 -> interface_4_in_0x5569250421b0;
interface_5_out_0x55691eafa110 -> interface_4_in_0x55691eafa110;
interface_5_out_0x55691ea9dae8 -> interface_4_in_0x55691ea9dae8;
interface_5_out_0x55691ea9dce8 -> interface_4_in_0x55691ea9dce8;

interface_4_out_0x5569250421b0 -> interface_3_in_0x5569250421b0;
interface_4_out_0x55691eafa110 -> interface_3_in_0x55691eafa110;
interface_4_out_0x55691ea9dae8 -> interface_3_in_0x55691ea9dae8;
interface_4_out_0x556925042228 -> interface_3_in_0x556925042228;
interface_4_out_0x55691eab0860 -> interface_3_in_0x55691eab0860;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x55691eafa128 [label="C_in", shape=none];
    interface_6_out_0x55691eab0878 [label="k_1", shape=none];
    interface_6_out_0x55691eaf9f98 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x55691eafa128 -> interface_3_in_0x55691eafa128;
interface_6_out_0x55691eab0878 -> interface_3_in_0x55691eab0878;
interface_6_out_0x55691eaf9f98 -> interface_3_in_0x55691eaf9f98;

interface_3_out_0x5569250421b0 -> interface_2_in_0x5569250421b0;
interface_3_out_0x55691eaa1e40 -> interface_2_in_0x55691eaa1e40;
interface_3_out_0x55691ea9dae8 -> interface_2_in_0x55691ea9dae8;
interface_3_out_0x556925042228 -> interface_2_in_0x556925042228;
interface_3_out_0x55691eaf9f30 -> interface_2_in_0x55691eaf9f30;
interface_3_out_0x55691eaf9ee0 -> interface_2_in_0x55691eaf9ee0;

interface_2_out_0x5569250421b0 -> interface_1_in_0x5569250421b0;
interface_2_out_0x55691eaf9e40 -> interface_1_in_0x55691eaf9e40;
interface_2_out_0x55691ea9dae8 -> interface_1_in_0x55691ea9dae8;
interface_2_out_0x556925042228 -> interface_1_in_0x556925042228;
interface_2_out_0x55691eaf9f30 -> interface_1_in_0x55691eaf9f30;
interface_2_out_0x55691eaf9ee0 -> interface_1_in_0x55691eaf9ee0;

interface_1_out_0x5569250421b0 -> interface_0_in_0x5569250421b0;
interface_1_out_0x55691eaf9e40 -> interface_0_in_0x55691eaf9e40;
interface_1_out_0x556925042200 -> interface_0_in_0x556925042200;
interface_1_out_0x55691eaf9e90 -> interface_0_in_0x55691eaf9e90;
interface_1_out_0x556925042228 -> interface_0_in_0x556925042228;
interface_1_out_0x55691eaf9f30 -> interface_0_in_0x55691eaf9f30;
interface_1_out_0x55691eaf9ee0 -> interface_0_in_0x55691eaf9ee0;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x55691eaf9e58 [label="g", shape=none];
    interface_7_out_0x55691eaf9ea8 [label="k_1", shape=none];
    interface_7_out_0x55691eaf9f48 [label="k_1", shape=none];
    interface_7_out_0x55691eaf9db8 [label="C_out", shape=none];
    interface_7_out_0x55691eaf9ef8 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x55691eaf9e58 -> interface_0_in_0x55691eaf9e58;
interface_7_out_0x55691eaf9ea8 -> interface_0_in_0x55691eaf9ea8;
interface_7_out_0x55691eaf9f48 -> interface_0_in_0x55691eaf9f48;
interface_7_out_0x55691eaf9db8 -> interface_0_in_0x55691eaf9db8;
interface_7_out_0x55691eaf9ef8 -> interface_0_in_0x55691eaf9ef8;

{
    rank = same;
    interface_5_out_0x5569250421b0;
    interface_5_out_0x55691eafa110;
    interface_5_out_0x55691ea9dae8;
    interface_5_out_0x55691ea9dce8;
    interface_7_out_0x55691eaf9e58;
    interface_7_out_0x55691eaf9ea8;
    interface_7_out_0x55691eaf9f48;
    interface_7_out_0x55691eaf9db8;
    interface_7_out_0x55691eaf9ef8;
    interface_6_out_0x55691eafa128;
    interface_6_out_0x55691eab0878;
    interface_6_out_0x55691eaf9f98;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x5569250421b0 [label="N", shape=none];
    interface_8_in_0x5569250421d8 [label="C_out", shape=none];
    interface_8_in_0x556925042200 [label="H", shape=none];
    interface_8_in_0x556925042228 [label="H", shape=none];
}
interface_0_out_0x5569250421b0 -> interface_8_in_0x5569250421b0;
interface_0_out_0x5569250421d8 -> interface_8_in_0x5569250421d8;
interface_0_out_0x556925042200 -> interface_8_in_0x556925042200;
interface_0_out_0x556925042228 -> interface_8_in_0x556925042228;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 64, 1]),
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

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mklni, kij -> mklnij", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 2, 56, 56, 3, 1, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 32, 56, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 56, 56, 3, 1, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("njokpml, jkmil -> nopi", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 128, 2]),
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

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mklni, kij -> mklnij", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 2, 28, 28, 3, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 32, 28, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 28, 28, 3, 2, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("njokpml, jkmil -> nopi", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 128, 2]),
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

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mklni, kij -> mklnij", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 4, 28, 28, 3, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 32, 28, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 28, 28, 3, 2, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("njokpml, jkmil -> nopi", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 256, 4]),
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

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mklni, kij -> mklnij", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 4, 14, 14, 3, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 32, 14, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 14, 14, 3, 4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("njokpml, jkmil -> nopi", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 256, 4]),
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

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mklni, kij -> mklnij", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 8, 14, 14, 3, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 32, 14, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 14, 14, 3, 4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("njokpml, jkmil -> nopi", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 512, 8]),
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

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mklni, kij -> mklnij", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 8, 7, 7, 3, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 32, 7, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 7, 7, 3, 8, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("njokpml, jkmil -> nopi", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 512, 8]),
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

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mklni, kij -> mklnij", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 16, 7, 7, 3, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1024, 32, 7, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 7, 7, 3, 8, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, 5, 6, ))

		# Perform contraction.
		t_7 = torch.einsum("njokpml, jkmil -> nopi", t_6, in_1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_7

		return y

