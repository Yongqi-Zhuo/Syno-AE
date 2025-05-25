import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f7a80001928 [label="Sum", shape=box];
    reduce_0x7f7a80001ab0 [label="Sum", shape=box];
    reduce_0x7f7a80001a98 [label="Sum", shape=box];
    reduce_0x7f7a80009288 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x556456d73040 [label="N", shape=none];
        interface_0_out_0x556456d73068 [label="C_out", shape=none];
        interface_0_out_0x556456d73090 [label="H", shape=none];
        interface_0_out_0x556456d730b8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f7a80001928;
        reduce_0x7f7a80001ab0;
        reduce_0x7f7a80001a98;
        reduce_0x7f7a80009288;
        interface_0_out_0x556456d73040;
        interface_0_out_0x556456d73068;
        interface_0_out_0x556456d73090;
        interface_0_out_0x556456d730b8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x556456d73040 [label="N", shape=none];
        interface_0_in_0x55645d092cc0 [label="g", shape=none];
        interface_0_in_0x55645d092db0 [label="k_1", shape=none];
        interface_0_in_0x556456d73090 [label="H", shape=none];
        interface_0_in_0x55645d092d10 [label="k_1", shape=none];
        interface_0_in_0x556456d730b8 [label="H", shape=none];
        interface_0_in_0x55645d092d60 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x55645d092c38 [label="C_out", shape=none];
        interface_0_in_0x55645d092cd8 [label="g", shape=none];
        interface_0_in_0x55645d092dc8 [label="k_1", shape=none];
        interface_0_in_0x55645d092d28 [label="k_1", shape=none];
        interface_0_in_0x55645d092d78 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x556456d73040;
        interface_0_in_0x55645d092cc0;
        interface_0_in_0x55645d092db0;
        interface_0_in_0x556456d73090;
        interface_0_in_0x55645d092d10;
        interface_0_in_0x556456d730b8;
        interface_0_in_0x55645d092d60;
        interface_0_in_0x55645d092c38;
        interface_0_in_0x55645d092cd8;
        interface_0_in_0x55645d092dc8;
        interface_0_in_0x55645d092d28;
        interface_0_in_0x55645d092d78;
    }
    // Op's.
    op_0x55645c0c6938 [label="Expand"];
    op_0x55645d092c00 [label="Share"];
    op_0x55645d092ca0 [label="Share"];
    op_0x55645d092cf0 [label="Share"];
    op_0x55645d092d40 [label="Share"];
    op_0x55645d092d90 [label="Share"];
    // Dimension's.
    interface_0_in_0x556456d73040 -> interface_0_out_0x556456d73040 [label="N"];
    op_0x55645d092c00 -> interface_0_out_0x556456d73068 [label="C_out"];
    interface_0_in_0x556456d73090 -> interface_0_out_0x556456d73090 [label="H"];
    interface_0_in_0x556456d730b8 -> interface_0_out_0x556456d730b8 [label="H"];
    op_0x55645c0c6938 -> op_0x55645d092c00 [label="C_out"];
    interface_0_in_0x55645d092c38 -> op_0x55645d092c00 [label="C_out"];
    interface_0_in_0x55645d092cc0 -> op_0x55645d092ca0 [label="g"];
    interface_0_in_0x55645d092cd8 -> op_0x55645d092ca0 [label="g"];
    interface_0_in_0x55645d092d10 -> op_0x55645d092cf0 [label="k_1"];
    interface_0_in_0x55645d092d28 -> op_0x55645d092cf0 [label="k_1"];
    interface_0_in_0x55645d092d60 -> op_0x55645d092d40 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x55645d092d78 -> op_0x55645d092d40 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x55645d092db0 -> op_0x55645d092d90 [label="k_1"];
    interface_0_in_0x55645d092dc8 -> op_0x55645d092d90 [label="k_1"];
    op_0x55645d092ca0 -> reduce_0x7f7a80001928 [label="g"];
    op_0x55645d092cf0 -> reduce_0x7f7a80001a98 [label="k_1"];
    op_0x55645d092d90 -> reduce_0x7f7a80001ab0 [label="k_1"];
    op_0x55645d092d40 -> reduce_0x7f7a80009288 [label="g^-1*s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x556456d73040 [label="N", shape=none];
        interface_1_out_0x55645d092cc0 [label="g", shape=none];
        interface_1_out_0x55645d092db0 [label="k_1", shape=none];
        interface_1_out_0x556456d73090 [label="H", shape=none];
        interface_1_out_0x55645d092d10 [label="k_1", shape=none];
        interface_1_out_0x556456d730b8 [label="H", shape=none];
        interface_1_out_0x55645d092d60 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x556456d73040;
        interface_1_out_0x55645d092cc0;
        interface_1_out_0x55645d092db0;
        interface_1_out_0x556456d73090;
        interface_1_out_0x55645d092d10;
        interface_1_out_0x556456d730b8;
        interface_1_out_0x55645d092d60;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x556456d73040 [label="N", shape=none];
        interface_1_in_0x55645d092cc0 [label="g", shape=none];
        interface_1_in_0x55645d865b80 [label="H", shape=none];
        interface_1_in_0x55645d092d10 [label="k_1", shape=none];
        interface_1_in_0x556456d730b8 [label="H", shape=none];
        interface_1_in_0x55645d092d60 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x556456d73040;
        interface_1_in_0x55645d092cc0;
        interface_1_in_0x55645d865b80;
        interface_1_in_0x55645d092d10;
        interface_1_in_0x556456d730b8;
        interface_1_in_0x55645d092d60;
    }
    // Op's.
    op_0x55645c238f80 [label="Unfold"];
    op_0x55645d865b60 [label="Shift"];
    // Dimension's.
    interface_1_in_0x556456d73040 -> interface_1_out_0x556456d73040 [label="N"];
    op_0x55645c238f80 -> interface_1_out_0x556456d73090 [label="H"];
    interface_1_in_0x556456d730b8 -> interface_1_out_0x556456d730b8 [label="H"];
    op_0x55645d865b60 -> op_0x55645c238f80 [label="H"];
    interface_1_in_0x55645d092cc0 -> interface_1_out_0x55645d092cc0 [label="g"];
    interface_1_in_0x55645d092d10 -> interface_1_out_0x55645d092d10 [label="k_1"];
    interface_1_in_0x55645d092d60 -> interface_1_out_0x55645d092d60 [label="g^-1*s^-1*C_out"];
    op_0x55645c238f80 -> interface_1_out_0x55645d092db0 [label="k_1"];
    interface_1_in_0x55645d865b80 -> op_0x55645d865b60 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f7a80005a90 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x556456d73040 [label="N", shape=none];
        interface_2_out_0x55645d092cc0 [label="g", shape=none];
        interface_2_out_0x55645d865b80 [label="H", shape=none];
        interface_2_out_0x55645d092d10 [label="k_1", shape=none];
        interface_2_out_0x556456d730b8 [label="H", shape=none];
        interface_2_out_0x55645d092d60 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7f7a80005a90;
        interface_2_out_0x556456d73040;
        interface_2_out_0x55645d092cc0;
        interface_2_out_0x55645d865b80;
        interface_2_out_0x55645d092d10;
        interface_2_out_0x556456d730b8;
        interface_2_out_0x55645d092d60;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x556456d73040 [label="N", shape=none];
        interface_2_in_0x55645ba8fd10 [label="C_in", shape=none];
        interface_2_in_0x55645d865b80 [label="H", shape=none];
        interface_2_in_0x55645d092d10 [label="k_1", shape=none];
        interface_2_in_0x556456d730b8 [label="H", shape=none];
        interface_2_in_0x55645d092d60 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x556456d73040;
        interface_2_in_0x55645ba8fd10;
        interface_2_in_0x55645d865b80;
        interface_2_in_0x55645d092d10;
        interface_2_in_0x556456d730b8;
        interface_2_in_0x55645d092d60;
    }
    // Op's.
    op_0x55645ba8fcd0 [label="Split"];
    // Dimension's.
    interface_2_in_0x556456d73040 -> interface_2_out_0x556456d73040 [label="N"];
    interface_2_in_0x556456d730b8 -> interface_2_out_0x556456d730b8 [label="H"];
    interface_2_in_0x55645ba8fd10 -> op_0x55645ba8fcd0 [label="C_in"];
    op_0x55645ba8fcd0 -> interface_2_out_0x55645d092cc0 [label="g"];
    interface_2_in_0x55645d092d10 -> interface_2_out_0x55645d092d10 [label="k_1"];
    interface_2_in_0x55645d092d60 -> interface_2_out_0x55645d092d60 [label="g^-1*s^-1*C_out"];
    interface_2_in_0x55645d865b80 -> interface_2_out_0x55645d865b80 [label="H"];
    op_0x55645ba8fcd0 -> reduce_0x7f7a80005a90 [label="g^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x556456d73040 [label="N", shape=none];
        interface_3_out_0x55645ba8fd10 [label="C_in", shape=none];
        interface_3_out_0x55645d865b80 [label="H", shape=none];
        interface_3_out_0x55645d092d10 [label="k_1", shape=none];
        interface_3_out_0x556456d730b8 [label="H", shape=none];
        interface_3_out_0x55645d092d60 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x556456d73040;
        interface_3_out_0x55645ba8fd10;
        interface_3_out_0x55645d865b80;
        interface_3_out_0x55645d092d10;
        interface_3_out_0x556456d730b8;
        interface_3_out_0x55645d092d60;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x556456d73040 [label="N", shape=none];
        interface_3_in_0x55645d092f90 [label="C_in", shape=none];
        interface_3_in_0x55645d865b80 [label="H", shape=none];
        interface_3_in_0x55645d092e50 [label="k_1", shape=none];
        interface_3_in_0x556456d730b8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x55645d092fa8 [label="C_in", shape=none];
        interface_3_in_0x55645d092e68 [label="k_1", shape=none];
        interface_3_in_0x55645d092e18 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x556456d73040;
        interface_3_in_0x55645d092f90;
        interface_3_in_0x55645d865b80;
        interface_3_in_0x55645d092e50;
        interface_3_in_0x556456d730b8;
        interface_3_in_0x55645d092fa8;
        interface_3_in_0x55645d092e68;
        interface_3_in_0x55645d092e18;
    }
    // Op's.
    op_0x55645c0c6958 [label="Expand"];
    op_0x55645d092de0 [label="Share"];
    op_0x55645d092e30 [label="Share"];
    op_0x55645d092f70 [label="Share"];
    // Dimension's.
    interface_3_in_0x556456d73040 -> interface_3_out_0x556456d73040 [label="N"];
    interface_3_in_0x556456d730b8 -> interface_3_out_0x556456d730b8 [label="H"];
    op_0x55645d092f70 -> interface_3_out_0x55645ba8fd10 [label="C_in"];
    op_0x55645d092e30 -> interface_3_out_0x55645d092d10 [label="k_1"];
    op_0x55645d092de0 -> interface_3_out_0x55645d092d60 [label="g^-1*s^-1*C_out"];
    op_0x55645c0c6958 -> op_0x55645d092de0 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x55645d092e18 -> op_0x55645d092de0 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x55645d092e50 -> op_0x55645d092e30 [label="k_1"];
    interface_3_in_0x55645d092e68 -> op_0x55645d092e30 [label="k_1"];
    interface_3_in_0x55645d092f90 -> op_0x55645d092f70 [label="C_in"];
    interface_3_in_0x55645d092fa8 -> op_0x55645d092f70 [label="C_in"];
    interface_3_in_0x55645d865b80 -> interface_3_out_0x55645d865b80 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x556456d73040 [label="N", shape=none];
        interface_4_out_0x55645d092f90 [label="C_in", shape=none];
        interface_4_out_0x55645d865b80 [label="H", shape=none];
        interface_4_out_0x55645d092e50 [label="k_1", shape=none];
        interface_4_out_0x556456d730b8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x556456d73040;
        interface_4_out_0x55645d092f90;
        interface_4_out_0x55645d865b80;
        interface_4_out_0x55645d092e50;
        interface_4_out_0x556456d730b8;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x556456d73040 [label="N", shape=none];
        interface_4_in_0x55645d092f90 [label="C_in", shape=none];
        interface_4_in_0x55645d865b80 [label="H", shape=none];
        interface_4_in_0x55645c2390e8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x556456d73040;
        interface_4_in_0x55645d092f90;
        interface_4_in_0x55645d865b80;
        interface_4_in_0x55645c2390e8;
    }
    // Op's.
    op_0x55645c2390c0 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x556456d73040 -> interface_4_out_0x556456d73040 [label="N"];
    op_0x55645c2390c0 -> interface_4_out_0x556456d730b8 [label="H"];
    interface_4_in_0x55645c2390e8 -> op_0x55645c2390c0 [label="H"];
    op_0x55645c2390c0 -> interface_4_out_0x55645d092e50 [label="k_1"];
    interface_4_in_0x55645d092f90 -> interface_4_out_0x55645d092f90 [label="C_in"];
    interface_4_in_0x55645d865b80 -> interface_4_out_0x55645d865b80 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x556456d73040 [label="N", shape=none];
    interface_5_out_0x55645d092f90 [label="C_in", shape=none];
    interface_5_out_0x55645d865b80 [label="H", shape=none];
    interface_5_out_0x55645c2390e8 [label="H", shape=none];
}

interface_5_out_0x556456d73040 -> interface_4_in_0x556456d73040;
interface_5_out_0x55645d092f90 -> interface_4_in_0x55645d092f90;
interface_5_out_0x55645d865b80 -> interface_4_in_0x55645d865b80;
interface_5_out_0x55645c2390e8 -> interface_4_in_0x55645c2390e8;

interface_4_out_0x556456d73040 -> interface_3_in_0x556456d73040;
interface_4_out_0x55645d092f90 -> interface_3_in_0x55645d092f90;
interface_4_out_0x55645d865b80 -> interface_3_in_0x55645d865b80;
interface_4_out_0x55645d092e50 -> interface_3_in_0x55645d092e50;
interface_4_out_0x556456d730b8 -> interface_3_in_0x556456d730b8;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x55645d092fa8 [label="C_in", shape=none];
    interface_6_out_0x55645d092e68 [label="k_1", shape=none];
    interface_6_out_0x55645d092e18 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x55645d092fa8 -> interface_3_in_0x55645d092fa8;
interface_6_out_0x55645d092e68 -> interface_3_in_0x55645d092e68;
interface_6_out_0x55645d092e18 -> interface_3_in_0x55645d092e18;

interface_3_out_0x556456d73040 -> interface_2_in_0x556456d73040;
interface_3_out_0x55645ba8fd10 -> interface_2_in_0x55645ba8fd10;
interface_3_out_0x55645d865b80 -> interface_2_in_0x55645d865b80;
interface_3_out_0x55645d092d10 -> interface_2_in_0x55645d092d10;
interface_3_out_0x556456d730b8 -> interface_2_in_0x556456d730b8;
interface_3_out_0x55645d092d60 -> interface_2_in_0x55645d092d60;

interface_2_out_0x556456d73040 -> interface_1_in_0x556456d73040;
interface_2_out_0x55645d092cc0 -> interface_1_in_0x55645d092cc0;
interface_2_out_0x55645d865b80 -> interface_1_in_0x55645d865b80;
interface_2_out_0x55645d092d10 -> interface_1_in_0x55645d092d10;
interface_2_out_0x556456d730b8 -> interface_1_in_0x556456d730b8;
interface_2_out_0x55645d092d60 -> interface_1_in_0x55645d092d60;

interface_1_out_0x556456d73040 -> interface_0_in_0x556456d73040;
interface_1_out_0x55645d092cc0 -> interface_0_in_0x55645d092cc0;
interface_1_out_0x55645d092db0 -> interface_0_in_0x55645d092db0;
interface_1_out_0x556456d73090 -> interface_0_in_0x556456d73090;
interface_1_out_0x55645d092d10 -> interface_0_in_0x55645d092d10;
interface_1_out_0x556456d730b8 -> interface_0_in_0x556456d730b8;
interface_1_out_0x55645d092d60 -> interface_0_in_0x55645d092d60;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x55645d092c38 [label="C_out", shape=none];
    interface_7_out_0x55645d092cd8 [label="g", shape=none];
    interface_7_out_0x55645d092dc8 [label="k_1", shape=none];
    interface_7_out_0x55645d092d28 [label="k_1", shape=none];
    interface_7_out_0x55645d092d78 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x55645d092c38 -> interface_0_in_0x55645d092c38;
interface_7_out_0x55645d092cd8 -> interface_0_in_0x55645d092cd8;
interface_7_out_0x55645d092dc8 -> interface_0_in_0x55645d092dc8;
interface_7_out_0x55645d092d28 -> interface_0_in_0x55645d092d28;
interface_7_out_0x55645d092d78 -> interface_0_in_0x55645d092d78;

{
    rank = same;
    interface_5_out_0x556456d73040;
    interface_5_out_0x55645d092f90;
    interface_5_out_0x55645d865b80;
    interface_5_out_0x55645c2390e8;
    interface_7_out_0x55645d092c38;
    interface_7_out_0x55645d092cd8;
    interface_7_out_0x55645d092dc8;
    interface_7_out_0x55645d092d28;
    interface_7_out_0x55645d092d78;
    interface_6_out_0x55645d092fa8;
    interface_6_out_0x55645d092e68;
    interface_6_out_0x55645d092e18;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x556456d73040 [label="N", shape=none];
    interface_8_in_0x556456d73068 [label="C_out", shape=none];
    interface_8_in_0x556456d73090 [label="H", shape=none];
    interface_8_in_0x556456d730b8 [label="H", shape=none];
}
interface_0_out_0x556456d73040 -> interface_8_in_0x556456d73040;
interface_0_out_0x556456d73068 -> interface_8_in_0x556456d73068;
interface_0_out_0x556456d73090 -> interface_8_in_0x556456d73090;
interface_0_out_0x556456d730b8 -> interface_8_in_0x556456d730b8;

}

"""
class kernel_generated_0(torch.nn.Module):
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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (1024, 3584, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 56, 3, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, kji -> lknjmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 2, 56, 3, 56, 1, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 56, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 56, 3, 56, 1, ))

		# Perform contraction.
		t_7 = torch.einsum("njmokpl, ijmkl -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_1(torch.nn.Module):
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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (1024, 1792, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, kji -> lknjmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 2, 28, 3, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 28, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 28, 3, 28, 2, ))

		# Perform contraction.
		t_7 = torch.einsum("njmokpl, ijmkl -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_2(torch.nn.Module):
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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (1024, 3584, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, kji -> lknjmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 4, 28, 3, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 28, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 28, 3, 28, 2, ))

		# Perform contraction.
		t_7 = torch.einsum("njmokpl, ijmkl -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_3(torch.nn.Module):
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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (1024, 1792, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, kji -> lknjmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 4, 14, 3, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 14, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 14, 3, 14, 4, ))

		# Perform contraction.
		t_7 = torch.einsum("njmokpl, ijmkl -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_4(torch.nn.Module):
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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (1024, 3584, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 256, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, kji -> lknjmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 8, 14, 3, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 14, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 14, 3, 14, 4, ))

		# Perform contraction.
		t_7 = torch.einsum("njmokpl, ijmkl -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_5(torch.nn.Module):
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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (1024, 1792, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 256, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, kji -> lknjmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 8, 7, 3, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 7, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 7, 3, 7, 8, ))

		# Perform contraction.
		t_7 = torch.einsum("njmokpl, ijmkl -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_6(torch.nn.Module):
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

		# [H]@Unfolde3f17abf629a5707 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareffd3dd34f2fd42e9
		t_3 = torch.reshape(t_3, (1024, 3584, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 512, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, kji -> lknjmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (1024, 32, 16, 7, 3, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_6 = torch.reshape(t_6, (1024, 32, 7, 168, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1024, 32, 3, 7, 3, 7, 8, ))

		# Perform contraction.
		t_7 = torch.einsum("njmokpl, ijmkl -> niop", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

