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
        interface_0_out_0x5604185d74e0 [label="N", shape=none];
        interface_0_out_0x5604185d7508 [label="C_out", shape=none];
        interface_0_out_0x5604185d7530 [label="H", shape=none];
        interface_0_out_0x5604185d7558 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x5604185d74e0;
        interface_0_out_0x5604185d7508;
        interface_0_out_0x5604185d7530;
        interface_0_out_0x5604185d7558;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5604185d74e0 [label="N", shape=none];
        interface_0_in_0x5604185d7508 [label="C_out", shape=none];
        interface_0_in_0x560419919480 [label="s", shape=none];
        interface_0_in_0x560419919498 [label="s^-1*H", shape=none];
        interface_0_in_0x560419917fd0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5604185d74e0;
        interface_0_in_0x5604185d7508;
        interface_0_in_0x560419919480;
        interface_0_in_0x560419919498;
        interface_0_in_0x560419917fd0;
    }
    // Op's.
    op_0x560419917fb0 [label="Shift"];
    op_0x560419919440 [label="Merge"];
    // Dimension's.
    interface_0_in_0x5604185d74e0 -> interface_0_out_0x5604185d74e0 [label="N"];
    interface_0_in_0x5604185d7508 -> interface_0_out_0x5604185d7508 [label="C_out"];
    op_0x560419919440 -> interface_0_out_0x5604185d7530 [label="H"];
    op_0x560419917fb0 -> interface_0_out_0x5604185d7558 [label="H"];
    interface_0_in_0x560419917fd0 -> op_0x560419917fb0 [label="H"];
    interface_0_in_0x560419919480 -> op_0x560419919440 [label="s"];
    interface_0_in_0x560419919498 -> op_0x560419919440 [label="s^-1*H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fc32c003a98 [label="Sum", shape=box];
    reduce_0x7fc32c0054d0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5604185d74e0 [label="N", shape=none];
        interface_1_out_0x5604185d7508 [label="C_out", shape=none];
        interface_1_out_0x560419919480 [label="s", shape=none];
        interface_1_out_0x560419919498 [label="s^-1*H", shape=none];
        interface_1_out_0x560419917fd0 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc32c003a98;
        reduce_0x7fc32c0054d0;
        interface_1_out_0x5604185d74e0;
        interface_1_out_0x5604185d7508;
        interface_1_out_0x560419919480;
        interface_1_out_0x560419919498;
        interface_1_out_0x560419917fd0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5604185d74e0 [label="N", shape=none];
        interface_1_in_0x560419919480 [label="s", shape=none];
        interface_1_in_0x56041991c920 [label="k_1", shape=none];
        interface_1_in_0x560419919498 [label="s^-1*H", shape=none];
        interface_1_in_0x560419917fd0 [label="H", shape=none];
        interface_1_in_0x5604199175c0 [label="k_2*s", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x5604199172b8 [label="C_out", shape=none];
        interface_1_in_0x56041991c938 [label="k_1", shape=none];
        interface_1_in_0x5604199175d8 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5604185d74e0;
        interface_1_in_0x560419919480;
        interface_1_in_0x56041991c920;
        interface_1_in_0x560419919498;
        interface_1_in_0x560419917fd0;
        interface_1_in_0x5604199175c0;
        interface_1_in_0x5604199172b8;
        interface_1_in_0x56041991c938;
        interface_1_in_0x5604199175d8;
    }
    // Op's.
    op_0x560419917280 [label="Share"];
    op_0x5604199175a0 [label="Share"];
    op_0x560419917758 [label="Expand"];
    op_0x56041991c900 [label="Share"];
    // Dimension's.
    interface_1_in_0x5604185d74e0 -> interface_1_out_0x5604185d74e0 [label="N"];
    op_0x560419917280 -> interface_1_out_0x5604185d7508 [label="C_out"];
    op_0x560419917758 -> op_0x560419917280 [label="C_out"];
    interface_1_in_0x5604199172b8 -> op_0x560419917280 [label="C_out"];
    interface_1_in_0x5604199175c0 -> op_0x5604199175a0 [label="k_2*s"];
    interface_1_in_0x5604199175d8 -> op_0x5604199175a0 [label="k_2*s"];
    interface_1_in_0x560419917fd0 -> interface_1_out_0x560419917fd0 [label="H"];
    interface_1_in_0x560419919480 -> interface_1_out_0x560419919480 [label="s"];
    interface_1_in_0x560419919498 -> interface_1_out_0x560419919498 [label="s^-1*H"];
    interface_1_in_0x56041991c920 -> op_0x56041991c900 [label="k_1"];
    interface_1_in_0x56041991c938 -> op_0x56041991c900 [label="k_1"];
    op_0x56041991c900 -> reduce_0x7fc32c003a98 [label="k_1"];
    op_0x5604199175a0 -> reduce_0x7fc32c0054d0 [label="k_2*s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5604185d74e0 [label="N", shape=none];
        interface_2_out_0x560419919480 [label="s", shape=none];
        interface_2_out_0x56041991c920 [label="k_1", shape=none];
        interface_2_out_0x560419919498 [label="s^-1*H", shape=none];
        interface_2_out_0x560419917fd0 [label="H", shape=none];
        interface_2_out_0x5604199175c0 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x5604185d74e0;
        interface_2_out_0x560419919480;
        interface_2_out_0x56041991c920;
        interface_2_out_0x560419919498;
        interface_2_out_0x560419917fd0;
        interface_2_out_0x5604199175c0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5604185d74e0 [label="N", shape=none];
        interface_2_in_0x5604199a9bc0 [label="H", shape=none];
        interface_2_in_0x560419917fd0 [label="H", shape=none];
        interface_2_in_0x5604199175c0 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5604185d74e0;
        interface_2_in_0x5604199a9bc0;
        interface_2_in_0x560419917fd0;
        interface_2_in_0x5604199175c0;
    }
    // Op's.
    op_0x5604199a9b80 [label="Split"];
    op_0x5604199b2f80 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x5604185d74e0 -> interface_2_out_0x5604185d74e0 [label="N"];
    interface_2_in_0x5604199175c0 -> interface_2_out_0x5604199175c0 [label="k_2*s"];
    interface_2_in_0x560419917fd0 -> interface_2_out_0x560419917fd0 [label="H"];
    op_0x5604199a9b80 -> interface_2_out_0x560419919480 [label="s"];
    op_0x5604199b2f80 -> interface_2_out_0x560419919498 [label="s^-1*H"];
    op_0x5604199b2f80 -> interface_2_out_0x56041991c920 [label="k_1"];
    interface_2_in_0x5604199a9bc0 -> op_0x5604199a9b80 [label="H"];
    op_0x5604199a9b80 -> op_0x5604199b2f80 [label="s^-1*H"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7fc32c007b70 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5604185d74e0 [label="N", shape=none];
        interface_3_out_0x5604199a9bc0 [label="H", shape=none];
        interface_3_out_0x560419917fd0 [label="H", shape=none];
        interface_3_out_0x5604199175c0 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc32c007b70;
        interface_3_out_0x5604185d74e0;
        interface_3_out_0x5604199a9bc0;
        interface_3_out_0x560419917fd0;
        interface_3_out_0x5604199175c0;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5604185d74e0 [label="N", shape=none];
        interface_3_in_0x560419917660 [label="C_in", shape=none];
        interface_3_in_0x5604199a9bc0 [label="H", shape=none];
        interface_3_in_0x560419917fd0 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x560419917678 [label="C_in", shape=none];
        interface_3_in_0x5604199176c8 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5604185d74e0;
        interface_3_in_0x560419917660;
        interface_3_in_0x5604199a9bc0;
        interface_3_in_0x560419917fd0;
        interface_3_in_0x560419917678;
        interface_3_in_0x5604199176c8;
    }
    // Op's.
    op_0x560419917640 [label="Share"];
    op_0x560419917690 [label="Share"];
    op_0x5604199177f8 [label="Expand"];
    // Dimension's.
    interface_3_in_0x5604185d74e0 -> interface_3_out_0x5604185d74e0 [label="N"];
    op_0x560419917690 -> interface_3_out_0x5604199175c0 [label="k_2*s"];
    interface_3_in_0x560419917660 -> op_0x560419917640 [label="C_in"];
    interface_3_in_0x560419917678 -> op_0x560419917640 [label="C_in"];
    op_0x5604199177f8 -> op_0x560419917690 [label="k_2*s"];
    interface_3_in_0x5604199176c8 -> op_0x560419917690 [label="k_2*s"];
    interface_3_in_0x560419917fd0 -> interface_3_out_0x560419917fd0 [label="H"];
    interface_3_in_0x5604199a9bc0 -> interface_3_out_0x5604199a9bc0 [label="H"];
    op_0x560419917640 -> reduce_0x7fc32c007b70 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x5604185d74e0 [label="N", shape=none];
    interface_4_out_0x560419917660 [label="C_in", shape=none];
    interface_4_out_0x5604199a9bc0 [label="H", shape=none];
    interface_4_out_0x560419917fd0 [label="H", shape=none];
}

interface_4_out_0x5604185d74e0 -> interface_3_in_0x5604185d74e0;
interface_4_out_0x560419917660 -> interface_3_in_0x560419917660;
interface_4_out_0x5604199a9bc0 -> interface_3_in_0x5604199a9bc0;
interface_4_out_0x560419917fd0 -> interface_3_in_0x560419917fd0;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 2";
    interface_5_out_0x560419917678 [label="C_in", shape=none];
    interface_5_out_0x5604199176c8 [label="k_2*s", shape=none];
}

interface_5_out_0x560419917678 -> interface_3_in_0x560419917678;
interface_5_out_0x5604199176c8 -> interface_3_in_0x5604199176c8;

interface_3_out_0x5604185d74e0 -> interface_2_in_0x5604185d74e0;
interface_3_out_0x5604199a9bc0 -> interface_2_in_0x5604199a9bc0;
interface_3_out_0x560419917fd0 -> interface_2_in_0x560419917fd0;
interface_3_out_0x5604199175c0 -> interface_2_in_0x5604199175c0;

interface_2_out_0x5604185d74e0 -> interface_1_in_0x5604185d74e0;
interface_2_out_0x560419919480 -> interface_1_in_0x560419919480;
interface_2_out_0x56041991c920 -> interface_1_in_0x56041991c920;
interface_2_out_0x560419919498 -> interface_1_in_0x560419919498;
interface_2_out_0x560419917fd0 -> interface_1_in_0x560419917fd0;
interface_2_out_0x5604199175c0 -> interface_1_in_0x5604199175c0;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 1";
    interface_6_out_0x5604199172b8 [label="C_out", shape=none];
    interface_6_out_0x56041991c938 [label="k_1", shape=none];
    interface_6_out_0x5604199175d8 [label="k_2*s", shape=none];
}

interface_6_out_0x5604199172b8 -> interface_1_in_0x5604199172b8;
interface_6_out_0x56041991c938 -> interface_1_in_0x56041991c938;
interface_6_out_0x5604199175d8 -> interface_1_in_0x5604199175d8;

interface_1_out_0x5604185d74e0 -> interface_0_in_0x5604185d74e0;
interface_1_out_0x5604185d7508 -> interface_0_in_0x5604185d7508;
interface_1_out_0x560419919480 -> interface_0_in_0x560419919480;
interface_1_out_0x560419919498 -> interface_0_in_0x560419919498;
interface_1_out_0x560419917fd0 -> interface_0_in_0x560419917fd0;

{
    rank = same;
    interface_4_out_0x5604185d74e0;
    interface_4_out_0x560419917660;
    interface_4_out_0x5604199a9bc0;
    interface_4_out_0x560419917fd0;
    interface_6_out_0x5604199172b8;
    interface_6_out_0x56041991c938;
    interface_6_out_0x5604199175d8;
    interface_5_out_0x560419917678;
    interface_5_out_0x5604199176c8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_7_in_0x5604185d74e0 [label="N", shape=none];
    interface_7_in_0x5604185d7508 [label="C_out", shape=none];
    interface_7_in_0x5604185d7530 [label="H", shape=none];
    interface_7_in_0x5604185d7558 [label="H", shape=none];
}
interface_0_out_0x5604185d74e0 -> interface_7_in_0x5604185d74e0;
interface_0_out_0x5604185d7508 -> interface_7_in_0x5604185d7508;
interface_0_out_0x5604185d7530 -> interface_7_in_0x5604185d7530;
interface_0_out_0x5604185d7558 -> interface_7_in_0x5604185d7558;

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
		t_5 = torch.einsum("lnkomj, ikj -> linom", t_4, in_1)

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
		t_5 = torch.einsum("lnkomj, ikj -> linom", t_4, in_1)

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
		t_5 = torch.einsum("lnkomj, ikj -> linom", t_4, in_1)

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
		t_5 = torch.einsum("lnkomj, ikj -> linom", t_4, in_1)

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
		t_5 = torch.einsum("lnkomj, ikj -> linom", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merged3c50a2f22396ae4, [s^-1*H]@Merged3c50a2f22396aeb -> [H]@Iterator96123ba3184da39c
		t_6 = torch.reshape(t_6, (1, 256, 28, 28, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_6

		return y

