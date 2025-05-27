import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7fc32c003cc0 [label="Sum", shape=box];
    reduce_0x7fc32c0054d0 [label="Sum", shape=box];
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
        reduce_0x7fc32c003cc0;
        reduce_0x7fc32c0054d0;
        interface_0_out_0x5604185d74e0;
        interface_0_out_0x5604185d7508;
        interface_0_out_0x5604185d7530;
        interface_0_out_0x5604185d7558;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5604185d74e0 [label="N", shape=none];
        interface_0_in_0x5604185d7530 [label="H", shape=none];
        interface_0_in_0x560419917340 [label="k_1^2", shape=none];
        interface_0_in_0x5604185d7558 [label="H", shape=none];
        interface_0_in_0x5604199175c0 [label="k_2*s", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x5604199172b8 [label="C_out", shape=none];
        interface_0_in_0x560419917358 [label="k_1^2", shape=none];
        interface_0_in_0x5604199175d8 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5604185d74e0;
        interface_0_in_0x5604185d7530;
        interface_0_in_0x560419917340;
        interface_0_in_0x5604185d7558;
        interface_0_in_0x5604199175c0;
        interface_0_in_0x5604199172b8;
        interface_0_in_0x560419917358;
        interface_0_in_0x5604199175d8;
    }
    // Op's.
    op_0x560419917280 [label="Share"];
    op_0x560419917320 [label="Share"];
    op_0x5604199175a0 [label="Share"];
    op_0x560419917758 [label="Expand"];
    // Dimension's.
    interface_0_in_0x5604185d74e0 -> interface_0_out_0x5604185d74e0 [label="N"];
    op_0x560419917280 -> interface_0_out_0x5604185d7508 [label="C_out"];
    interface_0_in_0x5604185d7530 -> interface_0_out_0x5604185d7530 [label="H"];
    interface_0_in_0x5604185d7558 -> interface_0_out_0x5604185d7558 [label="H"];
    op_0x560419917758 -> op_0x560419917280 [label="C_out"];
    interface_0_in_0x5604199172b8 -> op_0x560419917280 [label="C_out"];
    interface_0_in_0x560419917340 -> op_0x560419917320 [label="k_1^2"];
    interface_0_in_0x560419917358 -> op_0x560419917320 [label="k_1^2"];
    interface_0_in_0x5604199175c0 -> op_0x5604199175a0 [label="k_2*s"];
    interface_0_in_0x5604199175d8 -> op_0x5604199175a0 [label="k_2*s"];
    op_0x560419917320 -> reduce_0x7fc32c003cc0 [label="k_1^2"];
    op_0x5604199175a0 -> reduce_0x7fc32c0054d0 [label="k_2*s"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fc32c004e58 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5604185d74e0 [label="N", shape=none];
        interface_1_out_0x5604185d7530 [label="H", shape=none];
        interface_1_out_0x560419917340 [label="k_1^2", shape=none];
        interface_1_out_0x5604185d7558 [label="H", shape=none];
        interface_1_out_0x5604199175c0 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc32c004e58;
        interface_1_out_0x5604185d74e0;
        interface_1_out_0x5604185d7530;
        interface_1_out_0x560419917340;
        interface_1_out_0x5604185d7558;
        interface_1_out_0x5604199175c0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5604185d74e0 [label="N", shape=none];
        interface_1_in_0x5604185d7530 [label="H", shape=none];
        interface_1_in_0x5604199199e8 [label="H", shape=none];
        interface_1_in_0x560419919888 [label="s", shape=none];
        interface_1_in_0x5604199175c0 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5604185d74e0;
        interface_1_in_0x5604185d7530;
        interface_1_in_0x5604199199e8;
        interface_1_in_0x560419919888;
        interface_1_in_0x5604199175c0;
    }
    // Op's.
    op_0x560419917fe0 [label="Shift"];
    op_0x560419919830 [label="Merge"];
    op_0x5604199199c0 [label="Unfold"];
    op_0x56041991a190 [label="Split"];
    // Dimension's.
    interface_1_in_0x5604185d74e0 -> interface_1_out_0x5604185d74e0 [label="N"];
    interface_1_in_0x5604185d7530 -> interface_1_out_0x5604185d7530 [label="H"];
    op_0x56041991a190 -> interface_1_out_0x5604185d7558 [label="H"];
    op_0x5604199199c0 -> interface_1_out_0x560419917340 [label="k_1^2"];
    interface_1_in_0x5604199175c0 -> interface_1_out_0x5604199175c0 [label="k_2*s"];
    op_0x560419919830 -> op_0x560419917fe0 [label="s*H"];
    op_0x5604199199c0 -> op_0x560419919830 [label="H"];
    interface_1_in_0x560419919888 -> op_0x560419919830 [label="s"];
    interface_1_in_0x5604199199e8 -> op_0x5604199199c0 [label="H"];
    op_0x560419917fe0 -> op_0x56041991a190 [label="s*H"];
    op_0x56041991a190 -> reduce_0x7fc32c004e58 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7fc32c007b70 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5604185d74e0 [label="N", shape=none];
        interface_2_out_0x5604185d7530 [label="H", shape=none];
        interface_2_out_0x5604199199e8 [label="H", shape=none];
        interface_2_out_0x560419919888 [label="s", shape=none];
        interface_2_out_0x5604199175c0 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc32c007b70;
        interface_2_out_0x5604185d74e0;
        interface_2_out_0x5604185d7530;
        interface_2_out_0x5604199199e8;
        interface_2_out_0x560419919888;
        interface_2_out_0x5604199175c0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5604185d74e0 [label="N", shape=none];
        interface_2_in_0x560419917660 [label="C_in", shape=none];
        interface_2_in_0x5604185d7530 [label="H", shape=none];
        interface_2_in_0x5604199199e8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x560419917678 [label="C_in", shape=none];
        interface_2_in_0x560419917718 [label="s", shape=none];
        interface_2_in_0x5604199176c8 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5604185d74e0;
        interface_2_in_0x560419917660;
        interface_2_in_0x5604185d7530;
        interface_2_in_0x5604199199e8;
        interface_2_in_0x560419917678;
        interface_2_in_0x560419917718;
        interface_2_in_0x5604199176c8;
    }
    // Op's.
    op_0x560419917640 [label="Share"];
    op_0x560419917690 [label="Share"];
    op_0x5604199176e0 [label="Share"];
    op_0x5604199177f8 [label="Expand"];
    op_0x560419917818 [label="Expand"];
    // Dimension's.
    interface_2_in_0x5604185d74e0 -> interface_2_out_0x5604185d74e0 [label="N"];
    interface_2_in_0x5604185d7530 -> interface_2_out_0x5604185d7530 [label="H"];
    op_0x560419917690 -> interface_2_out_0x5604199175c0 [label="k_2*s"];
    interface_2_in_0x560419917660 -> op_0x560419917640 [label="C_in"];
    interface_2_in_0x560419917678 -> op_0x560419917640 [label="C_in"];
    op_0x5604199177f8 -> op_0x560419917690 [label="k_2*s"];
    interface_2_in_0x5604199176c8 -> op_0x560419917690 [label="k_2*s"];
    op_0x560419917818 -> op_0x5604199176e0 [label="s"];
    interface_2_in_0x560419917718 -> op_0x5604199176e0 [label="s"];
    op_0x5604199176e0 -> interface_2_out_0x560419919888 [label="s"];
    interface_2_in_0x5604199199e8 -> interface_2_out_0x5604199199e8 [label="H"];
    op_0x560419917640 -> reduce_0x7fc32c007b70 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x5604185d74e0 [label="N", shape=none];
    interface_3_out_0x560419917660 [label="C_in", shape=none];
    interface_3_out_0x5604185d7530 [label="H", shape=none];
    interface_3_out_0x5604199199e8 [label="H", shape=none];
}

interface_3_out_0x5604185d74e0 -> interface_2_in_0x5604185d74e0;
interface_3_out_0x560419917660 -> interface_2_in_0x560419917660;
interface_3_out_0x5604185d7530 -> interface_2_in_0x5604185d7530;
interface_3_out_0x5604199199e8 -> interface_2_in_0x5604199199e8;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 2";
    interface_4_out_0x560419917678 [label="C_in", shape=none];
    interface_4_out_0x560419917718 [label="s", shape=none];
    interface_4_out_0x5604199176c8 [label="k_2*s", shape=none];
}

interface_4_out_0x560419917678 -> interface_2_in_0x560419917678;
interface_4_out_0x560419917718 -> interface_2_in_0x560419917718;
interface_4_out_0x5604199176c8 -> interface_2_in_0x5604199176c8;

interface_2_out_0x5604185d74e0 -> interface_1_in_0x5604185d74e0;
interface_2_out_0x5604185d7530 -> interface_1_in_0x5604185d7530;
interface_2_out_0x5604199199e8 -> interface_1_in_0x5604199199e8;
interface_2_out_0x560419919888 -> interface_1_in_0x560419919888;
interface_2_out_0x5604199175c0 -> interface_1_in_0x5604199175c0;

interface_1_out_0x5604185d74e0 -> interface_0_in_0x5604185d74e0;
interface_1_out_0x5604185d7530 -> interface_0_in_0x5604185d7530;
interface_1_out_0x560419917340 -> interface_0_in_0x560419917340;
interface_1_out_0x5604185d7558 -> interface_0_in_0x5604185d7558;
interface_1_out_0x5604199175c0 -> interface_0_in_0x5604199175c0;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x5604199172b8 [label="C_out", shape=none];
    interface_5_out_0x560419917358 [label="k_1^2", shape=none];
    interface_5_out_0x5604199175d8 [label="k_2*s", shape=none];
}

interface_5_out_0x5604199172b8 -> interface_0_in_0x5604199172b8;
interface_5_out_0x560419917358 -> interface_0_in_0x560419917358;
interface_5_out_0x5604199175d8 -> interface_0_in_0x5604199175d8;

{
    rank = same;
    interface_3_out_0x5604185d74e0;
    interface_3_out_0x560419917660;
    interface_3_out_0x5604185d7530;
    interface_3_out_0x5604199199e8;
    interface_5_out_0x5604199172b8;
    interface_5_out_0x560419917358;
    interface_5_out_0x5604199175d8;
    interface_4_out_0x560419917678;
    interface_4_out_0x560419917718;
    interface_4_out_0x5604199176c8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x5604185d74e0 [label="N", shape=none];
    interface_6_in_0x5604185d7508 [label="C_out", shape=none];
    interface_6_in_0x5604185d7530 [label="H", shape=none];
    interface_6_in_0x5604185d7558 [label="H", shape=none];
}
interface_0_out_0x5604185d74e0 -> interface_6_in_0x5604185d74e0;
interface_0_out_0x5604185d7508 -> interface_6_in_0x5604185d7508;
interface_0_out_0x5604185d7530 -> interface_6_in_0x5604185d7530;
interface_0_out_0x5604185d7558 -> interface_6_in_0x5604185d7558;

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

