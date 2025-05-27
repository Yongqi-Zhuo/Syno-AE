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
        interface_1_in_0x55d1ce264f70 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x55d1b6969810 [label="H", shape=none];
        interface_1_in_0x55d1ce264fc0 [label="k_1", shape=none];
        interface_1_in_0x55d1b6969838 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55d1ce264ee8 [label="g", shape=none];
        interface_1_in_0x55d1ce264f88 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x55d1ce264fd8 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55d1b69697c0;
        interface_1_in_0x55d1ce270318;
        interface_1_in_0x55d1ce264f70;
        interface_1_in_0x55d1b6969810;
        interface_1_in_0x55d1ce264fc0;
        interface_1_in_0x55d1b6969838;
        interface_1_in_0x55d1ce264ee8;
        interface_1_in_0x55d1ce264f88;
        interface_1_in_0x55d1ce264fd8;
    }
    // Op's.
    op_0x55d1ce264eb0 [label="Share"];
    op_0x55d1ce264f50 [label="Share"];
    op_0x55d1ce264fa0 [label="Share"];
    op_0x55d1ce2651b8 [label="Expand"];
    // Dimension's.
    interface_1_in_0x55d1b69697c0 -> interface_1_out_0x55d1b69697c0 [label="N"];
    interface_1_in_0x55d1b6969810 -> interface_1_out_0x55d1b6969810 [label="H"];
    interface_1_in_0x55d1b6969838 -> interface_1_out_0x55d1b6969838 [label="H"];
    op_0x55d1ce2651b8 -> op_0x55d1ce264eb0 [label="g"];
    interface_1_in_0x55d1ce264ee8 -> op_0x55d1ce264eb0 [label="g"];
    interface_1_in_0x55d1ce264f70 -> op_0x55d1ce264f50 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x55d1ce264f88 -> op_0x55d1ce264f50 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x55d1ce264fc0 -> op_0x55d1ce264fa0 [label="k_1"];
    interface_1_in_0x55d1ce264fd8 -> op_0x55d1ce264fa0 [label="k_1"];
    op_0x55d1ce264eb0 -> interface_1_out_0x55d1ce270300 [label="g"];
    interface_1_in_0x55d1ce270318 -> interface_1_out_0x55d1ce270318 [label="g^-1*C_out"];
    op_0x55d1ce264fa0 -> reduce_0x7f2690003a98 [label="k_1"];
    op_0x55d1ce264f50 -> reduce_0x7f2690007720 [label="g^-1*s^-1*C_in"];
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
        interface_2_out_0x55d1ce264f70 [label="g^-1*s^-1*C_in", shape=none];
        interface_2_out_0x55d1b6969810 [label="H", shape=none];
        interface_2_out_0x55d1ce264fc0 [label="k_1", shape=none];
        interface_2_out_0x55d1b6969838 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x55d1b69697c0;
        interface_2_out_0x55d1ce270318;
        interface_2_out_0x55d1ce264f70;
        interface_2_out_0x55d1b6969810;
        interface_2_out_0x55d1ce264fc0;
        interface_2_out_0x55d1b6969838;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55d1b69697c0 [label="N", shape=none];
        interface_2_in_0x55d1ce270318 [label="g^-1*C_out", shape=none];
        interface_2_in_0x55d1ce264f70 [label="g^-1*s^-1*C_in", shape=none];
        interface_2_in_0x55d1b6969810 [label="H", shape=none];
        interface_2_in_0x55d1ce2864a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55d1b69697c0;
        interface_2_in_0x55d1ce270318;
        interface_2_in_0x55d1ce264f70;
        interface_2_in_0x55d1b6969810;
        interface_2_in_0x55d1ce2864a8;
    }
    // Op's.
    op_0x55d1ce286480 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x55d1b69697c0 -> interface_2_out_0x55d1b69697c0 [label="N"];
    interface_2_in_0x55d1b6969810 -> interface_2_out_0x55d1b6969810 [label="H"];
    op_0x55d1ce286480 -> interface_2_out_0x55d1b6969838 [label="H"];
    interface_2_in_0x55d1ce264f70 -> interface_2_out_0x55d1ce264f70 [label="g^-1*s^-1*C_in"];
    op_0x55d1ce286480 -> interface_2_out_0x55d1ce264fc0 [label="k_1"];
    interface_2_in_0x55d1ce270318 -> interface_2_out_0x55d1ce270318 [label="g^-1*C_out"];
    interface_2_in_0x55d1ce2864a8 -> op_0x55d1ce286480 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7f2690004f10 [label="Sum", shape=box];
    reduce_0x7f2690003ab0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55d1b69697c0 [label="N", shape=none];
        interface_3_out_0x55d1ce270318 [label="g^-1*C_out", shape=none];
        interface_3_out_0x55d1ce264f70 [label="g^-1*s^-1*C_in", shape=none];
        interface_3_out_0x55d1b6969810 [label="H", shape=none];
        interface_3_out_0x55d1ce2864a8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f2690004f10;
        reduce_0x7f2690003ab0;
        interface_3_out_0x55d1b69697c0;
        interface_3_out_0x55d1ce270318;
        interface_3_out_0x55d1ce264f70;
        interface_3_out_0x55d1b6969810;
        interface_3_out_0x55d1ce2864a8;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55d1b69697c0 [label="N", shape=none];
        interface_3_in_0x55d1ce264d40 [label="g*s", shape=none];
        interface_3_in_0x55d1ce264f70 [label="g^-1*s^-1*C_in", shape=none];
        interface_3_in_0x55d1ce264de0 [label="k_1", shape=none];
        interface_3_in_0x55d1b6969810 [label="H", shape=none];
        interface_3_in_0x55d1ce2864a8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x55d1ce264e98 [label="g^-1*C_out", shape=none];
        interface_3_in_0x55d1ce264d58 [label="g*s", shape=none];
        interface_3_in_0x55d1ce264df8 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55d1b69697c0;
        interface_3_in_0x55d1ce264d40;
        interface_3_in_0x55d1ce264f70;
        interface_3_in_0x55d1ce264de0;
        interface_3_in_0x55d1b6969810;
        interface_3_in_0x55d1ce2864a8;
        interface_3_in_0x55d1ce264e98;
        interface_3_in_0x55d1ce264d58;
        interface_3_in_0x55d1ce264df8;
    }
    // Op's.
    op_0x55d1ce264d20 [label="Share"];
    op_0x55d1ce264dc0 [label="Share"];
    op_0x55d1ce264e60 [label="Share"];
    op_0x55d1ce265198 [label="Expand"];
    // Dimension's.
    interface_3_in_0x55d1b69697c0 -> interface_3_out_0x55d1b69697c0 [label="N"];
    interface_3_in_0x55d1b6969810 -> interface_3_out_0x55d1b6969810 [label="H"];
    interface_3_in_0x55d1ce264d40 -> op_0x55d1ce264d20 [label="g*s"];
    interface_3_in_0x55d1ce264d58 -> op_0x55d1ce264d20 [label="g*s"];
    interface_3_in_0x55d1ce264de0 -> op_0x55d1ce264dc0 [label="k_1"];
    interface_3_in_0x55d1ce264df8 -> op_0x55d1ce264dc0 [label="k_1"];
    op_0x55d1ce265198 -> op_0x55d1ce264e60 [label="g^-1*C_out"];
    interface_3_in_0x55d1ce264e98 -> op_0x55d1ce264e60 [label="g^-1*C_out"];
    interface_3_in_0x55d1ce264f70 -> interface_3_out_0x55d1ce264f70 [label="g^-1*s^-1*C_in"];
    op_0x55d1ce264e60 -> interface_3_out_0x55d1ce270318 [label="g^-1*C_out"];
    interface_3_in_0x55d1ce2864a8 -> interface_3_out_0x55d1ce2864a8 [label="H"];
    op_0x55d1ce264dc0 -> reduce_0x7f2690003ab0 [label="k_1"];
    op_0x55d1ce264d20 -> reduce_0x7f2690004f10 [label="g*s"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x55d1b69697c0 [label="N", shape=none];
        interface_4_out_0x55d1ce264d40 [label="g*s", shape=none];
        interface_4_out_0x55d1ce264f70 [label="g^-1*s^-1*C_in", shape=none];
        interface_4_out_0x55d1ce264de0 [label="k_1", shape=none];
        interface_4_out_0x55d1b6969810 [label="H", shape=none];
        interface_4_out_0x55d1ce2864a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x55d1b69697c0;
        interface_4_out_0x55d1ce264d40;
        interface_4_out_0x55d1ce264f70;
        interface_4_out_0x55d1ce264de0;
        interface_4_out_0x55d1b6969810;
        interface_4_out_0x55d1ce2864a8;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x55d1b69697c0 [label="N", shape=none];
        interface_4_in_0x55d1ce27a750 [label="C_in", shape=none];
        interface_4_in_0x55d1ce266c80 [label="H", shape=none];
        interface_4_in_0x55d1ce2864a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x55d1b69697c0;
        interface_4_in_0x55d1ce27a750;
        interface_4_in_0x55d1ce266c80;
        interface_4_in_0x55d1ce2864a8;
    }
    // Op's.
    op_0x55d1ce266c60 [label="Shift"];
    op_0x55d1ce27a710 [label="Split"];
    op_0x55d1ce286400 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x55d1b69697c0 -> interface_4_out_0x55d1b69697c0 [label="N"];
    op_0x55d1ce286400 -> interface_4_out_0x55d1b6969810 [label="H"];
    op_0x55d1ce27a710 -> interface_4_out_0x55d1ce264d40 [label="g*s"];
    op_0x55d1ce286400 -> interface_4_out_0x55d1ce264de0 [label="k_1"];
    op_0x55d1ce27a710 -> interface_4_out_0x55d1ce264f70 [label="g^-1*s^-1*C_in"];
    interface_4_in_0x55d1ce266c80 -> op_0x55d1ce266c60 [label="H"];
    interface_4_in_0x55d1ce27a750 -> op_0x55d1ce27a710 [label="C_in"];
    op_0x55d1ce266c60 -> op_0x55d1ce286400 [label="H"];
    interface_4_in_0x55d1ce2864a8 -> interface_4_out_0x55d1ce2864a8 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x55d1b69697c0 [label="N", shape=none];
    interface_5_out_0x55d1ce27a750 [label="C_in", shape=none];
    interface_5_out_0x55d1ce266c80 [label="H", shape=none];
    interface_5_out_0x55d1ce2864a8 [label="H", shape=none];
}

interface_5_out_0x55d1b69697c0 -> interface_4_in_0x55d1b69697c0;
interface_5_out_0x55d1ce27a750 -> interface_4_in_0x55d1ce27a750;
interface_5_out_0x55d1ce266c80 -> interface_4_in_0x55d1ce266c80;
interface_5_out_0x55d1ce2864a8 -> interface_4_in_0x55d1ce2864a8;

interface_4_out_0x55d1b69697c0 -> interface_3_in_0x55d1b69697c0;
interface_4_out_0x55d1ce264d40 -> interface_3_in_0x55d1ce264d40;
interface_4_out_0x55d1ce264f70 -> interface_3_in_0x55d1ce264f70;
interface_4_out_0x55d1ce264de0 -> interface_3_in_0x55d1ce264de0;
interface_4_out_0x55d1b6969810 -> interface_3_in_0x55d1b6969810;
interface_4_out_0x55d1ce2864a8 -> interface_3_in_0x55d1ce2864a8;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 1";
    interface_6_out_0x55d1ce264e98 [label="g^-1*C_out", shape=none];
    interface_6_out_0x55d1ce264d58 [label="g*s", shape=none];
    interface_6_out_0x55d1ce264df8 [label="k_1", shape=none];
}

interface_6_out_0x55d1ce264e98 -> interface_3_in_0x55d1ce264e98;
interface_6_out_0x55d1ce264d58 -> interface_3_in_0x55d1ce264d58;
interface_6_out_0x55d1ce264df8 -> interface_3_in_0x55d1ce264df8;

interface_3_out_0x55d1b69697c0 -> interface_2_in_0x55d1b69697c0;
interface_3_out_0x55d1ce270318 -> interface_2_in_0x55d1ce270318;
interface_3_out_0x55d1ce264f70 -> interface_2_in_0x55d1ce264f70;
interface_3_out_0x55d1b6969810 -> interface_2_in_0x55d1b6969810;
interface_3_out_0x55d1ce2864a8 -> interface_2_in_0x55d1ce2864a8;

interface_2_out_0x55d1b69697c0 -> interface_1_in_0x55d1b69697c0;
interface_2_out_0x55d1ce270318 -> interface_1_in_0x55d1ce270318;
interface_2_out_0x55d1ce264f70 -> interface_1_in_0x55d1ce264f70;
interface_2_out_0x55d1b6969810 -> interface_1_in_0x55d1b6969810;
interface_2_out_0x55d1ce264fc0 -> interface_1_in_0x55d1ce264fc0;
interface_2_out_0x55d1b6969838 -> interface_1_in_0x55d1b6969838;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 2";
    interface_7_out_0x55d1ce264ee8 [label="g", shape=none];
    interface_7_out_0x55d1ce264f88 [label="g^-1*s^-1*C_in", shape=none];
    interface_7_out_0x55d1ce264fd8 [label="k_1", shape=none];
}

interface_7_out_0x55d1ce264ee8 -> interface_1_in_0x55d1ce264ee8;
interface_7_out_0x55d1ce264f88 -> interface_1_in_0x55d1ce264f88;
interface_7_out_0x55d1ce264fd8 -> interface_1_in_0x55d1ce264fd8;

interface_1_out_0x55d1b69697c0 -> interface_0_in_0x55d1b69697c0;
interface_1_out_0x55d1ce270300 -> interface_0_in_0x55d1ce270300;
interface_1_out_0x55d1ce270318 -> interface_0_in_0x55d1ce270318;
interface_1_out_0x55d1b6969810 -> interface_0_in_0x55d1b6969810;
interface_1_out_0x55d1b6969838 -> interface_0_in_0x55d1b6969838;

{
    rank = same;
    interface_5_out_0x55d1b69697c0;
    interface_5_out_0x55d1ce27a750;
    interface_5_out_0x55d1ce266c80;
    interface_5_out_0x55d1ce2864a8;
    interface_6_out_0x55d1ce264e98;
    interface_6_out_0x55d1ce264d58;
    interface_6_out_0x55d1ce264df8;
    interface_7_out_0x55d1ce264ee8;
    interface_7_out_0x55d1ce264f88;
    interface_7_out_0x55d1ce264fd8;
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
			torch.randn([4, 64, 3]),
			torch.randn([32, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Splitfaea1e47551cefb0 -> [g*s]@Share8fb28f0c9326f917, [g^-1*s^-1*C_in]@Share5d155fcebfb4fc10
		t_3 = torch.reshape(t_3, (1, 64, 2, 56, 56, ))

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_3 = torch.roll(t_3, self.shift_direction, 3)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (1, 128, 56, 56, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 2, 3, 56, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("linjmo, kij -> lknmo", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_5 = torch.reshape(t_5, (1, 448, 56, 1, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (1, 4, 2, 56, 3, 56, ))

		# Perform contraction.
		t_6 = torch.einsum("lojmkn, ijk -> liomn", t_5, in_2)

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
			torch.randn([8, 64, 3]),
			torch.randn([32, 4, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Splitfaea1e47551cefb0 -> [g*s]@Share8fb28f0c9326f917, [g^-1*s^-1*C_in]@Share5d155fcebfb4fc10
		t_3 = torch.reshape(t_3, (1, 64, 4, 28, 28, ))

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_3 = torch.roll(t_3, self.shift_direction, 3)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (1, 256, 28, 28, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 4, 3, 28, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("linjmo, kij -> lknmo", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_5 = torch.reshape(t_5, (1, 896, 28, 1, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (1, 8, 4, 28, 3, 28, ))

		# Perform contraction.
		t_6 = torch.einsum("lojmkn, ijk -> liomn", t_5, in_2)

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
			torch.randn([16, 64, 3]),
			torch.randn([32, 8, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Splitfaea1e47551cefb0 -> [g*s]@Share8fb28f0c9326f917, [g^-1*s^-1*C_in]@Share5d155fcebfb4fc10
		t_3 = torch.reshape(t_3, (1, 64, 8, 14, 14, ))

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_3 = torch.roll(t_3, self.shift_direction, 3)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (1, 512, 14, 14, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 8, 3, 14, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("linjmo, kij -> lknmo", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_5 = torch.reshape(t_5, (1, 1792, 14, 1, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (1, 16, 8, 14, 3, 14, ))

		# Perform contraction.
		t_6 = torch.einsum("lojmkn, ijk -> liomn", t_5, in_2)

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
			torch.randn([32, 64, 3]),
			torch.randn([32, 16, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Splitfaea1e47551cefb0 -> [g*s]@Share8fb28f0c9326f917, [g^-1*s^-1*C_in]@Share5d155fcebfb4fc10
		t_3 = torch.reshape(t_3, (1, 64, 16, 7, 7, ))

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_3 = torch.roll(t_3, self.shift_direction, 3)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (1, 1024, 7, 7, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 16, 3, 7, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("linjmo, kij -> lknmo", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_5 = torch.reshape(t_5, (1, 3584, 7, 1, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (1, 32, 16, 7, 3, 7, ))

		# Perform contraction.
		t_6 = torch.einsum("lojmkn, ijk -> liomn", t_5, in_2)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 1024, 7, 7, ))

		# No need to crop the output tensor.
		y = t_7

		return y

