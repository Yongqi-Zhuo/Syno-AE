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
        interface_0_out_0x564137b896f0 [label="N", shape=none];
        interface_0_out_0x564137b89718 [label="C_out", shape=none];
        interface_0_out_0x564137b89740 [label="H", shape=none];
        interface_0_out_0x564137b89768 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x564137b896f0;
        interface_0_out_0x564137b89718;
        interface_0_out_0x564137b89740;
        interface_0_out_0x564137b89768;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x564137b896f0 [label="N", shape=none];
        interface_0_in_0x564137c34360 [label="g", shape=none];
        interface_0_in_0x564137c34378 [label="g^-1*C_out", shape=none];
        interface_0_in_0x564137c33660 [label="H", shape=none];
        interface_0_in_0x564137b89768 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x564137b896f0;
        interface_0_in_0x564137c34360;
        interface_0_in_0x564137c34378;
        interface_0_in_0x564137c33660;
        interface_0_in_0x564137b89768;
    }
    // Op's.
    op_0x564137c33640 [label="Shift"];
    op_0x564137c34320 [label="Merge"];
    // Dimension's.
    interface_0_in_0x564137b896f0 -> interface_0_out_0x564137b896f0 [label="N"];
    op_0x564137c34320 -> interface_0_out_0x564137b89718 [label="C_out"];
    op_0x564137c33640 -> interface_0_out_0x564137b89740 [label="H"];
    interface_0_in_0x564137b89768 -> interface_0_out_0x564137b89768 [label="H"];
    interface_0_in_0x564137c33660 -> op_0x564137c33640 [label="H"];
    interface_0_in_0x564137c34360 -> op_0x564137c34320 [label="g"];
    interface_0_in_0x564137c34378 -> op_0x564137c34320 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f0fc000c2d8 [label="Sum", shape=box];
    reduce_0x7f0fc00058d8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x564137b896f0 [label="N", shape=none];
        interface_1_out_0x564137c34360 [label="g", shape=none];
        interface_1_out_0x564137c34378 [label="g^-1*C_out", shape=none];
        interface_1_out_0x564137c33660 [label="H", shape=none];
        interface_1_out_0x564137b89768 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f0fc000c2d8;
        reduce_0x7f0fc00058d8;
        interface_1_out_0x564137b896f0;
        interface_1_out_0x564137c34360;
        interface_1_out_0x564137c34378;
        interface_1_out_0x564137c33660;
        interface_1_out_0x564137b89768;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x564137b896f0 [label="N", shape=none];
        interface_1_in_0x564137c34378 [label="g^-1*C_out", shape=none];
        interface_1_in_0x564137c32a10 [label="g^-2*k_1*C_out^2", shape=none];
        interface_1_in_0x564137c32970 [label="C_in", shape=none];
        interface_1_in_0x564137c33660 [label="H", shape=none];
        interface_1_in_0x564137b89768 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x564137c329d8 [label="g", shape=none];
        interface_1_in_0x564137c32a28 [label="g^-2*k_1*C_out^2", shape=none];
        interface_1_in_0x564137c32988 [label="C_in", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x564137b896f0;
        interface_1_in_0x564137c34378;
        interface_1_in_0x564137c32a10;
        interface_1_in_0x564137c32970;
        interface_1_in_0x564137c33660;
        interface_1_in_0x564137b89768;
        interface_1_in_0x564137c329d8;
        interface_1_in_0x564137c32a28;
        interface_1_in_0x564137c32988;
    }
    // Op's.
    op_0x564137c32950 [label="Share"];
    op_0x564137c329a0 [label="Share"];
    op_0x564137c329f0 [label="Share"];
    op_0x564137c32df8 [label="Expand"];
    // Dimension's.
    interface_1_in_0x564137b896f0 -> interface_1_out_0x564137b896f0 [label="N"];
    interface_1_in_0x564137b89768 -> interface_1_out_0x564137b89768 [label="H"];
    interface_1_in_0x564137c32970 -> op_0x564137c32950 [label="C_in"];
    interface_1_in_0x564137c32988 -> op_0x564137c32950 [label="C_in"];
    op_0x564137c32df8 -> op_0x564137c329a0 [label="g"];
    interface_1_in_0x564137c329d8 -> op_0x564137c329a0 [label="g"];
    interface_1_in_0x564137c32a10 -> op_0x564137c329f0 [label="g^-2*k_1*C_out^2"];
    interface_1_in_0x564137c32a28 -> op_0x564137c329f0 [label="g^-2*k_1*C_out^2"];
    interface_1_in_0x564137c33660 -> interface_1_out_0x564137c33660 [label="H"];
    op_0x564137c329a0 -> interface_1_out_0x564137c34360 [label="g"];
    interface_1_in_0x564137c34378 -> interface_1_out_0x564137c34378 [label="g^-1*C_out"];
    op_0x564137c32950 -> reduce_0x7f0fc00058d8 [label="C_in"];
    op_0x564137c329f0 -> reduce_0x7f0fc000c2d8 [label="g^-2*k_1*C_out^2"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x564137b896f0 [label="N", shape=none];
        interface_2_out_0x564137c34378 [label="g^-1*C_out", shape=none];
        interface_2_out_0x564137c32a10 [label="g^-2*k_1*C_out^2", shape=none];
        interface_2_out_0x564137c32970 [label="C_in", shape=none];
        interface_2_out_0x564137c33660 [label="H", shape=none];
        interface_2_out_0x564137b89768 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x564137b896f0;
        interface_2_out_0x564137c34378;
        interface_2_out_0x564137c32a10;
        interface_2_out_0x564137c32970;
        interface_2_out_0x564137c33660;
        interface_2_out_0x564137b89768;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x564137b896f0 [label="N", shape=none];
        interface_2_in_0x564137c32970 [label="C_in", shape=none];
        interface_2_in_0x564137c33660 [label="H", shape=none];
        interface_2_in_0x564137c33840 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x564137b896f0;
        interface_2_in_0x564137c32970;
        interface_2_in_0x564137c33660;
        interface_2_in_0x564137c33840;
    }
    // Op's.
    op_0x564137c33820 [label="Shift"];
    op_0x564137c35440 [label="Unfold"];
    op_0x564137c3ab40 [label="Split"];
    // Dimension's.
    interface_2_in_0x564137b896f0 -> interface_2_out_0x564137b896f0 [label="N"];
    op_0x564137c35440 -> interface_2_out_0x564137b89768 [label="H"];
    interface_2_in_0x564137c32970 -> interface_2_out_0x564137c32970 [label="C_in"];
    op_0x564137c3ab40 -> interface_2_out_0x564137c32a10 [label="g^-2*k_1*C_out^2"];
    interface_2_in_0x564137c33660 -> interface_2_out_0x564137c33660 [label="H"];
    interface_2_in_0x564137c33840 -> op_0x564137c33820 [label="H"];
    op_0x564137c3ab40 -> interface_2_out_0x564137c34378 [label="g^-1*C_out"];
    op_0x564137c33820 -> op_0x564137c35440 [label="H"];
    op_0x564137c35440 -> op_0x564137c3ab40 [label="g^-3*k_1*C_out^3"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x564137b896f0 [label="N", shape=none];
    interface_3_out_0x564137c32970 [label="C_in", shape=none];
    interface_3_out_0x564137c33660 [label="H", shape=none];
    interface_3_out_0x564137c33840 [label="H", shape=none];
}

interface_3_out_0x564137b896f0 -> interface_2_in_0x564137b896f0;
interface_3_out_0x564137c32970 -> interface_2_in_0x564137c32970;
interface_3_out_0x564137c33660 -> interface_2_in_0x564137c33660;
interface_3_out_0x564137c33840 -> interface_2_in_0x564137c33840;

interface_2_out_0x564137b896f0 -> interface_1_in_0x564137b896f0;
interface_2_out_0x564137c34378 -> interface_1_in_0x564137c34378;
interface_2_out_0x564137c32a10 -> interface_1_in_0x564137c32a10;
interface_2_out_0x564137c32970 -> interface_1_in_0x564137c32970;
interface_2_out_0x564137c33660 -> interface_1_in_0x564137c33660;
interface_2_out_0x564137b89768 -> interface_1_in_0x564137b89768;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x564137c329d8 [label="g", shape=none];
    interface_4_out_0x564137c32a28 [label="g^-2*k_1*C_out^2", shape=none];
    interface_4_out_0x564137c32988 [label="C_in", shape=none];
}

interface_4_out_0x564137c329d8 -> interface_1_in_0x564137c329d8;
interface_4_out_0x564137c32a28 -> interface_1_in_0x564137c32a28;
interface_4_out_0x564137c32988 -> interface_1_in_0x564137c32988;

interface_1_out_0x564137b896f0 -> interface_0_in_0x564137b896f0;
interface_1_out_0x564137c34360 -> interface_0_in_0x564137c34360;
interface_1_out_0x564137c34378 -> interface_0_in_0x564137c34378;
interface_1_out_0x564137c33660 -> interface_0_in_0x564137c33660;
interface_1_out_0x564137b89768 -> interface_0_in_0x564137b89768;

{
    rank = same;
    interface_3_out_0x564137b896f0;
    interface_3_out_0x564137c32970;
    interface_3_out_0x564137c33660;
    interface_3_out_0x564137c33840;
    interface_4_out_0x564137c329d8;
    interface_4_out_0x564137c32a28;
    interface_4_out_0x564137c32988;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x564137b896f0 [label="N", shape=none];
    interface_5_in_0x564137b89718 [label="C_out", shape=none];
    interface_5_in_0x564137b89740 [label="H", shape=none];
    interface_5_in_0x564137b89768 [label="H", shape=none];
}
interface_0_out_0x564137b896f0 -> interface_5_in_0x564137b896f0;
interface_0_out_0x564137b89718 -> interface_5_in_0x564137b89718;
interface_0_out_0x564137b89740 -> interface_5_in_0x564137b89740;
interface_0_out_0x564137b89768 -> interface_5_in_0x564137b89768;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shiftfc60687302f6e070 -> [H]@Unfold1bce12f3db877caf
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfold1bce12f3db877caf -> [H]@Iteratorb0a1def4ad5784ec, [g^-3*k_1*C_out^3]@Split76d6c5cc2b3c6b35
		t_2 = torch.reshape(t_2, (1, 7168, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 128, 56, 3, 56, ))

		# [g^-3*k_1*C_out^3]@Split76d6c5cc2b3c6b35 -> [g^-1*C_out]@Merge402ce7fe20a0a5f8, [g^-2*k_1*C_out^2]@Sharebed6e62aeea7a7a2
		t_2 = torch.reshape(t_2, (1, 128, 56, 1, 3, 56, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 3, 4, 1, 2, 5, ))

		# Perform contraction.
		t_3 = torch.einsum("lokinm, jki -> ljonm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 32, 56, 56, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shiftfc60687302f6e070 -> [H]@Unfold1bce12f3db877caf
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfold1bce12f3db877caf -> [H]@Iteratorb0a1def4ad5784ec, [g^-3*k_1*C_out^3]@Split76d6c5cc2b3c6b35
		t_2 = torch.reshape(t_2, (1, 3584, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 128, 28, 3, 28, ))

		# [g^-3*k_1*C_out^3]@Split76d6c5cc2b3c6b35 -> [g^-1*C_out]@Merge402ce7fe20a0a5f8, [g^-2*k_1*C_out^2]@Sharebed6e62aeea7a7a2
		t_2 = torch.reshape(t_2, (1, 128, 28, 1, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 3, 4, 1, 2, 5, ))

		# Perform contraction.
		t_3 = torch.einsum("lokinm, jki -> ljonm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 32, 28, 28, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shiftfc60687302f6e070 -> [H]@Unfold1bce12f3db877caf
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfold1bce12f3db877caf -> [H]@Iteratorb0a1def4ad5784ec, [g^-3*k_1*C_out^3]@Split76d6c5cc2b3c6b35
		t_2 = torch.reshape(t_2, (1, 1792, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 128, 14, 3, 14, ))

		# [g^-3*k_1*C_out^3]@Split76d6c5cc2b3c6b35 -> [g^-1*C_out]@Merge402ce7fe20a0a5f8, [g^-2*k_1*C_out^2]@Sharebed6e62aeea7a7a2
		t_2 = torch.reshape(t_2, (1, 128, 14, 1, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 3, 4, 1, 2, 5, ))

		# Perform contraction.
		t_3 = torch.einsum("lokinm, jki -> ljonm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 32, 14, 14, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shiftfc60687302f6e070 -> [H]@Unfold1bce12f3db877caf
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfold1bce12f3db877caf -> [H]@Iteratorb0a1def4ad5784ec, [g^-3*k_1*C_out^3]@Split76d6c5cc2b3c6b35
		t_2 = torch.reshape(t_2, (1, 896, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 128, 7, 3, 7, ))

		# [g^-3*k_1*C_out^3]@Split76d6c5cc2b3c6b35 -> [g^-1*C_out]@Merge402ce7fe20a0a5f8, [g^-2*k_1*C_out^2]@Sharebed6e62aeea7a7a2
		t_2 = torch.reshape(t_2, (1, 128, 7, 1, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 3, 4, 1, 2, 5, ))

		# Perform contraction.
		t_3 = torch.einsum("lokinm, jki -> ljonm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 32, 7, 7, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_4

		return y

