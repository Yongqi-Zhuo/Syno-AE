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
        interface_0_out_0x5596d7788c60 [label="N", shape=none];
        interface_0_out_0x5596d7788c88 [label="C_out", shape=none];
        interface_0_out_0x5596d7788cb0 [label="H", shape=none];
        interface_0_out_0x5596d7788cd8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x5596d7788c60;
        interface_0_out_0x5596d7788c88;
        interface_0_out_0x5596d7788cb0;
        interface_0_out_0x5596d7788cd8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5596d7788c60 [label="N", shape=none];
        interface_0_in_0x5596d7788c88 [label="C_out", shape=none];
        interface_0_in_0x5596d78772b0 [label="s^-1*H", shape=none];
        interface_0_in_0x5596d78772c8 [label="s", shape=none];
        interface_0_in_0x5596d7875ed0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5596d7788c60;
        interface_0_in_0x5596d7788c88;
        interface_0_in_0x5596d78772b0;
        interface_0_in_0x5596d78772c8;
        interface_0_in_0x5596d7875ed0;
    }
    // Op's.
    op_0x5596d7875eb0 [label="Shift"];
    op_0x5596d7877270 [label="Merge"];
    // Dimension's.
    interface_0_in_0x5596d7788c60 -> interface_0_out_0x5596d7788c60 [label="N"];
    interface_0_in_0x5596d7788c88 -> interface_0_out_0x5596d7788c88 [label="C_out"];
    op_0x5596d7877270 -> interface_0_out_0x5596d7788cb0 [label="H"];
    op_0x5596d7875eb0 -> interface_0_out_0x5596d7788cd8 [label="H"];
    interface_0_in_0x5596d7875ed0 -> op_0x5596d7875eb0 [label="H"];
    interface_0_in_0x5596d78772b0 -> op_0x5596d7877270 [label="s^-1*H"];
    interface_0_in_0x5596d78772c8 -> op_0x5596d7877270 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7ef0e4005c70 [label="Sum", shape=box];
    reduce_0x7ef0e4001a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5596d7788c60 [label="N", shape=none];
        interface_1_out_0x5596d7788c88 [label="C_out", shape=none];
        interface_1_out_0x5596d78772b0 [label="s^-1*H", shape=none];
        interface_1_out_0x5596d78772c8 [label="s", shape=none];
        interface_1_out_0x5596d7875ed0 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7ef0e4005c70;
        reduce_0x7ef0e4001a98;
        interface_1_out_0x5596d7788c60;
        interface_1_out_0x5596d7788c88;
        interface_1_out_0x5596d78772b0;
        interface_1_out_0x5596d78772c8;
        interface_1_out_0x5596d7875ed0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5596d7788c60 [label="N", shape=none];
        interface_1_in_0x5596d7875440 [label="C_in", shape=none];
        interface_1_in_0x5596d7875490 [label="k_1", shape=none];
        interface_1_in_0x5596d78772b0 [label="s^-1*H", shape=none];
        interface_1_in_0x5596d78772c8 [label="s", shape=none];
        interface_1_in_0x5596d7875ed0 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x5596d7875138 [label="C_out", shape=none];
        interface_1_in_0x5596d7875458 [label="C_in", shape=none];
        interface_1_in_0x5596d78754a8 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5596d7788c60;
        interface_1_in_0x5596d7875440;
        interface_1_in_0x5596d7875490;
        interface_1_in_0x5596d78772b0;
        interface_1_in_0x5596d78772c8;
        interface_1_in_0x5596d7875ed0;
        interface_1_in_0x5596d7875138;
        interface_1_in_0x5596d7875458;
        interface_1_in_0x5596d78754a8;
    }
    // Op's.
    op_0x5596d7875100 [label="Share"];
    op_0x5596d7875420 [label="Share"];
    op_0x5596d7875470 [label="Share"];
    op_0x5596d7875618 [label="Expand"];
    // Dimension's.
    interface_1_in_0x5596d7788c60 -> interface_1_out_0x5596d7788c60 [label="N"];
    op_0x5596d7875100 -> interface_1_out_0x5596d7788c88 [label="C_out"];
    op_0x5596d7875618 -> op_0x5596d7875100 [label="C_out"];
    interface_1_in_0x5596d7875138 -> op_0x5596d7875100 [label="C_out"];
    interface_1_in_0x5596d7875440 -> op_0x5596d7875420 [label="C_in"];
    interface_1_in_0x5596d7875458 -> op_0x5596d7875420 [label="C_in"];
    interface_1_in_0x5596d7875490 -> op_0x5596d7875470 [label="k_1"];
    interface_1_in_0x5596d78754a8 -> op_0x5596d7875470 [label="k_1"];
    interface_1_in_0x5596d7875ed0 -> interface_1_out_0x5596d7875ed0 [label="H"];
    interface_1_in_0x5596d78772b0 -> interface_1_out_0x5596d78772b0 [label="s^-1*H"];
    interface_1_in_0x5596d78772c8 -> interface_1_out_0x5596d78772c8 [label="s"];
    op_0x5596d7875470 -> reduce_0x7ef0e4001a98 [label="k_1"];
    op_0x5596d7875420 -> reduce_0x7ef0e4005c70 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5596d7788c60 [label="N", shape=none];
        interface_2_out_0x5596d7875440 [label="C_in", shape=none];
        interface_2_out_0x5596d7875490 [label="k_1", shape=none];
        interface_2_out_0x5596d78772b0 [label="s^-1*H", shape=none];
        interface_2_out_0x5596d78772c8 [label="s", shape=none];
        interface_2_out_0x5596d7875ed0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x5596d7788c60;
        interface_2_out_0x5596d7875440;
        interface_2_out_0x5596d7875490;
        interface_2_out_0x5596d78772b0;
        interface_2_out_0x5596d78772c8;
        interface_2_out_0x5596d7875ed0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5596d7788c60 [label="N", shape=none];
        interface_2_in_0x5596d7875440 [label="C_in", shape=none];
        interface_2_in_0x5596d787f100 [label="H", shape=none];
        interface_2_in_0x5596d7875ed0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5596d7788c60;
        interface_2_in_0x5596d7875440;
        interface_2_in_0x5596d787f100;
        interface_2_in_0x5596d7875ed0;
    }
    // Op's.
    op_0x5596d7875f70 [label="Shift"];
    op_0x5596d7879480 [label="Unfold"];
    op_0x5596d787f0c0 [label="Split"];
    // Dimension's.
    interface_2_in_0x5596d7788c60 -> interface_2_out_0x5596d7788c60 [label="N"];
    interface_2_in_0x5596d7875440 -> interface_2_out_0x5596d7875440 [label="C_in"];
    op_0x5596d7879480 -> interface_2_out_0x5596d7875490 [label="k_1"];
    interface_2_in_0x5596d7875ed0 -> interface_2_out_0x5596d7875ed0 [label="H"];
    op_0x5596d787f0c0 -> op_0x5596d7875f70 [label="s^-1*H"];
    op_0x5596d7879480 -> interface_2_out_0x5596d78772b0 [label="s^-1*H"];
    op_0x5596d787f0c0 -> interface_2_out_0x5596d78772c8 [label="s"];
    op_0x5596d7875f70 -> op_0x5596d7879480 [label="s^-1*H"];
    interface_2_in_0x5596d787f100 -> op_0x5596d787f0c0 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x5596d7788c60 [label="N", shape=none];
    interface_3_out_0x5596d7875440 [label="C_in", shape=none];
    interface_3_out_0x5596d787f100 [label="H", shape=none];
    interface_3_out_0x5596d7875ed0 [label="H", shape=none];
}

interface_3_out_0x5596d7788c60 -> interface_2_in_0x5596d7788c60;
interface_3_out_0x5596d7875440 -> interface_2_in_0x5596d7875440;
interface_3_out_0x5596d787f100 -> interface_2_in_0x5596d787f100;
interface_3_out_0x5596d7875ed0 -> interface_2_in_0x5596d7875ed0;

interface_2_out_0x5596d7788c60 -> interface_1_in_0x5596d7788c60;
interface_2_out_0x5596d7875440 -> interface_1_in_0x5596d7875440;
interface_2_out_0x5596d7875490 -> interface_1_in_0x5596d7875490;
interface_2_out_0x5596d78772b0 -> interface_1_in_0x5596d78772b0;
interface_2_out_0x5596d78772c8 -> interface_1_in_0x5596d78772c8;
interface_2_out_0x5596d7875ed0 -> interface_1_in_0x5596d7875ed0;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x5596d7875138 [label="C_out", shape=none];
    interface_4_out_0x5596d7875458 [label="C_in", shape=none];
    interface_4_out_0x5596d78754a8 [label="k_1", shape=none];
}

interface_4_out_0x5596d7875138 -> interface_1_in_0x5596d7875138;
interface_4_out_0x5596d7875458 -> interface_1_in_0x5596d7875458;
interface_4_out_0x5596d78754a8 -> interface_1_in_0x5596d78754a8;

interface_1_out_0x5596d7788c60 -> interface_0_in_0x5596d7788c60;
interface_1_out_0x5596d7788c88 -> interface_0_in_0x5596d7788c88;
interface_1_out_0x5596d78772b0 -> interface_0_in_0x5596d78772b0;
interface_1_out_0x5596d78772c8 -> interface_0_in_0x5596d78772c8;
interface_1_out_0x5596d7875ed0 -> interface_0_in_0x5596d7875ed0;

{
    rank = same;
    interface_3_out_0x5596d7788c60;
    interface_3_out_0x5596d7875440;
    interface_3_out_0x5596d787f100;
    interface_3_out_0x5596d7875ed0;
    interface_4_out_0x5596d7875138;
    interface_4_out_0x5596d7875458;
    interface_4_out_0x5596d78754a8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x5596d7788c60 [label="N", shape=none];
    interface_5_in_0x5596d7788c88 [label="C_out", shape=none];
    interface_5_in_0x5596d7788cb0 [label="H", shape=none];
    interface_5_in_0x5596d7788cd8 [label="H", shape=none];
}
interface_0_out_0x5596d7788c60 -> interface_5_in_0x5596d7788c60;
interface_0_out_0x5596d7788c88 -> interface_5_in_0x5596d7788c88;
interface_0_out_0x5596d7788cb0 -> interface_5_in_0x5596d7788cb0;
interface_0_out_0x5596d7788cd8 -> interface_5_in_0x5596d7788cd8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([24, 24, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Split14839c94d488f758 -> [s^-1*H]@Shiftcdaaca31e176569f, [s]@Merge3e25d6fc76d0e079
		t_2 = torch.reshape(t_2, (1, 24, 56, 2, 112, ))

		# [s^-1*H]@Shiftcdaaca31e176569f -> [s^-1*H]@Unfold0a04b4b1bf080a1e
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s^-1*H]@Unfold0a04b4b1bf080a1e -> [s^-1*H]@Merge3e25d6fc76d0e07a, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 24, 56, 224, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 24, 3, 56, 2, 112, ))

		# Perform contraction.
		t_3 = torch.einsum("ljknom, ijk -> linom", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s^-1*H]@Merge3e25d6fc76d0e07a, [s]@Merge3e25d6fc76d0e079 -> [H]@Iterator96123ba3184da39c
		t_4 = torch.reshape(t_4, (1, 24, 112, 112, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([96, 24, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Split14839c94d488f758 -> [s^-1*H]@Shiftcdaaca31e176569f, [s]@Merge3e25d6fc76d0e079
		t_2 = torch.reshape(t_2, (1, 24, 28, 2, 56, ))

		# [s^-1*H]@Shiftcdaaca31e176569f -> [s^-1*H]@Unfold0a04b4b1bf080a1e
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s^-1*H]@Unfold0a04b4b1bf080a1e -> [s^-1*H]@Merge3e25d6fc76d0e07a, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 24, 28, 112, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 24, 3, 28, 2, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("ljknom, ijk -> linom", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s^-1*H]@Merge3e25d6fc76d0e07a, [s]@Merge3e25d6fc76d0e079 -> [H]@Iterator96123ba3184da39c
		t_4 = torch.reshape(t_4, (1, 96, 56, 56, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([192, 48, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Split14839c94d488f758 -> [s^-1*H]@Shiftcdaaca31e176569f, [s]@Merge3e25d6fc76d0e079
		t_2 = torch.reshape(t_2, (1, 48, 28, 2, 56, ))

		# [s^-1*H]@Shiftcdaaca31e176569f -> [s^-1*H]@Unfold0a04b4b1bf080a1e
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s^-1*H]@Unfold0a04b4b1bf080a1e -> [s^-1*H]@Merge3e25d6fc76d0e07a, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 48, 28, 112, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 48, 3, 28, 2, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("ljknom, ijk -> linom", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s^-1*H]@Merge3e25d6fc76d0e07a, [s]@Merge3e25d6fc76d0e079 -> [H]@Iterator96123ba3184da39c
		t_4 = torch.reshape(t_4, (1, 192, 56, 56, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([192, 48, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Split14839c94d488f758 -> [s^-1*H]@Shiftcdaaca31e176569f, [s]@Merge3e25d6fc76d0e079
		t_2 = torch.reshape(t_2, (1, 48, 14, 2, 28, ))

		# [s^-1*H]@Shiftcdaaca31e176569f -> [s^-1*H]@Unfold0a04b4b1bf080a1e
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s^-1*H]@Unfold0a04b4b1bf080a1e -> [s^-1*H]@Merge3e25d6fc76d0e07a, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 48, 14, 56, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 48, 3, 14, 2, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("ljknom, ijk -> linom", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s^-1*H]@Merge3e25d6fc76d0e07a, [s]@Merge3e25d6fc76d0e079 -> [H]@Iterator96123ba3184da39c
		t_4 = torch.reshape(t_4, (1, 192, 28, 28, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Split14839c94d488f758 -> [s^-1*H]@Shiftcdaaca31e176569f, [s]@Merge3e25d6fc76d0e079
		t_2 = torch.reshape(t_2, (1, 64, 14, 2, 28, ))

		# [s^-1*H]@Shiftcdaaca31e176569f -> [s^-1*H]@Unfold0a04b4b1bf080a1e
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s^-1*H]@Unfold0a04b4b1bf080a1e -> [s^-1*H]@Merge3e25d6fc76d0e07a, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 64, 14, 56, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 64, 3, 14, 2, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("ljknom, ijk -> linom", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s^-1*H]@Merge3e25d6fc76d0e07a, [s]@Merge3e25d6fc76d0e079 -> [H]@Iterator96123ba3184da39c
		t_4 = torch.reshape(t_4, (1, 256, 28, 28, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_4

		return y

