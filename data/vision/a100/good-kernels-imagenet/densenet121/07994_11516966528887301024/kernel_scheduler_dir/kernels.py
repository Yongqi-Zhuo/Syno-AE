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
        interface_0_out_0x55e3a880e020 [label="N", shape=none];
        interface_0_out_0x55e3a880e048 [label="C_out", shape=none];
        interface_0_out_0x55e3a880e070 [label="H", shape=none];
        interface_0_out_0x55e3a880e098 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55e3a880e020;
        interface_0_out_0x55e3a880e048;
        interface_0_out_0x55e3a880e070;
        interface_0_out_0x55e3a880e098;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55e3a880e020 [label="N", shape=none];
        interface_0_in_0x55e3a8935870 [label="g", shape=none];
        interface_0_in_0x55e3a8935888 [label="g^-1*C_out", shape=none];
        interface_0_in_0x55e39eb542e0 [label="H", shape=none];
        interface_0_in_0x55e3a880e098 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55e3a880e020;
        interface_0_in_0x55e3a8935870;
        interface_0_in_0x55e3a8935888;
        interface_0_in_0x55e39eb542e0;
        interface_0_in_0x55e3a880e098;
    }
    // Op's.
    op_0x55e39eb542c0 [label="Shift"];
    op_0x55e3a8935830 [label="Merge"];
    // Dimension's.
    interface_0_in_0x55e39eb542e0 -> op_0x55e39eb542c0 [label="H"];
    interface_0_in_0x55e3a880e020 -> interface_0_out_0x55e3a880e020 [label="N"];
    op_0x55e3a8935830 -> interface_0_out_0x55e3a880e048 [label="C_out"];
    op_0x55e39eb542c0 -> interface_0_out_0x55e3a880e070 [label="H"];
    interface_0_in_0x55e3a880e098 -> interface_0_out_0x55e3a880e098 [label="H"];
    interface_0_in_0x55e3a8935870 -> op_0x55e3a8935830 [label="g"];
    interface_0_in_0x55e3a8935888 -> op_0x55e3a8935830 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fb2b800e0d8 [label="Sum", shape=box];
    reduce_0x7fb2b80077d8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55e3a880e020 [label="N", shape=none];
        interface_1_out_0x55e3a8935870 [label="g", shape=none];
        interface_1_out_0x55e3a8935888 [label="g^-1*C_out", shape=none];
        interface_1_out_0x55e39eb542e0 [label="H", shape=none];
        interface_1_out_0x55e3a880e098 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fb2b800e0d8;
        reduce_0x7fb2b80077d8;
        interface_1_out_0x55e3a880e020;
        interface_1_out_0x55e3a8935870;
        interface_1_out_0x55e3a8935888;
        interface_1_out_0x55e39eb542e0;
        interface_1_out_0x55e3a880e098;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55e3a880e020 [label="N", shape=none];
        interface_1_in_0x55e3a8935888 [label="g^-1*C_out", shape=none];
        interface_1_in_0x55e3a8934650 [label="g^-2*k_1*C_out^2", shape=none];
        interface_1_in_0x55e3a89345b0 [label="C_in", shape=none];
        interface_1_in_0x55e39eb542e0 [label="H", shape=none];
        interface_1_in_0x55e3a880e098 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55e3a8934618 [label="g", shape=none];
        interface_1_in_0x55e3a8934668 [label="g^-2*k_1*C_out^2", shape=none];
        interface_1_in_0x55e3a89345c8 [label="C_in", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55e3a880e020;
        interface_1_in_0x55e3a8935888;
        interface_1_in_0x55e3a8934650;
        interface_1_in_0x55e3a89345b0;
        interface_1_in_0x55e39eb542e0;
        interface_1_in_0x55e3a880e098;
        interface_1_in_0x55e3a8934618;
        interface_1_in_0x55e3a8934668;
        interface_1_in_0x55e3a89345c8;
    }
    // Op's.
    op_0x55e3a8934590 [label="Share"];
    op_0x55e3a89345e0 [label="Share"];
    op_0x55e3a8934630 [label="Share"];
    op_0x55e3a8934938 [label="Expand"];
    // Dimension's.
    interface_1_in_0x55e39eb542e0 -> interface_1_out_0x55e39eb542e0 [label="H"];
    interface_1_in_0x55e3a880e020 -> interface_1_out_0x55e3a880e020 [label="N"];
    interface_1_in_0x55e3a880e098 -> interface_1_out_0x55e3a880e098 [label="H"];
    interface_1_in_0x55e3a89345b0 -> op_0x55e3a8934590 [label="C_in"];
    interface_1_in_0x55e3a89345c8 -> op_0x55e3a8934590 [label="C_in"];
    op_0x55e3a8934938 -> op_0x55e3a89345e0 [label="g"];
    interface_1_in_0x55e3a8934618 -> op_0x55e3a89345e0 [label="g"];
    interface_1_in_0x55e3a8934650 -> op_0x55e3a8934630 [label="g^-2*k_1*C_out^2"];
    interface_1_in_0x55e3a8934668 -> op_0x55e3a8934630 [label="g^-2*k_1*C_out^2"];
    op_0x55e3a89345e0 -> interface_1_out_0x55e3a8935870 [label="g"];
    interface_1_in_0x55e3a8935888 -> interface_1_out_0x55e3a8935888 [label="g^-1*C_out"];
    op_0x55e3a8934590 -> reduce_0x7fb2b80077d8 [label="C_in"];
    op_0x55e3a8934630 -> reduce_0x7fb2b800e0d8 [label="g^-2*k_1*C_out^2"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55e3a880e020 [label="N", shape=none];
        interface_2_out_0x55e3a8935888 [label="g^-1*C_out", shape=none];
        interface_2_out_0x55e3a8934650 [label="g^-2*k_1*C_out^2", shape=none];
        interface_2_out_0x55e3a89345b0 [label="C_in", shape=none];
        interface_2_out_0x55e39eb542e0 [label="H", shape=none];
        interface_2_out_0x55e3a880e098 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x55e3a880e020;
        interface_2_out_0x55e3a8935888;
        interface_2_out_0x55e3a8934650;
        interface_2_out_0x55e3a89345b0;
        interface_2_out_0x55e39eb542e0;
        interface_2_out_0x55e3a880e098;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55e3a880e020 [label="N", shape=none];
        interface_2_in_0x55e3a89345b0 [label="C_in", shape=none];
        interface_2_in_0x55e39eb542e0 [label="H", shape=none];
        interface_2_in_0x55e39eb543d0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55e3a880e020;
        interface_2_in_0x55e3a89345b0;
        interface_2_in_0x55e39eb542e0;
        interface_2_in_0x55e39eb543d0;
    }
    // Op's.
    op_0x55e39eb543b0 [label="Shift"];
    op_0x55e3a8936800 [label="Unfold"];
    op_0x55e3a8937a50 [label="Split"];
    // Dimension's.
    interface_2_in_0x55e39eb542e0 -> interface_2_out_0x55e39eb542e0 [label="H"];
    interface_2_in_0x55e39eb543d0 -> op_0x55e39eb543b0 [label="H"];
    interface_2_in_0x55e3a880e020 -> interface_2_out_0x55e3a880e020 [label="N"];
    op_0x55e3a8936800 -> interface_2_out_0x55e3a880e098 [label="H"];
    interface_2_in_0x55e3a89345b0 -> interface_2_out_0x55e3a89345b0 [label="C_in"];
    op_0x55e3a8937a50 -> interface_2_out_0x55e3a8934650 [label="g^-2*k_1*C_out^2"];
    op_0x55e3a8937a50 -> interface_2_out_0x55e3a8935888 [label="g^-1*C_out"];
    op_0x55e39eb543b0 -> op_0x55e3a8936800 [label="H"];
    op_0x55e3a8936800 -> op_0x55e3a8937a50 [label="g^-3*k_1*C_out^3"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x55e3a880e020 [label="N", shape=none];
    interface_3_out_0x55e3a89345b0 [label="C_in", shape=none];
    interface_3_out_0x55e39eb542e0 [label="H", shape=none];
    interface_3_out_0x55e39eb543d0 [label="H", shape=none];
}

interface_3_out_0x55e3a880e020 -> interface_2_in_0x55e3a880e020;
interface_3_out_0x55e3a89345b0 -> interface_2_in_0x55e3a89345b0;
interface_3_out_0x55e39eb542e0 -> interface_2_in_0x55e39eb542e0;
interface_3_out_0x55e39eb543d0 -> interface_2_in_0x55e39eb543d0;

interface_2_out_0x55e3a880e020 -> interface_1_in_0x55e3a880e020;
interface_2_out_0x55e3a8935888 -> interface_1_in_0x55e3a8935888;
interface_2_out_0x55e3a8934650 -> interface_1_in_0x55e3a8934650;
interface_2_out_0x55e3a89345b0 -> interface_1_in_0x55e3a89345b0;
interface_2_out_0x55e39eb542e0 -> interface_1_in_0x55e39eb542e0;
interface_2_out_0x55e3a880e098 -> interface_1_in_0x55e3a880e098;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x55e3a8934618 [label="g", shape=none];
    interface_4_out_0x55e3a8934668 [label="g^-2*k_1*C_out^2", shape=none];
    interface_4_out_0x55e3a89345c8 [label="C_in", shape=none];
}

interface_4_out_0x55e3a8934618 -> interface_1_in_0x55e3a8934618;
interface_4_out_0x55e3a8934668 -> interface_1_in_0x55e3a8934668;
interface_4_out_0x55e3a89345c8 -> interface_1_in_0x55e3a89345c8;

interface_1_out_0x55e3a880e020 -> interface_0_in_0x55e3a880e020;
interface_1_out_0x55e3a8935870 -> interface_0_in_0x55e3a8935870;
interface_1_out_0x55e3a8935888 -> interface_0_in_0x55e3a8935888;
interface_1_out_0x55e39eb542e0 -> interface_0_in_0x55e39eb542e0;
interface_1_out_0x55e3a880e098 -> interface_0_in_0x55e3a880e098;

{
    rank = same;
    interface_3_out_0x55e3a880e020;
    interface_3_out_0x55e3a89345b0;
    interface_3_out_0x55e39eb542e0;
    interface_3_out_0x55e39eb543d0;
    interface_4_out_0x55e3a8934618;
    interface_4_out_0x55e3a8934668;
    interface_4_out_0x55e3a89345c8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x55e3a880e020 [label="N", shape=none];
    interface_5_in_0x55e3a880e048 [label="C_out", shape=none];
    interface_5_in_0x55e3a880e070 [label="H", shape=none];
    interface_5_in_0x55e3a880e098 [label="H", shape=none];
}
interface_0_out_0x55e3a880e020 -> interface_5_in_0x55e3a880e020;
interface_0_out_0x55e3a880e048 -> interface_5_in_0x55e3a880e048;
interface_0_out_0x55e3a880e070 -> interface_5_in_0x55e3a880e070;
interface_0_out_0x55e3a880e098 -> interface_5_in_0x55e3a880e098;

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
		t_3 = torch.einsum("mokiln, jki -> mjoln", t_2, in_1)

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
		t_3 = torch.einsum("mokiln, jki -> mjoln", t_2, in_1)

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
		t_3 = torch.einsum("mokiln, jki -> mjoln", t_2, in_1)

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
		t_3 = torch.einsum("mokiln, jki -> mjoln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 32, 7, 7, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_4

		return y

