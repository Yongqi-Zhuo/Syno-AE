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
        interface_0_in_0x560cbdd1aa70 [label="g", shape=none];
        interface_0_in_0x560cbdcf2e60 [label="H", shape=none];
        interface_0_in_0x560cbdd1e5a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x560cbdec1c00;
        interface_0_in_0x560cbdd1aa70;
        interface_0_in_0x560cbdcf2e60;
        interface_0_in_0x560cbdd1e5a8;
    }
    // Op's.
    op_0x560cbdcf2e40 [label="Shift"];
    op_0x560cbdd1aa30 [label="Merge"];
    op_0x560cbdd1e580 [label="Unfold"];
    // Dimension's.
    interface_0_in_0x560cbdcf2e60 -> op_0x560cbdcf2e40 [label="H"];
    interface_0_in_0x560cbdd1aa70 -> op_0x560cbdd1aa30 [label="g"];
    op_0x560cbdd1e580 -> op_0x560cbdd1aa30 [label="g^-1*C_out"];
    interface_0_in_0x560cbdd1e5a8 -> op_0x560cbdd1e580 [label="H"];
    interface_0_in_0x560cbdec1c00 -> interface_0_out_0x560cbdec1c00 [label="N"];
    op_0x560cbdd1aa30 -> interface_0_out_0x560cbdec1c28 [label="C_out"];
    op_0x560cbdcf2e40 -> interface_0_out_0x560cbdec1c50 [label="H"];
    op_0x560cbdd1e580 -> interface_0_out_0x560cbdec1c78 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f5178005ad8 [label="Sum", shape=box];
    reduce_0x7f517800c4d8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x560cbdec1c00 [label="N", shape=none];
        interface_1_out_0x560cbdd1aa70 [label="g", shape=none];
        interface_1_out_0x560cbdcf2e60 [label="H", shape=none];
        interface_1_out_0x560cbdd1e5a8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5178005ad8;
        reduce_0x7f517800c4d8;
        interface_1_out_0x560cbdec1c00;
        interface_1_out_0x560cbdd1aa70;
        interface_1_out_0x560cbdcf2e60;
        interface_1_out_0x560cbdd1e5a8;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x560cbdec1c00 [label="N", shape=none];
        interface_1_in_0x560cbe30f5a0 [label="C_in", shape=none];
        interface_1_in_0x560cbdcf2e60 [label="H", shape=none];
        interface_1_in_0x560cbe30f640 [label="g^-2*k_1*C_out^2", shape=none];
        interface_1_in_0x560cbdd1e5a8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x560cbe30f608 [label="g", shape=none];
        interface_1_in_0x560cbe30f5b8 [label="C_in", shape=none];
        interface_1_in_0x560cbe30f658 [label="g^-2*k_1*C_out^2", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x560cbdec1c00;
        interface_1_in_0x560cbe30f5a0;
        interface_1_in_0x560cbdcf2e60;
        interface_1_in_0x560cbe30f640;
        interface_1_in_0x560cbdd1e5a8;
        interface_1_in_0x560cbe30f608;
        interface_1_in_0x560cbe30f5b8;
        interface_1_in_0x560cbe30f658;
    }
    // Op's.
    op_0x560cbdd008b8 [label="Expand"];
    op_0x560cbe30f580 [label="Share"];
    op_0x560cbe30f5d0 [label="Share"];
    op_0x560cbe30f620 [label="Share"];
    // Dimension's.
    interface_1_in_0x560cbdcf2e60 -> interface_1_out_0x560cbdcf2e60 [label="H"];
    op_0x560cbe30f5d0 -> interface_1_out_0x560cbdd1aa70 [label="g"];
    interface_1_in_0x560cbdd1e5a8 -> interface_1_out_0x560cbdd1e5a8 [label="H"];
    interface_1_in_0x560cbdec1c00 -> interface_1_out_0x560cbdec1c00 [label="N"];
    interface_1_in_0x560cbe30f5a0 -> op_0x560cbe30f580 [label="C_in"];
    interface_1_in_0x560cbe30f5b8 -> op_0x560cbe30f580 [label="C_in"];
    op_0x560cbdd008b8 -> op_0x560cbe30f5d0 [label="g"];
    interface_1_in_0x560cbe30f608 -> op_0x560cbe30f5d0 [label="g"];
    interface_1_in_0x560cbe30f640 -> op_0x560cbe30f620 [label="g^-2*k_1*C_out^2"];
    interface_1_in_0x560cbe30f658 -> op_0x560cbe30f620 [label="g^-2*k_1*C_out^2"];
    op_0x560cbe30f580 -> reduce_0x7f5178005ad8 [label="C_in"];
    op_0x560cbe30f620 -> reduce_0x7f517800c4d8 [label="g^-2*k_1*C_out^2"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x560cbdec1c00 [label="N", shape=none];
        interface_2_out_0x560cbe30f5a0 [label="C_in", shape=none];
        interface_2_out_0x560cbdcf2e60 [label="H", shape=none];
        interface_2_out_0x560cbe30f640 [label="g^-2*k_1*C_out^2", shape=none];
        interface_2_out_0x560cbdd1e5a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x560cbdec1c00;
        interface_2_out_0x560cbe30f5a0;
        interface_2_out_0x560cbdcf2e60;
        interface_2_out_0x560cbe30f640;
        interface_2_out_0x560cbdd1e5a8;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x560cbdec1c00 [label="N", shape=none];
        interface_2_in_0x560cbe30f5a0 [label="C_in", shape=none];
        interface_2_in_0x560cbdcf2e60 [label="H", shape=none];
        interface_2_in_0x560cbdd1e6a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x560cbdec1c00;
        interface_2_in_0x560cbe30f5a0;
        interface_2_in_0x560cbdcf2e60;
        interface_2_in_0x560cbdd1e6a8;
    }
    // Op's.
    op_0x560cbdd1e680 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x560cbdcf2e60 -> interface_2_out_0x560cbdcf2e60 [label="H"];
    op_0x560cbdd1e680 -> interface_2_out_0x560cbdd1e5a8 [label="H"];
    interface_2_in_0x560cbdd1e6a8 -> op_0x560cbdd1e680 [label="H"];
    interface_2_in_0x560cbdec1c00 -> interface_2_out_0x560cbdec1c00 [label="N"];
    interface_2_in_0x560cbe30f5a0 -> interface_2_out_0x560cbe30f5a0 [label="C_in"];
    op_0x560cbdd1e680 -> interface_2_out_0x560cbe30f640 [label="g^-2*k_1*C_out^2"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x560cbdec1c00 [label="N", shape=none];
    interface_3_out_0x560cbe30f5a0 [label="C_in", shape=none];
    interface_3_out_0x560cbdcf2e60 [label="H", shape=none];
    interface_3_out_0x560cbdd1e6a8 [label="H", shape=none];
}

interface_3_out_0x560cbdec1c00 -> interface_2_in_0x560cbdec1c00;
interface_3_out_0x560cbe30f5a0 -> interface_2_in_0x560cbe30f5a0;
interface_3_out_0x560cbdcf2e60 -> interface_2_in_0x560cbdcf2e60;
interface_3_out_0x560cbdd1e6a8 -> interface_2_in_0x560cbdd1e6a8;

interface_2_out_0x560cbdec1c00 -> interface_1_in_0x560cbdec1c00;
interface_2_out_0x560cbe30f5a0 -> interface_1_in_0x560cbe30f5a0;
interface_2_out_0x560cbdcf2e60 -> interface_1_in_0x560cbdcf2e60;
interface_2_out_0x560cbe30f640 -> interface_1_in_0x560cbe30f640;
interface_2_out_0x560cbdd1e5a8 -> interface_1_in_0x560cbdd1e5a8;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x560cbe30f608 [label="g", shape=none];
    interface_4_out_0x560cbe30f5b8 [label="C_in", shape=none];
    interface_4_out_0x560cbe30f658 [label="g^-2*k_1*C_out^2", shape=none];
}

interface_4_out_0x560cbe30f608 -> interface_1_in_0x560cbe30f608;
interface_4_out_0x560cbe30f5b8 -> interface_1_in_0x560cbe30f5b8;
interface_4_out_0x560cbe30f658 -> interface_1_in_0x560cbe30f658;

interface_1_out_0x560cbdec1c00 -> interface_0_in_0x560cbdec1c00;
interface_1_out_0x560cbdd1aa70 -> interface_0_in_0x560cbdd1aa70;
interface_1_out_0x560cbdcf2e60 -> interface_0_in_0x560cbdcf2e60;
interface_1_out_0x560cbdd1e5a8 -> interface_0_in_0x560cbdd1e5a8;

{
    rank = same;
    interface_3_out_0x560cbdec1c00;
    interface_3_out_0x560cbe30f5a0;
    interface_3_out_0x560cbdcf2e60;
    interface_3_out_0x560cbdd1e6a8;
    interface_4_out_0x560cbe30f608;
    interface_4_out_0x560cbe30f5b8;
    interface_4_out_0x560cbe30f658;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x560cbdec1c00 [label="N", shape=none];
    interface_5_in_0x560cbdec1c28 [label="C_out", shape=none];
    interface_5_in_0x560cbdec1c50 [label="H", shape=none];
    interface_5_in_0x560cbdec1c78 [label="H", shape=none];
}
interface_0_out_0x560cbdec1c00 -> interface_5_in_0x560cbdec1c00;
interface_0_out_0x560cbdec1c28 -> interface_5_in_0x560cbdec1c28;
interface_0_out_0x560cbdec1c50 -> interface_5_in_0x560cbdec1c50;
interface_0_out_0x560cbdec1c78 -> interface_5_in_0x560cbdec1c78;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 128, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold4253203f7467f468 -> [H]@Unfold0e52d9ad217142d1, [g^-2*k_1*C_out^2]@Sharebed6e62aeea7a7a2
		t_2 = torch.reshape(t_2, (128, 7168, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 128, 56, 3, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("nilkm, jik -> njlm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfold0e52d9ad217142d1 -> [H]@Iteratorb0a1def4ad5784ec, [g^-1*C_out]@Merge402ce7fe20a0a5f8
		t_4 = torch.reshape(t_4, (128, 1792, 56, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (1, 1, ), padding=(0, 0, ))
		t_4 = torch.reshape(t_4, (128, 32, 56, 1, 56, ))

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.permute(t_4, (0, 2, 1, 3, 4, ))
		t_4 = torch.reshape(t_4, (128, 56, 32, 56, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 2, 1, 3, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 128, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold4253203f7467f468 -> [H]@Unfold0e52d9ad217142d1, [g^-2*k_1*C_out^2]@Sharebed6e62aeea7a7a2
		t_2 = torch.reshape(t_2, (128, 3584, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 128, 28, 3, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("nilkm, jik -> njlm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfold0e52d9ad217142d1 -> [H]@Iteratorb0a1def4ad5784ec, [g^-1*C_out]@Merge402ce7fe20a0a5f8
		t_4 = torch.reshape(t_4, (128, 896, 28, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (1, 1, ), padding=(0, 0, ))
		t_4 = torch.reshape(t_4, (128, 32, 28, 1, 28, ))

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.permute(t_4, (0, 2, 1, 3, 4, ))
		t_4 = torch.reshape(t_4, (128, 28, 32, 28, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 2, 1, 3, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 128, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold4253203f7467f468 -> [H]@Unfold0e52d9ad217142d1, [g^-2*k_1*C_out^2]@Sharebed6e62aeea7a7a2
		t_2 = torch.reshape(t_2, (128, 1792, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 128, 14, 3, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("nilkm, jik -> njlm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfold0e52d9ad217142d1 -> [H]@Iteratorb0a1def4ad5784ec, [g^-1*C_out]@Merge402ce7fe20a0a5f8
		t_4 = torch.reshape(t_4, (128, 448, 14, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (1, 1, ), padding=(0, 0, ))
		t_4 = torch.reshape(t_4, (128, 32, 14, 1, 14, ))

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.permute(t_4, (0, 2, 1, 3, 4, ))
		t_4 = torch.reshape(t_4, (128, 14, 32, 14, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 2, 1, 3, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 128, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold4253203f7467f468 -> [H]@Unfold0e52d9ad217142d1, [g^-2*k_1*C_out^2]@Sharebed6e62aeea7a7a2
		t_2 = torch.reshape(t_2, (128, 896, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 128, 7, 3, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("nilkm, jik -> njlm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfold0e52d9ad217142d1 -> [H]@Iteratorb0a1def4ad5784ec, [g^-1*C_out]@Merge402ce7fe20a0a5f8
		t_4 = torch.reshape(t_4, (128, 224, 7, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (1, 1, ), padding=(0, 0, ))
		t_4 = torch.reshape(t_4, (128, 32, 7, 1, 7, ))

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.permute(t_4, (0, 2, 1, 3, 4, ))
		t_4 = torch.reshape(t_4, (128, 7, 32, 7, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 2, 1, 3, ))

		# No need to crop the output tensor.
		y = t_4

		return y

