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
        interface_0_out_0x55fdefc1ee20 [label="N", shape=none];
        interface_0_out_0x55fdefc1ee48 [label="C_out", shape=none];
        interface_0_out_0x55fdefc1ee70 [label="H", shape=none];
        interface_0_out_0x55fdefc1ee98 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55fdefc1ee20;
        interface_0_out_0x55fdefc1ee48;
        interface_0_out_0x55fdefc1ee70;
        interface_0_out_0x55fdefc1ee98;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55fdefc1ee20 [label="N", shape=none];
        interface_0_in_0x55fdefc1ee48 [label="C_out", shape=none];
        interface_0_in_0x7fa910005d20 [label="s", shape=none];
        interface_0_in_0x7fa910005d38 [label="s^-1*H", shape=none];
        interface_0_in_0x7fa950005dd0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55fdefc1ee20;
        interface_0_in_0x55fdefc1ee48;
        interface_0_in_0x7fa910005d20;
        interface_0_in_0x7fa910005d38;
        interface_0_in_0x7fa950005dd0;
    }
    // Op's.
    op_0x7fa910005ce0 [label="Merge"];
    op_0x7fa950005db0 [label="Shift"];
    // Dimension's.
    interface_0_in_0x55fdefc1ee20 -> interface_0_out_0x55fdefc1ee20 [label="N"];
    interface_0_in_0x55fdefc1ee48 -> interface_0_out_0x55fdefc1ee48 [label="C_out"];
    op_0x7fa910005ce0 -> interface_0_out_0x55fdefc1ee70 [label="H"];
    op_0x7fa950005db0 -> interface_0_out_0x55fdefc1ee98 [label="H"];
    interface_0_in_0x7fa910005d20 -> op_0x7fa910005ce0 [label="s"];
    interface_0_in_0x7fa910005d38 -> op_0x7fa910005ce0 [label="s^-1*H"];
    interface_0_in_0x7fa950005dd0 -> op_0x7fa950005db0 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fa1a4001998 [label="Sum", shape=box];
    reduce_0x7fa1a40035d0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55fdefc1ee20 [label="N", shape=none];
        interface_1_out_0x55fdefc1ee48 [label="C_out", shape=none];
        interface_1_out_0x7fa910005d20 [label="s", shape=none];
        interface_1_out_0x7fa910005d38 [label="s^-1*H", shape=none];
        interface_1_out_0x7fa950005dd0 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fa1a4001998;
        reduce_0x7fa1a40035d0;
        interface_1_out_0x55fdefc1ee20;
        interface_1_out_0x55fdefc1ee48;
        interface_1_out_0x7fa910005d20;
        interface_1_out_0x7fa910005d38;
        interface_1_out_0x7fa950005dd0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55fdefc1ee20 [label="N", shape=none];
        interface_1_in_0x7fa910005d20 [label="s", shape=none];
        interface_1_in_0x7fa8e4004650 [label="k_1", shape=none];
        interface_1_in_0x7fa910005d38 [label="s^-1*H", shape=none];
        interface_1_in_0x7fa950005dd0 [label="H", shape=none];
        interface_1_in_0x7fa8fc004ca0 [label="k_2*s", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x7fa950004638 [label="C_out", shape=none];
        interface_1_in_0x7fa8e4004668 [label="k_1", shape=none];
        interface_1_in_0x7fa8fc004cb8 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55fdefc1ee20;
        interface_1_in_0x7fa910005d20;
        interface_1_in_0x7fa8e4004650;
        interface_1_in_0x7fa910005d38;
        interface_1_in_0x7fa950005dd0;
        interface_1_in_0x7fa8fc004ca0;
        interface_1_in_0x7fa950004638;
        interface_1_in_0x7fa8e4004668;
        interface_1_in_0x7fa8fc004cb8;
    }
    // Op's.
    op_0x7fa8e4004630 [label="Share"];
    op_0x7fa8fc004c80 [label="Share"];
    op_0x7fa950004600 [label="Share"];
    op_0x7fa950004cf8 [label="Expand"];
    // Dimension's.
    interface_1_in_0x55fdefc1ee20 -> interface_1_out_0x55fdefc1ee20 [label="N"];
    op_0x7fa950004600 -> interface_1_out_0x55fdefc1ee48 [label="C_out"];
    op_0x7fa8e4004630 -> reduce_0x7fa1a4001998 [label="k_1"];
    op_0x7fa8fc004c80 -> reduce_0x7fa1a40035d0 [label="k_2*s"];
    interface_1_in_0x7fa8e4004650 -> op_0x7fa8e4004630 [label="k_1"];
    interface_1_in_0x7fa8e4004668 -> op_0x7fa8e4004630 [label="k_1"];
    interface_1_in_0x7fa8fc004ca0 -> op_0x7fa8fc004c80 [label="k_2*s"];
    interface_1_in_0x7fa8fc004cb8 -> op_0x7fa8fc004c80 [label="k_2*s"];
    interface_1_in_0x7fa910005d20 -> interface_1_out_0x7fa910005d20 [label="s"];
    interface_1_in_0x7fa910005d38 -> interface_1_out_0x7fa910005d38 [label="s^-1*H"];
    op_0x7fa950004cf8 -> op_0x7fa950004600 [label="C_out"];
    interface_1_in_0x7fa950004638 -> op_0x7fa950004600 [label="C_out"];
    interface_1_in_0x7fa950005dd0 -> interface_1_out_0x7fa950005dd0 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55fdefc1ee20 [label="N", shape=none];
        interface_2_out_0x7fa910005d20 [label="s", shape=none];
        interface_2_out_0x7fa8e4004650 [label="k_1", shape=none];
        interface_2_out_0x7fa910005d38 [label="s^-1*H", shape=none];
        interface_2_out_0x7fa950005dd0 [label="H", shape=none];
        interface_2_out_0x7fa8fc004ca0 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x55fdefc1ee20;
        interface_2_out_0x7fa910005d20;
        interface_2_out_0x7fa8e4004650;
        interface_2_out_0x7fa910005d38;
        interface_2_out_0x7fa950005dd0;
        interface_2_out_0x7fa8fc004ca0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55fdefc1ee20 [label="N", shape=none];
        interface_2_in_0x7fa050194330 [label="H", shape=none];
        interface_2_in_0x7fa950005dd0 [label="H", shape=none];
        interface_2_in_0x7fa8fc004ca0 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55fdefc1ee20;
        interface_2_in_0x7fa050194330;
        interface_2_in_0x7fa950005dd0;
        interface_2_in_0x7fa8fc004ca0;
    }
    // Op's.
    op_0x7fa0501942f0 [label="Split"];
    op_0x7fa4d8030c80 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x55fdefc1ee20 -> interface_2_out_0x55fdefc1ee20 [label="N"];
    interface_2_in_0x7fa050194330 -> op_0x7fa0501942f0 [label="H"];
    op_0x7fa0501942f0 -> op_0x7fa4d8030c80 [label="s^-1*H"];
    op_0x7fa4d8030c80 -> interface_2_out_0x7fa8e4004650 [label="k_1"];
    interface_2_in_0x7fa8fc004ca0 -> interface_2_out_0x7fa8fc004ca0 [label="k_2*s"];
    op_0x7fa0501942f0 -> interface_2_out_0x7fa910005d20 [label="s"];
    op_0x7fa4d8030c80 -> interface_2_out_0x7fa910005d38 [label="s^-1*H"];
    interface_2_in_0x7fa950005dd0 -> interface_2_out_0x7fa950005dd0 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7fa1a4005e70 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55fdefc1ee20 [label="N", shape=none];
        interface_3_out_0x7fa050194330 [label="H", shape=none];
        interface_3_out_0x7fa950005dd0 [label="H", shape=none];
        interface_3_out_0x7fa8fc004ca0 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        reduce_0x7fa1a4005e70;
        interface_3_out_0x55fdefc1ee20;
        interface_3_out_0x7fa050194330;
        interface_3_out_0x7fa950005dd0;
        interface_3_out_0x7fa8fc004ca0;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55fdefc1ee20 [label="N", shape=none];
        interface_3_in_0x7fa58c00af20 [label="C_in", shape=none];
        interface_3_in_0x7fa050194330 [label="H", shape=none];
        interface_3_in_0x7fa950005dd0 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x7fa58c00af38 [label="C_in", shape=none];
        interface_3_in_0x7fa58c0096d8 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55fdefc1ee20;
        interface_3_in_0x7fa58c00af20;
        interface_3_in_0x7fa050194330;
        interface_3_in_0x7fa950005dd0;
        interface_3_in_0x7fa58c00af38;
        interface_3_in_0x7fa58c0096d8;
    }
    // Op's.
    op_0x7fa58c0096a0 [label="Share"];
    op_0x7fa58c00af00 [label="Share"];
    op_0x7fa950004d98 [label="Expand"];
    // Dimension's.
    interface_3_in_0x55fdefc1ee20 -> interface_3_out_0x55fdefc1ee20 [label="N"];
    interface_3_in_0x7fa050194330 -> interface_3_out_0x7fa050194330 [label="H"];
    op_0x7fa58c00af00 -> reduce_0x7fa1a4005e70 [label="C_in"];
    op_0x7fa950004d98 -> op_0x7fa58c0096a0 [label="k_2*s"];
    interface_3_in_0x7fa58c0096d8 -> op_0x7fa58c0096a0 [label="k_2*s"];
    interface_3_in_0x7fa58c00af20 -> op_0x7fa58c00af00 [label="C_in"];
    interface_3_in_0x7fa58c00af38 -> op_0x7fa58c00af00 [label="C_in"];
    op_0x7fa58c0096a0 -> interface_3_out_0x7fa8fc004ca0 [label="k_2*s"];
    interface_3_in_0x7fa950005dd0 -> interface_3_out_0x7fa950005dd0 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x55fdefc1ee20 [label="N", shape=none];
    interface_4_out_0x7fa58c00af20 [label="C_in", shape=none];
    interface_4_out_0x7fa050194330 [label="H", shape=none];
    interface_4_out_0x7fa950005dd0 [label="H", shape=none];
}

interface_4_out_0x55fdefc1ee20 -> interface_3_in_0x55fdefc1ee20;
interface_4_out_0x7fa58c00af20 -> interface_3_in_0x7fa58c00af20;
interface_4_out_0x7fa050194330 -> interface_3_in_0x7fa050194330;
interface_4_out_0x7fa950005dd0 -> interface_3_in_0x7fa950005dd0;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 2";
    interface_5_out_0x7fa58c00af38 [label="C_in", shape=none];
    interface_5_out_0x7fa58c0096d8 [label="k_2*s", shape=none];
}

interface_5_out_0x7fa58c00af38 -> interface_3_in_0x7fa58c00af38;
interface_5_out_0x7fa58c0096d8 -> interface_3_in_0x7fa58c0096d8;

interface_3_out_0x55fdefc1ee20 -> interface_2_in_0x55fdefc1ee20;
interface_3_out_0x7fa050194330 -> interface_2_in_0x7fa050194330;
interface_3_out_0x7fa950005dd0 -> interface_2_in_0x7fa950005dd0;
interface_3_out_0x7fa8fc004ca0 -> interface_2_in_0x7fa8fc004ca0;

interface_2_out_0x55fdefc1ee20 -> interface_1_in_0x55fdefc1ee20;
interface_2_out_0x7fa910005d20 -> interface_1_in_0x7fa910005d20;
interface_2_out_0x7fa8e4004650 -> interface_1_in_0x7fa8e4004650;
interface_2_out_0x7fa910005d38 -> interface_1_in_0x7fa910005d38;
interface_2_out_0x7fa950005dd0 -> interface_1_in_0x7fa950005dd0;
interface_2_out_0x7fa8fc004ca0 -> interface_1_in_0x7fa8fc004ca0;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 1";
    interface_6_out_0x7fa950004638 [label="C_out", shape=none];
    interface_6_out_0x7fa8e4004668 [label="k_1", shape=none];
    interface_6_out_0x7fa8fc004cb8 [label="k_2*s", shape=none];
}

interface_6_out_0x7fa950004638 -> interface_1_in_0x7fa950004638;
interface_6_out_0x7fa8e4004668 -> interface_1_in_0x7fa8e4004668;
interface_6_out_0x7fa8fc004cb8 -> interface_1_in_0x7fa8fc004cb8;

interface_1_out_0x55fdefc1ee20 -> interface_0_in_0x55fdefc1ee20;
interface_1_out_0x55fdefc1ee48 -> interface_0_in_0x55fdefc1ee48;
interface_1_out_0x7fa910005d20 -> interface_0_in_0x7fa910005d20;
interface_1_out_0x7fa910005d38 -> interface_0_in_0x7fa910005d38;
interface_1_out_0x7fa950005dd0 -> interface_0_in_0x7fa950005dd0;

{
    rank = same;
    interface_4_out_0x55fdefc1ee20;
    interface_4_out_0x7fa58c00af20;
    interface_4_out_0x7fa050194330;
    interface_4_out_0x7fa950005dd0;
    interface_6_out_0x7fa950004638;
    interface_6_out_0x7fa8e4004668;
    interface_6_out_0x7fa8fc004cb8;
    interface_5_out_0x7fa58c00af38;
    interface_5_out_0x7fa58c0096d8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_7_in_0x55fdefc1ee20 [label="N", shape=none];
    interface_7_in_0x55fdefc1ee48 [label="C_out", shape=none];
    interface_7_in_0x55fdefc1ee70 [label="H", shape=none];
    interface_7_in_0x55fdefc1ee98 [label="H", shape=none];
}
interface_0_out_0x55fdefc1ee20 -> interface_7_in_0x55fdefc1ee20;
interface_0_out_0x55fdefc1ee48 -> interface_7_in_0x55fdefc1ee48;
interface_0_out_0x55fdefc1ee70 -> interface_7_in_0x55fdefc1ee70;
interface_0_out_0x55fdefc1ee98 -> interface_7_in_0x55fdefc1ee98;

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
		t_3 = torch.einsum("kjlm, ji -> klmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Split9d4d44f1bf98c2cc -> [s]@Merged3c50a2f22396ae4, [s^-1*H]@Unfold13a2e71a3ce37a21
		t_4 = torch.reshape(t_4, (128, 2, 56, 112, 14, ))

		# [s^-1*H]@Unfold13a2e71a3ce37a21 -> [s^-1*H]@Merged3c50a2f22396aeb, [k_1]@Share26cfa48d169008e4
		t_4 = torch.reshape(t_4, (128, 2, 56, 1568, ))
		t_4 = torch.nn.functional.unfold(t_4, (3, 1, ), padding=(1, 0, ))
		t_4 = torch.reshape(t_4, (128, 2, 3, 56, 112, 14, ))

		# Perform contraction.
		t_5 = torch.einsum("lminoj, kij -> lkmno", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merged3c50a2f22396ae4, [s^-1*H]@Merged3c50a2f22396aeb -> [H]@Iterator96123ba3184da39c
		t_6 = torch.reshape(t_6, (128, 24, 112, 112, ))

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
		t_3 = torch.einsum("kjlm, ji -> klmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Split9d4d44f1bf98c2cc -> [s]@Merged3c50a2f22396ae4, [s^-1*H]@Unfold13a2e71a3ce37a21
		t_4 = torch.reshape(t_4, (128, 2, 28, 56, 14, ))

		# [s^-1*H]@Unfold13a2e71a3ce37a21 -> [s^-1*H]@Merged3c50a2f22396aeb, [k_1]@Share26cfa48d169008e4
		t_4 = torch.reshape(t_4, (128, 2, 28, 784, ))
		t_4 = torch.nn.functional.unfold(t_4, (3, 1, ), padding=(1, 0, ))
		t_4 = torch.reshape(t_4, (128, 2, 3, 28, 56, 14, ))

		# Perform contraction.
		t_5 = torch.einsum("lminoj, kij -> lkmno", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merged3c50a2f22396ae4, [s^-1*H]@Merged3c50a2f22396aeb -> [H]@Iterator96123ba3184da39c
		t_6 = torch.reshape(t_6, (128, 96, 56, 56, ))

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
		t_3 = torch.einsum("kjlm, ji -> klmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Split9d4d44f1bf98c2cc -> [s]@Merged3c50a2f22396ae4, [s^-1*H]@Unfold13a2e71a3ce37a21
		t_4 = torch.reshape(t_4, (128, 2, 28, 56, 14, ))

		# [s^-1*H]@Unfold13a2e71a3ce37a21 -> [s^-1*H]@Merged3c50a2f22396aeb, [k_1]@Share26cfa48d169008e4
		t_4 = torch.reshape(t_4, (128, 2, 28, 784, ))
		t_4 = torch.nn.functional.unfold(t_4, (3, 1, ), padding=(1, 0, ))
		t_4 = torch.reshape(t_4, (128, 2, 3, 28, 56, 14, ))

		# Perform contraction.
		t_5 = torch.einsum("lminoj, kij -> lkmno", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merged3c50a2f22396ae4, [s^-1*H]@Merged3c50a2f22396aeb -> [H]@Iterator96123ba3184da39c
		t_6 = torch.reshape(t_6, (128, 192, 56, 56, ))

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
		t_3 = torch.einsum("kjlm, ji -> klmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Split9d4d44f1bf98c2cc -> [s]@Merged3c50a2f22396ae4, [s^-1*H]@Unfold13a2e71a3ce37a21
		t_4 = torch.reshape(t_4, (128, 2, 14, 28, 14, ))

		# [s^-1*H]@Unfold13a2e71a3ce37a21 -> [s^-1*H]@Merged3c50a2f22396aeb, [k_1]@Share26cfa48d169008e4
		t_4 = torch.reshape(t_4, (128, 2, 14, 392, ))
		t_4 = torch.nn.functional.unfold(t_4, (3, 1, ), padding=(1, 0, ))
		t_4 = torch.reshape(t_4, (128, 2, 3, 14, 28, 14, ))

		# Perform contraction.
		t_5 = torch.einsum("lminoj, kij -> lkmno", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merged3c50a2f22396ae4, [s^-1*H]@Merged3c50a2f22396aeb -> [H]@Iterator96123ba3184da39c
		t_6 = torch.reshape(t_6, (128, 192, 28, 28, ))

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
		t_3 = torch.einsum("kjlm, ji -> klmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Split9d4d44f1bf98c2cc -> [s]@Merged3c50a2f22396ae4, [s^-1*H]@Unfold13a2e71a3ce37a21
		t_4 = torch.reshape(t_4, (128, 2, 14, 28, 14, ))

		# [s^-1*H]@Unfold13a2e71a3ce37a21 -> [s^-1*H]@Merged3c50a2f22396aeb, [k_1]@Share26cfa48d169008e4
		t_4 = torch.reshape(t_4, (128, 2, 14, 392, ))
		t_4 = torch.nn.functional.unfold(t_4, (3, 1, ), padding=(1, 0, ))
		t_4 = torch.reshape(t_4, (128, 2, 3, 14, 28, 14, ))

		# Perform contraction.
		t_5 = torch.einsum("lminoj, kij -> lkmno", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merged3c50a2f22396ae4, [s^-1*H]@Merged3c50a2f22396aeb -> [H]@Iterator96123ba3184da39c
		t_6 = torch.reshape(t_6, (128, 256, 28, 28, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_6

		return y

