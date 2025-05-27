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
        interface_0_out_0x56459a9d6050 [label="N", shape=none];
        interface_0_out_0x56459a9d6078 [label="C_out", shape=none];
        interface_0_out_0x56459a9d60a0 [label="H", shape=none];
        interface_0_out_0x56459a9d60c8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x56459a9d6050;
        interface_0_out_0x56459a9d6078;
        interface_0_out_0x56459a9d60a0;
        interface_0_out_0x56459a9d60c8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x56459a9d6050 [label="N", shape=none];
        interface_0_in_0x56459a9d6078 [label="C_out", shape=none];
        interface_0_in_0x56459c25a500 [label="s", shape=none];
        interface_0_in_0x56459c25a518 [label="s^-1*H", shape=none];
        interface_0_in_0x56459c259050 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x56459a9d6050;
        interface_0_in_0x56459a9d6078;
        interface_0_in_0x56459c25a500;
        interface_0_in_0x56459c25a518;
        interface_0_in_0x56459c259050;
    }
    // Op's.
    op_0x56459c259030 [label="Shift"];
    op_0x56459c25a4c0 [label="Merge"];
    // Dimension's.
    interface_0_in_0x56459a9d6050 -> interface_0_out_0x56459a9d6050 [label="N"];
    interface_0_in_0x56459a9d6078 -> interface_0_out_0x56459a9d6078 [label="C_out"];
    op_0x56459c25a4c0 -> interface_0_out_0x56459a9d60a0 [label="H"];
    op_0x56459c259030 -> interface_0_out_0x56459a9d60c8 [label="H"];
    interface_0_in_0x56459c259050 -> op_0x56459c259030 [label="H"];
    interface_0_in_0x56459c25a500 -> op_0x56459c25a4c0 [label="s"];
    interface_0_in_0x56459c25a518 -> op_0x56459c25a4c0 [label="s^-1*H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fdbac001a98 [label="Sum", shape=box];
    reduce_0x7fdbac0034d0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x56459a9d6050 [label="N", shape=none];
        interface_1_out_0x56459a9d6078 [label="C_out", shape=none];
        interface_1_out_0x56459c25a500 [label="s", shape=none];
        interface_1_out_0x56459c25a518 [label="s^-1*H", shape=none];
        interface_1_out_0x56459c259050 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fdbac001a98;
        reduce_0x7fdbac0034d0;
        interface_1_out_0x56459a9d6050;
        interface_1_out_0x56459a9d6078;
        interface_1_out_0x56459c25a500;
        interface_1_out_0x56459c25a518;
        interface_1_out_0x56459c259050;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x56459a9d6050 [label="N", shape=none];
        interface_1_in_0x56459c25a500 [label="s", shape=none];
        interface_1_in_0x56459c258610 [label="k_1", shape=none];
        interface_1_in_0x56459c25a518 [label="s^-1*H", shape=none];
        interface_1_in_0x56459c259050 [label="H", shape=none];
        interface_1_in_0x56459c258700 [label="k_2*s", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x56459c2582b8 [label="C_out", shape=none];
        interface_1_in_0x56459c258628 [label="k_1", shape=none];
        interface_1_in_0x56459c258718 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x56459a9d6050;
        interface_1_in_0x56459c25a500;
        interface_1_in_0x56459c258610;
        interface_1_in_0x56459c25a518;
        interface_1_in_0x56459c259050;
        interface_1_in_0x56459c258700;
        interface_1_in_0x56459c2582b8;
        interface_1_in_0x56459c258628;
        interface_1_in_0x56459c258718;
    }
    // Op's.
    op_0x56459c258280 [label="Share"];
    op_0x56459c2585f0 [label="Share"];
    op_0x56459c2586e0 [label="Share"];
    op_0x56459c258778 [label="Expand"];
    // Dimension's.
    interface_1_in_0x56459a9d6050 -> interface_1_out_0x56459a9d6050 [label="N"];
    op_0x56459c258280 -> interface_1_out_0x56459a9d6078 [label="C_out"];
    op_0x56459c258778 -> op_0x56459c258280 [label="C_out"];
    interface_1_in_0x56459c2582b8 -> op_0x56459c258280 [label="C_out"];
    interface_1_in_0x56459c258610 -> op_0x56459c2585f0 [label="k_1"];
    interface_1_in_0x56459c258628 -> op_0x56459c2585f0 [label="k_1"];
    interface_1_in_0x56459c258700 -> op_0x56459c2586e0 [label="k_2*s"];
    interface_1_in_0x56459c258718 -> op_0x56459c2586e0 [label="k_2*s"];
    interface_1_in_0x56459c259050 -> interface_1_out_0x56459c259050 [label="H"];
    interface_1_in_0x56459c25a500 -> interface_1_out_0x56459c25a500 [label="s"];
    interface_1_in_0x56459c25a518 -> interface_1_out_0x56459c25a518 [label="s^-1*H"];
    op_0x56459c2585f0 -> reduce_0x7fdbac001a98 [label="k_1"];
    op_0x56459c2586e0 -> reduce_0x7fdbac0034d0 [label="k_2*s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x56459a9d6050 [label="N", shape=none];
        interface_2_out_0x56459c25a500 [label="s", shape=none];
        interface_2_out_0x56459c258610 [label="k_1", shape=none];
        interface_2_out_0x56459c25a518 [label="s^-1*H", shape=none];
        interface_2_out_0x56459c259050 [label="H", shape=none];
        interface_2_out_0x56459c258700 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x56459a9d6050;
        interface_2_out_0x56459c25a500;
        interface_2_out_0x56459c258610;
        interface_2_out_0x56459c25a518;
        interface_2_out_0x56459c259050;
        interface_2_out_0x56459c258700;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x56459a9d6050 [label="N", shape=none];
        interface_2_in_0x56459c2ce540 [label="H", shape=none];
        interface_2_in_0x56459c259050 [label="H", shape=none];
        interface_2_in_0x56459c258700 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x56459a9d6050;
        interface_2_in_0x56459c2ce540;
        interface_2_in_0x56459c259050;
        interface_2_in_0x56459c258700;
    }
    // Op's.
    op_0x56459c2ce500 [label="Split"];
    op_0x56459c2d7940 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x56459a9d6050 -> interface_2_out_0x56459a9d6050 [label="N"];
    op_0x56459c2d7940 -> interface_2_out_0x56459c258610 [label="k_1"];
    interface_2_in_0x56459c258700 -> interface_2_out_0x56459c258700 [label="k_2*s"];
    interface_2_in_0x56459c259050 -> interface_2_out_0x56459c259050 [label="H"];
    op_0x56459c2ce500 -> interface_2_out_0x56459c25a500 [label="s"];
    op_0x56459c2d7940 -> interface_2_out_0x56459c25a518 [label="s^-1*H"];
    interface_2_in_0x56459c2ce540 -> op_0x56459c2ce500 [label="H"];
    op_0x56459c2ce500 -> op_0x56459c2d7940 [label="s^-1*H"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7fdbac005c70 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x56459a9d6050 [label="N", shape=none];
        interface_3_out_0x56459c2ce540 [label="H", shape=none];
        interface_3_out_0x56459c259050 [label="H", shape=none];
        interface_3_out_0x56459c258700 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        reduce_0x7fdbac005c70;
        interface_3_out_0x56459a9d6050;
        interface_3_out_0x56459c2ce540;
        interface_3_out_0x56459c259050;
        interface_3_out_0x56459c258700;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x56459a9d6050 [label="N", shape=none];
        interface_3_in_0x56459c25eaf0 [label="C_in", shape=none];
        interface_3_in_0x56459c2ce540 [label="H", shape=none];
        interface_3_in_0x56459c259050 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x56459c25eb08 [label="C_in", shape=none];
        interface_3_in_0x56459c25eb58 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x56459a9d6050;
        interface_3_in_0x56459c25eaf0;
        interface_3_in_0x56459c2ce540;
        interface_3_in_0x56459c259050;
        interface_3_in_0x56459c25eb08;
        interface_3_in_0x56459c25eb58;
    }
    // Op's.
    op_0x56459c258858 [label="Expand"];
    op_0x56459c25ead0 [label="Share"];
    op_0x56459c25eb20 [label="Share"];
    // Dimension's.
    interface_3_in_0x56459a9d6050 -> interface_3_out_0x56459a9d6050 [label="N"];
    op_0x56459c25eb20 -> interface_3_out_0x56459c258700 [label="k_2*s"];
    interface_3_in_0x56459c259050 -> interface_3_out_0x56459c259050 [label="H"];
    interface_3_in_0x56459c25eaf0 -> op_0x56459c25ead0 [label="C_in"];
    interface_3_in_0x56459c25eb08 -> op_0x56459c25ead0 [label="C_in"];
    op_0x56459c258858 -> op_0x56459c25eb20 [label="k_2*s"];
    interface_3_in_0x56459c25eb58 -> op_0x56459c25eb20 [label="k_2*s"];
    interface_3_in_0x56459c2ce540 -> interface_3_out_0x56459c2ce540 [label="H"];
    op_0x56459c25ead0 -> reduce_0x7fdbac005c70 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x56459a9d6050 [label="N", shape=none];
    interface_4_out_0x56459c25eaf0 [label="C_in", shape=none];
    interface_4_out_0x56459c2ce540 [label="H", shape=none];
    interface_4_out_0x56459c259050 [label="H", shape=none];
}

interface_4_out_0x56459a9d6050 -> interface_3_in_0x56459a9d6050;
interface_4_out_0x56459c25eaf0 -> interface_3_in_0x56459c25eaf0;
interface_4_out_0x56459c2ce540 -> interface_3_in_0x56459c2ce540;
interface_4_out_0x56459c259050 -> interface_3_in_0x56459c259050;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 2";
    interface_5_out_0x56459c25eb08 [label="C_in", shape=none];
    interface_5_out_0x56459c25eb58 [label="k_2*s", shape=none];
}

interface_5_out_0x56459c25eb08 -> interface_3_in_0x56459c25eb08;
interface_5_out_0x56459c25eb58 -> interface_3_in_0x56459c25eb58;

interface_3_out_0x56459a9d6050 -> interface_2_in_0x56459a9d6050;
interface_3_out_0x56459c2ce540 -> interface_2_in_0x56459c2ce540;
interface_3_out_0x56459c259050 -> interface_2_in_0x56459c259050;
interface_3_out_0x56459c258700 -> interface_2_in_0x56459c258700;

interface_2_out_0x56459a9d6050 -> interface_1_in_0x56459a9d6050;
interface_2_out_0x56459c25a500 -> interface_1_in_0x56459c25a500;
interface_2_out_0x56459c258610 -> interface_1_in_0x56459c258610;
interface_2_out_0x56459c25a518 -> interface_1_in_0x56459c25a518;
interface_2_out_0x56459c259050 -> interface_1_in_0x56459c259050;
interface_2_out_0x56459c258700 -> interface_1_in_0x56459c258700;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 1";
    interface_6_out_0x56459c2582b8 [label="C_out", shape=none];
    interface_6_out_0x56459c258628 [label="k_1", shape=none];
    interface_6_out_0x56459c258718 [label="k_2*s", shape=none];
}

interface_6_out_0x56459c2582b8 -> interface_1_in_0x56459c2582b8;
interface_6_out_0x56459c258628 -> interface_1_in_0x56459c258628;
interface_6_out_0x56459c258718 -> interface_1_in_0x56459c258718;

interface_1_out_0x56459a9d6050 -> interface_0_in_0x56459a9d6050;
interface_1_out_0x56459a9d6078 -> interface_0_in_0x56459a9d6078;
interface_1_out_0x56459c25a500 -> interface_0_in_0x56459c25a500;
interface_1_out_0x56459c25a518 -> interface_0_in_0x56459c25a518;
interface_1_out_0x56459c259050 -> interface_0_in_0x56459c259050;

{
    rank = same;
    interface_4_out_0x56459a9d6050;
    interface_4_out_0x56459c25eaf0;
    interface_4_out_0x56459c2ce540;
    interface_4_out_0x56459c259050;
    interface_6_out_0x56459c2582b8;
    interface_6_out_0x56459c258628;
    interface_6_out_0x56459c258718;
    interface_5_out_0x56459c25eb08;
    interface_5_out_0x56459c25eb58;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_7_in_0x56459a9d6050 [label="N", shape=none];
    interface_7_in_0x56459a9d6078 [label="C_out", shape=none];
    interface_7_in_0x56459a9d60a0 [label="H", shape=none];
    interface_7_in_0x56459a9d60c8 [label="H", shape=none];
}
interface_0_out_0x56459a9d6050 -> interface_7_in_0x56459a9d6050;
interface_0_out_0x56459a9d6078 -> interface_7_in_0x56459a9d6078;
interface_0_out_0x56459a9d60a0 -> interface_7_in_0x56459a9d60a0;
interface_0_out_0x56459a9d60c8 -> interface_7_in_0x56459a9d60c8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([24, 3, 14]),
			torch.randn([24, 14]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("kiml, ij -> kmlj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Split9d4d44f1bf98c2cc -> [s]@Merged3c50a2f22396ae4, [s^-1*H]@Unfold13a2e71a3ce37a21
		t_4 = torch.reshape(t_4, (1, 2, 56, 112, 14, ))

		# [s^-1*H]@Unfold13a2e71a3ce37a21 -> [s^-1*H]@Merged3c50a2f22396aeb, [k_1]@Share26cfa48d169008e4
		t_4 = torch.reshape(t_4, (1, 2, 56, 1568, ))
		t_4 = torch.nn.functional.unfold(t_4, (3, 1, ), padding=(1, 0, ))
		t_4 = torch.reshape(t_4, (1, 2, 3, 56, 112, 14, ))

		# Perform contraction.
		t_5 = torch.einsum("lnjomk, ijk -> linom", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merged3c50a2f22396ae4, [s^-1*H]@Merged3c50a2f22396aeb -> [H]@Iterator96123ba3184da39c
		t_6 = torch.reshape(t_6, (1, 24, 112, 112, ))

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
			torch.randn([96, 3, 14]),
			torch.randn([24, 14]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("kiml, ij -> kmlj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Split9d4d44f1bf98c2cc -> [s]@Merged3c50a2f22396ae4, [s^-1*H]@Unfold13a2e71a3ce37a21
		t_4 = torch.reshape(t_4, (1, 2, 28, 56, 14, ))

		# [s^-1*H]@Unfold13a2e71a3ce37a21 -> [s^-1*H]@Merged3c50a2f22396aeb, [k_1]@Share26cfa48d169008e4
		t_4 = torch.reshape(t_4, (1, 2, 28, 784, ))
		t_4 = torch.nn.functional.unfold(t_4, (3, 1, ), padding=(1, 0, ))
		t_4 = torch.reshape(t_4, (1, 2, 3, 28, 56, 14, ))

		# Perform contraction.
		t_5 = torch.einsum("lnjomk, ijk -> linom", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merged3c50a2f22396ae4, [s^-1*H]@Merged3c50a2f22396aeb -> [H]@Iterator96123ba3184da39c
		t_6 = torch.reshape(t_6, (1, 96, 56, 56, ))

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
			torch.randn([192, 3, 14]),
			torch.randn([48, 14]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("kiml, ij -> kmlj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Split9d4d44f1bf98c2cc -> [s]@Merged3c50a2f22396ae4, [s^-1*H]@Unfold13a2e71a3ce37a21
		t_4 = torch.reshape(t_4, (1, 2, 28, 56, 14, ))

		# [s^-1*H]@Unfold13a2e71a3ce37a21 -> [s^-1*H]@Merged3c50a2f22396aeb, [k_1]@Share26cfa48d169008e4
		t_4 = torch.reshape(t_4, (1, 2, 28, 784, ))
		t_4 = torch.nn.functional.unfold(t_4, (3, 1, ), padding=(1, 0, ))
		t_4 = torch.reshape(t_4, (1, 2, 3, 28, 56, 14, ))

		# Perform contraction.
		t_5 = torch.einsum("lnjomk, ijk -> linom", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merged3c50a2f22396ae4, [s^-1*H]@Merged3c50a2f22396aeb -> [H]@Iterator96123ba3184da39c
		t_6 = torch.reshape(t_6, (1, 192, 56, 56, ))

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
			torch.randn([192, 3, 14]),
			torch.randn([48, 14]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("kiml, ij -> kmlj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Split9d4d44f1bf98c2cc -> [s]@Merged3c50a2f22396ae4, [s^-1*H]@Unfold13a2e71a3ce37a21
		t_4 = torch.reshape(t_4, (1, 2, 14, 28, 14, ))

		# [s^-1*H]@Unfold13a2e71a3ce37a21 -> [s^-1*H]@Merged3c50a2f22396aeb, [k_1]@Share26cfa48d169008e4
		t_4 = torch.reshape(t_4, (1, 2, 14, 392, ))
		t_4 = torch.nn.functional.unfold(t_4, (3, 1, ), padding=(1, 0, ))
		t_4 = torch.reshape(t_4, (1, 2, 3, 14, 28, 14, ))

		# Perform contraction.
		t_5 = torch.einsum("lnjomk, ijk -> linom", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merged3c50a2f22396ae4, [s^-1*H]@Merged3c50a2f22396aeb -> [H]@Iterator96123ba3184da39c
		t_6 = torch.reshape(t_6, (1, 192, 28, 28, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 14]),
			torch.randn([64, 14]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("kiml, ij -> kmlj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Split9d4d44f1bf98c2cc -> [s]@Merged3c50a2f22396ae4, [s^-1*H]@Unfold13a2e71a3ce37a21
		t_4 = torch.reshape(t_4, (1, 2, 14, 28, 14, ))

		# [s^-1*H]@Unfold13a2e71a3ce37a21 -> [s^-1*H]@Merged3c50a2f22396aeb, [k_1]@Share26cfa48d169008e4
		t_4 = torch.reshape(t_4, (1, 2, 14, 392, ))
		t_4 = torch.nn.functional.unfold(t_4, (3, 1, ), padding=(1, 0, ))
		t_4 = torch.reshape(t_4, (1, 2, 3, 14, 28, 14, ))

		# Perform contraction.
		t_5 = torch.einsum("lnjomk, ijk -> linom", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merged3c50a2f22396ae4, [s^-1*H]@Merged3c50a2f22396aeb -> [H]@Iterator96123ba3184da39c
		t_6 = torch.reshape(t_6, (1, 256, 28, 28, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_6

		return y

