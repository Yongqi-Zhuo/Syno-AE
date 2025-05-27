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
        interface_0_in_0x560419919330 [label="s^-1*H", shape=none];
        interface_0_in_0x560419919348 [label="s", shape=none];
        interface_0_in_0x560419917fd0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5604185d74e0;
        interface_0_in_0x5604185d7508;
        interface_0_in_0x560419919330;
        interface_0_in_0x560419919348;
        interface_0_in_0x560419917fd0;
    }
    // Op's.
    op_0x560419917fb0 [label="Shift"];
    op_0x5604199192f0 [label="Merge"];
    // Dimension's.
    interface_0_in_0x5604185d74e0 -> interface_0_out_0x5604185d74e0 [label="N"];
    interface_0_in_0x5604185d7508 -> interface_0_out_0x5604185d7508 [label="C_out"];
    op_0x5604199192f0 -> interface_0_out_0x5604185d7530 [label="H"];
    op_0x560419917fb0 -> interface_0_out_0x5604185d7558 [label="H"];
    interface_0_in_0x560419917fd0 -> op_0x560419917fb0 [label="H"];
    interface_0_in_0x560419919330 -> op_0x5604199192f0 [label="s^-1*H"];
    interface_0_in_0x560419919348 -> op_0x5604199192f0 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fc32c007b70 [label="Sum", shape=box];
    reduce_0x7fc32c003a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5604185d74e0 [label="N", shape=none];
        interface_1_out_0x5604185d7508 [label="C_out", shape=none];
        interface_1_out_0x560419919330 [label="s^-1*H", shape=none];
        interface_1_out_0x560419919348 [label="s", shape=none];
        interface_1_out_0x560419917fd0 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc32c007b70;
        reduce_0x7fc32c003a98;
        interface_1_out_0x5604185d74e0;
        interface_1_out_0x5604185d7508;
        interface_1_out_0x560419919330;
        interface_1_out_0x560419919348;
        interface_1_out_0x560419917fd0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5604185d74e0 [label="N", shape=none];
        interface_1_in_0x560419917520 [label="C_in", shape=none];
        interface_1_in_0x56041991c920 [label="k_1", shape=none];
        interface_1_in_0x560419919330 [label="s^-1*H", shape=none];
        interface_1_in_0x560419919348 [label="s", shape=none];
        interface_1_in_0x560419917fd0 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x5604199172b8 [label="C_out", shape=none];
        interface_1_in_0x560419917538 [label="C_in", shape=none];
        interface_1_in_0x56041991c938 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5604185d74e0;
        interface_1_in_0x560419917520;
        interface_1_in_0x56041991c920;
        interface_1_in_0x560419919330;
        interface_1_in_0x560419919348;
        interface_1_in_0x560419917fd0;
        interface_1_in_0x5604199172b8;
        interface_1_in_0x560419917538;
        interface_1_in_0x56041991c938;
    }
    // Op's.
    op_0x560419917280 [label="Share"];
    op_0x560419917500 [label="Share"];
    op_0x560419917758 [label="Expand"];
    op_0x56041991c900 [label="Share"];
    // Dimension's.
    interface_1_in_0x5604185d74e0 -> interface_1_out_0x5604185d74e0 [label="N"];
    op_0x560419917280 -> interface_1_out_0x5604185d7508 [label="C_out"];
    op_0x560419917758 -> op_0x560419917280 [label="C_out"];
    interface_1_in_0x5604199172b8 -> op_0x560419917280 [label="C_out"];
    interface_1_in_0x560419917520 -> op_0x560419917500 [label="C_in"];
    interface_1_in_0x560419917538 -> op_0x560419917500 [label="C_in"];
    interface_1_in_0x560419917fd0 -> interface_1_out_0x560419917fd0 [label="H"];
    interface_1_in_0x560419919330 -> interface_1_out_0x560419919330 [label="s^-1*H"];
    interface_1_in_0x560419919348 -> interface_1_out_0x560419919348 [label="s"];
    interface_1_in_0x56041991c920 -> op_0x56041991c900 [label="k_1"];
    interface_1_in_0x56041991c938 -> op_0x56041991c900 [label="k_1"];
    op_0x56041991c900 -> reduce_0x7fc32c003a98 [label="k_1"];
    op_0x560419917500 -> reduce_0x7fc32c007b70 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5604185d74e0 [label="N", shape=none];
        interface_2_out_0x560419917520 [label="C_in", shape=none];
        interface_2_out_0x56041991c920 [label="k_1", shape=none];
        interface_2_out_0x560419919330 [label="s^-1*H", shape=none];
        interface_2_out_0x560419919348 [label="s", shape=none];
        interface_2_out_0x560419917fd0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x5604185d74e0;
        interface_2_out_0x560419917520;
        interface_2_out_0x56041991c920;
        interface_2_out_0x560419919330;
        interface_2_out_0x560419919348;
        interface_2_out_0x560419917fd0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5604185d74e0 [label="N", shape=none];
        interface_2_in_0x560419917520 [label="C_in", shape=none];
        interface_2_in_0x560419947e50 [label="H", shape=none];
        interface_2_in_0x560419917fd0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5604185d74e0;
        interface_2_in_0x560419917520;
        interface_2_in_0x560419947e50;
        interface_2_in_0x560419917fd0;
    }
    // Op's.
    op_0x5604199182b0 [label="Shift"];
    op_0x560419919cc0 [label="Unfold"];
    op_0x560419947e10 [label="Split"];
    // Dimension's.
    interface_2_in_0x5604185d74e0 -> interface_2_out_0x5604185d74e0 [label="N"];
    interface_2_in_0x560419917520 -> interface_2_out_0x560419917520 [label="C_in"];
    interface_2_in_0x560419917fd0 -> interface_2_out_0x560419917fd0 [label="H"];
    op_0x560419947e10 -> op_0x5604199182b0 [label="s^-1*H"];
    op_0x560419919cc0 -> interface_2_out_0x560419919330 [label="s^-1*H"];
    op_0x560419947e10 -> interface_2_out_0x560419919348 [label="s"];
    op_0x5604199182b0 -> op_0x560419919cc0 [label="s^-1*H"];
    op_0x560419919cc0 -> interface_2_out_0x56041991c920 [label="k_1"];
    interface_2_in_0x560419947e50 -> op_0x560419947e10 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x5604185d74e0 [label="N", shape=none];
    interface_3_out_0x560419917520 [label="C_in", shape=none];
    interface_3_out_0x560419947e50 [label="H", shape=none];
    interface_3_out_0x560419917fd0 [label="H", shape=none];
}

interface_3_out_0x5604185d74e0 -> interface_2_in_0x5604185d74e0;
interface_3_out_0x560419917520 -> interface_2_in_0x560419917520;
interface_3_out_0x560419947e50 -> interface_2_in_0x560419947e50;
interface_3_out_0x560419917fd0 -> interface_2_in_0x560419917fd0;

interface_2_out_0x5604185d74e0 -> interface_1_in_0x5604185d74e0;
interface_2_out_0x560419917520 -> interface_1_in_0x560419917520;
interface_2_out_0x56041991c920 -> interface_1_in_0x56041991c920;
interface_2_out_0x560419919330 -> interface_1_in_0x560419919330;
interface_2_out_0x560419919348 -> interface_1_in_0x560419919348;
interface_2_out_0x560419917fd0 -> interface_1_in_0x560419917fd0;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x5604199172b8 [label="C_out", shape=none];
    interface_4_out_0x560419917538 [label="C_in", shape=none];
    interface_4_out_0x56041991c938 [label="k_1", shape=none];
}

interface_4_out_0x5604199172b8 -> interface_1_in_0x5604199172b8;
interface_4_out_0x560419917538 -> interface_1_in_0x560419917538;
interface_4_out_0x56041991c938 -> interface_1_in_0x56041991c938;

interface_1_out_0x5604185d74e0 -> interface_0_in_0x5604185d74e0;
interface_1_out_0x5604185d7508 -> interface_0_in_0x5604185d7508;
interface_1_out_0x560419919330 -> interface_0_in_0x560419919330;
interface_1_out_0x560419919348 -> interface_0_in_0x560419919348;
interface_1_out_0x560419917fd0 -> interface_0_in_0x560419917fd0;

{
    rank = same;
    interface_3_out_0x5604185d74e0;
    interface_3_out_0x560419917520;
    interface_3_out_0x560419947e50;
    interface_3_out_0x560419917fd0;
    interface_4_out_0x5604199172b8;
    interface_4_out_0x560419917538;
    interface_4_out_0x56041991c938;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x5604185d74e0 [label="N", shape=none];
    interface_5_in_0x5604185d7508 [label="C_out", shape=none];
    interface_5_in_0x5604185d7530 [label="H", shape=none];
    interface_5_in_0x5604185d7558 [label="H", shape=none];
}
interface_0_out_0x5604185d74e0 -> interface_5_in_0x5604185d74e0;
interface_0_out_0x5604185d7508 -> interface_5_in_0x5604185d7508;
interface_0_out_0x5604185d7530 -> interface_5_in_0x5604185d7530;
interface_0_out_0x5604185d7558 -> interface_5_in_0x5604185d7558;

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

