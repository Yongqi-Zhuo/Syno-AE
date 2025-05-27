import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f51b0001a98 [label="Sum", shape=box];
    reduce_0x7f51b0001ab0 [label="Sum", shape=box];
    reduce_0x7f51b0005540 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x5590c9c880c0 [label="N", shape=none];
        interface_0_out_0x5590c9c880e8 [label="C_out", shape=none];
        interface_0_out_0x5590c9c88110 [label="H", shape=none];
        interface_0_out_0x5590c9c88138 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f51b0001a98;
        reduce_0x7f51b0001ab0;
        reduce_0x7f51b0005540;
        interface_0_out_0x5590c9c880c0;
        interface_0_out_0x5590c9c880e8;
        interface_0_out_0x5590c9c88110;
        interface_0_out_0x5590c9c88138;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5590c9c880c0 [label="N", shape=none];
        interface_0_in_0x5590da8a7590 [label="k_1", shape=none];
        interface_0_in_0x5590c9c88110 [label="H", shape=none];
        interface_0_in_0x5590da8a7860 [label="k_1", shape=none];
        interface_0_in_0x5590c9c88138 [label="H", shape=none];
        interface_0_in_0x5590da8f9cb0 [label="s^-1*C_in", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x5590da8a74b8 [label="C_out", shape=none];
        interface_0_in_0x5590da8a75a8 [label="k_1", shape=none];
        interface_0_in_0x5590da8a7878 [label="k_1", shape=none];
        interface_0_in_0x5590da8f9cc8 [label="s^-1*C_in", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5590c9c880c0;
        interface_0_in_0x5590da8a7590;
        interface_0_in_0x5590c9c88110;
        interface_0_in_0x5590da8a7860;
        interface_0_in_0x5590c9c88138;
        interface_0_in_0x5590da8f9cb0;
        interface_0_in_0x5590da8a74b8;
        interface_0_in_0x5590da8a75a8;
        interface_0_in_0x5590da8a7878;
        interface_0_in_0x5590da8f9cc8;
    }
    // Op's.
    op_0x5590da8a7480 [label="Share"];
    op_0x5590da8a7570 [label="Share"];
    op_0x5590da8a7840 [label="Share"];
    op_0x5590da8a7a38 [label="Expand"];
    op_0x5590da8f9c90 [label="Share"];
    // Dimension's.
    interface_0_in_0x5590c9c880c0 -> interface_0_out_0x5590c9c880c0 [label="N"];
    op_0x5590da8a7480 -> interface_0_out_0x5590c9c880e8 [label="C_out"];
    interface_0_in_0x5590c9c88110 -> interface_0_out_0x5590c9c88110 [label="H"];
    interface_0_in_0x5590c9c88138 -> interface_0_out_0x5590c9c88138 [label="H"];
    op_0x5590da8a7a38 -> op_0x5590da8a7480 [label="C_out"];
    interface_0_in_0x5590da8a74b8 -> op_0x5590da8a7480 [label="C_out"];
    interface_0_in_0x5590da8a7590 -> op_0x5590da8a7570 [label="k_1"];
    interface_0_in_0x5590da8a75a8 -> op_0x5590da8a7570 [label="k_1"];
    interface_0_in_0x5590da8a7860 -> op_0x5590da8a7840 [label="k_1"];
    interface_0_in_0x5590da8a7878 -> op_0x5590da8a7840 [label="k_1"];
    interface_0_in_0x5590da8f9cb0 -> op_0x5590da8f9c90 [label="s^-1*C_in"];
    interface_0_in_0x5590da8f9cc8 -> op_0x5590da8f9c90 [label="s^-1*C_in"];
    op_0x5590da8a7570 -> reduce_0x7f51b0001a98 [label="k_1"];
    op_0x5590da8a7840 -> reduce_0x7f51b0001ab0 [label="k_1"];
    op_0x5590da8f9c90 -> reduce_0x7f51b0005540 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5590c9c880c0 [label="N", shape=none];
        interface_1_out_0x5590da8a7590 [label="k_1", shape=none];
        interface_1_out_0x5590c9c88110 [label="H", shape=none];
        interface_1_out_0x5590da8a7860 [label="k_1", shape=none];
        interface_1_out_0x5590c9c88138 [label="H", shape=none];
        interface_1_out_0x5590da8f9cb0 [label="s^-1*C_in", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x5590c9c880c0;
        interface_1_out_0x5590da8a7590;
        interface_1_out_0x5590c9c88110;
        interface_1_out_0x5590da8a7860;
        interface_1_out_0x5590c9c88138;
        interface_1_out_0x5590da8f9cb0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5590c9c880c0 [label="N", shape=none];
        interface_1_in_0x5590da8bf128 [label="H", shape=none];
        interface_1_in_0x5590da8a7860 [label="k_1", shape=none];
        interface_1_in_0x5590c9c88138 [label="H", shape=none];
        interface_1_in_0x5590da8f9cb0 [label="s^-1*C_in", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5590c9c880c0;
        interface_1_in_0x5590da8bf128;
        interface_1_in_0x5590da8a7860;
        interface_1_in_0x5590c9c88138;
        interface_1_in_0x5590da8f9cb0;
    }
    // Op's.
    op_0x5590da8bf100 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x5590c9c880c0 -> interface_1_out_0x5590c9c880c0 [label="N"];
    op_0x5590da8bf100 -> interface_1_out_0x5590c9c88110 [label="H"];
    interface_1_in_0x5590c9c88138 -> interface_1_out_0x5590c9c88138 [label="H"];
    op_0x5590da8bf100 -> interface_1_out_0x5590da8a7590 [label="k_1"];
    interface_1_in_0x5590da8a7860 -> interface_1_out_0x5590da8a7860 [label="k_1"];
    interface_1_in_0x5590da8bf128 -> op_0x5590da8bf100 [label="H"];
    interface_1_in_0x5590da8f9cb0 -> interface_1_out_0x5590da8f9cb0 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f51b0002ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5590c9c880c0 [label="N", shape=none];
        interface_2_out_0x5590da8bf128 [label="H", shape=none];
        interface_2_out_0x5590da8a7860 [label="k_1", shape=none];
        interface_2_out_0x5590c9c88138 [label="H", shape=none];
        interface_2_out_0x5590da8f9cb0 [label="s^-1*C_in", shape=none];
    }
    {
        rank = same;
        reduce_0x7f51b0002ce8;
        interface_2_out_0x5590c9c880c0;
        interface_2_out_0x5590da8bf128;
        interface_2_out_0x5590da8a7860;
        interface_2_out_0x5590c9c88138;
        interface_2_out_0x5590da8f9cb0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5590c9c880c0 [label="N", shape=none];
        interface_2_in_0x5590da90a100 [label="C_in", shape=none];
        interface_2_in_0x5590da8bf128 [label="H", shape=none];
        interface_2_in_0x5590da8a9730 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5590c9c880c0;
        interface_2_in_0x5590da90a100;
        interface_2_in_0x5590da8bf128;
        interface_2_in_0x5590da8a9730;
    }
    // Op's.
    op_0x5590da8a9680 [label="Shift"];
    op_0x5590da8a9710 [label="Shift"];
    op_0x5590da8a9e80 [label="Split"];
    op_0x5590da8ae720 [label="Merge"];
    op_0x5590da90a0c0 [label="Split"];
    op_0x5590da948740 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x5590c9c880c0 -> interface_2_out_0x5590c9c880c0 [label="N"];
    op_0x5590da8a9e80 -> interface_2_out_0x5590c9c88138 [label="H"];
    op_0x5590da948740 -> interface_2_out_0x5590da8a7860 [label="k_1"];
    op_0x5590da8ae720 -> op_0x5590da8a9680 [label="s*H"];
    interface_2_in_0x5590da8a9730 -> op_0x5590da8a9710 [label="H"];
    op_0x5590da8a9680 -> op_0x5590da8a9e80 [label="s*H"];
    op_0x5590da948740 -> op_0x5590da8ae720 [label="H"];
    op_0x5590da90a0c0 -> op_0x5590da8ae720 [label="s"];
    interface_2_in_0x5590da8bf128 -> interface_2_out_0x5590da8bf128 [label="H"];
    op_0x5590da90a0c0 -> interface_2_out_0x5590da8f9cb0 [label="s^-1*C_in"];
    interface_2_in_0x5590da90a100 -> op_0x5590da90a0c0 [label="C_in"];
    op_0x5590da8a9710 -> op_0x5590da948740 [label="H"];
    op_0x5590da8a9e80 -> reduce_0x7f51b0002ce8 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x5590c9c880c0 [label="N", shape=none];
    interface_3_out_0x5590da90a100 [label="C_in", shape=none];
    interface_3_out_0x5590da8bf128 [label="H", shape=none];
    interface_3_out_0x5590da8a9730 [label="H", shape=none];
}

interface_3_out_0x5590c9c880c0 -> interface_2_in_0x5590c9c880c0;
interface_3_out_0x5590da90a100 -> interface_2_in_0x5590da90a100;
interface_3_out_0x5590da8bf128 -> interface_2_in_0x5590da8bf128;
interface_3_out_0x5590da8a9730 -> interface_2_in_0x5590da8a9730;

interface_2_out_0x5590c9c880c0 -> interface_1_in_0x5590c9c880c0;
interface_2_out_0x5590da8bf128 -> interface_1_in_0x5590da8bf128;
interface_2_out_0x5590da8a7860 -> interface_1_in_0x5590da8a7860;
interface_2_out_0x5590c9c88138 -> interface_1_in_0x5590c9c88138;
interface_2_out_0x5590da8f9cb0 -> interface_1_in_0x5590da8f9cb0;

interface_1_out_0x5590c9c880c0 -> interface_0_in_0x5590c9c880c0;
interface_1_out_0x5590da8a7590 -> interface_0_in_0x5590da8a7590;
interface_1_out_0x5590c9c88110 -> interface_0_in_0x5590c9c88110;
interface_1_out_0x5590da8a7860 -> interface_0_in_0x5590da8a7860;
interface_1_out_0x5590c9c88138 -> interface_0_in_0x5590c9c88138;
interface_1_out_0x5590da8f9cb0 -> interface_0_in_0x5590da8f9cb0;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x5590da8a74b8 [label="C_out", shape=none];
    interface_4_out_0x5590da8a75a8 [label="k_1", shape=none];
    interface_4_out_0x5590da8a7878 [label="k_1", shape=none];
    interface_4_out_0x5590da8f9cc8 [label="s^-1*C_in", shape=none];
}

interface_4_out_0x5590da8a74b8 -> interface_0_in_0x5590da8a74b8;
interface_4_out_0x5590da8a75a8 -> interface_0_in_0x5590da8a75a8;
interface_4_out_0x5590da8a7878 -> interface_0_in_0x5590da8a7878;
interface_4_out_0x5590da8f9cc8 -> interface_0_in_0x5590da8f9cc8;

{
    rank = same;
    interface_3_out_0x5590c9c880c0;
    interface_3_out_0x5590da90a100;
    interface_3_out_0x5590da8bf128;
    interface_3_out_0x5590da8a9730;
    interface_4_out_0x5590da8a74b8;
    interface_4_out_0x5590da8a75a8;
    interface_4_out_0x5590da8a7878;
    interface_4_out_0x5590da8f9cc8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x5590c9c880c0 [label="N", shape=none];
    interface_5_in_0x5590c9c880e8 [label="C_out", shape=none];
    interface_5_in_0x5590c9c88110 [label="H", shape=none];
    interface_5_in_0x5590c9c88138 [label="H", shape=none];
}
interface_0_out_0x5590c9c880c0 -> interface_5_in_0x5590c9c880c0;
interface_0_out_0x5590c9c880e8 -> interface_5_in_0x5590c9c880e8;
interface_0_out_0x5590c9c88110 -> interface_5_in_0x5590c9c88110;
interface_0_out_0x5590c9c88138 -> interface_5_in_0x5590c9c88138;

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
		t_4 = torch.einsum("mjnkol, ijkl -> mino", t_3, in_1)

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
		t_4 = torch.einsum("mjnkol, ijkl -> mino", t_3, in_1)

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
		t_4 = torch.einsum("mjnkol, ijkl -> mino", t_3, in_1)

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
		t_4 = torch.einsum("mjnkol, ijkl -> mino", t_3, in_1)

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
		t_4 = torch.einsum("mjnkol, ijkl -> mino", t_3, in_1)

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
		t_4 = torch.einsum("mjnkol, ijkl -> mino", t_3, in_1)

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
		t_4 = torch.einsum("mjnkol, ijkl -> mino", t_3, in_1)

		# No need to crop the output tensor.
		y = t_4

		return y

