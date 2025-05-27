import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f8754003a98 [label="Sum", shape=box];
    reduce_0x7f8754003ab0 [label="Sum", shape=box];
    reduce_0x7f8754007440 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x55dcca2d4a60 [label="N", shape=none];
        interface_0_out_0x55dcca2d4a88 [label="C_out", shape=none];
        interface_0_out_0x55dcca2d4ab0 [label="H", shape=none];
        interface_0_out_0x55dcca2d4ad8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f8754003a98;
        reduce_0x7f8754003ab0;
        reduce_0x7f8754007440;
        interface_0_out_0x55dcca2d4a60;
        interface_0_out_0x55dcca2d4a88;
        interface_0_out_0x55dcca2d4ab0;
        interface_0_out_0x55dcca2d4ad8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55dcca2d4a60 [label="N", shape=none];
        interface_0_in_0x55dcd9672b10 [label="k_1", shape=none];
        interface_0_in_0x55dcca2d4ab0 [label="H", shape=none];
        interface_0_in_0x55dcd9672d40 [label="k_1", shape=none];
        interface_0_in_0x55dcca2d4ad8 [label="H", shape=none];
        interface_0_in_0x55dcd9672cf0 [label="s^-1*C_in", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x55dcd9672a38 [label="C_out", shape=none];
        interface_0_in_0x55dcd9672b28 [label="k_1", shape=none];
        interface_0_in_0x55dcd9672d58 [label="k_1", shape=none];
        interface_0_in_0x55dcd9672d08 [label="s^-1*C_in", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55dcca2d4a60;
        interface_0_in_0x55dcd9672b10;
        interface_0_in_0x55dcca2d4ab0;
        interface_0_in_0x55dcd9672d40;
        interface_0_in_0x55dcca2d4ad8;
        interface_0_in_0x55dcd9672cf0;
        interface_0_in_0x55dcd9672a38;
        interface_0_in_0x55dcd9672b28;
        interface_0_in_0x55dcd9672d58;
        interface_0_in_0x55dcd9672d08;
    }
    // Op's.
    op_0x55dcd9672a00 [label="Share"];
    op_0x55dcd9672af0 [label="Share"];
    op_0x55dcd9672cd0 [label="Share"];
    op_0x55dcd9672d20 [label="Share"];
    op_0x55dcd9672ed8 [label="Expand"];
    // Dimension's.
    interface_0_in_0x55dcca2d4a60 -> interface_0_out_0x55dcca2d4a60 [label="N"];
    op_0x55dcd9672a00 -> interface_0_out_0x55dcca2d4a88 [label="C_out"];
    interface_0_in_0x55dcca2d4ab0 -> interface_0_out_0x55dcca2d4ab0 [label="H"];
    interface_0_in_0x55dcca2d4ad8 -> interface_0_out_0x55dcca2d4ad8 [label="H"];
    op_0x55dcd9672ed8 -> op_0x55dcd9672a00 [label="C_out"];
    interface_0_in_0x55dcd9672a38 -> op_0x55dcd9672a00 [label="C_out"];
    interface_0_in_0x55dcd9672b10 -> op_0x55dcd9672af0 [label="k_1"];
    interface_0_in_0x55dcd9672b28 -> op_0x55dcd9672af0 [label="k_1"];
    interface_0_in_0x55dcd9672cf0 -> op_0x55dcd9672cd0 [label="s^-1*C_in"];
    interface_0_in_0x55dcd9672d08 -> op_0x55dcd9672cd0 [label="s^-1*C_in"];
    interface_0_in_0x55dcd9672d40 -> op_0x55dcd9672d20 [label="k_1"];
    interface_0_in_0x55dcd9672d58 -> op_0x55dcd9672d20 [label="k_1"];
    op_0x55dcd9672af0 -> reduce_0x7f8754003a98 [label="k_1"];
    op_0x55dcd9672d20 -> reduce_0x7f8754003ab0 [label="k_1"];
    op_0x55dcd9672cd0 -> reduce_0x7f8754007440 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55dcca2d4a60 [label="N", shape=none];
        interface_1_out_0x55dcd9672b10 [label="k_1", shape=none];
        interface_1_out_0x55dcca2d4ab0 [label="H", shape=none];
        interface_1_out_0x55dcd9672d40 [label="k_1", shape=none];
        interface_1_out_0x55dcca2d4ad8 [label="H", shape=none];
        interface_1_out_0x55dcd9672cf0 [label="s^-1*C_in", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x55dcca2d4a60;
        interface_1_out_0x55dcd9672b10;
        interface_1_out_0x55dcca2d4ab0;
        interface_1_out_0x55dcd9672d40;
        interface_1_out_0x55dcca2d4ad8;
        interface_1_out_0x55dcd9672cf0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55dcca2d4a60 [label="N", shape=none];
        interface_1_in_0x55dcd96807a8 [label="H", shape=none];
        interface_1_in_0x55dcd9672d40 [label="k_1", shape=none];
        interface_1_in_0x55dcca2d4ad8 [label="H", shape=none];
        interface_1_in_0x55dcd9672cf0 [label="s^-1*C_in", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55dcca2d4a60;
        interface_1_in_0x55dcd96807a8;
        interface_1_in_0x55dcd9672d40;
        interface_1_in_0x55dcca2d4ad8;
        interface_1_in_0x55dcd9672cf0;
    }
    // Op's.
    op_0x55dcd9680780 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x55dcca2d4a60 -> interface_1_out_0x55dcca2d4a60 [label="N"];
    op_0x55dcd9680780 -> interface_1_out_0x55dcca2d4ab0 [label="H"];
    interface_1_in_0x55dcca2d4ad8 -> interface_1_out_0x55dcca2d4ad8 [label="H"];
    op_0x55dcd9680780 -> interface_1_out_0x55dcd9672b10 [label="k_1"];
    interface_1_in_0x55dcd9672cf0 -> interface_1_out_0x55dcd9672cf0 [label="s^-1*C_in"];
    interface_1_in_0x55dcd9672d40 -> interface_1_out_0x55dcd9672d40 [label="k_1"];
    interface_1_in_0x55dcd96807a8 -> op_0x55dcd9680780 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f8754004ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55dcca2d4a60 [label="N", shape=none];
        interface_2_out_0x55dcd96807a8 [label="H", shape=none];
        interface_2_out_0x55dcd9672d40 [label="k_1", shape=none];
        interface_2_out_0x55dcca2d4ad8 [label="H", shape=none];
        interface_2_out_0x55dcd9672cf0 [label="s^-1*C_in", shape=none];
    }
    {
        rank = same;
        reduce_0x7f8754004ce8;
        interface_2_out_0x55dcca2d4a60;
        interface_2_out_0x55dcd96807a8;
        interface_2_out_0x55dcd9672d40;
        interface_2_out_0x55dcca2d4ad8;
        interface_2_out_0x55dcd9672cf0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55dcca2d4a60 [label="N", shape=none];
        interface_2_in_0x55dcd9693f50 [label="C_in", shape=none];
        interface_2_in_0x55dcd96807a8 [label="H", shape=none];
        interface_2_in_0x55dcca86de70 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55dcca2d4a60;
        interface_2_in_0x55dcd9693f50;
        interface_2_in_0x55dcd96807a8;
        interface_2_in_0x55dcca86de70;
    }
    // Op's.
    op_0x55dcca86ddc0 [label="Shift"];
    op_0x55dcca86de50 [label="Shift"];
    op_0x55dcd9673c00 [label="Split"];
    op_0x55dcd9674df0 [label="Merge"];
    op_0x55dcd96806c0 [label="Unfold"];
    op_0x55dcd9693f10 [label="Split"];
    // Dimension's.
    interface_2_in_0x55dcca2d4a60 -> interface_2_out_0x55dcca2d4a60 [label="N"];
    op_0x55dcd9673c00 -> interface_2_out_0x55dcca2d4ad8 [label="H"];
    op_0x55dcd9674df0 -> op_0x55dcca86ddc0 [label="s*H"];
    interface_2_in_0x55dcca86de70 -> op_0x55dcca86de50 [label="H"];
    op_0x55dcd9693f10 -> interface_2_out_0x55dcd9672cf0 [label="s^-1*C_in"];
    op_0x55dcd96806c0 -> interface_2_out_0x55dcd9672d40 [label="k_1"];
    op_0x55dcca86ddc0 -> op_0x55dcd9673c00 [label="s*H"];
    op_0x55dcd96806c0 -> op_0x55dcd9674df0 [label="H"];
    op_0x55dcd9693f10 -> op_0x55dcd9674df0 [label="s"];
    op_0x55dcca86de50 -> op_0x55dcd96806c0 [label="H"];
    interface_2_in_0x55dcd96807a8 -> interface_2_out_0x55dcd96807a8 [label="H"];
    interface_2_in_0x55dcd9693f50 -> op_0x55dcd9693f10 [label="C_in"];
    op_0x55dcd9673c00 -> reduce_0x7f8754004ce8 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x55dcca2d4a60 [label="N", shape=none];
    interface_3_out_0x55dcd9693f50 [label="C_in", shape=none];
    interface_3_out_0x55dcd96807a8 [label="H", shape=none];
    interface_3_out_0x55dcca86de70 [label="H", shape=none];
}

interface_3_out_0x55dcca2d4a60 -> interface_2_in_0x55dcca2d4a60;
interface_3_out_0x55dcd9693f50 -> interface_2_in_0x55dcd9693f50;
interface_3_out_0x55dcd96807a8 -> interface_2_in_0x55dcd96807a8;
interface_3_out_0x55dcca86de70 -> interface_2_in_0x55dcca86de70;

interface_2_out_0x55dcca2d4a60 -> interface_1_in_0x55dcca2d4a60;
interface_2_out_0x55dcd96807a8 -> interface_1_in_0x55dcd96807a8;
interface_2_out_0x55dcd9672d40 -> interface_1_in_0x55dcd9672d40;
interface_2_out_0x55dcca2d4ad8 -> interface_1_in_0x55dcca2d4ad8;
interface_2_out_0x55dcd9672cf0 -> interface_1_in_0x55dcd9672cf0;

interface_1_out_0x55dcca2d4a60 -> interface_0_in_0x55dcca2d4a60;
interface_1_out_0x55dcd9672b10 -> interface_0_in_0x55dcd9672b10;
interface_1_out_0x55dcca2d4ab0 -> interface_0_in_0x55dcca2d4ab0;
interface_1_out_0x55dcd9672d40 -> interface_0_in_0x55dcd9672d40;
interface_1_out_0x55dcca2d4ad8 -> interface_0_in_0x55dcca2d4ad8;
interface_1_out_0x55dcd9672cf0 -> interface_0_in_0x55dcd9672cf0;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x55dcd9672a38 [label="C_out", shape=none];
    interface_4_out_0x55dcd9672b28 [label="k_1", shape=none];
    interface_4_out_0x55dcd9672d58 [label="k_1", shape=none];
    interface_4_out_0x55dcd9672d08 [label="s^-1*C_in", shape=none];
}

interface_4_out_0x55dcd9672a38 -> interface_0_in_0x55dcd9672a38;
interface_4_out_0x55dcd9672b28 -> interface_0_in_0x55dcd9672b28;
interface_4_out_0x55dcd9672d58 -> interface_0_in_0x55dcd9672d58;
interface_4_out_0x55dcd9672d08 -> interface_0_in_0x55dcd9672d08;

{
    rank = same;
    interface_3_out_0x55dcca2d4a60;
    interface_3_out_0x55dcd9693f50;
    interface_3_out_0x55dcd96807a8;
    interface_3_out_0x55dcca86de70;
    interface_4_out_0x55dcd9672a38;
    interface_4_out_0x55dcd9672b28;
    interface_4_out_0x55dcd9672d58;
    interface_4_out_0x55dcd9672d08;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x55dcca2d4a60 [label="N", shape=none];
    interface_5_in_0x55dcca2d4a88 [label="C_out", shape=none];
    interface_5_in_0x55dcca2d4ab0 [label="H", shape=none];
    interface_5_in_0x55dcca2d4ad8 [label="H", shape=none];
}
interface_0_out_0x55dcca2d4a60 -> interface_5_in_0x55dcca2d4a60;
interface_0_out_0x55dcca2d4a88 -> interface_5_in_0x55dcca2d4a88;
interface_0_out_0x55dcca2d4ab0 -> interface_5_in_0x55dcca2d4ab0;
interface_0_out_0x55dcca2d4ad8 -> interface_5_in_0x55dcca2d4ad8;

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
		t_2 = torch.einsum("ilkj -> ikjl", in_0)

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1, 56, 56, 64, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 56, 3, 56, 64, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 56, 3, 56, 2, 32, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.reshape(t_2, (1, 56, 3, 112, 32, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1, 56, 3, 56, 2, 32, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(4, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 1, 56, 5376, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 56, 3, 56, 32, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnlok, ijlk -> mino", t_3, in_1)

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
		t_2 = torch.einsum("ilkj -> ikjl", in_0)

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1, 28, 28, 64, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 28, 3, 28, 64, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 28, 3, 28, 2, 32, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.reshape(t_2, (1, 28, 3, 56, 32, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1, 28, 3, 28, 2, 32, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(4, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 1, 28, 2688, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 28, 3, 28, 32, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnlok, ijlk -> mino", t_3, in_1)

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
		t_2 = torch.einsum("ilkj -> ikjl", in_0)

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1, 28, 28, 128, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 28, 3, 28, 128, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 28, 3, 28, 2, 64, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.reshape(t_2, (1, 28, 3, 56, 64, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1, 28, 3, 28, 2, 64, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(4, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 1, 28, 5376, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 28, 3, 28, 64, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnlok, ijlk -> mino", t_3, in_1)

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
		t_2 = torch.einsum("ilkj -> ikjl", in_0)

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1, 14, 14, 128, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 14, 3, 14, 128, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 14, 3, 14, 2, 64, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.reshape(t_2, (1, 14, 3, 28, 64, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1, 14, 3, 14, 2, 64, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(4, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 1, 14, 2688, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 14, 3, 14, 64, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnlok, ijlk -> mino", t_3, in_1)

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
		t_2 = torch.einsum("ilkj -> ikjl", in_0)

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1, 14, 14, 256, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 14, 3, 14, 256, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 14, 3, 14, 2, 128, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.reshape(t_2, (1, 14, 3, 28, 128, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1, 14, 3, 14, 2, 128, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(4, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 1, 14, 5376, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 14, 3, 14, 128, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnlok, ijlk -> mino", t_3, in_1)

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
		t_2 = torch.einsum("ilkj -> ikjl", in_0)

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1, 7, 7, 256, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 7, 3, 7, 256, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 7, 3, 7, 2, 128, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.reshape(t_2, (1, 7, 3, 14, 128, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1, 7, 3, 7, 2, 128, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(4, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 1, 7, 2688, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 7, 3, 7, 128, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnlok, ijlk -> mino", t_3, in_1)

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
		t_2 = torch.einsum("ilkj -> ikjl", in_0)

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (1, 7, 7, 512, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 7, 3, 7, 512, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 7, 3, 7, 2, 256, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.reshape(t_2, (1, 7, 3, 14, 256, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (1, 7, 3, 7, 2, 256, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(4, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (1, 1, 7, 5376, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 3, 7, 3, 7, 256, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnlok, ijlk -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

