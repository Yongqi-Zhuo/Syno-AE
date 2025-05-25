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
        interface_0_out_0x560cbdec1c00 [label="N", shape=none];
        interface_0_out_0x560cbdec1c28 [label="C_out", shape=none];
        interface_0_out_0x560cbdec1c50 [label="H", shape=none];
        interface_0_out_0x560cbdec1c78 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x560cbdec1c00;
        interface_0_out_0x560cbdec1c28;
        interface_0_out_0x560cbdec1c50;
        interface_0_out_0x560cbdec1c78;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x560cbdec1c00 [label="N", shape=none];
        interface_0_in_0x560cbdec1c28 [label="C_out", shape=none];
        interface_0_in_0x560cbdec1c50 [label="H", shape=none];
        interface_0_in_0x560cbdcf2e90 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x560cbdec1c00;
        interface_0_in_0x560cbdec1c28;
        interface_0_in_0x560cbdec1c50;
        interface_0_in_0x560cbdcf2e90;
    }
    // Op's.
    op_0x560cbdcf2e70 [label="Shift"];
    // Dimension's.
    interface_0_in_0x560cbdcf2e90 -> op_0x560cbdcf2e70 [label="H"];
    interface_0_in_0x560cbdec1c00 -> interface_0_out_0x560cbdec1c00 [label="N"];
    interface_0_in_0x560cbdec1c28 -> interface_0_out_0x560cbdec1c28 [label="C_out"];
    interface_0_in_0x560cbdec1c50 -> interface_0_out_0x560cbdec1c50 [label="H"];
    op_0x560cbdcf2e70 -> interface_0_out_0x560cbdec1c78 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f51780055d0 [label="Sum", shape=box];
    reduce_0x7f5178001998 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x560cbdec1c00 [label="N", shape=none];
        interface_1_out_0x560cbdec1c28 [label="C_out", shape=none];
        interface_1_out_0x560cbdec1c50 [label="H", shape=none];
        interface_1_out_0x560cbdcf2e90 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f51780055d0;
        reduce_0x7f5178001998;
        interface_1_out_0x560cbdec1c00;
        interface_1_out_0x560cbdec1c28;
        interface_1_out_0x560cbdec1c50;
        interface_1_out_0x560cbdcf2e90;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x560cbdec1c00 [label="N", shape=none];
        interface_1_in_0x560cbe30f370 [label="s^-1*C_in", shape=none];
        interface_1_in_0x560cbe30f3c0 [label="k_1", shape=none];
        interface_1_in_0x560cbdec1c50 [label="H", shape=none];
        interface_1_in_0x560cbdcf2e90 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x560cbe30f338 [label="C_out", shape=none];
        interface_1_in_0x560cbe30f388 [label="s^-1*C_in", shape=none];
        interface_1_in_0x560cbe30f3d8 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x560cbdec1c00;
        interface_1_in_0x560cbe30f370;
        interface_1_in_0x560cbe30f3c0;
        interface_1_in_0x560cbdec1c50;
        interface_1_in_0x560cbdcf2e90;
        interface_1_in_0x560cbe30f338;
        interface_1_in_0x560cbe30f388;
        interface_1_in_0x560cbe30f3d8;
    }
    // Op's.
    op_0x560cbdd00858 [label="Expand"];
    op_0x560cbe30f300 [label="Share"];
    op_0x560cbe30f350 [label="Share"];
    op_0x560cbe30f3a0 [label="Share"];
    // Dimension's.
    interface_1_in_0x560cbdcf2e90 -> interface_1_out_0x560cbdcf2e90 [label="H"];
    interface_1_in_0x560cbdec1c00 -> interface_1_out_0x560cbdec1c00 [label="N"];
    op_0x560cbe30f300 -> interface_1_out_0x560cbdec1c28 [label="C_out"];
    interface_1_in_0x560cbdec1c50 -> interface_1_out_0x560cbdec1c50 [label="H"];
    op_0x560cbdd00858 -> op_0x560cbe30f300 [label="C_out"];
    interface_1_in_0x560cbe30f338 -> op_0x560cbe30f300 [label="C_out"];
    interface_1_in_0x560cbe30f370 -> op_0x560cbe30f350 [label="s^-1*C_in"];
    interface_1_in_0x560cbe30f388 -> op_0x560cbe30f350 [label="s^-1*C_in"];
    interface_1_in_0x560cbe30f3c0 -> op_0x560cbe30f3a0 [label="k_1"];
    interface_1_in_0x560cbe30f3d8 -> op_0x560cbe30f3a0 [label="k_1"];
    op_0x560cbe30f3a0 -> reduce_0x7f5178001998 [label="k_1"];
    op_0x560cbe30f350 -> reduce_0x7f51780055d0 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f517800c2b0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x560cbdec1c00 [label="N", shape=none];
        interface_2_out_0x560cbe30f370 [label="s^-1*C_in", shape=none];
        interface_2_out_0x560cbe30f3c0 [label="k_1", shape=none];
        interface_2_out_0x560cbdec1c50 [label="H", shape=none];
        interface_2_out_0x560cbdcf2e90 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f517800c2b0;
        interface_2_out_0x560cbdec1c00;
        interface_2_out_0x560cbe30f370;
        interface_2_out_0x560cbe30f3c0;
        interface_2_out_0x560cbdec1c50;
        interface_2_out_0x560cbdcf2e90;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x560cbdec1c00 [label="N", shape=none];
        interface_2_in_0x560cbe30f370 [label="s^-1*C_in", shape=none];
        interface_2_in_0x560cbdd1d450 [label="g^-2*k_1*C_out^2", shape=none];
        interface_2_in_0x560cbdec1c50 [label="H", shape=none];
        interface_2_in_0x560cbdcf2e90 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x560cbdec1c00;
        interface_2_in_0x560cbe30f370;
        interface_2_in_0x560cbdd1d450;
        interface_2_in_0x560cbdec1c50;
        interface_2_in_0x560cbdcf2e90;
    }
    // Op's.
    op_0x560cbdd1d410 [label="Split"];
    // Dimension's.
    interface_2_in_0x560cbdcf2e90 -> interface_2_out_0x560cbdcf2e90 [label="H"];
    interface_2_in_0x560cbdd1d450 -> op_0x560cbdd1d410 [label="g^-2*k_1*C_out^2"];
    interface_2_in_0x560cbdec1c00 -> interface_2_out_0x560cbdec1c00 [label="N"];
    interface_2_in_0x560cbdec1c50 -> interface_2_out_0x560cbdec1c50 [label="H"];
    interface_2_in_0x560cbe30f370 -> interface_2_out_0x560cbe30f370 [label="s^-1*C_in"];
    op_0x560cbdd1d410 -> interface_2_out_0x560cbe30f3c0 [label="k_1"];
    op_0x560cbdd1d410 -> reduce_0x7f517800c2b0 [label="g^-2*C_out^2"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7f5178009a70 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x560cbdec1c00 [label="N", shape=none];
        interface_3_out_0x560cbe30f370 [label="s^-1*C_in", shape=none];
        interface_3_out_0x560cbdd1d450 [label="g^-2*k_1*C_out^2", shape=none];
        interface_3_out_0x560cbdec1c50 [label="H", shape=none];
        interface_3_out_0x560cbdcf2e90 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5178009a70;
        interface_3_out_0x560cbdec1c00;
        interface_3_out_0x560cbe30f370;
        interface_3_out_0x560cbdd1d450;
        interface_3_out_0x560cbdec1c50;
        interface_3_out_0x560cbdcf2e90;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x560cbdec1c00 [label="N", shape=none];
        interface_3_in_0x560cbe30f370 [label="s^-1*C_in", shape=none];
        interface_3_in_0x560cbdd1e4a8 [label="H", shape=none];
        interface_3_in_0x560cbdcf2e90 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x560cbdec1c00;
        interface_3_in_0x560cbe30f370;
        interface_3_in_0x560cbdd1e4a8;
        interface_3_in_0x560cbdcf2e90;
    }
    // Op's.
    op_0x560cbdd1e480 [label="Unfold"];
    op_0x560cbe2ee790 [label="Split"];
    // Dimension's.
    interface_3_in_0x560cbdcf2e90 -> interface_3_out_0x560cbdcf2e90 [label="H"];
    op_0x560cbe2ee790 -> interface_3_out_0x560cbdd1d450 [label="g^-2*k_1*C_out^2"];
    interface_3_in_0x560cbdd1e4a8 -> op_0x560cbdd1e480 [label="H"];
    interface_3_in_0x560cbdec1c00 -> interface_3_out_0x560cbdec1c00 [label="N"];
    op_0x560cbdd1e480 -> interface_3_out_0x560cbdec1c50 [label="H"];
    op_0x560cbdd1e480 -> op_0x560cbe2ee790 [label="g^-3*k_1*C_out^3"];
    interface_3_in_0x560cbe30f370 -> interface_3_out_0x560cbe30f370 [label="s^-1*C_in"];
    op_0x560cbe2ee790 -> reduce_0x7f5178009a70 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    reduce_0x7f5178002d30 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x560cbdec1c00 [label="N", shape=none];
        interface_4_out_0x560cbe30f370 [label="s^-1*C_in", shape=none];
        interface_4_out_0x560cbdd1e4a8 [label="H", shape=none];
        interface_4_out_0x560cbdcf2e90 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5178002d30;
        interface_4_out_0x560cbdec1c00;
        interface_4_out_0x560cbe30f370;
        interface_4_out_0x560cbdd1e4a8;
        interface_4_out_0x560cbdcf2e90;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x560cbdec1c00 [label="N", shape=none];
        interface_4_in_0x560cbe2ee6e0 [label="C_in", shape=none];
        interface_4_in_0x560cbdd1e4a8 [label="H", shape=none];
        interface_4_in_0x560cbdcf2e90 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x560cbdec1c00;
        interface_4_in_0x560cbe2ee6e0;
        interface_4_in_0x560cbdd1e4a8;
        interface_4_in_0x560cbdcf2e90;
    }
    // Op's.
    op_0x560cbe2ee6a0 [label="Split"];
    // Dimension's.
    interface_4_in_0x560cbdcf2e90 -> interface_4_out_0x560cbdcf2e90 [label="H"];
    interface_4_in_0x560cbdd1e4a8 -> interface_4_out_0x560cbdd1e4a8 [label="H"];
    interface_4_in_0x560cbdec1c00 -> interface_4_out_0x560cbdec1c00 [label="N"];
    interface_4_in_0x560cbe2ee6e0 -> op_0x560cbe2ee6a0 [label="C_in"];
    op_0x560cbe2ee6a0 -> interface_4_out_0x560cbe30f370 [label="s^-1*C_in"];
    op_0x560cbe2ee6a0 -> reduce_0x7f5178002d30 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x560cbdec1c00 [label="N", shape=none];
    interface_5_out_0x560cbe2ee6e0 [label="C_in", shape=none];
    interface_5_out_0x560cbdd1e4a8 [label="H", shape=none];
    interface_5_out_0x560cbdcf2e90 [label="H", shape=none];
}

interface_5_out_0x560cbdec1c00 -> interface_4_in_0x560cbdec1c00;
interface_5_out_0x560cbe2ee6e0 -> interface_4_in_0x560cbe2ee6e0;
interface_5_out_0x560cbdd1e4a8 -> interface_4_in_0x560cbdd1e4a8;
interface_5_out_0x560cbdcf2e90 -> interface_4_in_0x560cbdcf2e90;

interface_4_out_0x560cbdec1c00 -> interface_3_in_0x560cbdec1c00;
interface_4_out_0x560cbe30f370 -> interface_3_in_0x560cbe30f370;
interface_4_out_0x560cbdd1e4a8 -> interface_3_in_0x560cbdd1e4a8;
interface_4_out_0x560cbdcf2e90 -> interface_3_in_0x560cbdcf2e90;

interface_3_out_0x560cbdec1c00 -> interface_2_in_0x560cbdec1c00;
interface_3_out_0x560cbe30f370 -> interface_2_in_0x560cbe30f370;
interface_3_out_0x560cbdd1d450 -> interface_2_in_0x560cbdd1d450;
interface_3_out_0x560cbdec1c50 -> interface_2_in_0x560cbdec1c50;
interface_3_out_0x560cbdcf2e90 -> interface_2_in_0x560cbdcf2e90;

interface_2_out_0x560cbdec1c00 -> interface_1_in_0x560cbdec1c00;
interface_2_out_0x560cbe30f370 -> interface_1_in_0x560cbe30f370;
interface_2_out_0x560cbe30f3c0 -> interface_1_in_0x560cbe30f3c0;
interface_2_out_0x560cbdec1c50 -> interface_1_in_0x560cbdec1c50;
interface_2_out_0x560cbdcf2e90 -> interface_1_in_0x560cbdcf2e90;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 1";
    interface_6_out_0x560cbe30f338 [label="C_out", shape=none];
    interface_6_out_0x560cbe30f388 [label="s^-1*C_in", shape=none];
    interface_6_out_0x560cbe30f3d8 [label="k_1", shape=none];
}

interface_6_out_0x560cbe30f338 -> interface_1_in_0x560cbe30f338;
interface_6_out_0x560cbe30f388 -> interface_1_in_0x560cbe30f388;
interface_6_out_0x560cbe30f3d8 -> interface_1_in_0x560cbe30f3d8;

interface_1_out_0x560cbdec1c00 -> interface_0_in_0x560cbdec1c00;
interface_1_out_0x560cbdec1c28 -> interface_0_in_0x560cbdec1c28;
interface_1_out_0x560cbdec1c50 -> interface_0_in_0x560cbdec1c50;
interface_1_out_0x560cbdcf2e90 -> interface_0_in_0x560cbdcf2e90;

{
    rank = same;
    interface_5_out_0x560cbdec1c00;
    interface_5_out_0x560cbe2ee6e0;
    interface_5_out_0x560cbdd1e4a8;
    interface_5_out_0x560cbdcf2e90;
    interface_6_out_0x560cbe30f338;
    interface_6_out_0x560cbe30f388;
    interface_6_out_0x560cbe30f3d8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_7_in_0x560cbdec1c00 [label="N", shape=none];
    interface_7_in_0x560cbdec1c28 [label="C_out", shape=none];
    interface_7_in_0x560cbdec1c50 [label="H", shape=none];
    interface_7_in_0x560cbdec1c78 [label="H", shape=none];
}
interface_0_out_0x560cbdec1c00 -> interface_7_in_0x560cbdec1c00;
interface_0_out_0x560cbdec1c28 -> interface_7_in_0x560cbdec1c28;
interface_0_out_0x560cbdec1c50 -> interface_7_in_0x560cbdec1c50;
interface_0_out_0x560cbdec1c78 -> interface_7_in_0x560cbdec1c78;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Splitcfaed9699d036d38 -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 64, 56, 56, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4aa57e8190ebe608 -> [H]@Iterator96123ba3184da39c, [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05
		t_3 = torch.reshape(t_3, (128, 64, 56, 56, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 3, 56, 56, ))

		# [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05 -> [g^-1*C_out]@Reduce28c4f9e5abf023cf, [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3
		t_3 = torch.reshape(t_3, (128, 64, 1, 3, 56, 56, ))

		# [g^-1*C_out]@Reduce
		t_3 = torch.sum(t_3, dim=(2, ))

		# No contraction needed.
		t_4 = t_3

		# [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3 -> [k_1]@Share26cfa48d169008e4, [g^-2*C_out^2]@Reduce159437b921f023cf
		t_4 = torch.reshape(t_4, (128, 64, 3, 1, 56, 56, ))

		# [g^-2*C_out^2]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# Perform contraction.
		t_5 = torch.einsum("mjknl, ijk -> minl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Splitcfaed9699d036d38 -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 64, 28, 28, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4aa57e8190ebe608 -> [H]@Iterator96123ba3184da39c, [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05
		t_3 = torch.reshape(t_3, (128, 64, 28, 28, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 3, 28, 28, ))

		# [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05 -> [g^-1*C_out]@Reduce28c4f9e5abf023cf, [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3
		t_3 = torch.reshape(t_3, (128, 64, 1, 3, 28, 28, ))

		# [g^-1*C_out]@Reduce
		t_3 = torch.sum(t_3, dim=(2, ))

		# No contraction needed.
		t_4 = t_3

		# [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3 -> [k_1]@Share26cfa48d169008e4, [g^-2*C_out^2]@Reduce159437b921f023cf
		t_4 = torch.reshape(t_4, (128, 64, 3, 1, 28, 28, ))

		# [g^-2*C_out^2]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# Perform contraction.
		t_5 = torch.einsum("mjknl, ijk -> minl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Splitcfaed9699d036d38 -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 64, 14, 14, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4aa57e8190ebe608 -> [H]@Iterator96123ba3184da39c, [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05
		t_3 = torch.reshape(t_3, (128, 64, 14, 14, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 3, 14, 14, ))

		# [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05 -> [g^-1*C_out]@Reduce28c4f9e5abf023cf, [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3
		t_3 = torch.reshape(t_3, (128, 64, 1, 3, 14, 14, ))

		# [g^-1*C_out]@Reduce
		t_3 = torch.sum(t_3, dim=(2, ))

		# No contraction needed.
		t_4 = t_3

		# [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3 -> [k_1]@Share26cfa48d169008e4, [g^-2*C_out^2]@Reduce159437b921f023cf
		t_4 = torch.reshape(t_4, (128, 64, 3, 1, 14, 14, ))

		# [g^-2*C_out^2]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# Perform contraction.
		t_5 = torch.einsum("mjknl, ijk -> minl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Splitcfaed9699d036d38 -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 64, 7, 7, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4aa57e8190ebe608 -> [H]@Iterator96123ba3184da39c, [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05
		t_3 = torch.reshape(t_3, (128, 64, 7, 7, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 3, 7, 7, ))

		# [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05 -> [g^-1*C_out]@Reduce28c4f9e5abf023cf, [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3
		t_3 = torch.reshape(t_3, (128, 64, 1, 3, 7, 7, ))

		# [g^-1*C_out]@Reduce
		t_3 = torch.sum(t_3, dim=(2, ))

		# No contraction needed.
		t_4 = t_3

		# [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3 -> [k_1]@Share26cfa48d169008e4, [g^-2*C_out^2]@Reduce159437b921f023cf
		t_4 = torch.reshape(t_4, (128, 64, 3, 1, 7, 7, ))

		# [g^-2*C_out^2]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# Perform contraction.
		t_5 = torch.einsum("mjknl, ijk -> minl", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_6

		return y

