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
        interface_0_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_0_out_0x55f1ee7b7dc8 [label="C_out", shape=none];
        interface_0_out_0x55f1ee7b7df0 [label="H", shape=none];
        interface_0_out_0x55f1ee7b7e18 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55f1ee7b7da0;
        interface_0_out_0x55f1ee7b7dc8;
        interface_0_out_0x55f1ee7b7df0;
        interface_0_out_0x55f1ee7b7e18;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_0_in_0x55f1ee7b7dc8 [label="C_out", shape=none];
        interface_0_in_0x55f1f89def00 [label="s", shape=none];
        interface_0_in_0x55f1f89def18 [label="s^-1*H", shape=none];
        interface_0_in_0x55f1eba3e3d0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55f1ee7b7da0;
        interface_0_in_0x55f1ee7b7dc8;
        interface_0_in_0x55f1f89def00;
        interface_0_in_0x55f1f89def18;
        interface_0_in_0x55f1eba3e3d0;
    }
    // Op's.
    op_0x55f1eba3e3b0 [label="Shift"];
    op_0x55f1f89deec0 [label="Merge"];
    // Dimension's.
    interface_0_in_0x55f1eba3e3d0 -> op_0x55f1eba3e3b0 [label="H"];
    interface_0_in_0x55f1ee7b7da0 -> interface_0_out_0x55f1ee7b7da0 [label="N"];
    interface_0_in_0x55f1ee7b7dc8 -> interface_0_out_0x55f1ee7b7dc8 [label="C_out"];
    op_0x55f1f89deec0 -> interface_0_out_0x55f1ee7b7df0 [label="H"];
    op_0x55f1eba3e3b0 -> interface_0_out_0x55f1ee7b7e18 [label="H"];
    interface_0_in_0x55f1f89def00 -> op_0x55f1f89deec0 [label="s"];
    interface_0_in_0x55f1f89def18 -> op_0x55f1f89deec0 [label="s^-1*H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f5f78003a98 [label="Sum", shape=box];
    reduce_0x7f5f780054d0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_1_out_0x55f1ee7b7dc8 [label="C_out", shape=none];
        interface_1_out_0x55f1f89def00 [label="s", shape=none];
        interface_1_out_0x55f1f89def18 [label="s^-1*H", shape=none];
        interface_1_out_0x55f1eba3e3d0 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5f78003a98;
        reduce_0x7f5f780054d0;
        interface_1_out_0x55f1ee7b7da0;
        interface_1_out_0x55f1ee7b7dc8;
        interface_1_out_0x55f1f89def00;
        interface_1_out_0x55f1f89def18;
        interface_1_out_0x55f1eba3e3d0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_1_in_0x55f1f89def00 [label="s", shape=none];
        interface_1_in_0x55f1f89e2c20 [label="k_1", shape=none];
        interface_1_in_0x55f1f89def18 [label="s^-1*H", shape=none];
        interface_1_in_0x55f1eba3e3d0 [label="H", shape=none];
        interface_1_in_0x55f1f89ddc40 [label="k_2*s", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55f1f89dd938 [label="C_out", shape=none];
        interface_1_in_0x55f1f89e2c38 [label="k_1", shape=none];
        interface_1_in_0x55f1f89ddc58 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55f1ee7b7da0;
        interface_1_in_0x55f1f89def00;
        interface_1_in_0x55f1f89e2c20;
        interface_1_in_0x55f1f89def18;
        interface_1_in_0x55f1eba3e3d0;
        interface_1_in_0x55f1f89ddc40;
        interface_1_in_0x55f1f89dd938;
        interface_1_in_0x55f1f89e2c38;
        interface_1_in_0x55f1f89ddc58;
    }
    // Op's.
    op_0x55f1f88b2978 [label="Expand"];
    op_0x55f1f89dd900 [label="Share"];
    op_0x55f1f89ddc20 [label="Share"];
    op_0x55f1f89e2c00 [label="Share"];
    // Dimension's.
    interface_1_in_0x55f1eba3e3d0 -> interface_1_out_0x55f1eba3e3d0 [label="H"];
    interface_1_in_0x55f1ee7b7da0 -> interface_1_out_0x55f1ee7b7da0 [label="N"];
    op_0x55f1f89dd900 -> interface_1_out_0x55f1ee7b7dc8 [label="C_out"];
    op_0x55f1f88b2978 -> op_0x55f1f89dd900 [label="C_out"];
    interface_1_in_0x55f1f89dd938 -> op_0x55f1f89dd900 [label="C_out"];
    interface_1_in_0x55f1f89ddc40 -> op_0x55f1f89ddc20 [label="k_2*s"];
    interface_1_in_0x55f1f89ddc58 -> op_0x55f1f89ddc20 [label="k_2*s"];
    interface_1_in_0x55f1f89def00 -> interface_1_out_0x55f1f89def00 [label="s"];
    interface_1_in_0x55f1f89def18 -> interface_1_out_0x55f1f89def18 [label="s^-1*H"];
    interface_1_in_0x55f1f89e2c20 -> op_0x55f1f89e2c00 [label="k_1"];
    interface_1_in_0x55f1f89e2c38 -> op_0x55f1f89e2c00 [label="k_1"];
    op_0x55f1f89e2c00 -> reduce_0x7f5f78003a98 [label="k_1"];
    op_0x55f1f89ddc20 -> reduce_0x7f5f780054d0 [label="k_2*s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_2_out_0x55f1f89def00 [label="s", shape=none];
        interface_2_out_0x55f1f89e2c20 [label="k_1", shape=none];
        interface_2_out_0x55f1f89def18 [label="s^-1*H", shape=none];
        interface_2_out_0x55f1eba3e3d0 [label="H", shape=none];
        interface_2_out_0x55f1f89ddc40 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x55f1ee7b7da0;
        interface_2_out_0x55f1f89def00;
        interface_2_out_0x55f1f89e2c20;
        interface_2_out_0x55f1f89def18;
        interface_2_out_0x55f1eba3e3d0;
        interface_2_out_0x55f1f89ddc40;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_2_in_0x55f1f8a6bcc0 [label="H", shape=none];
        interface_2_in_0x55f1eba3e3d0 [label="H", shape=none];
        interface_2_in_0x55f1f89ddc40 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55f1ee7b7da0;
        interface_2_in_0x55f1f8a6bcc0;
        interface_2_in_0x55f1eba3e3d0;
        interface_2_in_0x55f1f89ddc40;
    }
    // Op's.
    op_0x55f1f8a6bc80 [label="Split"];
    op_0x55f1f8a75080 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x55f1eba3e3d0 -> interface_2_out_0x55f1eba3e3d0 [label="H"];
    interface_2_in_0x55f1ee7b7da0 -> interface_2_out_0x55f1ee7b7da0 [label="N"];
    interface_2_in_0x55f1f89ddc40 -> interface_2_out_0x55f1f89ddc40 [label="k_2*s"];
    op_0x55f1f8a6bc80 -> interface_2_out_0x55f1f89def00 [label="s"];
    op_0x55f1f8a75080 -> interface_2_out_0x55f1f89def18 [label="s^-1*H"];
    op_0x55f1f8a75080 -> interface_2_out_0x55f1f89e2c20 [label="k_1"];
    interface_2_in_0x55f1f8a6bcc0 -> op_0x55f1f8a6bc80 [label="H"];
    op_0x55f1f8a6bc80 -> op_0x55f1f8a75080 [label="s^-1*H"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7f5f78007b70 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_3_out_0x55f1f8a6bcc0 [label="H", shape=none];
        interface_3_out_0x55f1eba3e3d0 [label="H", shape=none];
        interface_3_out_0x55f1f89ddc40 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5f78007b70;
        interface_3_out_0x55f1ee7b7da0;
        interface_3_out_0x55f1f8a6bcc0;
        interface_3_out_0x55f1eba3e3d0;
        interface_3_out_0x55f1f89ddc40;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_3_in_0x55f1f89ddce0 [label="C_in", shape=none];
        interface_3_in_0x55f1f8a6bcc0 [label="H", shape=none];
        interface_3_in_0x55f1eba3e3d0 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x55f1f89ddcf8 [label="C_in", shape=none];
        interface_3_in_0x55f1f89ddd48 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55f1ee7b7da0;
        interface_3_in_0x55f1f89ddce0;
        interface_3_in_0x55f1f8a6bcc0;
        interface_3_in_0x55f1eba3e3d0;
        interface_3_in_0x55f1f89ddcf8;
        interface_3_in_0x55f1f89ddd48;
    }
    // Op's.
    op_0x55f1f88b2a18 [label="Expand"];
    op_0x55f1f89ddcc0 [label="Share"];
    op_0x55f1f89ddd10 [label="Share"];
    // Dimension's.
    interface_3_in_0x55f1eba3e3d0 -> interface_3_out_0x55f1eba3e3d0 [label="H"];
    interface_3_in_0x55f1ee7b7da0 -> interface_3_out_0x55f1ee7b7da0 [label="N"];
    op_0x55f1f89ddd10 -> interface_3_out_0x55f1f89ddc40 [label="k_2*s"];
    interface_3_in_0x55f1f89ddce0 -> op_0x55f1f89ddcc0 [label="C_in"];
    interface_3_in_0x55f1f89ddcf8 -> op_0x55f1f89ddcc0 [label="C_in"];
    op_0x55f1f88b2a18 -> op_0x55f1f89ddd10 [label="k_2*s"];
    interface_3_in_0x55f1f89ddd48 -> op_0x55f1f89ddd10 [label="k_2*s"];
    interface_3_in_0x55f1f8a6bcc0 -> interface_3_out_0x55f1f8a6bcc0 [label="H"];
    op_0x55f1f89ddcc0 -> reduce_0x7f5f78007b70 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x55f1ee7b7da0 [label="N", shape=none];
    interface_4_out_0x55f1f89ddce0 [label="C_in", shape=none];
    interface_4_out_0x55f1f8a6bcc0 [label="H", shape=none];
    interface_4_out_0x55f1eba3e3d0 [label="H", shape=none];
}

interface_4_out_0x55f1ee7b7da0 -> interface_3_in_0x55f1ee7b7da0;
interface_4_out_0x55f1f89ddce0 -> interface_3_in_0x55f1f89ddce0;
interface_4_out_0x55f1f8a6bcc0 -> interface_3_in_0x55f1f8a6bcc0;
interface_4_out_0x55f1eba3e3d0 -> interface_3_in_0x55f1eba3e3d0;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 2";
    interface_5_out_0x55f1f89ddcf8 [label="C_in", shape=none];
    interface_5_out_0x55f1f89ddd48 [label="k_2*s", shape=none];
}

interface_5_out_0x55f1f89ddcf8 -> interface_3_in_0x55f1f89ddcf8;
interface_5_out_0x55f1f89ddd48 -> interface_3_in_0x55f1f89ddd48;

interface_3_out_0x55f1ee7b7da0 -> interface_2_in_0x55f1ee7b7da0;
interface_3_out_0x55f1f8a6bcc0 -> interface_2_in_0x55f1f8a6bcc0;
interface_3_out_0x55f1eba3e3d0 -> interface_2_in_0x55f1eba3e3d0;
interface_3_out_0x55f1f89ddc40 -> interface_2_in_0x55f1f89ddc40;

interface_2_out_0x55f1ee7b7da0 -> interface_1_in_0x55f1ee7b7da0;
interface_2_out_0x55f1f89def00 -> interface_1_in_0x55f1f89def00;
interface_2_out_0x55f1f89e2c20 -> interface_1_in_0x55f1f89e2c20;
interface_2_out_0x55f1f89def18 -> interface_1_in_0x55f1f89def18;
interface_2_out_0x55f1eba3e3d0 -> interface_1_in_0x55f1eba3e3d0;
interface_2_out_0x55f1f89ddc40 -> interface_1_in_0x55f1f89ddc40;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 1";
    interface_6_out_0x55f1f89dd938 [label="C_out", shape=none];
    interface_6_out_0x55f1f89e2c38 [label="k_1", shape=none];
    interface_6_out_0x55f1f89ddc58 [label="k_2*s", shape=none];
}

interface_6_out_0x55f1f89dd938 -> interface_1_in_0x55f1f89dd938;
interface_6_out_0x55f1f89e2c38 -> interface_1_in_0x55f1f89e2c38;
interface_6_out_0x55f1f89ddc58 -> interface_1_in_0x55f1f89ddc58;

interface_1_out_0x55f1ee7b7da0 -> interface_0_in_0x55f1ee7b7da0;
interface_1_out_0x55f1ee7b7dc8 -> interface_0_in_0x55f1ee7b7dc8;
interface_1_out_0x55f1f89def00 -> interface_0_in_0x55f1f89def00;
interface_1_out_0x55f1f89def18 -> interface_0_in_0x55f1f89def18;
interface_1_out_0x55f1eba3e3d0 -> interface_0_in_0x55f1eba3e3d0;

{
    rank = same;
    interface_4_out_0x55f1ee7b7da0;
    interface_4_out_0x55f1f89ddce0;
    interface_4_out_0x55f1f8a6bcc0;
    interface_4_out_0x55f1eba3e3d0;
    interface_6_out_0x55f1f89dd938;
    interface_6_out_0x55f1f89e2c38;
    interface_6_out_0x55f1f89ddc58;
    interface_5_out_0x55f1f89ddcf8;
    interface_5_out_0x55f1f89ddd48;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_7_in_0x55f1ee7b7da0 [label="N", shape=none];
    interface_7_in_0x55f1ee7b7dc8 [label="C_out", shape=none];
    interface_7_in_0x55f1ee7b7df0 [label="H", shape=none];
    interface_7_in_0x55f1ee7b7e18 [label="H", shape=none];
}
interface_0_out_0x55f1ee7b7da0 -> interface_7_in_0x55f1ee7b7da0;
interface_0_out_0x55f1ee7b7dc8 -> interface_7_in_0x55f1ee7b7dc8;
interface_0_out_0x55f1ee7b7df0 -> interface_7_in_0x55f1ee7b7df0;
interface_0_out_0x55f1ee7b7e18 -> interface_7_in_0x55f1ee7b7e18;

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
		t_3 = torch.einsum("limk, ij -> lmkj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Split9d4d44f1bf98c2cc -> [s]@Merged3c50a2f22396ae4, [s^-1*H]@Unfold13a2e71a3ce37a21
		t_4 = torch.reshape(t_4, (1, 2, 56, 112, 14, ))

		# [s^-1*H]@Unfold13a2e71a3ce37a21 -> [s^-1*H]@Merged3c50a2f22396aeb, [k_1]@Share26cfa48d169008e4
		t_4 = torch.reshape(t_4, (1, 2, 56, 1568, ))
		t_4 = torch.nn.functional.unfold(t_4, (3, 1, ), padding=(1, 0, ))
		t_4 = torch.reshape(t_4, (1, 2, 3, 56, 112, 14, ))

		# Perform contraction.
		t_5 = torch.einsum("mnkolj, ikj -> minol", t_4, in_1)

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
		t_3 = torch.einsum("limk, ij -> lmkj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Split9d4d44f1bf98c2cc -> [s]@Merged3c50a2f22396ae4, [s^-1*H]@Unfold13a2e71a3ce37a21
		t_4 = torch.reshape(t_4, (1, 2, 28, 56, 14, ))

		# [s^-1*H]@Unfold13a2e71a3ce37a21 -> [s^-1*H]@Merged3c50a2f22396aeb, [k_1]@Share26cfa48d169008e4
		t_4 = torch.reshape(t_4, (1, 2, 28, 784, ))
		t_4 = torch.nn.functional.unfold(t_4, (3, 1, ), padding=(1, 0, ))
		t_4 = torch.reshape(t_4, (1, 2, 3, 28, 56, 14, ))

		# Perform contraction.
		t_5 = torch.einsum("mnkolj, ikj -> minol", t_4, in_1)

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
		t_3 = torch.einsum("limk, ij -> lmkj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Split9d4d44f1bf98c2cc -> [s]@Merged3c50a2f22396ae4, [s^-1*H]@Unfold13a2e71a3ce37a21
		t_4 = torch.reshape(t_4, (1, 2, 28, 56, 14, ))

		# [s^-1*H]@Unfold13a2e71a3ce37a21 -> [s^-1*H]@Merged3c50a2f22396aeb, [k_1]@Share26cfa48d169008e4
		t_4 = torch.reshape(t_4, (1, 2, 28, 784, ))
		t_4 = torch.nn.functional.unfold(t_4, (3, 1, ), padding=(1, 0, ))
		t_4 = torch.reshape(t_4, (1, 2, 3, 28, 56, 14, ))

		# Perform contraction.
		t_5 = torch.einsum("mnkolj, ikj -> minol", t_4, in_1)

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
		t_3 = torch.einsum("limk, ij -> lmkj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Split9d4d44f1bf98c2cc -> [s]@Merged3c50a2f22396ae4, [s^-1*H]@Unfold13a2e71a3ce37a21
		t_4 = torch.reshape(t_4, (1, 2, 14, 28, 14, ))

		# [s^-1*H]@Unfold13a2e71a3ce37a21 -> [s^-1*H]@Merged3c50a2f22396aeb, [k_1]@Share26cfa48d169008e4
		t_4 = torch.reshape(t_4, (1, 2, 14, 392, ))
		t_4 = torch.nn.functional.unfold(t_4, (3, 1, ), padding=(1, 0, ))
		t_4 = torch.reshape(t_4, (1, 2, 3, 14, 28, 14, ))

		# Perform contraction.
		t_5 = torch.einsum("mnkolj, ikj -> minol", t_4, in_1)

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
		t_3 = torch.einsum("limk, ij -> lmkj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Split9d4d44f1bf98c2cc -> [s]@Merged3c50a2f22396ae4, [s^-1*H]@Unfold13a2e71a3ce37a21
		t_4 = torch.reshape(t_4, (1, 2, 14, 28, 14, ))

		# [s^-1*H]@Unfold13a2e71a3ce37a21 -> [s^-1*H]@Merged3c50a2f22396aeb, [k_1]@Share26cfa48d169008e4
		t_4 = torch.reshape(t_4, (1, 2, 14, 392, ))
		t_4 = torch.nn.functional.unfold(t_4, (3, 1, ), padding=(1, 0, ))
		t_4 = torch.reshape(t_4, (1, 2, 3, 14, 28, 14, ))

		# Perform contraction.
		t_5 = torch.einsum("mnkolj, ikj -> minol", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merged3c50a2f22396ae4, [s^-1*H]@Merged3c50a2f22396aeb -> [H]@Iterator96123ba3184da39c
		t_6 = torch.reshape(t_6, (1, 256, 28, 28, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_6

		return y

