import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f2ec4001998 [label="Sum", shape=box];
    reduce_0x7f2ec40019b0 [label="Sum", shape=box];
    reduce_0x7f2ec4005740 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x55dc70221130 [label="N", shape=none];
        interface_0_out_0x55dc70221158 [label="C_out", shape=none];
        interface_0_out_0x55dc70221180 [label="H", shape=none];
        interface_0_out_0x55dc702211a8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f2ec4001998;
        reduce_0x7f2ec40019b0;
        reduce_0x7f2ec4005740;
        interface_0_out_0x55dc70221130;
        interface_0_out_0x55dc70221158;
        interface_0_out_0x55dc70221180;
        interface_0_out_0x55dc702211a8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55dc70221130 [label="N", shape=none];
        interface_0_in_0x7f3628004af0 [label="s^-1*C_in", shape=none];
        interface_0_in_0x55dc70221180 [label="H", shape=none];
        interface_0_in_0x7f3628004d70 [label="k_1", shape=none];
        interface_0_in_0x55dc702211a8 [label="H", shape=none];
        interface_0_in_0x7f3510005860 [label="k_1", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x7f3628004b08 [label="s^-1*C_in", shape=none];
        interface_0_in_0x7f3628004d88 [label="k_1", shape=none];
        interface_0_in_0x7f3510005878 [label="k_1", shape=none];
        interface_0_in_0x7f3668004038 [label="C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55dc70221130;
        interface_0_in_0x7f3628004af0;
        interface_0_in_0x55dc70221180;
        interface_0_in_0x7f3628004d70;
        interface_0_in_0x55dc702211a8;
        interface_0_in_0x7f3510005860;
        interface_0_in_0x7f3628004b08;
        interface_0_in_0x7f3628004d88;
        interface_0_in_0x7f3510005878;
        interface_0_in_0x7f3668004038;
    }
    // Op's.
    op_0x7f3510005840 [label="Share"];
    op_0x7f3628004ad0 [label="Share"];
    op_0x7f3628004d50 [label="Share"];
    op_0x7f3668004000 [label="Share"];
    op_0x7f36680046b8 [label="Expand"];
    // Dimension's.
    interface_0_in_0x55dc70221130 -> interface_0_out_0x55dc70221130 [label="N"];
    op_0x7f3668004000 -> interface_0_out_0x55dc70221158 [label="C_out"];
    interface_0_in_0x55dc70221180 -> interface_0_out_0x55dc70221180 [label="H"];
    interface_0_in_0x55dc702211a8 -> interface_0_out_0x55dc702211a8 [label="H"];
    op_0x7f3628004d50 -> reduce_0x7f2ec4001998 [label="k_1"];
    op_0x7f3510005840 -> reduce_0x7f2ec40019b0 [label="k_1"];
    op_0x7f3628004ad0 -> reduce_0x7f2ec4005740 [label="s^-1*C_in"];
    interface_0_in_0x7f3510005860 -> op_0x7f3510005840 [label="k_1"];
    interface_0_in_0x7f3510005878 -> op_0x7f3510005840 [label="k_1"];
    interface_0_in_0x7f3628004af0 -> op_0x7f3628004ad0 [label="s^-1*C_in"];
    interface_0_in_0x7f3628004b08 -> op_0x7f3628004ad0 [label="s^-1*C_in"];
    interface_0_in_0x7f3628004d70 -> op_0x7f3628004d50 [label="k_1"];
    interface_0_in_0x7f3628004d88 -> op_0x7f3628004d50 [label="k_1"];
    op_0x7f36680046b8 -> op_0x7f3668004000 [label="C_out"];
    interface_0_in_0x7f3668004038 -> op_0x7f3668004000 [label="C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55dc70221130 [label="N", shape=none];
        interface_1_out_0x7f3628004af0 [label="s^-1*C_in", shape=none];
        interface_1_out_0x55dc70221180 [label="H", shape=none];
        interface_1_out_0x7f3628004d70 [label="k_1", shape=none];
        interface_1_out_0x55dc702211a8 [label="H", shape=none];
        interface_1_out_0x7f3510005860 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x55dc70221130;
        interface_1_out_0x7f3628004af0;
        interface_1_out_0x55dc70221180;
        interface_1_out_0x7f3628004d70;
        interface_1_out_0x55dc702211a8;
        interface_1_out_0x7f3510005860;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55dc70221130 [label="N", shape=none];
        interface_1_in_0x7f3628004af0 [label="s^-1*C_in", shape=none];
        interface_1_in_0x7f357400a7a8 [label="H", shape=none];
        interface_1_in_0x55dc702211a8 [label="H", shape=none];
        interface_1_in_0x7f3510005860 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55dc70221130;
        interface_1_in_0x7f3628004af0;
        interface_1_in_0x7f357400a7a8;
        interface_1_in_0x55dc702211a8;
        interface_1_in_0x7f3510005860;
    }
    // Op's.
    op_0x7f357400a780 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x55dc70221130 -> interface_1_out_0x55dc70221130 [label="N"];
    op_0x7f357400a780 -> interface_1_out_0x55dc70221180 [label="H"];
    interface_1_in_0x55dc702211a8 -> interface_1_out_0x55dc702211a8 [label="H"];
    interface_1_in_0x7f3510005860 -> interface_1_out_0x7f3510005860 [label="k_1"];
    interface_1_in_0x7f357400a7a8 -> op_0x7f357400a780 [label="H"];
    interface_1_in_0x7f3628004af0 -> interface_1_out_0x7f3628004af0 [label="s^-1*C_in"];
    op_0x7f357400a780 -> interface_1_out_0x7f3628004d70 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f2ec4002de8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55dc70221130 [label="N", shape=none];
        interface_2_out_0x7f3628004af0 [label="s^-1*C_in", shape=none];
        interface_2_out_0x7f357400a7a8 [label="H", shape=none];
        interface_2_out_0x55dc702211a8 [label="H", shape=none];
        interface_2_out_0x7f3510005860 [label="k_1", shape=none];
    }
    {
        rank = same;
        reduce_0x7f2ec4002de8;
        interface_2_out_0x55dc70221130;
        interface_2_out_0x7f3628004af0;
        interface_2_out_0x7f357400a7a8;
        interface_2_out_0x55dc702211a8;
        interface_2_out_0x7f3510005860;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55dc70221130 [label="N", shape=none];
        interface_2_in_0x7f33bc54c4c0 [label="C_in", shape=none];
        interface_2_in_0x7f357400a7a8 [label="H", shape=none];
        interface_2_in_0x7f33d88ceb40 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55dc70221130;
        interface_2_in_0x7f33bc54c4c0;
        interface_2_in_0x7f357400a7a8;
        interface_2_in_0x7f33d88ceb40;
    }
    // Op's.
    op_0x7f3398003c40 [label="Split"];
    op_0x7f33bc54c480 [label="Split"];
    op_0x7f33d88ceb20 [label="Shift"];
    op_0x7f344466d600 [label="Unfold"];
    op_0x7f3614025b80 [label="Merge"];
    op_0x7f3668005a00 [label="Shift"];
    // Dimension's.
    interface_2_in_0x55dc70221130 -> interface_2_out_0x55dc70221130 [label="N"];
    op_0x7f3398003c40 -> interface_2_out_0x55dc702211a8 [label="H"];
    op_0x7f3398003c40 -> reduce_0x7f2ec4002de8 [label="s"];
    op_0x7f3668005a00 -> op_0x7f3398003c40 [label="s*H"];
    interface_2_in_0x7f33bc54c4c0 -> op_0x7f33bc54c480 [label="C_in"];
    interface_2_in_0x7f33d88ceb40 -> op_0x7f33d88ceb20 [label="H"];
    op_0x7f33d88ceb20 -> op_0x7f344466d600 [label="H"];
    op_0x7f344466d600 -> interface_2_out_0x7f3510005860 [label="k_1"];
    interface_2_in_0x7f357400a7a8 -> interface_2_out_0x7f357400a7a8 [label="H"];
    op_0x7f344466d600 -> op_0x7f3614025b80 [label="H"];
    op_0x7f33bc54c480 -> op_0x7f3614025b80 [label="s"];
    op_0x7f33bc54c480 -> interface_2_out_0x7f3628004af0 [label="s^-1*C_in"];
    op_0x7f3614025b80 -> op_0x7f3668005a00 [label="s*H"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x55dc70221130 [label="N", shape=none];
    interface_3_out_0x7f33bc54c4c0 [label="C_in", shape=none];
    interface_3_out_0x7f357400a7a8 [label="H", shape=none];
    interface_3_out_0x7f33d88ceb40 [label="H", shape=none];
}

interface_3_out_0x55dc70221130 -> interface_2_in_0x55dc70221130;
interface_3_out_0x7f33bc54c4c0 -> interface_2_in_0x7f33bc54c4c0;
interface_3_out_0x7f357400a7a8 -> interface_2_in_0x7f357400a7a8;
interface_3_out_0x7f33d88ceb40 -> interface_2_in_0x7f33d88ceb40;

interface_2_out_0x55dc70221130 -> interface_1_in_0x55dc70221130;
interface_2_out_0x7f3628004af0 -> interface_1_in_0x7f3628004af0;
interface_2_out_0x7f357400a7a8 -> interface_1_in_0x7f357400a7a8;
interface_2_out_0x55dc702211a8 -> interface_1_in_0x55dc702211a8;
interface_2_out_0x7f3510005860 -> interface_1_in_0x7f3510005860;

interface_1_out_0x55dc70221130 -> interface_0_in_0x55dc70221130;
interface_1_out_0x7f3628004af0 -> interface_0_in_0x7f3628004af0;
interface_1_out_0x55dc70221180 -> interface_0_in_0x55dc70221180;
interface_1_out_0x7f3628004d70 -> interface_0_in_0x7f3628004d70;
interface_1_out_0x55dc702211a8 -> interface_0_in_0x55dc702211a8;
interface_1_out_0x7f3510005860 -> interface_0_in_0x7f3510005860;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x7f3628004b08 [label="s^-1*C_in", shape=none];
    interface_4_out_0x7f3628004d88 [label="k_1", shape=none];
    interface_4_out_0x7f3510005878 [label="k_1", shape=none];
    interface_4_out_0x7f3668004038 [label="C_out", shape=none];
}

interface_4_out_0x7f3628004b08 -> interface_0_in_0x7f3628004b08;
interface_4_out_0x7f3628004d88 -> interface_0_in_0x7f3628004d88;
interface_4_out_0x7f3510005878 -> interface_0_in_0x7f3510005878;
interface_4_out_0x7f3668004038 -> interface_0_in_0x7f3668004038;

{
    rank = same;
    interface_3_out_0x55dc70221130;
    interface_3_out_0x7f33bc54c4c0;
    interface_3_out_0x7f357400a7a8;
    interface_3_out_0x7f33d88ceb40;
    interface_4_out_0x7f3628004b08;
    interface_4_out_0x7f3628004d88;
    interface_4_out_0x7f3510005878;
    interface_4_out_0x7f3668004038;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x55dc70221130 [label="N", shape=none];
    interface_5_in_0x55dc70221158 [label="C_out", shape=none];
    interface_5_in_0x55dc70221180 [label="H", shape=none];
    interface_5_in_0x55dc702211a8 [label="H", shape=none];
}
interface_0_out_0x55dc70221130 -> interface_5_in_0x55dc70221130;
interface_0_out_0x55dc70221158 -> interface_5_in_0x55dc70221158;
interface_0_out_0x55dc70221180 -> interface_5_in_0x55dc70221180;
interface_0_out_0x55dc702211a8 -> interface_5_in_0x55dc702211a8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (128, 3584, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 64, 56, 3, 56, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 32, 56, 3, 56, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.permute(t_2, (0, 2, 3, 4, 5, 1, ))
		t_2 = torch.reshape(t_2, (128, 32, 56, 3, 112, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (128, 32, 56, 3, 56, 2, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(5, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (128, 32, 56, 168, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 32, 3, 56, 56, 3, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnkoi, jkil -> mnol", t_3, in_1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (128, 1792, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 64, 28, 3, 28, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 32, 28, 3, 28, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.permute(t_2, (0, 2, 3, 4, 5, 1, ))
		t_2 = torch.reshape(t_2, (128, 32, 28, 3, 56, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (128, 32, 28, 3, 28, 2, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(5, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (128, 32, 28, 84, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 32, 3, 28, 28, 3, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnkoi, jkil -> mnol", t_3, in_1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 3, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (128, 3584, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 128, 28, 3, 28, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 64, 28, 3, 28, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.permute(t_2, (0, 2, 3, 4, 5, 1, ))
		t_2 = torch.reshape(t_2, (128, 64, 28, 3, 56, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (128, 64, 28, 3, 28, 2, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(5, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (128, 64, 28, 84, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 3, 28, 28, 3, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnkoi, jkil -> mnol", t_3, in_1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 3, 3, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (128, 1792, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 128, 14, 3, 14, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 64, 14, 3, 14, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.permute(t_2, (0, 2, 3, 4, 5, 1, ))
		t_2 = torch.reshape(t_2, (128, 64, 14, 3, 28, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (128, 64, 14, 3, 14, 2, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(5, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (128, 64, 14, 42, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 3, 14, 14, 3, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnkoi, jkil -> mnol", t_3, in_1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 3, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (128, 3584, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 256, 14, 3, 14, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 128, 14, 3, 14, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.permute(t_2, (0, 2, 3, 4, 5, 1, ))
		t_2 = torch.reshape(t_2, (128, 128, 14, 3, 28, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (128, 128, 14, 3, 14, 2, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(5, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (128, 128, 14, 42, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 128, 3, 14, 14, 3, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnkoi, jkil -> mnol", t_3, in_1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 3, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (128, 1792, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 256, 7, 3, 7, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 128, 7, 3, 7, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.permute(t_2, (0, 2, 3, 4, 5, 1, ))
		t_2 = torch.reshape(t_2, (128, 128, 7, 3, 14, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (128, 128, 7, 3, 7, 2, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(5, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (128, 128, 7, 21, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 128, 3, 7, 7, 3, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnkoi, jkil -> mnol", t_3, in_1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 3, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Shift2906cc2f461505d0 -> [H]@Unfoldeeb0aec8202b574f
		t_2 = torch.roll(t_2, self.shift_direction, 3)

		# [H]@Unfoldeeb0aec8202b574f -> [H]@Merge0bce4580e08cd69c, [k_1]@Share02da0a485106ab3d
		t_2 = torch.reshape(t_2, (128, 3584, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 512, 7, 3, 7, ))

		# [C_in]@Split3524ae88ad3a30bc -> [s]@Merge0bce4580e08cd69d, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 256, 7, 3, 7, ))

		# [H]@Merge0bce4580e08cd69c, [s]@Merge0bce4580e08cd69d -> [s*H]@Shift8a9f243357a7f717
		t_2 = torch.permute(t_2, (0, 2, 3, 4, 5, 1, ))
		t_2 = torch.reshape(t_2, (128, 256, 7, 3, 14, ))

		# [s*H]@Shift8a9f243357a7f717 -> [s*H]@Split511946b410b86996
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [s*H]@Split511946b410b86996 -> [H]@Iteratorb0a1def4ad5784ec, [s]@Reduced95c644a3c072d9a
		t_2 = torch.reshape(t_2, (128, 256, 7, 3, 7, 2, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(5, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_3 = t_2

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (128, 256, 7, 21, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 256, 3, 7, 7, 3, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 3, 2, 4, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("mjnkoi, jkil -> mnol", t_3, in_1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_4

		return y

