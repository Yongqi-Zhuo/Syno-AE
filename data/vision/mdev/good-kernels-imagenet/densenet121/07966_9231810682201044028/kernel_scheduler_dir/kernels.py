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
        interface_0_out_0x55672bcd7b90 [label="N", shape=none];
        interface_0_out_0x55672bcd7bb8 [label="C_out", shape=none];
        interface_0_out_0x55672bcd7be0 [label="H", shape=none];
        interface_0_out_0x55672bcd7c08 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55672bcd7b90;
        interface_0_out_0x55672bcd7bb8;
        interface_0_out_0x55672bcd7be0;
        interface_0_out_0x55672bcd7c08;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55672bcd7b90 [label="N", shape=none];
        interface_0_in_0x55672bcd7bb8 [label="C_out", shape=none];
        interface_0_in_0x55672bcd7be0 [label="H", shape=none];
        interface_0_in_0x55672bdfb2d0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55672bcd7b90;
        interface_0_in_0x55672bcd7bb8;
        interface_0_in_0x55672bcd7be0;
        interface_0_in_0x55672bdfb2d0;
    }
    // Op's.
    op_0x55672bdfb2b0 [label="Shift"];
    // Dimension's.
    interface_0_in_0x55672bcd7b90 -> interface_0_out_0x55672bcd7b90 [label="N"];
    interface_0_in_0x55672bcd7bb8 -> interface_0_out_0x55672bcd7bb8 [label="C_out"];
    interface_0_in_0x55672bcd7be0 -> interface_0_out_0x55672bcd7be0 [label="H"];
    op_0x55672bdfb2b0 -> interface_0_out_0x55672bcd7c08 [label="H"];
    interface_0_in_0x55672bdfb2d0 -> op_0x55672bdfb2b0 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f52780072d0 [label="Sum", shape=box];
    reduce_0x7f5278003a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55672bcd7b90 [label="N", shape=none];
        interface_1_out_0x55672bcd7bb8 [label="C_out", shape=none];
        interface_1_out_0x55672bcd7be0 [label="H", shape=none];
        interface_1_out_0x55672bdfb2d0 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f52780072d0;
        reduce_0x7f5278003a98;
        interface_1_out_0x55672bcd7b90;
        interface_1_out_0x55672bcd7bb8;
        interface_1_out_0x55672bcd7be0;
        interface_1_out_0x55672bdfb2d0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55672bcd7b90 [label="N", shape=none];
        interface_1_in_0x55672bdfa5f0 [label="s^-1*C_in", shape=none];
        interface_1_in_0x55672bdfa870 [label="k_1", shape=none];
        interface_1_in_0x55672bcd7be0 [label="H", shape=none];
        interface_1_in_0x55672bdfb2d0 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55672bdfa5b8 [label="C_out", shape=none];
        interface_1_in_0x55672bdfa608 [label="s^-1*C_in", shape=none];
        interface_1_in_0x55672bdfa888 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55672bcd7b90;
        interface_1_in_0x55672bdfa5f0;
        interface_1_in_0x55672bdfa870;
        interface_1_in_0x55672bcd7be0;
        interface_1_in_0x55672bdfb2d0;
        interface_1_in_0x55672bdfa5b8;
        interface_1_in_0x55672bdfa608;
        interface_1_in_0x55672bdfa888;
    }
    // Op's.
    op_0x55672bdfa580 [label="Share"];
    op_0x55672bdfa5d0 [label="Share"];
    op_0x55672bdfa850 [label="Share"];
    op_0x55672bdfaa58 [label="Expand"];
    // Dimension's.
    interface_1_in_0x55672bcd7b90 -> interface_1_out_0x55672bcd7b90 [label="N"];
    op_0x55672bdfa580 -> interface_1_out_0x55672bcd7bb8 [label="C_out"];
    interface_1_in_0x55672bcd7be0 -> interface_1_out_0x55672bcd7be0 [label="H"];
    op_0x55672bdfaa58 -> op_0x55672bdfa580 [label="C_out"];
    interface_1_in_0x55672bdfa5b8 -> op_0x55672bdfa580 [label="C_out"];
    interface_1_in_0x55672bdfa5f0 -> op_0x55672bdfa5d0 [label="s^-1*C_in"];
    interface_1_in_0x55672bdfa608 -> op_0x55672bdfa5d0 [label="s^-1*C_in"];
    interface_1_in_0x55672bdfa870 -> op_0x55672bdfa850 [label="k_1"];
    interface_1_in_0x55672bdfa888 -> op_0x55672bdfa850 [label="k_1"];
    interface_1_in_0x55672bdfb2d0 -> interface_1_out_0x55672bdfb2d0 [label="H"];
    op_0x55672bdfa850 -> reduce_0x7f5278003a98 [label="k_1"];
    op_0x55672bdfa5d0 -> reduce_0x7f52780072d0 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f527800deb0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55672bcd7b90 [label="N", shape=none];
        interface_2_out_0x55672bdfa5f0 [label="s^-1*C_in", shape=none];
        interface_2_out_0x55672bdfa870 [label="k_1", shape=none];
        interface_2_out_0x55672bcd7be0 [label="H", shape=none];
        interface_2_out_0x55672bdfb2d0 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f527800deb0;
        interface_2_out_0x55672bcd7b90;
        interface_2_out_0x55672bdfa5f0;
        interface_2_out_0x55672bdfa870;
        interface_2_out_0x55672bcd7be0;
        interface_2_out_0x55672bdfb2d0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55672bcd7b90 [label="N", shape=none];
        interface_2_in_0x55672bdfa5f0 [label="s^-1*C_in", shape=none];
        interface_2_in_0x55672be1cb50 [label="g^-2*k_1*C_out^2", shape=none];
        interface_2_in_0x55672bcd7be0 [label="H", shape=none];
        interface_2_in_0x55672bdfb2d0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55672bcd7b90;
        interface_2_in_0x55672bdfa5f0;
        interface_2_in_0x55672be1cb50;
        interface_2_in_0x55672bcd7be0;
        interface_2_in_0x55672bdfb2d0;
    }
    // Op's.
    op_0x55672be1cb10 [label="Split"];
    // Dimension's.
    interface_2_in_0x55672bcd7b90 -> interface_2_out_0x55672bcd7b90 [label="N"];
    interface_2_in_0x55672bcd7be0 -> interface_2_out_0x55672bcd7be0 [label="H"];
    interface_2_in_0x55672bdfa5f0 -> interface_2_out_0x55672bdfa5f0 [label="s^-1*C_in"];
    op_0x55672be1cb10 -> interface_2_out_0x55672bdfa870 [label="k_1"];
    interface_2_in_0x55672bdfb2d0 -> interface_2_out_0x55672bdfb2d0 [label="H"];
    interface_2_in_0x55672be1cb50 -> op_0x55672be1cb10 [label="g^-2*k_1*C_out^2"];
    op_0x55672be1cb10 -> reduce_0x7f527800deb0 [label="g^-2*C_out^2"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7f527800b670 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55672bcd7b90 [label="N", shape=none];
        interface_3_out_0x55672bdfa5f0 [label="s^-1*C_in", shape=none];
        interface_3_out_0x55672be1cb50 [label="g^-2*k_1*C_out^2", shape=none];
        interface_3_out_0x55672bcd7be0 [label="H", shape=none];
        interface_3_out_0x55672bdfb2d0 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f527800b670;
        interface_3_out_0x55672bcd7b90;
        interface_3_out_0x55672bdfa5f0;
        interface_3_out_0x55672be1cb50;
        interface_3_out_0x55672bcd7be0;
        interface_3_out_0x55672bdfb2d0;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55672bcd7b90 [label="N", shape=none];
        interface_3_in_0x55672bdfa5f0 [label="s^-1*C_in", shape=none];
        interface_3_in_0x55672bdfcf28 [label="H", shape=none];
        interface_3_in_0x55672bdfb2d0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55672bcd7b90;
        interface_3_in_0x55672bdfa5f0;
        interface_3_in_0x55672bdfcf28;
        interface_3_in_0x55672bdfb2d0;
    }
    // Op's.
    op_0x55672bdfcf00 [label="Unfold"];
    op_0x55672be1dbf0 [label="Split"];
    // Dimension's.
    interface_3_in_0x55672bcd7b90 -> interface_3_out_0x55672bcd7b90 [label="N"];
    op_0x55672bdfcf00 -> interface_3_out_0x55672bcd7be0 [label="H"];
    interface_3_in_0x55672bdfa5f0 -> interface_3_out_0x55672bdfa5f0 [label="s^-1*C_in"];
    interface_3_in_0x55672bdfb2d0 -> interface_3_out_0x55672bdfb2d0 [label="H"];
    interface_3_in_0x55672bdfcf28 -> op_0x55672bdfcf00 [label="H"];
    op_0x55672be1dbf0 -> interface_3_out_0x55672be1cb50 [label="g^-2*k_1*C_out^2"];
    op_0x55672bdfcf00 -> op_0x55672be1dbf0 [label="g^-3*k_1*C_out^3"];
    op_0x55672be1dbf0 -> reduce_0x7f527800b670 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    reduce_0x7f5278004c30 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x55672bcd7b90 [label="N", shape=none];
        interface_4_out_0x55672bdfa5f0 [label="s^-1*C_in", shape=none];
        interface_4_out_0x55672bdfcf28 [label="H", shape=none];
        interface_4_out_0x55672bdfb2d0 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5278004c30;
        interface_4_out_0x55672bcd7b90;
        interface_4_out_0x55672bdfa5f0;
        interface_4_out_0x55672bdfcf28;
        interface_4_out_0x55672bdfb2d0;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x55672bcd7b90 [label="N", shape=none];
        interface_4_in_0x55672be1db40 [label="C_in", shape=none];
        interface_4_in_0x55672bdfcf28 [label="H", shape=none];
        interface_4_in_0x55672bdfb2d0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x55672bcd7b90;
        interface_4_in_0x55672be1db40;
        interface_4_in_0x55672bdfcf28;
        interface_4_in_0x55672bdfb2d0;
    }
    // Op's.
    op_0x55672be1db00 [label="Split"];
    // Dimension's.
    interface_4_in_0x55672bcd7b90 -> interface_4_out_0x55672bcd7b90 [label="N"];
    op_0x55672be1db00 -> interface_4_out_0x55672bdfa5f0 [label="s^-1*C_in"];
    interface_4_in_0x55672bdfb2d0 -> interface_4_out_0x55672bdfb2d0 [label="H"];
    interface_4_in_0x55672bdfcf28 -> interface_4_out_0x55672bdfcf28 [label="H"];
    interface_4_in_0x55672be1db40 -> op_0x55672be1db00 [label="C_in"];
    op_0x55672be1db00 -> reduce_0x7f5278004c30 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x55672bcd7b90 [label="N", shape=none];
    interface_5_out_0x55672be1db40 [label="C_in", shape=none];
    interface_5_out_0x55672bdfcf28 [label="H", shape=none];
    interface_5_out_0x55672bdfb2d0 [label="H", shape=none];
}

interface_5_out_0x55672bcd7b90 -> interface_4_in_0x55672bcd7b90;
interface_5_out_0x55672be1db40 -> interface_4_in_0x55672be1db40;
interface_5_out_0x55672bdfcf28 -> interface_4_in_0x55672bdfcf28;
interface_5_out_0x55672bdfb2d0 -> interface_4_in_0x55672bdfb2d0;

interface_4_out_0x55672bcd7b90 -> interface_3_in_0x55672bcd7b90;
interface_4_out_0x55672bdfa5f0 -> interface_3_in_0x55672bdfa5f0;
interface_4_out_0x55672bdfcf28 -> interface_3_in_0x55672bdfcf28;
interface_4_out_0x55672bdfb2d0 -> interface_3_in_0x55672bdfb2d0;

interface_3_out_0x55672bcd7b90 -> interface_2_in_0x55672bcd7b90;
interface_3_out_0x55672bdfa5f0 -> interface_2_in_0x55672bdfa5f0;
interface_3_out_0x55672be1cb50 -> interface_2_in_0x55672be1cb50;
interface_3_out_0x55672bcd7be0 -> interface_2_in_0x55672bcd7be0;
interface_3_out_0x55672bdfb2d0 -> interface_2_in_0x55672bdfb2d0;

interface_2_out_0x55672bcd7b90 -> interface_1_in_0x55672bcd7b90;
interface_2_out_0x55672bdfa5f0 -> interface_1_in_0x55672bdfa5f0;
interface_2_out_0x55672bdfa870 -> interface_1_in_0x55672bdfa870;
interface_2_out_0x55672bcd7be0 -> interface_1_in_0x55672bcd7be0;
interface_2_out_0x55672bdfb2d0 -> interface_1_in_0x55672bdfb2d0;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 1";
    interface_6_out_0x55672bdfa5b8 [label="C_out", shape=none];
    interface_6_out_0x55672bdfa608 [label="s^-1*C_in", shape=none];
    interface_6_out_0x55672bdfa888 [label="k_1", shape=none];
}

interface_6_out_0x55672bdfa5b8 -> interface_1_in_0x55672bdfa5b8;
interface_6_out_0x55672bdfa608 -> interface_1_in_0x55672bdfa608;
interface_6_out_0x55672bdfa888 -> interface_1_in_0x55672bdfa888;

interface_1_out_0x55672bcd7b90 -> interface_0_in_0x55672bcd7b90;
interface_1_out_0x55672bcd7bb8 -> interface_0_in_0x55672bcd7bb8;
interface_1_out_0x55672bcd7be0 -> interface_0_in_0x55672bcd7be0;
interface_1_out_0x55672bdfb2d0 -> interface_0_in_0x55672bdfb2d0;

{
    rank = same;
    interface_5_out_0x55672bcd7b90;
    interface_5_out_0x55672be1db40;
    interface_5_out_0x55672bdfcf28;
    interface_5_out_0x55672bdfb2d0;
    interface_6_out_0x55672bdfa5b8;
    interface_6_out_0x55672bdfa608;
    interface_6_out_0x55672bdfa888;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_7_in_0x55672bcd7b90 [label="N", shape=none];
    interface_7_in_0x55672bcd7bb8 [label="C_out", shape=none];
    interface_7_in_0x55672bcd7be0 [label="H", shape=none];
    interface_7_in_0x55672bcd7c08 [label="H", shape=none];
}
interface_0_out_0x55672bcd7b90 -> interface_7_in_0x55672bcd7b90;
interface_0_out_0x55672bcd7bb8 -> interface_7_in_0x55672bcd7bb8;
interface_0_out_0x55672bcd7be0 -> interface_7_in_0x55672bcd7be0;
interface_0_out_0x55672bcd7c08 -> interface_7_in_0x55672bcd7c08;

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
		t_2 = torch.reshape(t_2, (1, 2, 64, 56, 56, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4aa57e8190ebe608 -> [H]@Iterator96123ba3184da39c, [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05
		t_3 = torch.reshape(t_3, (1, 64, 56, 56, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 3, 56, 56, ))

		# [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05 -> [g^-1*C_out]@Reduce28c4f9e5abf023cf, [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3
		t_3 = torch.reshape(t_3, (1, 64, 1, 3, 56, 56, ))

		# [g^-1*C_out]@Reduce
		t_3 = torch.sum(t_3, dim=(2, ))

		# No contraction needed.
		t_4 = t_3

		# [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3 -> [k_1]@Share26cfa48d169008e4, [g^-2*C_out^2]@Reduce159437b921f023cf
		t_4 = torch.reshape(t_4, (1, 64, 3, 1, 56, 56, ))

		# [g^-2*C_out^2]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# Perform contraction.
		t_5 = torch.einsum("ljkmn, ijk -> limn", t_4, in_1)

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
		t_2 = torch.reshape(t_2, (1, 2, 64, 28, 28, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4aa57e8190ebe608 -> [H]@Iterator96123ba3184da39c, [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05
		t_3 = torch.reshape(t_3, (1, 64, 28, 28, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 3, 28, 28, ))

		# [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05 -> [g^-1*C_out]@Reduce28c4f9e5abf023cf, [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3
		t_3 = torch.reshape(t_3, (1, 64, 1, 3, 28, 28, ))

		# [g^-1*C_out]@Reduce
		t_3 = torch.sum(t_3, dim=(2, ))

		# No contraction needed.
		t_4 = t_3

		# [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3 -> [k_1]@Share26cfa48d169008e4, [g^-2*C_out^2]@Reduce159437b921f023cf
		t_4 = torch.reshape(t_4, (1, 64, 3, 1, 28, 28, ))

		# [g^-2*C_out^2]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# Perform contraction.
		t_5 = torch.einsum("ljkmn, ijk -> limn", t_4, in_1)

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
		t_2 = torch.reshape(t_2, (1, 2, 64, 14, 14, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4aa57e8190ebe608 -> [H]@Iterator96123ba3184da39c, [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05
		t_3 = torch.reshape(t_3, (1, 64, 14, 14, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 3, 14, 14, ))

		# [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05 -> [g^-1*C_out]@Reduce28c4f9e5abf023cf, [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3
		t_3 = torch.reshape(t_3, (1, 64, 1, 3, 14, 14, ))

		# [g^-1*C_out]@Reduce
		t_3 = torch.sum(t_3, dim=(2, ))

		# No contraction needed.
		t_4 = t_3

		# [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3 -> [k_1]@Share26cfa48d169008e4, [g^-2*C_out^2]@Reduce159437b921f023cf
		t_4 = torch.reshape(t_4, (1, 64, 3, 1, 14, 14, ))

		# [g^-2*C_out^2]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# Perform contraction.
		t_5 = torch.einsum("ljkmn, ijk -> limn", t_4, in_1)

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
		t_2 = torch.reshape(t_2, (1, 2, 64, 7, 7, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4aa57e8190ebe608 -> [H]@Iterator96123ba3184da39c, [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05
		t_3 = torch.reshape(t_3, (1, 64, 7, 7, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 3, 7, 7, ))

		# [g^-3*k_1*C_out^3]@Splite17fc0c11dbe5a05 -> [g^-1*C_out]@Reduce28c4f9e5abf023cf, [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3
		t_3 = torch.reshape(t_3, (1, 64, 1, 3, 7, 7, ))

		# [g^-1*C_out]@Reduce
		t_3 = torch.sum(t_3, dim=(2, ))

		# No contraction needed.
		t_4 = t_3

		# [g^-2*k_1*C_out^2]@Split5f8295cb2a9219e3 -> [k_1]@Share26cfa48d169008e4, [g^-2*C_out^2]@Reduce159437b921f023cf
		t_4 = torch.reshape(t_4, (1, 64, 3, 1, 7, 7, ))

		# [g^-2*C_out^2]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# Perform contraction.
		t_5 = torch.einsum("ljkmn, ijk -> limn", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_6

		return y

