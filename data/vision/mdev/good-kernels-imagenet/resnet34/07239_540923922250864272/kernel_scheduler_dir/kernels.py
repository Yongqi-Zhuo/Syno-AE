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
        interface_0_out_0x55dcca2d4a60 [label="N", shape=none];
        interface_0_out_0x55dcca2d4a88 [label="C_out", shape=none];
        interface_0_out_0x55dcca2d4ab0 [label="H", shape=none];
        interface_0_out_0x55dcca2d4ad8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55dcca2d4a60;
        interface_0_out_0x55dcca2d4a88;
        interface_0_out_0x55dcca2d4ab0;
        interface_0_out_0x55dcca2d4ad8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55dcca2d4a60 [label="N", shape=none];
        interface_0_in_0x55dcca2d4a88 [label="C_out", shape=none];
        interface_0_in_0x55dcca2d4ab0 [label="H", shape=none];
        interface_0_in_0x55dcca86dd50 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55dcca2d4a60;
        interface_0_in_0x55dcca2d4a88;
        interface_0_in_0x55dcca2d4ab0;
        interface_0_in_0x55dcca86dd50;
    }
    // Op's.
    op_0x55dcca86dd30 [label="Shift"];
    // Dimension's.
    interface_0_in_0x55dcca2d4a60 -> interface_0_out_0x55dcca2d4a60 [label="N"];
    interface_0_in_0x55dcca2d4a88 -> interface_0_out_0x55dcca2d4a88 [label="C_out"];
    interface_0_in_0x55dcca2d4ab0 -> interface_0_out_0x55dcca2d4ab0 [label="H"];
    op_0x55dcca86dd30 -> interface_0_out_0x55dcca2d4ad8 [label="H"];
    interface_0_in_0x55dcca86dd50 -> op_0x55dcca86dd30 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f8754004ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55dcca2d4a60 [label="N", shape=none];
        interface_1_out_0x55dcca2d4a88 [label="C_out", shape=none];
        interface_1_out_0x55dcca2d4ab0 [label="H", shape=none];
        interface_1_out_0x55dcca86dd50 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f8754004ce8;
        interface_1_out_0x55dcca2d4a60;
        interface_1_out_0x55dcca2d4a88;
        interface_1_out_0x55dcca2d4ab0;
        interface_1_out_0x55dcca86dd50;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55dcca2d4a60 [label="N", shape=none];
        interface_1_in_0x55dcca2d4a88 [label="C_out", shape=none];
        interface_1_in_0x55dcd9674dc0 [label="H", shape=none];
        interface_1_in_0x55dcd9674dd8 [label="s", shape=none];
        interface_1_in_0x55dcca86dd50 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55dcca2d4a60;
        interface_1_in_0x55dcca2d4a88;
        interface_1_in_0x55dcd9674dc0;
        interface_1_in_0x55dcd9674dd8;
        interface_1_in_0x55dcca86dd50;
    }
    // Op's.
    op_0x55dcca86dd90 [label="Shift"];
    op_0x55dcd9673a20 [label="Split"];
    op_0x55dcd9674d80 [label="Merge"];
    // Dimension's.
    interface_1_in_0x55dcca2d4a60 -> interface_1_out_0x55dcca2d4a60 [label="N"];
    interface_1_in_0x55dcca2d4a88 -> interface_1_out_0x55dcca2d4a88 [label="C_out"];
    op_0x55dcd9673a20 -> interface_1_out_0x55dcca2d4ab0 [label="H"];
    interface_1_in_0x55dcca86dd50 -> interface_1_out_0x55dcca86dd50 [label="H"];
    op_0x55dcd9674d80 -> op_0x55dcca86dd90 [label="s*H"];
    op_0x55dcca86dd90 -> op_0x55dcd9673a20 [label="s*H"];
    interface_1_in_0x55dcd9674dc0 -> op_0x55dcd9674d80 [label="H"];
    interface_1_in_0x55dcd9674dd8 -> op_0x55dcd9674d80 [label="s"];
    op_0x55dcd9673a20 -> reduce_0x7f8754004ce8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f8754003a98 [label="Sum", shape=box];
    reduce_0x7f8754007948 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55dcca2d4a60 [label="N", shape=none];
        interface_2_out_0x55dcca2d4a88 [label="C_out", shape=none];
        interface_2_out_0x55dcd9674dc0 [label="H", shape=none];
        interface_2_out_0x55dcd9674dd8 [label="s", shape=none];
        interface_2_out_0x55dcca86dd50 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f8754003a98;
        reduce_0x7f8754007948;
        interface_2_out_0x55dcca2d4a60;
        interface_2_out_0x55dcca2d4a88;
        interface_2_out_0x55dcd9674dc0;
        interface_2_out_0x55dcd9674dd8;
        interface_2_out_0x55dcca86dd50;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55dcca2d4a60 [label="N", shape=none];
        interface_2_in_0x55dcd9672b10 [label="k_1", shape=none];
        interface_2_in_0x55dcd9674dc0 [label="H", shape=none];
        interface_2_in_0x55dcd9672ac0 [label="C_in", shape=none];
        interface_2_in_0x55dcca86dd50 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x55dcd9672a38 [label="C_out", shape=none];
        interface_2_in_0x55dcd9672b28 [label="k_1", shape=none];
        interface_2_in_0x55dcd9672bc8 [label="s", shape=none];
        interface_2_in_0x55dcd9672ad8 [label="C_in", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55dcca2d4a60;
        interface_2_in_0x55dcd9672b10;
        interface_2_in_0x55dcd9674dc0;
        interface_2_in_0x55dcd9672ac0;
        interface_2_in_0x55dcca86dd50;
        interface_2_in_0x55dcd9672a38;
        interface_2_in_0x55dcd9672b28;
        interface_2_in_0x55dcd9672bc8;
        interface_2_in_0x55dcd9672ad8;
    }
    // Op's.
    op_0x55dcd9672a00 [label="Share"];
    op_0x55dcd9672aa0 [label="Share"];
    op_0x55dcd9672af0 [label="Share"];
    op_0x55dcd9672b90 [label="Share"];
    op_0x55dcd9672ed8 [label="Expand"];
    op_0x55dcd9672f18 [label="Expand"];
    // Dimension's.
    interface_2_in_0x55dcca2d4a60 -> interface_2_out_0x55dcca2d4a60 [label="N"];
    op_0x55dcd9672a00 -> interface_2_out_0x55dcca2d4a88 [label="C_out"];
    interface_2_in_0x55dcca86dd50 -> interface_2_out_0x55dcca86dd50 [label="H"];
    op_0x55dcd9672ed8 -> op_0x55dcd9672a00 [label="C_out"];
    interface_2_in_0x55dcd9672a38 -> op_0x55dcd9672a00 [label="C_out"];
    interface_2_in_0x55dcd9672ac0 -> op_0x55dcd9672aa0 [label="C_in"];
    interface_2_in_0x55dcd9672ad8 -> op_0x55dcd9672aa0 [label="C_in"];
    interface_2_in_0x55dcd9672b10 -> op_0x55dcd9672af0 [label="k_1"];
    interface_2_in_0x55dcd9672b28 -> op_0x55dcd9672af0 [label="k_1"];
    op_0x55dcd9672f18 -> op_0x55dcd9672b90 [label="s"];
    interface_2_in_0x55dcd9672bc8 -> op_0x55dcd9672b90 [label="s"];
    interface_2_in_0x55dcd9674dc0 -> interface_2_out_0x55dcd9674dc0 [label="H"];
    op_0x55dcd9672b90 -> interface_2_out_0x55dcd9674dd8 [label="s"];
    op_0x55dcd9672af0 -> reduce_0x7f8754003a98 [label="k_1"];
    op_0x55dcd9672aa0 -> reduce_0x7f8754007948 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55dcca2d4a60 [label="N", shape=none];
        interface_3_out_0x55dcd9672b10 [label="k_1", shape=none];
        interface_3_out_0x55dcd9674dc0 [label="H", shape=none];
        interface_3_out_0x55dcd9672ac0 [label="C_in", shape=none];
        interface_3_out_0x55dcca86dd50 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x55dcca2d4a60;
        interface_3_out_0x55dcd9672b10;
        interface_3_out_0x55dcd9674dc0;
        interface_3_out_0x55dcd9672ac0;
        interface_3_out_0x55dcca86dd50;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55dcca2d4a60 [label="N", shape=none];
        interface_3_in_0x55dcd9672ac0 [label="C_in", shape=none];
        interface_3_in_0x55dcca86dd50 [label="H", shape=none];
        interface_3_in_0x55dcd9680868 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55dcca2d4a60;
        interface_3_in_0x55dcd9672ac0;
        interface_3_in_0x55dcca86dd50;
        interface_3_in_0x55dcd9680868;
    }
    // Op's.
    op_0x55dcd9680840 [label="Unfold"];
    // Dimension's.
    interface_3_in_0x55dcca2d4a60 -> interface_3_out_0x55dcca2d4a60 [label="N"];
    interface_3_in_0x55dcca86dd50 -> interface_3_out_0x55dcca86dd50 [label="H"];
    interface_3_in_0x55dcd9672ac0 -> interface_3_out_0x55dcd9672ac0 [label="C_in"];
    op_0x55dcd9680840 -> interface_3_out_0x55dcd9672b10 [label="k_1"];
    op_0x55dcd9680840 -> interface_3_out_0x55dcd9674dc0 [label="H"];
    interface_3_in_0x55dcd9680868 -> op_0x55dcd9680840 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x55dcca2d4a60 [label="N", shape=none];
    interface_4_out_0x55dcd9672ac0 [label="C_in", shape=none];
    interface_4_out_0x55dcca86dd50 [label="H", shape=none];
    interface_4_out_0x55dcd9680868 [label="H", shape=none];
}

interface_4_out_0x55dcca2d4a60 -> interface_3_in_0x55dcca2d4a60;
interface_4_out_0x55dcd9672ac0 -> interface_3_in_0x55dcd9672ac0;
interface_4_out_0x55dcca86dd50 -> interface_3_in_0x55dcca86dd50;
interface_4_out_0x55dcd9680868 -> interface_3_in_0x55dcd9680868;

interface_3_out_0x55dcca2d4a60 -> interface_2_in_0x55dcca2d4a60;
interface_3_out_0x55dcd9672b10 -> interface_2_in_0x55dcd9672b10;
interface_3_out_0x55dcd9674dc0 -> interface_2_in_0x55dcd9674dc0;
interface_3_out_0x55dcd9672ac0 -> interface_2_in_0x55dcd9672ac0;
interface_3_out_0x55dcca86dd50 -> interface_2_in_0x55dcca86dd50;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x55dcd9672a38 [label="C_out", shape=none];
    interface_5_out_0x55dcd9672b28 [label="k_1", shape=none];
    interface_5_out_0x55dcd9672bc8 [label="s", shape=none];
    interface_5_out_0x55dcd9672ad8 [label="C_in", shape=none];
}

interface_5_out_0x55dcd9672a38 -> interface_2_in_0x55dcd9672a38;
interface_5_out_0x55dcd9672b28 -> interface_2_in_0x55dcd9672b28;
interface_5_out_0x55dcd9672bc8 -> interface_2_in_0x55dcd9672bc8;
interface_5_out_0x55dcd9672ad8 -> interface_2_in_0x55dcd9672ad8;

interface_2_out_0x55dcca2d4a60 -> interface_1_in_0x55dcca2d4a60;
interface_2_out_0x55dcca2d4a88 -> interface_1_in_0x55dcca2d4a88;
interface_2_out_0x55dcd9674dc0 -> interface_1_in_0x55dcd9674dc0;
interface_2_out_0x55dcd9674dd8 -> interface_1_in_0x55dcd9674dd8;
interface_2_out_0x55dcca86dd50 -> interface_1_in_0x55dcca86dd50;

interface_1_out_0x55dcca2d4a60 -> interface_0_in_0x55dcca2d4a60;
interface_1_out_0x55dcca2d4a88 -> interface_0_in_0x55dcca2d4a88;
interface_1_out_0x55dcca2d4ab0 -> interface_0_in_0x55dcca2d4ab0;
interface_1_out_0x55dcca86dd50 -> interface_0_in_0x55dcca86dd50;

{
    rank = same;
    interface_4_out_0x55dcca2d4a60;
    interface_4_out_0x55dcd9672ac0;
    interface_4_out_0x55dcca86dd50;
    interface_4_out_0x55dcd9680868;
    interface_5_out_0x55dcd9672a38;
    interface_5_out_0x55dcd9672b28;
    interface_5_out_0x55dcd9672bc8;
    interface_5_out_0x55dcd9672ad8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x55dcca2d4a60 [label="N", shape=none];
    interface_6_in_0x55dcca2d4a88 [label="C_out", shape=none];
    interface_6_in_0x55dcca2d4ab0 [label="H", shape=none];
    interface_6_in_0x55dcca2d4ad8 [label="H", shape=none];
}
interface_0_out_0x55dcca2d4a60 -> interface_6_in_0x55dcca2d4a60;
interface_0_out_0x55dcca2d4a88 -> interface_6_in_0x55dcca2d4a88;
interface_0_out_0x55dcca2d4ab0 -> interface_6_in_0x55dcca2d4ab0;
interface_0_out_0x55dcca2d4ad8 -> interface_6_in_0x55dcca2d4ad8;

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
		t_2 = torch.einsum("ikjl -> ilkj", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 56, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 56, 64, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

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
		t_2 = torch.einsum("ikjl -> ilkj", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 28, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 28, 64, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

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
		t_2 = torch.einsum("ikjl -> ilkj", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 28, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 28, 128, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

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
		t_2 = torch.einsum("ikjl -> ilkj", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 14, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 14, 128, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

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
		t_2 = torch.einsum("ikjl -> ilkj", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 14, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 14, 256, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

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
		t_2 = torch.einsum("ikjl -> ilkj", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 7, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 7, 256, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

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
		t_2 = torch.einsum("ikjl -> ilkj", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 7, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 7, 512, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

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

