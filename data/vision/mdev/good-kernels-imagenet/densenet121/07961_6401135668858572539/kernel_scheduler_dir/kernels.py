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
        interface_0_out_0x55586e4eefd0 [label="N", shape=none];
        interface_0_out_0x55586e4eeff8 [label="C_out", shape=none];
        interface_0_out_0x55586e4ef020 [label="H", shape=none];
        interface_0_out_0x55586e4ef048 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55586e4eefd0;
        interface_0_out_0x55586e4eeff8;
        interface_0_out_0x55586e4ef020;
        interface_0_out_0x55586e4ef048;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55586e4eefd0 [label="N", shape=none];
        interface_0_in_0x55586e5a0260 [label="g", shape=none];
        interface_0_in_0x55586e59f5a0 [label="H", shape=none];
        interface_0_in_0x55586e5a10a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55586e4eefd0;
        interface_0_in_0x55586e5a0260;
        interface_0_in_0x55586e59f5a0;
        interface_0_in_0x55586e5a10a8;
    }
    // Op's.
    op_0x55586e59f580 [label="Shift"];
    op_0x55586e5a0220 [label="Merge"];
    op_0x55586e5a1080 [label="Unfold"];
    // Dimension's.
    interface_0_in_0x55586e4eefd0 -> interface_0_out_0x55586e4eefd0 [label="N"];
    op_0x55586e5a0220 -> interface_0_out_0x55586e4eeff8 [label="C_out"];
    op_0x55586e59f580 -> interface_0_out_0x55586e4ef020 [label="H"];
    op_0x55586e5a1080 -> interface_0_out_0x55586e4ef048 [label="H"];
    interface_0_in_0x55586e59f5a0 -> op_0x55586e59f580 [label="H"];
    interface_0_in_0x55586e5a0260 -> op_0x55586e5a0220 [label="g"];
    op_0x55586e5a1080 -> op_0x55586e5a0220 [label="g^-1*C_out"];
    interface_0_in_0x55586e5a10a8 -> op_0x55586e5a1080 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f51700058d8 [label="Sum", shape=box];
    reduce_0x7f517000c2d8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55586e4eefd0 [label="N", shape=none];
        interface_1_out_0x55586e5a0260 [label="g", shape=none];
        interface_1_out_0x55586e59f5a0 [label="H", shape=none];
        interface_1_out_0x55586e5a10a8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f51700058d8;
        reduce_0x7f517000c2d8;
        interface_1_out_0x55586e4eefd0;
        interface_1_out_0x55586e5a0260;
        interface_1_out_0x55586e59f5a0;
        interface_1_out_0x55586e5a10a8;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55586e4eefd0 [label="N", shape=none];
        interface_1_in_0x55586e59e870 [label="C_in", shape=none];
        interface_1_in_0x55586e59f5a0 [label="H", shape=none];
        interface_1_in_0x55586e59e910 [label="g^-2*k_1*C_out^2", shape=none];
        interface_1_in_0x55586e5a10a8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55586e59e8d8 [label="g", shape=none];
        interface_1_in_0x55586e59e888 [label="C_in", shape=none];
        interface_1_in_0x55586e59e928 [label="g^-2*k_1*C_out^2", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55586e4eefd0;
        interface_1_in_0x55586e59e870;
        interface_1_in_0x55586e59f5a0;
        interface_1_in_0x55586e59e910;
        interface_1_in_0x55586e5a10a8;
        interface_1_in_0x55586e59e8d8;
        interface_1_in_0x55586e59e888;
        interface_1_in_0x55586e59e928;
    }
    // Op's.
    op_0x55586e59e850 [label="Share"];
    op_0x55586e59e8a0 [label="Share"];
    op_0x55586e59e8f0 [label="Share"];
    op_0x55586e59ed18 [label="Expand"];
    // Dimension's.
    interface_1_in_0x55586e4eefd0 -> interface_1_out_0x55586e4eefd0 [label="N"];
    interface_1_in_0x55586e59e870 -> op_0x55586e59e850 [label="C_in"];
    interface_1_in_0x55586e59e888 -> op_0x55586e59e850 [label="C_in"];
    op_0x55586e59ed18 -> op_0x55586e59e8a0 [label="g"];
    interface_1_in_0x55586e59e8d8 -> op_0x55586e59e8a0 [label="g"];
    interface_1_in_0x55586e59e910 -> op_0x55586e59e8f0 [label="g^-2*k_1*C_out^2"];
    interface_1_in_0x55586e59e928 -> op_0x55586e59e8f0 [label="g^-2*k_1*C_out^2"];
    interface_1_in_0x55586e59f5a0 -> interface_1_out_0x55586e59f5a0 [label="H"];
    op_0x55586e59e8a0 -> interface_1_out_0x55586e5a0260 [label="g"];
    interface_1_in_0x55586e5a10a8 -> interface_1_out_0x55586e5a10a8 [label="H"];
    op_0x55586e59e850 -> reduce_0x7f51700058d8 [label="C_in"];
    op_0x55586e59e8f0 -> reduce_0x7f517000c2d8 [label="g^-2*k_1*C_out^2"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55586e4eefd0 [label="N", shape=none];
        interface_2_out_0x55586e59e870 [label="C_in", shape=none];
        interface_2_out_0x55586e59f5a0 [label="H", shape=none];
        interface_2_out_0x55586e59e910 [label="g^-2*k_1*C_out^2", shape=none];
        interface_2_out_0x55586e5a10a8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x55586e4eefd0;
        interface_2_out_0x55586e59e870;
        interface_2_out_0x55586e59f5a0;
        interface_2_out_0x55586e59e910;
        interface_2_out_0x55586e5a10a8;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55586e4eefd0 [label="N", shape=none];
        interface_2_in_0x55586e59e870 [label="C_in", shape=none];
        interface_2_in_0x55586e59f5a0 [label="H", shape=none];
        interface_2_in_0x55586e5a10e8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55586e4eefd0;
        interface_2_in_0x55586e59e870;
        interface_2_in_0x55586e59f5a0;
        interface_2_in_0x55586e5a10e8;
    }
    // Op's.
    op_0x55586e5a10c0 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x55586e4eefd0 -> interface_2_out_0x55586e4eefd0 [label="N"];
    interface_2_in_0x55586e59e870 -> interface_2_out_0x55586e59e870 [label="C_in"];
    op_0x55586e5a10c0 -> interface_2_out_0x55586e59e910 [label="g^-2*k_1*C_out^2"];
    interface_2_in_0x55586e59f5a0 -> interface_2_out_0x55586e59f5a0 [label="H"];
    op_0x55586e5a10c0 -> interface_2_out_0x55586e5a10a8 [label="H"];
    interface_2_in_0x55586e5a10e8 -> op_0x55586e5a10c0 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x55586e4eefd0 [label="N", shape=none];
    interface_3_out_0x55586e59e870 [label="C_in", shape=none];
    interface_3_out_0x55586e59f5a0 [label="H", shape=none];
    interface_3_out_0x55586e5a10e8 [label="H", shape=none];
}

interface_3_out_0x55586e4eefd0 -> interface_2_in_0x55586e4eefd0;
interface_3_out_0x55586e59e870 -> interface_2_in_0x55586e59e870;
interface_3_out_0x55586e59f5a0 -> interface_2_in_0x55586e59f5a0;
interface_3_out_0x55586e5a10e8 -> interface_2_in_0x55586e5a10e8;

interface_2_out_0x55586e4eefd0 -> interface_1_in_0x55586e4eefd0;
interface_2_out_0x55586e59e870 -> interface_1_in_0x55586e59e870;
interface_2_out_0x55586e59f5a0 -> interface_1_in_0x55586e59f5a0;
interface_2_out_0x55586e59e910 -> interface_1_in_0x55586e59e910;
interface_2_out_0x55586e5a10a8 -> interface_1_in_0x55586e5a10a8;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x55586e59e8d8 [label="g", shape=none];
    interface_4_out_0x55586e59e888 [label="C_in", shape=none];
    interface_4_out_0x55586e59e928 [label="g^-2*k_1*C_out^2", shape=none];
}

interface_4_out_0x55586e59e8d8 -> interface_1_in_0x55586e59e8d8;
interface_4_out_0x55586e59e888 -> interface_1_in_0x55586e59e888;
interface_4_out_0x55586e59e928 -> interface_1_in_0x55586e59e928;

interface_1_out_0x55586e4eefd0 -> interface_0_in_0x55586e4eefd0;
interface_1_out_0x55586e5a0260 -> interface_0_in_0x55586e5a0260;
interface_1_out_0x55586e59f5a0 -> interface_0_in_0x55586e59f5a0;
interface_1_out_0x55586e5a10a8 -> interface_0_in_0x55586e5a10a8;

{
    rank = same;
    interface_3_out_0x55586e4eefd0;
    interface_3_out_0x55586e59e870;
    interface_3_out_0x55586e59f5a0;
    interface_3_out_0x55586e5a10e8;
    interface_4_out_0x55586e59e8d8;
    interface_4_out_0x55586e59e888;
    interface_4_out_0x55586e59e928;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x55586e4eefd0 [label="N", shape=none];
    interface_5_in_0x55586e4eeff8 [label="C_out", shape=none];
    interface_5_in_0x55586e4ef020 [label="H", shape=none];
    interface_5_in_0x55586e4ef048 [label="H", shape=none];
}
interface_0_out_0x55586e4eefd0 -> interface_5_in_0x55586e4eefd0;
interface_0_out_0x55586e4eeff8 -> interface_5_in_0x55586e4eeff8;
interface_0_out_0x55586e4ef020 -> interface_5_in_0x55586e4ef020;
interface_0_out_0x55586e4ef048 -> interface_5_in_0x55586e4ef048;

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
		t_2 = torch.reshape(t_2, (1, 7168, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 128, 56, 3, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("limkn, jik -> ljmn", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfold0e52d9ad217142d1 -> [H]@Iteratorb0a1def4ad5784ec, [g^-1*C_out]@Merge402ce7fe20a0a5f8
		t_4 = torch.reshape(t_4, (1, 1792, 56, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (1, 1, ), padding=(0, 0, ))
		t_4 = torch.reshape(t_4, (1, 32, 56, 1, 56, ))

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.permute(t_4, (0, 2, 1, 3, 4, ))
		t_4 = torch.reshape(t_4, (1, 56, 32, 56, ))

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
		t_2 = torch.reshape(t_2, (1, 3584, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 128, 28, 3, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("limkn, jik -> ljmn", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfold0e52d9ad217142d1 -> [H]@Iteratorb0a1def4ad5784ec, [g^-1*C_out]@Merge402ce7fe20a0a5f8
		t_4 = torch.reshape(t_4, (1, 896, 28, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (1, 1, ), padding=(0, 0, ))
		t_4 = torch.reshape(t_4, (1, 32, 28, 1, 28, ))

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.permute(t_4, (0, 2, 1, 3, 4, ))
		t_4 = torch.reshape(t_4, (1, 28, 32, 28, ))

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
		t_2 = torch.reshape(t_2, (1, 1792, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 128, 14, 3, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("limkn, jik -> ljmn", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfold0e52d9ad217142d1 -> [H]@Iteratorb0a1def4ad5784ec, [g^-1*C_out]@Merge402ce7fe20a0a5f8
		t_4 = torch.reshape(t_4, (1, 448, 14, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (1, 1, ), padding=(0, 0, ))
		t_4 = torch.reshape(t_4, (1, 32, 14, 1, 14, ))

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.permute(t_4, (0, 2, 1, 3, 4, ))
		t_4 = torch.reshape(t_4, (1, 14, 32, 14, ))

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
		t_2 = torch.reshape(t_2, (1, 896, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 128, 7, 3, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("limkn, jik -> ljmn", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfold0e52d9ad217142d1 -> [H]@Iteratorb0a1def4ad5784ec, [g^-1*C_out]@Merge402ce7fe20a0a5f8
		t_4 = torch.reshape(t_4, (1, 224, 7, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (1, 1, ), padding=(0, 0, ))
		t_4 = torch.reshape(t_4, (1, 32, 7, 1, 7, ))

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.permute(t_4, (0, 2, 1, 3, 4, ))
		t_4 = torch.reshape(t_4, (1, 7, 32, 7, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 2, 1, 3, ))

		# No need to crop the output tensor.
		y = t_4

		return y

