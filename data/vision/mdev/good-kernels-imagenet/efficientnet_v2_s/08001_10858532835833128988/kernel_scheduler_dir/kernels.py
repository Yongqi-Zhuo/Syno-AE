import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f5f78003cc0 [label="Sum", shape=box];
    reduce_0x7f5f780054d0 [label="Sum", shape=box];
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
        reduce_0x7f5f78003cc0;
        reduce_0x7f5f780054d0;
        interface_0_out_0x55f1ee7b7da0;
        interface_0_out_0x55f1ee7b7dc8;
        interface_0_out_0x55f1ee7b7df0;
        interface_0_out_0x55f1ee7b7e18;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_0_in_0x55f1ee7b7df0 [label="H", shape=none];
        interface_0_in_0x55f1f89dd9c0 [label="k_1^2", shape=none];
        interface_0_in_0x55f1ee7b7e18 [label="H", shape=none];
        interface_0_in_0x55f1f89ddc40 [label="k_2*s", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x55f1f89dd938 [label="C_out", shape=none];
        interface_0_in_0x55f1f89dd9d8 [label="k_1^2", shape=none];
        interface_0_in_0x55f1f89ddc58 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55f1ee7b7da0;
        interface_0_in_0x55f1ee7b7df0;
        interface_0_in_0x55f1f89dd9c0;
        interface_0_in_0x55f1ee7b7e18;
        interface_0_in_0x55f1f89ddc40;
        interface_0_in_0x55f1f89dd938;
        interface_0_in_0x55f1f89dd9d8;
        interface_0_in_0x55f1f89ddc58;
    }
    // Op's.
    op_0x55f1f88b2978 [label="Expand"];
    op_0x55f1f89dd900 [label="Share"];
    op_0x55f1f89dd9a0 [label="Share"];
    op_0x55f1f89ddc20 [label="Share"];
    // Dimension's.
    interface_0_in_0x55f1ee7b7da0 -> interface_0_out_0x55f1ee7b7da0 [label="N"];
    op_0x55f1f89dd900 -> interface_0_out_0x55f1ee7b7dc8 [label="C_out"];
    interface_0_in_0x55f1ee7b7df0 -> interface_0_out_0x55f1ee7b7df0 [label="H"];
    interface_0_in_0x55f1ee7b7e18 -> interface_0_out_0x55f1ee7b7e18 [label="H"];
    op_0x55f1f88b2978 -> op_0x55f1f89dd900 [label="C_out"];
    interface_0_in_0x55f1f89dd938 -> op_0x55f1f89dd900 [label="C_out"];
    interface_0_in_0x55f1f89dd9c0 -> op_0x55f1f89dd9a0 [label="k_1^2"];
    interface_0_in_0x55f1f89dd9d8 -> op_0x55f1f89dd9a0 [label="k_1^2"];
    interface_0_in_0x55f1f89ddc40 -> op_0x55f1f89ddc20 [label="k_2*s"];
    interface_0_in_0x55f1f89ddc58 -> op_0x55f1f89ddc20 [label="k_2*s"];
    op_0x55f1f89dd9a0 -> reduce_0x7f5f78003cc0 [label="k_1^2"];
    op_0x55f1f89ddc20 -> reduce_0x7f5f780054d0 [label="k_2*s"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f5f78004e58 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_1_out_0x55f1ee7b7df0 [label="H", shape=none];
        interface_1_out_0x55f1f89dd9c0 [label="k_1^2", shape=none];
        interface_1_out_0x55f1ee7b7e18 [label="H", shape=none];
        interface_1_out_0x55f1f89ddc40 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5f78004e58;
        interface_1_out_0x55f1ee7b7da0;
        interface_1_out_0x55f1ee7b7df0;
        interface_1_out_0x55f1f89dd9c0;
        interface_1_out_0x55f1ee7b7e18;
        interface_1_out_0x55f1f89ddc40;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_1_in_0x55f1ee7b7df0 [label="H", shape=none];
        interface_1_in_0x55f1f88a6068 [label="H", shape=none];
        interface_1_in_0x55f1f89df308 [label="s", shape=none];
        interface_1_in_0x55f1f89ddc40 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55f1ee7b7da0;
        interface_1_in_0x55f1ee7b7df0;
        interface_1_in_0x55f1f88a6068;
        interface_1_in_0x55f1f89df308;
        interface_1_in_0x55f1f89ddc40;
    }
    // Op's.
    op_0x55f1eba3e3e0 [label="Shift"];
    op_0x55f1f88a6040 [label="Unfold"];
    op_0x55f1f89df2b0 [label="Merge"];
    op_0x55f1f89df810 [label="Split"];
    // Dimension's.
    op_0x55f1f89df2b0 -> op_0x55f1eba3e3e0 [label="s*H"];
    interface_1_in_0x55f1ee7b7da0 -> interface_1_out_0x55f1ee7b7da0 [label="N"];
    interface_1_in_0x55f1ee7b7df0 -> interface_1_out_0x55f1ee7b7df0 [label="H"];
    op_0x55f1f89df810 -> interface_1_out_0x55f1ee7b7e18 [label="H"];
    interface_1_in_0x55f1f88a6068 -> op_0x55f1f88a6040 [label="H"];
    op_0x55f1f88a6040 -> interface_1_out_0x55f1f89dd9c0 [label="k_1^2"];
    interface_1_in_0x55f1f89ddc40 -> interface_1_out_0x55f1f89ddc40 [label="k_2*s"];
    op_0x55f1f88a6040 -> op_0x55f1f89df2b0 [label="H"];
    interface_1_in_0x55f1f89df308 -> op_0x55f1f89df2b0 [label="s"];
    op_0x55f1eba3e3e0 -> op_0x55f1f89df810 [label="s*H"];
    op_0x55f1f89df810 -> reduce_0x7f5f78004e58 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f5f78007b70 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_2_out_0x55f1ee7b7df0 [label="H", shape=none];
        interface_2_out_0x55f1f88a6068 [label="H", shape=none];
        interface_2_out_0x55f1f89df308 [label="s", shape=none];
        interface_2_out_0x55f1f89ddc40 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5f78007b70;
        interface_2_out_0x55f1ee7b7da0;
        interface_2_out_0x55f1ee7b7df0;
        interface_2_out_0x55f1f88a6068;
        interface_2_out_0x55f1f89df308;
        interface_2_out_0x55f1f89ddc40;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_2_in_0x55f1f89ddce0 [label="C_in", shape=none];
        interface_2_in_0x55f1ee7b7df0 [label="H", shape=none];
        interface_2_in_0x55f1f88a6068 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x55f1f89ddcf8 [label="C_in", shape=none];
        interface_2_in_0x55f1f89ddd98 [label="s", shape=none];
        interface_2_in_0x55f1f89ddd48 [label="k_2*s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55f1ee7b7da0;
        interface_2_in_0x55f1f89ddce0;
        interface_2_in_0x55f1ee7b7df0;
        interface_2_in_0x55f1f88a6068;
        interface_2_in_0x55f1f89ddcf8;
        interface_2_in_0x55f1f89ddd98;
        interface_2_in_0x55f1f89ddd48;
    }
    // Op's.
    op_0x55f1f88b2a18 [label="Expand"];
    op_0x55f1f88b2a38 [label="Expand"];
    op_0x55f1f89ddcc0 [label="Share"];
    op_0x55f1f89ddd10 [label="Share"];
    op_0x55f1f89ddd60 [label="Share"];
    // Dimension's.
    interface_2_in_0x55f1ee7b7da0 -> interface_2_out_0x55f1ee7b7da0 [label="N"];
    interface_2_in_0x55f1ee7b7df0 -> interface_2_out_0x55f1ee7b7df0 [label="H"];
    interface_2_in_0x55f1f88a6068 -> interface_2_out_0x55f1f88a6068 [label="H"];
    op_0x55f1f89ddd10 -> interface_2_out_0x55f1f89ddc40 [label="k_2*s"];
    interface_2_in_0x55f1f89ddce0 -> op_0x55f1f89ddcc0 [label="C_in"];
    interface_2_in_0x55f1f89ddcf8 -> op_0x55f1f89ddcc0 [label="C_in"];
    op_0x55f1f88b2a18 -> op_0x55f1f89ddd10 [label="k_2*s"];
    interface_2_in_0x55f1f89ddd48 -> op_0x55f1f89ddd10 [label="k_2*s"];
    op_0x55f1f88b2a38 -> op_0x55f1f89ddd60 [label="s"];
    interface_2_in_0x55f1f89ddd98 -> op_0x55f1f89ddd60 [label="s"];
    op_0x55f1f89ddd60 -> interface_2_out_0x55f1f89df308 [label="s"];
    op_0x55f1f89ddcc0 -> reduce_0x7f5f78007b70 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x55f1ee7b7da0 [label="N", shape=none];
    interface_3_out_0x55f1f89ddce0 [label="C_in", shape=none];
    interface_3_out_0x55f1ee7b7df0 [label="H", shape=none];
    interface_3_out_0x55f1f88a6068 [label="H", shape=none];
}

interface_3_out_0x55f1ee7b7da0 -> interface_2_in_0x55f1ee7b7da0;
interface_3_out_0x55f1f89ddce0 -> interface_2_in_0x55f1f89ddce0;
interface_3_out_0x55f1ee7b7df0 -> interface_2_in_0x55f1ee7b7df0;
interface_3_out_0x55f1f88a6068 -> interface_2_in_0x55f1f88a6068;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 2";
    interface_4_out_0x55f1f89ddcf8 [label="C_in", shape=none];
    interface_4_out_0x55f1f89ddd98 [label="s", shape=none];
    interface_4_out_0x55f1f89ddd48 [label="k_2*s", shape=none];
}

interface_4_out_0x55f1f89ddcf8 -> interface_2_in_0x55f1f89ddcf8;
interface_4_out_0x55f1f89ddd98 -> interface_2_in_0x55f1f89ddd98;
interface_4_out_0x55f1f89ddd48 -> interface_2_in_0x55f1f89ddd48;

interface_2_out_0x55f1ee7b7da0 -> interface_1_in_0x55f1ee7b7da0;
interface_2_out_0x55f1ee7b7df0 -> interface_1_in_0x55f1ee7b7df0;
interface_2_out_0x55f1f88a6068 -> interface_1_in_0x55f1f88a6068;
interface_2_out_0x55f1f89df308 -> interface_1_in_0x55f1f89df308;
interface_2_out_0x55f1f89ddc40 -> interface_1_in_0x55f1f89ddc40;

interface_1_out_0x55f1ee7b7da0 -> interface_0_in_0x55f1ee7b7da0;
interface_1_out_0x55f1ee7b7df0 -> interface_0_in_0x55f1ee7b7df0;
interface_1_out_0x55f1f89dd9c0 -> interface_0_in_0x55f1f89dd9c0;
interface_1_out_0x55f1ee7b7e18 -> interface_0_in_0x55f1ee7b7e18;
interface_1_out_0x55f1f89ddc40 -> interface_0_in_0x55f1f89ddc40;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x55f1f89dd938 [label="C_out", shape=none];
    interface_5_out_0x55f1f89dd9d8 [label="k_1^2", shape=none];
    interface_5_out_0x55f1f89ddc58 [label="k_2*s", shape=none];
}

interface_5_out_0x55f1f89dd938 -> interface_0_in_0x55f1f89dd938;
interface_5_out_0x55f1f89dd9d8 -> interface_0_in_0x55f1f89dd9d8;
interface_5_out_0x55f1f89ddc58 -> interface_0_in_0x55f1f89ddc58;

{
    rank = same;
    interface_3_out_0x55f1ee7b7da0;
    interface_3_out_0x55f1f89ddce0;
    interface_3_out_0x55f1ee7b7df0;
    interface_3_out_0x55f1f88a6068;
    interface_5_out_0x55f1f89dd938;
    interface_5_out_0x55f1f89dd9d8;
    interface_5_out_0x55f1f89ddc58;
    interface_4_out_0x55f1f89ddcf8;
    interface_4_out_0x55f1f89ddd98;
    interface_4_out_0x55f1f89ddd48;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x55f1ee7b7da0 [label="N", shape=none];
    interface_6_in_0x55f1ee7b7dc8 [label="C_out", shape=none];
    interface_6_in_0x55f1ee7b7df0 [label="H", shape=none];
    interface_6_in_0x55f1ee7b7e18 [label="H", shape=none];
}
interface_0_out_0x55f1ee7b7da0 -> interface_6_in_0x55f1ee7b7da0;
interface_0_out_0x55f1ee7b7dc8 -> interface_6_in_0x55f1ee7b7dc8;
interface_0_out_0x55f1ee7b7df0 -> interface_6_in_0x55f1ee7b7df0;
interface_0_out_0x55f1ee7b7e18 -> interface_6_in_0x55f1ee7b7e18;

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

