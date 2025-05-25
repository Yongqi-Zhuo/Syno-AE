import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f6a88001a98 [label="Sum", shape=box];
    reduce_0x7f6a88001ab0 [label="Sum", shape=box];
    reduce_0x7f6a88005640 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x562957621960 [label="N", shape=none];
        interface_0_out_0x562957621988 [label="C_out", shape=none];
        interface_0_out_0x5629576219b0 [label="H", shape=none];
        interface_0_out_0x5629576219d8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f6a88001a98;
        reduce_0x7f6a88001ab0;
        reduce_0x7f6a88005640;
        interface_0_out_0x562957621960;
        interface_0_out_0x562957621988;
        interface_0_out_0x5629576219b0;
        interface_0_out_0x5629576219d8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x562957621960 [label="N", shape=none];
        interface_0_in_0x56295612ed90 [label="k_1", shape=none];
        interface_0_in_0x5629576219b0 [label="H", shape=none];
        interface_0_in_0x56295612ede0 [label="k_1", shape=none];
        interface_0_in_0x5629576219d8 [label="H", shape=none];
        interface_0_in_0x56295612ecf0 [label="s^-1*C_in", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x56295612ecb8 [label="C_out", shape=none];
        interface_0_in_0x56295612eda8 [label="k_1", shape=none];
        interface_0_in_0x56295612edf8 [label="k_1", shape=none];
        interface_0_in_0x56295612ed08 [label="s^-1*C_in", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x562957621960;
        interface_0_in_0x56295612ed90;
        interface_0_in_0x5629576219b0;
        interface_0_in_0x56295612ede0;
        interface_0_in_0x5629576219d8;
        interface_0_in_0x56295612ecf0;
        interface_0_in_0x56295612ecb8;
        interface_0_in_0x56295612eda8;
        interface_0_in_0x56295612edf8;
        interface_0_in_0x56295612ed08;
    }
    // Op's.
    op_0x56295611e1b8 [label="Expand"];
    op_0x56295612ec80 [label="Share"];
    op_0x56295612ecd0 [label="Share"];
    op_0x56295612ed70 [label="Share"];
    op_0x56295612edc0 [label="Share"];
    // Dimension's.
    op_0x56295611e1b8 -> op_0x56295612ec80 [label="C_out"];
    interface_0_in_0x56295612ecb8 -> op_0x56295612ec80 [label="C_out"];
    interface_0_in_0x56295612ecf0 -> op_0x56295612ecd0 [label="s^-1*C_in"];
    interface_0_in_0x56295612ed08 -> op_0x56295612ecd0 [label="s^-1*C_in"];
    interface_0_in_0x56295612ed90 -> op_0x56295612ed70 [label="k_1"];
    interface_0_in_0x56295612eda8 -> op_0x56295612ed70 [label="k_1"];
    interface_0_in_0x56295612ede0 -> op_0x56295612edc0 [label="k_1"];
    interface_0_in_0x56295612edf8 -> op_0x56295612edc0 [label="k_1"];
    interface_0_in_0x562957621960 -> interface_0_out_0x562957621960 [label="N"];
    op_0x56295612ec80 -> interface_0_out_0x562957621988 [label="C_out"];
    interface_0_in_0x5629576219b0 -> interface_0_out_0x5629576219b0 [label="H"];
    interface_0_in_0x5629576219d8 -> interface_0_out_0x5629576219d8 [label="H"];
    op_0x56295612ed70 -> reduce_0x7f6a88001a98 [label="k_1"];
    op_0x56295612edc0 -> reduce_0x7f6a88001ab0 [label="k_1"];
    op_0x56295612ecd0 -> reduce_0x7f6a88005640 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x562957621960 [label="N", shape=none];
        interface_1_out_0x56295612ed90 [label="k_1", shape=none];
        interface_1_out_0x5629576219b0 [label="H", shape=none];
        interface_1_out_0x56295612ede0 [label="k_1", shape=none];
        interface_1_out_0x5629576219d8 [label="H", shape=none];
        interface_1_out_0x56295612ecf0 [label="s^-1*C_in", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x562957621960;
        interface_1_out_0x56295612ed90;
        interface_1_out_0x5629576219b0;
        interface_1_out_0x56295612ede0;
        interface_1_out_0x5629576219d8;
        interface_1_out_0x56295612ecf0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x562957621960 [label="N", shape=none];
        interface_1_in_0x5629571d1ca8 [label="H", shape=none];
        interface_1_in_0x56295612ede0 [label="k_1", shape=none];
        interface_1_in_0x5629576219d8 [label="H", shape=none];
        interface_1_in_0x56295612ecf0 [label="s^-1*C_in", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x562957621960;
        interface_1_in_0x5629571d1ca8;
        interface_1_in_0x56295612ede0;
        interface_1_in_0x5629576219d8;
        interface_1_in_0x56295612ecf0;
    }
    // Op's.
    op_0x5629571d1c80 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x56295612ecf0 -> interface_1_out_0x56295612ecf0 [label="s^-1*C_in"];
    op_0x5629571d1c80 -> interface_1_out_0x56295612ed90 [label="k_1"];
    interface_1_in_0x56295612ede0 -> interface_1_out_0x56295612ede0 [label="k_1"];
    interface_1_in_0x5629571d1ca8 -> op_0x5629571d1c80 [label="H"];
    interface_1_in_0x562957621960 -> interface_1_out_0x562957621960 [label="N"];
    op_0x5629571d1c80 -> interface_1_out_0x5629576219b0 [label="H"];
    interface_1_in_0x5629576219d8 -> interface_1_out_0x5629576219d8 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f6a88002ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x562957621960 [label="N", shape=none];
        interface_2_out_0x5629571d1ca8 [label="H", shape=none];
        interface_2_out_0x56295612ede0 [label="k_1", shape=none];
        interface_2_out_0x5629576219d8 [label="H", shape=none];
        interface_2_out_0x56295612ecf0 [label="s^-1*C_in", shape=none];
    }
    {
        rank = same;
        reduce_0x7f6a88002ce8;
        interface_2_out_0x562957621960;
        interface_2_out_0x5629571d1ca8;
        interface_2_out_0x56295612ede0;
        interface_2_out_0x5629576219d8;
        interface_2_out_0x56295612ecf0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x562957621960 [label="N", shape=none];
        interface_2_in_0x5629571d11d0 [label="C_in", shape=none];
        interface_2_in_0x5629571d1ca8 [label="H", shape=none];
        interface_2_in_0x562956166b50 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x562957621960;
        interface_2_in_0x5629571d11d0;
        interface_2_in_0x5629571d1ca8;
        interface_2_in_0x562956166b50;
    }
    // Op's.
    op_0x562956166aa0 [label="Shift"];
    op_0x562956166b30 [label="Shift"];
    op_0x5629561674d0 [label="Split"];
    op_0x5629571cfb30 [label="Merge"];
    op_0x5629571d1190 [label="Split"];
    op_0x5629571d1bc0 [label="Unfold"];
    // Dimension's.
    op_0x5629571d1190 -> interface_2_out_0x56295612ecf0 [label="s^-1*C_in"];
    op_0x5629571d1bc0 -> interface_2_out_0x56295612ede0 [label="k_1"];
    op_0x5629571cfb30 -> op_0x562956166aa0 [label="s*H"];
    interface_2_in_0x562956166b50 -> op_0x562956166b30 [label="H"];
    op_0x562956166aa0 -> op_0x5629561674d0 [label="s*H"];
    op_0x5629571d1bc0 -> op_0x5629571cfb30 [label="H"];
    op_0x5629571d1190 -> op_0x5629571cfb30 [label="s"];
    interface_2_in_0x5629571d11d0 -> op_0x5629571d1190 [label="C_in"];
    op_0x562956166b30 -> op_0x5629571d1bc0 [label="H"];
    interface_2_in_0x5629571d1ca8 -> interface_2_out_0x5629571d1ca8 [label="H"];
    interface_2_in_0x562957621960 -> interface_2_out_0x562957621960 [label="N"];
    op_0x5629561674d0 -> interface_2_out_0x5629576219d8 [label="H"];
    op_0x5629561674d0 -> reduce_0x7f6a88002ce8 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x562957621960 [label="N", shape=none];
    interface_3_out_0x5629571d11d0 [label="C_in", shape=none];
    interface_3_out_0x5629571d1ca8 [label="H", shape=none];
    interface_3_out_0x562956166b50 [label="H", shape=none];
}

interface_3_out_0x562957621960 -> interface_2_in_0x562957621960;
interface_3_out_0x5629571d11d0 -> interface_2_in_0x5629571d11d0;
interface_3_out_0x5629571d1ca8 -> interface_2_in_0x5629571d1ca8;
interface_3_out_0x562956166b50 -> interface_2_in_0x562956166b50;

interface_2_out_0x562957621960 -> interface_1_in_0x562957621960;
interface_2_out_0x5629571d1ca8 -> interface_1_in_0x5629571d1ca8;
interface_2_out_0x56295612ede0 -> interface_1_in_0x56295612ede0;
interface_2_out_0x5629576219d8 -> interface_1_in_0x5629576219d8;
interface_2_out_0x56295612ecf0 -> interface_1_in_0x56295612ecf0;

interface_1_out_0x562957621960 -> interface_0_in_0x562957621960;
interface_1_out_0x56295612ed90 -> interface_0_in_0x56295612ed90;
interface_1_out_0x5629576219b0 -> interface_0_in_0x5629576219b0;
interface_1_out_0x56295612ede0 -> interface_0_in_0x56295612ede0;
interface_1_out_0x5629576219d8 -> interface_0_in_0x5629576219d8;
interface_1_out_0x56295612ecf0 -> interface_0_in_0x56295612ecf0;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x56295612ecb8 [label="C_out", shape=none];
    interface_4_out_0x56295612eda8 [label="k_1", shape=none];
    interface_4_out_0x56295612edf8 [label="k_1", shape=none];
    interface_4_out_0x56295612ed08 [label="s^-1*C_in", shape=none];
}

interface_4_out_0x56295612ecb8 -> interface_0_in_0x56295612ecb8;
interface_4_out_0x56295612eda8 -> interface_0_in_0x56295612eda8;
interface_4_out_0x56295612edf8 -> interface_0_in_0x56295612edf8;
interface_4_out_0x56295612ed08 -> interface_0_in_0x56295612ed08;

{
    rank = same;
    interface_3_out_0x562957621960;
    interface_3_out_0x5629571d11d0;
    interface_3_out_0x5629571d1ca8;
    interface_3_out_0x562956166b50;
    interface_4_out_0x56295612ecb8;
    interface_4_out_0x56295612eda8;
    interface_4_out_0x56295612edf8;
    interface_4_out_0x56295612ed08;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x562957621960 [label="N", shape=none];
    interface_5_in_0x562957621988 [label="C_out", shape=none];
    interface_5_in_0x5629576219b0 [label="H", shape=none];
    interface_5_in_0x5629576219d8 [label="H", shape=none];
}
interface_0_out_0x562957621960 -> interface_5_in_0x562957621960;
interface_0_out_0x562957621988 -> interface_5_in_0x562957621988;
interface_0_out_0x5629576219b0 -> interface_5_in_0x5629576219b0;
interface_0_out_0x5629576219d8 -> interface_5_in_0x5629576219d8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 3, 3, 32]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ljki -> lkij", in_0)

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 56, 56, 64, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 56, 3, 56, 64, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 56, 3, 56, 2, 32, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.reshape(t_2, (1024, 56, 3, 112, 32, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 56, 3, 56, 2, 32, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(4, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 1, 56, 5376, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 56, 3, 56, 32, ))

		# Perform contraction.
		t_4 = torch.einsum("mknloj, iklj -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 3, 32]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ljki -> lkij", in_0)

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 28, 28, 64, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 28, 3, 28, 64, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 28, 3, 28, 2, 32, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.reshape(t_2, (1024, 28, 3, 56, 32, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 28, 3, 28, 2, 32, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(4, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 1, 28, 2688, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 28, 3, 28, 32, ))

		# Perform contraction.
		t_4 = torch.einsum("mknloj, iklj -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 3, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ljki -> lkij", in_0)

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 28, 28, 128, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 28, 3, 28, 128, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 28, 3, 28, 2, 64, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.reshape(t_2, (1024, 28, 3, 56, 64, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 28, 3, 28, 2, 64, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(4, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 1, 28, 5376, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 28, 3, 28, 64, ))

		# Perform contraction.
		t_4 = torch.einsum("mknloj, iklj -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 3, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ljki -> lkij", in_0)

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 14, 14, 128, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 14, 3, 14, 128, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 14, 3, 14, 2, 64, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.reshape(t_2, (1024, 14, 3, 28, 64, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 14, 3, 14, 2, 64, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(4, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 1, 14, 2688, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 14, 3, 14, 64, ))

		# Perform contraction.
		t_4 = torch.einsum("mknloj, iklj -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ljki -> lkij", in_0)

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 14, 14, 256, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 14, 3, 14, 256, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 14, 3, 14, 2, 128, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.reshape(t_2, (1024, 14, 3, 28, 128, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 14, 3, 14, 2, 128, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(4, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 1, 14, 5376, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 14, 3, 14, 128, ))

		# Perform contraction.
		t_4 = torch.einsum("mknloj, iklj -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 3, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ljki -> lkij", in_0)

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 7, 7, 256, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 7, 3, 7, 256, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 7, 3, 7, 2, 128, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.reshape(t_2, (1024, 7, 3, 14, 128, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 7, 3, 7, 2, 128, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(4, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 1, 7, 2688, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 7, 3, 7, 128, ))

		# Perform contraction.
		t_4 = torch.einsum("mknloj, iklj -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 3, 3, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ljki -> lkij", in_0)

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1024, 7, 7, 512, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1024, 7, 3, 7, 512, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1024, 7, 3, 7, 2, 256, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.reshape(t_2, (1024, 7, 3, 14, 256, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1024, 7, 3, 7, 2, 256, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(4, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1024, 1, 7, 5376, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 3, 7, 3, 7, 256, ))

		# Perform contraction.
		t_4 = torch.einsum("mknloj, iklj -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

