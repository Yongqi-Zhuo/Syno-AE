import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7ef0e4001cc0 [label="Sum", shape=box];
    reduce_0x7ef0e40034d0 [label="Sum", shape=box];
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
        reduce_0x7ef0e4001cc0;
        reduce_0x7ef0e40034d0;
        interface_0_out_0x5596d7788c60;
        interface_0_out_0x5596d7788c88;
        interface_0_out_0x5596d7788cb0;
        interface_0_out_0x5596d7788cd8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5596d7788c60 [label="N", shape=none];
        interface_0_in_0x5596d7788cb0 [label="H", shape=none];
        interface_0_in_0x5596d7875210 [label="k_1^2", shape=none];
        interface_0_in_0x5596d7788cd8 [label="H", shape=none];
        interface_0_in_0x5596d7875580 [label="k_2*s", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x5596d7875138 [label="C_out", shape=none];
        interface_0_in_0x5596d7875228 [label="k_1^2", shape=none];
        interface_0_in_0x5596d7875598 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5596d7788c60;
        interface_0_in_0x5596d7788cb0;
        interface_0_in_0x5596d7875210;
        interface_0_in_0x5596d7788cd8;
        interface_0_in_0x5596d7875580;
        interface_0_in_0x5596d7875138;
        interface_0_in_0x5596d7875228;
        interface_0_in_0x5596d7875598;
    }
    // Op's.
    op_0x5596d7875100 [label="Share"];
    op_0x5596d78751f0 [label="Share"];
    op_0x5596d7875560 [label="Share"];
    op_0x5596d7875618 [label="Expand"];
    // Dimension's.
    interface_0_in_0x5596d7788c60 -> interface_0_out_0x5596d7788c60 [label="N"];
    op_0x5596d7875100 -> interface_0_out_0x5596d7788c88 [label="C_out"];
    interface_0_in_0x5596d7788cb0 -> interface_0_out_0x5596d7788cb0 [label="H"];
    interface_0_in_0x5596d7788cd8 -> interface_0_out_0x5596d7788cd8 [label="H"];
    op_0x5596d7875618 -> op_0x5596d7875100 [label="C_out"];
    interface_0_in_0x5596d7875138 -> op_0x5596d7875100 [label="C_out"];
    interface_0_in_0x5596d7875210 -> op_0x5596d78751f0 [label="k_1^2"];
    interface_0_in_0x5596d7875228 -> op_0x5596d78751f0 [label="k_1^2"];
    interface_0_in_0x5596d7875580 -> op_0x5596d7875560 [label="k_2*s"];
    interface_0_in_0x5596d7875598 -> op_0x5596d7875560 [label="k_2*s"];
    op_0x5596d78751f0 -> reduce_0x7ef0e4001cc0 [label="k_1^2"];
    op_0x5596d7875560 -> reduce_0x7ef0e40034d0 [label="k_2*s"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7ef0e4002e58 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5596d7788c60 [label="N", shape=none];
        interface_1_out_0x5596d7788cb0 [label="H", shape=none];
        interface_1_out_0x5596d7875210 [label="k_1^2", shape=none];
        interface_1_out_0x5596d7788cd8 [label="H", shape=none];
        interface_1_out_0x5596d7875580 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        reduce_0x7ef0e4002e58;
        interface_1_out_0x5596d7788c60;
        interface_1_out_0x5596d7788cb0;
        interface_1_out_0x5596d7875210;
        interface_1_out_0x5596d7788cd8;
        interface_1_out_0x5596d7875580;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5596d7788c60 [label="N", shape=none];
        interface_1_in_0x5596d7788cb0 [label="H", shape=none];
        interface_1_in_0x5596d78794e8 [label="H", shape=none];
        interface_1_in_0x5596d787d4d8 [label="s", shape=none];
        interface_1_in_0x5596d7875580 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5596d7788c60;
        interface_1_in_0x5596d7788cb0;
        interface_1_in_0x5596d78794e8;
        interface_1_in_0x5596d787d4d8;
        interface_1_in_0x5596d7875580;
    }
    // Op's.
    op_0x5596d7875fa0 [label="Shift"];
    op_0x5596d78794c0 [label="Unfold"];
    op_0x5596d787d480 [label="Merge"];
    op_0x5596d787f430 [label="Split"];
    // Dimension's.
    interface_1_in_0x5596d7788c60 -> interface_1_out_0x5596d7788c60 [label="N"];
    interface_1_in_0x5596d7788cb0 -> interface_1_out_0x5596d7788cb0 [label="H"];
    op_0x5596d787f430 -> interface_1_out_0x5596d7788cd8 [label="H"];
    op_0x5596d78794c0 -> interface_1_out_0x5596d7875210 [label="k_1^2"];
    interface_1_in_0x5596d7875580 -> interface_1_out_0x5596d7875580 [label="k_2*s"];
    op_0x5596d787d480 -> op_0x5596d7875fa0 [label="s*H"];
    interface_1_in_0x5596d78794e8 -> op_0x5596d78794c0 [label="H"];
    op_0x5596d78794c0 -> op_0x5596d787d480 [label="H"];
    interface_1_in_0x5596d787d4d8 -> op_0x5596d787d480 [label="s"];
    op_0x5596d7875fa0 -> op_0x5596d787f430 [label="s*H"];
    op_0x5596d787f430 -> reduce_0x7ef0e4002e58 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7ef0e4005c70 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5596d7788c60 [label="N", shape=none];
        interface_2_out_0x5596d7788cb0 [label="H", shape=none];
        interface_2_out_0x5596d78794e8 [label="H", shape=none];
        interface_2_out_0x5596d787d4d8 [label="s", shape=none];
        interface_2_out_0x5596d7875580 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        reduce_0x7ef0e4005c70;
        interface_2_out_0x5596d7788c60;
        interface_2_out_0x5596d7788cb0;
        interface_2_out_0x5596d78794e8;
        interface_2_out_0x5596d787d4d8;
        interface_2_out_0x5596d7875580;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5596d7788c60 [label="N", shape=none];
        interface_2_in_0x5596d787b9f0 [label="C_in", shape=none];
        interface_2_in_0x5596d7788cb0 [label="H", shape=none];
        interface_2_in_0x5596d78794e8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x5596d787ba08 [label="C_in", shape=none];
        interface_2_in_0x5596d787baa8 [label="s", shape=none];
        interface_2_in_0x5596d787ba58 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5596d7788c60;
        interface_2_in_0x5596d787b9f0;
        interface_2_in_0x5596d7788cb0;
        interface_2_in_0x5596d78794e8;
        interface_2_in_0x5596d787ba08;
        interface_2_in_0x5596d787baa8;
        interface_2_in_0x5596d787ba58;
    }
    // Op's.
    op_0x5596d78756f8 [label="Expand"];
    op_0x5596d7875718 [label="Expand"];
    op_0x5596d787b9d0 [label="Share"];
    op_0x5596d787ba20 [label="Share"];
    op_0x5596d787ba70 [label="Share"];
    // Dimension's.
    interface_2_in_0x5596d7788c60 -> interface_2_out_0x5596d7788c60 [label="N"];
    interface_2_in_0x5596d7788cb0 -> interface_2_out_0x5596d7788cb0 [label="H"];
    op_0x5596d787ba20 -> interface_2_out_0x5596d7875580 [label="k_2*s"];
    interface_2_in_0x5596d78794e8 -> interface_2_out_0x5596d78794e8 [label="H"];
    interface_2_in_0x5596d787b9f0 -> op_0x5596d787b9d0 [label="C_in"];
    interface_2_in_0x5596d787ba08 -> op_0x5596d787b9d0 [label="C_in"];
    op_0x5596d78756f8 -> op_0x5596d787ba20 [label="k_2*s"];
    interface_2_in_0x5596d787ba58 -> op_0x5596d787ba20 [label="k_2*s"];
    op_0x5596d7875718 -> op_0x5596d787ba70 [label="s"];
    interface_2_in_0x5596d787baa8 -> op_0x5596d787ba70 [label="s"];
    op_0x5596d787ba70 -> interface_2_out_0x5596d787d4d8 [label="s"];
    op_0x5596d787b9d0 -> reduce_0x7ef0e4005c70 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x5596d7788c60 [label="N", shape=none];
    interface_3_out_0x5596d787b9f0 [label="C_in", shape=none];
    interface_3_out_0x5596d7788cb0 [label="H", shape=none];
    interface_3_out_0x5596d78794e8 [label="H", shape=none];
}

interface_3_out_0x5596d7788c60 -> interface_2_in_0x5596d7788c60;
interface_3_out_0x5596d787b9f0 -> interface_2_in_0x5596d787b9f0;
interface_3_out_0x5596d7788cb0 -> interface_2_in_0x5596d7788cb0;
interface_3_out_0x5596d78794e8 -> interface_2_in_0x5596d78794e8;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 2";
    interface_4_out_0x5596d787ba08 [label="C_in", shape=none];
    interface_4_out_0x5596d787baa8 [label="s", shape=none];
    interface_4_out_0x5596d787ba58 [label="k_2*s", shape=none];
}

interface_4_out_0x5596d787ba08 -> interface_2_in_0x5596d787ba08;
interface_4_out_0x5596d787baa8 -> interface_2_in_0x5596d787baa8;
interface_4_out_0x5596d787ba58 -> interface_2_in_0x5596d787ba58;

interface_2_out_0x5596d7788c60 -> interface_1_in_0x5596d7788c60;
interface_2_out_0x5596d7788cb0 -> interface_1_in_0x5596d7788cb0;
interface_2_out_0x5596d78794e8 -> interface_1_in_0x5596d78794e8;
interface_2_out_0x5596d787d4d8 -> interface_1_in_0x5596d787d4d8;
interface_2_out_0x5596d7875580 -> interface_1_in_0x5596d7875580;

interface_1_out_0x5596d7788c60 -> interface_0_in_0x5596d7788c60;
interface_1_out_0x5596d7788cb0 -> interface_0_in_0x5596d7788cb0;
interface_1_out_0x5596d7875210 -> interface_0_in_0x5596d7875210;
interface_1_out_0x5596d7788cd8 -> interface_0_in_0x5596d7788cd8;
interface_1_out_0x5596d7875580 -> interface_0_in_0x5596d7875580;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x5596d7875138 [label="C_out", shape=none];
    interface_5_out_0x5596d7875228 [label="k_1^2", shape=none];
    interface_5_out_0x5596d7875598 [label="k_2*s", shape=none];
}

interface_5_out_0x5596d7875138 -> interface_0_in_0x5596d7875138;
interface_5_out_0x5596d7875228 -> interface_0_in_0x5596d7875228;
interface_5_out_0x5596d7875598 -> interface_0_in_0x5596d7875598;

{
    rank = same;
    interface_3_out_0x5596d7788c60;
    interface_3_out_0x5596d787b9f0;
    interface_3_out_0x5596d7788cb0;
    interface_3_out_0x5596d78794e8;
    interface_5_out_0x5596d7875138;
    interface_5_out_0x5596d7875228;
    interface_5_out_0x5596d7875598;
    interface_4_out_0x5596d787ba08;
    interface_4_out_0x5596d787baa8;
    interface_4_out_0x5596d787ba58;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x5596d7788c60 [label="N", shape=none];
    interface_6_in_0x5596d7788c88 [label="C_out", shape=none];
    interface_6_in_0x5596d7788cb0 [label="H", shape=none];
    interface_6_in_0x5596d7788cd8 [label="H", shape=none];
}
interface_0_out_0x5596d7788c60 -> interface_6_in_0x5596d7788c60;
interface_0_out_0x5596d7788c88 -> interface_6_in_0x5596d7788c88;
interface_0_out_0x5596d7788cb0 -> interface_6_in_0x5596d7788cb0;
interface_0_out_0x5596d7788cd8 -> interface_6_in_0x5596d7788cd8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([24, 9, 14]),
			torch.randn([24, 2, 14]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("limn, ikj -> lmnkj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfoldcb2b4caf443f161e -> [H]@Merge0bce4580e08cd69c, [k_1^2]@Share26ce4977369008e4
		t_4 = torch.reshape(t_4, (1, 112, 112, 28, ))
		t_4 = torch.nn.functional.unfold(t_4, (9, 1, ), padding=(4, 0, ))
		t_4 = torch.reshape(t_4, (1, 112, 9, 112, 2, 14, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_4 = torch.reshape(t_4, (1, 112, 9, 224, 14, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 112, 9, 112, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjnk, ijk -> limn", t_4, in_1)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([96, 9, 14]),
			torch.randn([24, 2, 14]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("limn, ikj -> lmnkj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfoldcb2b4caf443f161e -> [H]@Merge0bce4580e08cd69c, [k_1^2]@Share26ce4977369008e4
		t_4 = torch.reshape(t_4, (1, 56, 56, 28, ))
		t_4 = torch.nn.functional.unfold(t_4, (9, 1, ), padding=(4, 0, ))
		t_4 = torch.reshape(t_4, (1, 56, 9, 56, 2, 14, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_4 = torch.reshape(t_4, (1, 56, 9, 112, 14, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 56, 9, 56, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjnk, ijk -> limn", t_4, in_1)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([192, 9, 14]),
			torch.randn([48, 2, 14]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("limn, ikj -> lmnkj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfoldcb2b4caf443f161e -> [H]@Merge0bce4580e08cd69c, [k_1^2]@Share26ce4977369008e4
		t_4 = torch.reshape(t_4, (1, 56, 56, 28, ))
		t_4 = torch.nn.functional.unfold(t_4, (9, 1, ), padding=(4, 0, ))
		t_4 = torch.reshape(t_4, (1, 56, 9, 56, 2, 14, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_4 = torch.reshape(t_4, (1, 56, 9, 112, 14, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 56, 9, 56, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjnk, ijk -> limn", t_4, in_1)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([192, 9, 14]),
			torch.randn([48, 2, 14]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("limn, ikj -> lmnkj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfoldcb2b4caf443f161e -> [H]@Merge0bce4580e08cd69c, [k_1^2]@Share26ce4977369008e4
		t_4 = torch.reshape(t_4, (1, 28, 28, 28, ))
		t_4 = torch.nn.functional.unfold(t_4, (9, 1, ), padding=(4, 0, ))
		t_4 = torch.reshape(t_4, (1, 28, 9, 28, 2, 14, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_4 = torch.reshape(t_4, (1, 28, 9, 56, 14, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 28, 9, 28, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjnk, ijk -> limn", t_4, in_1)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 9, 14]),
			torch.randn([64, 2, 14]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("limn, ikj -> lmnkj", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [H]@Unfoldcb2b4caf443f161e -> [H]@Merge0bce4580e08cd69c, [k_1^2]@Share26ce4977369008e4
		t_4 = torch.reshape(t_4, (1, 28, 28, 28, ))
		t_4 = torch.nn.functional.unfold(t_4, (9, 1, ), padding=(4, 0, ))
		t_4 = torch.reshape(t_4, (1, 28, 9, 28, 2, 14, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_4 = torch.reshape(t_4, (1, 28, 9, 56, 14, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 28, 9, 28, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# Perform contraction.
		t_5 = torch.einsum("lmjnk, ijk -> limn", t_4, in_1)

		# No need to crop the output tensor.
		y = t_5

		return y

