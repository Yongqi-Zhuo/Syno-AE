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
        interface_0_out_0x5572df8cce60 [label="N", shape=none];
        interface_0_out_0x5572df8cce88 [label="C_out", shape=none];
        interface_0_out_0x5572df8cceb0 [label="H", shape=none];
        interface_0_out_0x5572df8cced8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x5572df8cce60;
        interface_0_out_0x5572df8cce88;
        interface_0_out_0x5572df8cceb0;
        interface_0_out_0x5572df8cced8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5572df8cce60 [label="N", shape=none];
        interface_0_in_0x5572df8cce88 [label="C_out", shape=none];
        interface_0_in_0x5572df8cceb0 [label="H", shape=none];
        interface_0_in_0x5572e409eb90 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5572df8cce60;
        interface_0_in_0x5572df8cce88;
        interface_0_in_0x5572df8cceb0;
        interface_0_in_0x5572e409eb90;
    }
    // Op's.
    op_0x5572e409eb70 [label="Shift"];
    // Dimension's.
    interface_0_in_0x5572df8cce60 -> interface_0_out_0x5572df8cce60 [label="N"];
    interface_0_in_0x5572df8cce88 -> interface_0_out_0x5572df8cce88 [label="C_out"];
    interface_0_in_0x5572df8cceb0 -> interface_0_out_0x5572df8cceb0 [label="H"];
    op_0x5572e409eb70 -> interface_0_out_0x5572df8cced8 [label="H"];
    interface_0_in_0x5572e409eb90 -> op_0x5572e409eb70 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f44f8004ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5572df8cce60 [label="N", shape=none];
        interface_1_out_0x5572df8cce88 [label="C_out", shape=none];
        interface_1_out_0x5572df8cceb0 [label="H", shape=none];
        interface_1_out_0x5572e409eb90 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f44f8004ce8;
        interface_1_out_0x5572df8cce60;
        interface_1_out_0x5572df8cce88;
        interface_1_out_0x5572df8cceb0;
        interface_1_out_0x5572e409eb90;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5572df8cce60 [label="N", shape=none];
        interface_1_in_0x5572df8cce88 [label="C_out", shape=none];
        interface_1_in_0x5572e40a50f0 [label="H", shape=none];
        interface_1_in_0x5572e40a5108 [label="s", shape=none];
        interface_1_in_0x5572e409eb90 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5572df8cce60;
        interface_1_in_0x5572df8cce88;
        interface_1_in_0x5572e40a50f0;
        interface_1_in_0x5572e40a5108;
        interface_1_in_0x5572e409eb90;
    }
    // Op's.
    op_0x5572e409eba0 [label="Shift"];
    op_0x5572e409f2a0 [label="Split"];
    op_0x5572e40a50b0 [label="Merge"];
    // Dimension's.
    interface_1_in_0x5572df8cce60 -> interface_1_out_0x5572df8cce60 [label="N"];
    interface_1_in_0x5572df8cce88 -> interface_1_out_0x5572df8cce88 [label="C_out"];
    op_0x5572e409f2a0 -> interface_1_out_0x5572df8cceb0 [label="H"];
    interface_1_in_0x5572e409eb90 -> interface_1_out_0x5572e409eb90 [label="H"];
    op_0x5572e40a50b0 -> op_0x5572e409eba0 [label="s*H"];
    op_0x5572e409eba0 -> op_0x5572e409f2a0 [label="s*H"];
    interface_1_in_0x5572e40a50f0 -> op_0x5572e40a50b0 [label="H"];
    interface_1_in_0x5572e40a5108 -> op_0x5572e40a50b0 [label="s"];
    op_0x5572e409f2a0 -> reduce_0x7f44f8004ce8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f44f8003a98 [label="Sum", shape=box];
    reduce_0x7f44f8007948 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5572df8cce60 [label="N", shape=none];
        interface_2_out_0x5572df8cce88 [label="C_out", shape=none];
        interface_2_out_0x5572e40a50f0 [label="H", shape=none];
        interface_2_out_0x5572e40a5108 [label="s", shape=none];
        interface_2_out_0x5572e409eb90 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f44f8003a98;
        reduce_0x7f44f8007948;
        interface_2_out_0x5572df8cce60;
        interface_2_out_0x5572df8cce88;
        interface_2_out_0x5572e40a50f0;
        interface_2_out_0x5572e40a5108;
        interface_2_out_0x5572e409eb90;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5572df8cce60 [label="N", shape=none];
        interface_2_in_0x5572e409cc10 [label="k_1", shape=none];
        interface_2_in_0x5572e40a50f0 [label="H", shape=none];
        interface_2_in_0x5572e40cbf40 [label="C_in", shape=none];
        interface_2_in_0x5572e409eb90 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x5572e409cb38 [label="C_out", shape=none];
        interface_2_in_0x5572e409cc28 [label="k_1", shape=none];
        interface_2_in_0x5572e409ccc8 [label="s", shape=none];
        interface_2_in_0x5572e40cbf58 [label="C_in", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5572df8cce60;
        interface_2_in_0x5572e409cc10;
        interface_2_in_0x5572e40a50f0;
        interface_2_in_0x5572e40cbf40;
        interface_2_in_0x5572e409eb90;
        interface_2_in_0x5572e409cb38;
        interface_2_in_0x5572e409cc28;
        interface_2_in_0x5572e409ccc8;
        interface_2_in_0x5572e40cbf58;
    }
    // Op's.
    op_0x5572e409cb00 [label="Share"];
    op_0x5572e409cbf0 [label="Share"];
    op_0x5572e409cc90 [label="Share"];
    op_0x5572e409cfd8 [label="Expand"];
    op_0x5572e409cff8 [label="Expand"];
    op_0x5572e40cbf20 [label="Share"];
    // Dimension's.
    interface_2_in_0x5572df8cce60 -> interface_2_out_0x5572df8cce60 [label="N"];
    op_0x5572e409cb00 -> interface_2_out_0x5572df8cce88 [label="C_out"];
    op_0x5572e409cfd8 -> op_0x5572e409cb00 [label="C_out"];
    interface_2_in_0x5572e409cb38 -> op_0x5572e409cb00 [label="C_out"];
    interface_2_in_0x5572e409cc10 -> op_0x5572e409cbf0 [label="k_1"];
    interface_2_in_0x5572e409cc28 -> op_0x5572e409cbf0 [label="k_1"];
    op_0x5572e409cff8 -> op_0x5572e409cc90 [label="s"];
    interface_2_in_0x5572e409ccc8 -> op_0x5572e409cc90 [label="s"];
    interface_2_in_0x5572e409eb90 -> interface_2_out_0x5572e409eb90 [label="H"];
    interface_2_in_0x5572e40a50f0 -> interface_2_out_0x5572e40a50f0 [label="H"];
    op_0x5572e409cc90 -> interface_2_out_0x5572e40a5108 [label="s"];
    interface_2_in_0x5572e40cbf40 -> op_0x5572e40cbf20 [label="C_in"];
    interface_2_in_0x5572e40cbf58 -> op_0x5572e40cbf20 [label="C_in"];
    op_0x5572e409cbf0 -> reduce_0x7f44f8003a98 [label="k_1"];
    op_0x5572e40cbf20 -> reduce_0x7f44f8007948 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5572df8cce60 [label="N", shape=none];
        interface_3_out_0x5572e409cc10 [label="k_1", shape=none];
        interface_3_out_0x5572e40a50f0 [label="H", shape=none];
        interface_3_out_0x5572e40cbf40 [label="C_in", shape=none];
        interface_3_out_0x5572e409eb90 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5572df8cce60;
        interface_3_out_0x5572e409cc10;
        interface_3_out_0x5572e40a50f0;
        interface_3_out_0x5572e40cbf40;
        interface_3_out_0x5572e409eb90;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5572df8cce60 [label="N", shape=none];
        interface_3_in_0x5572e40cbf40 [label="C_in", shape=none];
        interface_3_in_0x5572e409eb90 [label="H", shape=none];
        interface_3_in_0x5572e40b1de8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5572df8cce60;
        interface_3_in_0x5572e40cbf40;
        interface_3_in_0x5572e409eb90;
        interface_3_in_0x5572e40b1de8;
    }
    // Op's.
    op_0x5572e40b1dc0 [label="Unfold"];
    // Dimension's.
    interface_3_in_0x5572df8cce60 -> interface_3_out_0x5572df8cce60 [label="N"];
    op_0x5572e40b1dc0 -> interface_3_out_0x5572e409cc10 [label="k_1"];
    interface_3_in_0x5572e409eb90 -> interface_3_out_0x5572e409eb90 [label="H"];
    op_0x5572e40b1dc0 -> interface_3_out_0x5572e40a50f0 [label="H"];
    interface_3_in_0x5572e40b1de8 -> op_0x5572e40b1dc0 [label="H"];
    interface_3_in_0x5572e40cbf40 -> interface_3_out_0x5572e40cbf40 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x5572df8cce60 [label="N", shape=none];
    interface_4_out_0x5572e40cbf40 [label="C_in", shape=none];
    interface_4_out_0x5572e409eb90 [label="H", shape=none];
    interface_4_out_0x5572e40b1de8 [label="H", shape=none];
}

interface_4_out_0x5572df8cce60 -> interface_3_in_0x5572df8cce60;
interface_4_out_0x5572e40cbf40 -> interface_3_in_0x5572e40cbf40;
interface_4_out_0x5572e409eb90 -> interface_3_in_0x5572e409eb90;
interface_4_out_0x5572e40b1de8 -> interface_3_in_0x5572e40b1de8;

interface_3_out_0x5572df8cce60 -> interface_2_in_0x5572df8cce60;
interface_3_out_0x5572e409cc10 -> interface_2_in_0x5572e409cc10;
interface_3_out_0x5572e40a50f0 -> interface_2_in_0x5572e40a50f0;
interface_3_out_0x5572e40cbf40 -> interface_2_in_0x5572e40cbf40;
interface_3_out_0x5572e409eb90 -> interface_2_in_0x5572e409eb90;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x5572e409cb38 [label="C_out", shape=none];
    interface_5_out_0x5572e409cc28 [label="k_1", shape=none];
    interface_5_out_0x5572e409ccc8 [label="s", shape=none];
    interface_5_out_0x5572e40cbf58 [label="C_in", shape=none];
}

interface_5_out_0x5572e409cb38 -> interface_2_in_0x5572e409cb38;
interface_5_out_0x5572e409cc28 -> interface_2_in_0x5572e409cc28;
interface_5_out_0x5572e409ccc8 -> interface_2_in_0x5572e409ccc8;
interface_5_out_0x5572e40cbf58 -> interface_2_in_0x5572e40cbf58;

interface_2_out_0x5572df8cce60 -> interface_1_in_0x5572df8cce60;
interface_2_out_0x5572df8cce88 -> interface_1_in_0x5572df8cce88;
interface_2_out_0x5572e40a50f0 -> interface_1_in_0x5572e40a50f0;
interface_2_out_0x5572e40a5108 -> interface_1_in_0x5572e40a5108;
interface_2_out_0x5572e409eb90 -> interface_1_in_0x5572e409eb90;

interface_1_out_0x5572df8cce60 -> interface_0_in_0x5572df8cce60;
interface_1_out_0x5572df8cce88 -> interface_0_in_0x5572df8cce88;
interface_1_out_0x5572df8cceb0 -> interface_0_in_0x5572df8cceb0;
interface_1_out_0x5572e409eb90 -> interface_0_in_0x5572e409eb90;

{
    rank = same;
    interface_4_out_0x5572df8cce60;
    interface_4_out_0x5572e40cbf40;
    interface_4_out_0x5572e409eb90;
    interface_4_out_0x5572e40b1de8;
    interface_5_out_0x5572e409cb38;
    interface_5_out_0x5572e409cc28;
    interface_5_out_0x5572e409ccc8;
    interface_5_out_0x5572e40cbf58;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x5572df8cce60 [label="N", shape=none];
    interface_6_in_0x5572df8cce88 [label="C_out", shape=none];
    interface_6_in_0x5572df8cceb0 [label="H", shape=none];
    interface_6_in_0x5572df8cced8 [label="H", shape=none];
}
interface_0_out_0x5572df8cce60 -> interface_6_in_0x5572df8cce60;
interface_0_out_0x5572df8cce88 -> interface_6_in_0x5572df8cce88;
interface_0_out_0x5572df8cceb0 -> interface_6_in_0x5572df8cceb0;
interface_0_out_0x5572df8cced8 -> interface_6_in_0x5572df8cced8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 3, 2, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("iljk -> iklj", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 56, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 56, 64, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("mjoln, ijkl -> miokn", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 64, 112, 56, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 64, 56, 2, 56, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 2, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("iljk -> iklj", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 28, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 28, 64, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("mjoln, ijkl -> miokn", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 128, 56, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 128, 28, 2, 28, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 2, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("iljk -> iklj", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 28, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 28, 128, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("mjoln, ijkl -> miokn", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 128, 56, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 128, 28, 2, 28, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 2, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("iljk -> iklj", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 14, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 14, 128, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("mjoln, ijkl -> miokn", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 256, 28, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 256, 14, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 2, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("iljk -> iklj", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 14, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 14, 256, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("mjoln, ijkl -> miokn", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 256, 28, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 256, 14, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 3, 2, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("iljk -> iklj", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 7, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 7, 256, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("mjoln, ijkl -> miokn", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 512, 14, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 512, 7, 2, 7, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 3, 2, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("iljk -> iklj", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 7, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 7, 512, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("mjoln, ijkl -> miokn", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 512, 14, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 512, 7, 2, 7, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

