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
        interface_0_out_0x55d9c788f750 [label="N", shape=none];
        interface_0_out_0x55d9c788f778 [label="C_out", shape=none];
        interface_0_out_0x55d9c788f7a0 [label="H", shape=none];
        interface_0_out_0x55d9c788f7c8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55d9c788f750;
        interface_0_out_0x55d9c788f778;
        interface_0_out_0x55d9c788f7a0;
        interface_0_out_0x55d9c788f7c8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55d9c788f750 [label="N", shape=none];
        interface_0_in_0x7fea48007a50 [label="s", shape=none];
        interface_0_in_0x7fea480057a0 [label="H", shape=none];
        interface_0_in_0x55d9c788f7c8 [label="H", shape=none];
        interface_0_in_0x7fea48007a68 [label="s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55d9c788f750;
        interface_0_in_0x7fea48007a50;
        interface_0_in_0x7fea480057a0;
        interface_0_in_0x55d9c788f7c8;
        interface_0_in_0x7fea48007a68;
    }
    // Op's.
    op_0x7fea48005780 [label="Shift"];
    op_0x7fea48007a10 [label="Merge"];
    // Dimension's.
    interface_0_in_0x55d9c788f750 -> interface_0_out_0x55d9c788f750 [label="N"];
    op_0x7fea48007a10 -> interface_0_out_0x55d9c788f778 [label="C_out"];
    op_0x7fea48005780 -> interface_0_out_0x55d9c788f7a0 [label="H"];
    interface_0_in_0x55d9c788f7c8 -> interface_0_out_0x55d9c788f7c8 [label="H"];
    interface_0_in_0x7fea480057a0 -> op_0x7fea48005780 [label="H"];
    interface_0_in_0x7fea48007a50 -> op_0x7fea48007a10 [label="s"];
    interface_0_in_0x7fea48007a68 -> op_0x7fea48007a10 [label="s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fe2a8005ad8 [label="Sum", shape=box];
    reduce_0x7fe2a8001998 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55d9c788f750 [label="N", shape=none];
        interface_1_out_0x7fea48007a50 [label="s", shape=none];
        interface_1_out_0x7fea480057a0 [label="H", shape=none];
        interface_1_out_0x55d9c788f7c8 [label="H", shape=none];
        interface_1_out_0x7fea48007a68 [label="s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7fe2a8005ad8;
        reduce_0x7fe2a8001998;
        interface_1_out_0x55d9c788f750;
        interface_1_out_0x7fea48007a50;
        interface_1_out_0x7fea480057a0;
        interface_1_out_0x55d9c788f7c8;
        interface_1_out_0x7fea48007a68;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55d9c788f750 [label="N", shape=none];
        interface_1_in_0x7fea48007a50 [label="s", shape=none];
        interface_1_in_0x7fe9d40046f0 [label="s^-1*C_in", shape=none];
        interface_1_in_0x7fea480057a0 [label="H", shape=none];
        interface_1_in_0x55d9c788f7c8 [label="H", shape=none];
        interface_1_in_0x7fe9d4004830 [label="k_1", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x7fe9d4004708 [label="s^-1*C_in", shape=none];
        interface_1_in_0x7fe9d4004848 [label="k_1", shape=none];
        interface_1_in_0x7fe82c00ddb8 [label="s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55d9c788f750;
        interface_1_in_0x7fea48007a50;
        interface_1_in_0x7fe9d40046f0;
        interface_1_in_0x7fea480057a0;
        interface_1_in_0x55d9c788f7c8;
        interface_1_in_0x7fe9d4004830;
        interface_1_in_0x7fe9d4004708;
        interface_1_in_0x7fe9d4004848;
        interface_1_in_0x7fe82c00ddb8;
    }
    // Op's.
    op_0x7fe82c00dd80 [label="Share"];
    op_0x7fe9d40046d0 [label="Share"];
    op_0x7fe9d4004810 [label="Share"];
    op_0x7fea48004e18 [label="Expand"];
    // Dimension's.
    interface_1_in_0x55d9c788f750 -> interface_1_out_0x55d9c788f750 [label="N"];
    interface_1_in_0x55d9c788f7c8 -> interface_1_out_0x55d9c788f7c8 [label="H"];
    op_0x7fe9d4004810 -> reduce_0x7fe2a8001998 [label="k_1"];
    op_0x7fe9d40046d0 -> reduce_0x7fe2a8005ad8 [label="s^-1*C_in"];
    op_0x7fea48004e18 -> op_0x7fe82c00dd80 [label="s^-1*C_out"];
    interface_1_in_0x7fe82c00ddb8 -> op_0x7fe82c00dd80 [label="s^-1*C_out"];
    interface_1_in_0x7fe9d40046f0 -> op_0x7fe9d40046d0 [label="s^-1*C_in"];
    interface_1_in_0x7fe9d4004708 -> op_0x7fe9d40046d0 [label="s^-1*C_in"];
    interface_1_in_0x7fe9d4004830 -> op_0x7fe9d4004810 [label="k_1"];
    interface_1_in_0x7fe9d4004848 -> op_0x7fe9d4004810 [label="k_1"];
    interface_1_in_0x7fea480057a0 -> interface_1_out_0x7fea480057a0 [label="H"];
    interface_1_in_0x7fea48007a50 -> interface_1_out_0x7fea48007a50 [label="s"];
    op_0x7fe82c00dd80 -> interface_1_out_0x7fea48007a68 [label="s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55d9c788f750 [label="N", shape=none];
        interface_2_out_0x7fea48007a50 [label="s", shape=none];
        interface_2_out_0x7fe9d40046f0 [label="s^-1*C_in", shape=none];
        interface_2_out_0x7fea480057a0 [label="H", shape=none];
        interface_2_out_0x55d9c788f7c8 [label="H", shape=none];
        interface_2_out_0x7fe9d4004830 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x55d9c788f750;
        interface_2_out_0x7fea48007a50;
        interface_2_out_0x7fe9d40046f0;
        interface_2_out_0x7fea480057a0;
        interface_2_out_0x55d9c788f7c8;
        interface_2_out_0x7fe9d4004830;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55d9c788f750 [label="N", shape=none];
        interface_2_in_0x7fe7b0026030 [label="C_in", shape=none];
        interface_2_in_0x7fea480057a0 [label="H", shape=none];
        interface_2_in_0x7fea48005a70 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55d9c788f750;
        interface_2_in_0x7fe7b0026030;
        interface_2_in_0x7fea480057a0;
        interface_2_in_0x7fea48005a70;
    }
    // Op's.
    op_0x7fe6ac009c40 [label="Unfold"];
    op_0x7fe7b0025ff0 [label="Split"];
    op_0x7fea48005a50 [label="Shift"];
    // Dimension's.
    interface_2_in_0x55d9c788f750 -> interface_2_out_0x55d9c788f750 [label="N"];
    op_0x7fe6ac009c40 -> interface_2_out_0x55d9c788f7c8 [label="H"];
    op_0x7fea48005a50 -> op_0x7fe6ac009c40 [label="H"];
    interface_2_in_0x7fe7b0026030 -> op_0x7fe7b0025ff0 [label="C_in"];
    op_0x7fe7b0025ff0 -> interface_2_out_0x7fe9d40046f0 [label="s^-1*C_in"];
    op_0x7fe6ac009c40 -> interface_2_out_0x7fe9d4004830 [label="k_1"];
    interface_2_in_0x7fea480057a0 -> interface_2_out_0x7fea480057a0 [label="H"];
    interface_2_in_0x7fea48005a70 -> op_0x7fea48005a50 [label="H"];
    op_0x7fe7b0025ff0 -> interface_2_out_0x7fea48007a50 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x55d9c788f750 [label="N", shape=none];
    interface_3_out_0x7fe7b0026030 [label="C_in", shape=none];
    interface_3_out_0x7fea480057a0 [label="H", shape=none];
    interface_3_out_0x7fea48005a70 [label="H", shape=none];
}

interface_3_out_0x55d9c788f750 -> interface_2_in_0x55d9c788f750;
interface_3_out_0x7fe7b0026030 -> interface_2_in_0x7fe7b0026030;
interface_3_out_0x7fea480057a0 -> interface_2_in_0x7fea480057a0;
interface_3_out_0x7fea48005a70 -> interface_2_in_0x7fea48005a70;

interface_2_out_0x55d9c788f750 -> interface_1_in_0x55d9c788f750;
interface_2_out_0x7fea48007a50 -> interface_1_in_0x7fea48007a50;
interface_2_out_0x7fe9d40046f0 -> interface_1_in_0x7fe9d40046f0;
interface_2_out_0x7fea480057a0 -> interface_1_in_0x7fea480057a0;
interface_2_out_0x55d9c788f7c8 -> interface_1_in_0x55d9c788f7c8;
interface_2_out_0x7fe9d4004830 -> interface_1_in_0x7fe9d4004830;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x7fe9d4004708 [label="s^-1*C_in", shape=none];
    interface_4_out_0x7fe9d4004848 [label="k_1", shape=none];
    interface_4_out_0x7fe82c00ddb8 [label="s^-1*C_out", shape=none];
}

interface_4_out_0x7fe9d4004708 -> interface_1_in_0x7fe9d4004708;
interface_4_out_0x7fe9d4004848 -> interface_1_in_0x7fe9d4004848;
interface_4_out_0x7fe82c00ddb8 -> interface_1_in_0x7fe82c00ddb8;

interface_1_out_0x55d9c788f750 -> interface_0_in_0x55d9c788f750;
interface_1_out_0x7fea48007a50 -> interface_0_in_0x7fea48007a50;
interface_1_out_0x7fea480057a0 -> interface_0_in_0x7fea480057a0;
interface_1_out_0x55d9c788f7c8 -> interface_0_in_0x55d9c788f7c8;
interface_1_out_0x7fea48007a68 -> interface_0_in_0x7fea48007a68;

{
    rank = same;
    interface_3_out_0x55d9c788f750;
    interface_3_out_0x7fe7b0026030;
    interface_3_out_0x7fea480057a0;
    interface_3_out_0x7fea48005a70;
    interface_4_out_0x7fe9d4004708;
    interface_4_out_0x7fe9d4004848;
    interface_4_out_0x7fe82c00ddb8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x55d9c788f750 [label="N", shape=none];
    interface_5_in_0x55d9c788f778 [label="C_out", shape=none];
    interface_5_in_0x55d9c788f7a0 [label="H", shape=none];
    interface_5_in_0x55d9c788f7c8 [label="H", shape=none];
}
interface_0_out_0x55d9c788f750 -> interface_5_in_0x55d9c788f750;
interface_0_out_0x55d9c788f778 -> interface_5_in_0x55d9c788f778;
interface_0_out_0x55d9c788f7a0 -> interface_5_in_0x55d9c788f7a0;
interface_0_out_0x55d9c788f7c8 -> interface_5_in_0x55d9c788f7c8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 3, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 64, 56, 56, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 7168, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 2, 64, 56, 3, 56, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("lojnmk, jki -> lonmi", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (128, 56, 56, 128, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 1)

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
			torch.randn([128, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 128, 28, 28, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 7168, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 2, 128, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("lojnmk, jki -> lonmi", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (128, 28, 28, 256, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 1)

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
			torch.randn([256, 3, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 256, 14, 14, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 7168, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 2, 256, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("lojnmk, jki -> lonmi", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (128, 14, 14, 512, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 1)

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
			torch.randn([512, 3, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 512, 7, 7, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 7168, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 2, 512, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("lojnmk, jki -> lonmi", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.permute(t_4, (0, 2, 3, 1, 4, ))
		t_4 = torch.reshape(t_4, (128, 7, 7, 1024, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_4 = torch.permute(t_4, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_4

		return y

