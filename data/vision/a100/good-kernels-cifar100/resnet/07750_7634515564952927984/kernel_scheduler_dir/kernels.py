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
    reduce_0x7f2ec4002de8 [label="Sum", shape=box];
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
        reduce_0x7f2ec4002de8;
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
        interface_0_in_0x7f3628004b40 [label="s", shape=none];
        interface_0_in_0x55dc702211a8 [label="H", shape=none];
        interface_0_in_0x7f3628004d70 [label="k_1", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x7f3628004b58 [label="s", shape=none];
        interface_0_in_0x7f3628004b08 [label="s^-1*C_in", shape=none];
        interface_0_in_0x7f3628004d88 [label="k_1", shape=none];
        interface_0_in_0x7f3668004038 [label="C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55dc70221130;
        interface_0_in_0x7f3628004af0;
        interface_0_in_0x55dc70221180;
        interface_0_in_0x7f3628004b40;
        interface_0_in_0x55dc702211a8;
        interface_0_in_0x7f3628004d70;
        interface_0_in_0x7f3628004b58;
        interface_0_in_0x7f3628004b08;
        interface_0_in_0x7f3628004d88;
        interface_0_in_0x7f3668004038;
    }
    // Op's.
    op_0x7f3628004ad0 [label="Share"];
    op_0x7f3628004b20 [label="Share"];
    op_0x7f3628004d50 [label="Share"];
    op_0x7f3668004000 [label="Share"];
    op_0x7f36680046b8 [label="Expand"];
    // Dimension's.
    interface_0_in_0x55dc70221130 -> interface_0_out_0x55dc70221130 [label="N"];
    op_0x7f3668004000 -> interface_0_out_0x55dc70221158 [label="C_out"];
    interface_0_in_0x55dc70221180 -> interface_0_out_0x55dc70221180 [label="H"];
    interface_0_in_0x55dc702211a8 -> interface_0_out_0x55dc702211a8 [label="H"];
    op_0x7f3628004d50 -> reduce_0x7f2ec4001998 [label="k_1"];
    op_0x7f3628004b20 -> reduce_0x7f2ec4002de8 [label="s"];
    op_0x7f3628004ad0 -> reduce_0x7f2ec4005740 [label="s^-1*C_in"];
    interface_0_in_0x7f3628004af0 -> op_0x7f3628004ad0 [label="s^-1*C_in"];
    interface_0_in_0x7f3628004b08 -> op_0x7f3628004ad0 [label="s^-1*C_in"];
    interface_0_in_0x7f3628004b40 -> op_0x7f3628004b20 [label="s"];
    interface_0_in_0x7f3628004b58 -> op_0x7f3628004b20 [label="s"];
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
        interface_1_out_0x7f3628004b40 [label="s", shape=none];
        interface_1_out_0x55dc702211a8 [label="H", shape=none];
        interface_1_out_0x7f3628004d70 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x55dc70221130;
        interface_1_out_0x7f3628004af0;
        interface_1_out_0x55dc70221180;
        interface_1_out_0x7f3628004b40;
        interface_1_out_0x55dc702211a8;
        interface_1_out_0x7f3628004d70;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55dc70221130 [label="N", shape=none];
        interface_1_in_0x7f33bc543230 [label="C_in", shape=none];
        interface_1_in_0x7f3614026720 [label="H", shape=none];
        interface_1_in_0x7f3668005a80 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55dc70221130;
        interface_1_in_0x7f33bc543230;
        interface_1_in_0x7f3614026720;
        interface_1_in_0x7f3668005a80;
    }
    // Op's.
    op_0x7f30f80098e0 [label="Split"];
    op_0x7f33bc5431f0 [label="Split"];
    op_0x7f3528016c30 [label="Shift"];
    op_0x7f357400a7c0 [label="Unfold"];
    op_0x7f36140266e0 [label="Merge"];
    op_0x7f3668005a60 [label="Shift"];
    // Dimension's.
    interface_1_in_0x55dc70221130 -> interface_1_out_0x55dc70221130 [label="N"];
    op_0x7f30f80098e0 -> interface_1_out_0x55dc70221180 [label="H"];
    op_0x7f357400a7c0 -> interface_1_out_0x55dc702211a8 [label="H"];
    op_0x7f3528016c30 -> op_0x7f30f80098e0 [label="s*H"];
    interface_1_in_0x7f33bc543230 -> op_0x7f33bc5431f0 [label="C_in"];
    op_0x7f36140266e0 -> op_0x7f3528016c30 [label="s*H"];
    op_0x7f3668005a60 -> op_0x7f357400a7c0 [label="H"];
    interface_1_in_0x7f3614026720 -> op_0x7f36140266e0 [label="H"];
    op_0x7f33bc5431f0 -> op_0x7f36140266e0 [label="s"];
    op_0x7f33bc5431f0 -> interface_1_out_0x7f3628004af0 [label="s^-1*C_in"];
    op_0x7f30f80098e0 -> interface_1_out_0x7f3628004b40 [label="s"];
    op_0x7f357400a7c0 -> interface_1_out_0x7f3628004d70 [label="k_1"];
    interface_1_in_0x7f3668005a80 -> op_0x7f3668005a60 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_2 {
    label = "Input 0";
    interface_2_out_0x55dc70221130 [label="N", shape=none];
    interface_2_out_0x7f33bc543230 [label="C_in", shape=none];
    interface_2_out_0x7f3614026720 [label="H", shape=none];
    interface_2_out_0x7f3668005a80 [label="H", shape=none];
}

interface_2_out_0x55dc70221130 -> interface_1_in_0x55dc70221130;
interface_2_out_0x7f33bc543230 -> interface_1_in_0x7f33bc543230;
interface_2_out_0x7f3614026720 -> interface_1_in_0x7f3614026720;
interface_2_out_0x7f3668005a80 -> interface_1_in_0x7f3668005a80;

interface_1_out_0x55dc70221130 -> interface_0_in_0x55dc70221130;
interface_1_out_0x7f3628004af0 -> interface_0_in_0x7f3628004af0;
interface_1_out_0x55dc70221180 -> interface_0_in_0x55dc70221180;
interface_1_out_0x7f3628004b40 -> interface_0_in_0x7f3628004b40;
interface_1_out_0x55dc702211a8 -> interface_0_in_0x55dc702211a8;
interface_1_out_0x7f3628004d70 -> interface_0_in_0x7f3628004d70;

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 1";
    interface_3_out_0x7f3628004b58 [label="s", shape=none];
    interface_3_out_0x7f3628004b08 [label="s^-1*C_in", shape=none];
    interface_3_out_0x7f3628004d88 [label="k_1", shape=none];
    interface_3_out_0x7f3668004038 [label="C_out", shape=none];
}

interface_3_out_0x7f3628004b58 -> interface_0_in_0x7f3628004b58;
interface_3_out_0x7f3628004b08 -> interface_0_in_0x7f3628004b08;
interface_3_out_0x7f3628004d88 -> interface_0_in_0x7f3628004d88;
interface_3_out_0x7f3668004038 -> interface_0_in_0x7f3668004038;

{
    rank = same;
    interface_2_out_0x55dc70221130;
    interface_2_out_0x7f33bc543230;
    interface_2_out_0x7f3614026720;
    interface_2_out_0x7f3668005a80;
    interface_3_out_0x7f3628004b58;
    interface_3_out_0x7f3628004b08;
    interface_3_out_0x7f3628004d88;
    interface_3_out_0x7f3668004038;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_4_in_0x55dc70221130 [label="N", shape=none];
    interface_4_in_0x55dc70221158 [label="C_out", shape=none];
    interface_4_in_0x55dc70221180 [label="H", shape=none];
    interface_4_in_0x55dc702211a8 [label="H", shape=none];
}
interface_0_out_0x55dc70221130 -> interface_4_in_0x55dc70221130;
interface_0_out_0x55dc70221158 -> interface_4_in_0x55dc70221158;
interface_0_out_0x55dc70221180 -> interface_4_in_0x55dc70221180;
interface_0_out_0x55dc702211a8 -> interface_4_in_0x55dc702211a8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([2, 32, 3, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 32, 56, 56, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.permute(t_2, (0, 2, 3, 1, 4, ))
		t_2 = torch.reshape(t_2, (128, 32, 112, 56, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (128, 32, 56, 2, 56, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 3584, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 32, 56, 2, 3, 56, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("minjok, jikl -> mnol", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([2, 32, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 32, 28, 28, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.permute(t_2, (0, 2, 3, 1, 4, ))
		t_2 = torch.reshape(t_2, (128, 32, 56, 28, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (128, 32, 28, 2, 28, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 1792, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 32, 28, 2, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("minjok, jikl -> mnol", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([2, 64, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 64, 28, 28, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.permute(t_2, (0, 2, 3, 1, 4, ))
		t_2 = torch.reshape(t_2, (128, 64, 56, 28, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (128, 64, 28, 2, 28, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 3584, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 64, 28, 2, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("minjok, jikl -> mnol", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([2, 64, 3, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 64, 14, 14, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.permute(t_2, (0, 2, 3, 1, 4, ))
		t_2 = torch.reshape(t_2, (128, 64, 28, 14, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (128, 64, 14, 2, 14, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 1792, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 64, 14, 2, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("minjok, jikl -> mnol", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([2, 128, 3, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 128, 14, 14, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.permute(t_2, (0, 2, 3, 1, 4, ))
		t_2 = torch.reshape(t_2, (128, 128, 28, 14, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (128, 128, 14, 2, 14, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 3584, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 128, 14, 2, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("minjok, jikl -> mnol", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([2, 128, 3, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 128, 7, 7, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.permute(t_2, (0, 2, 3, 1, 4, ))
		t_2 = torch.reshape(t_2, (128, 128, 14, 7, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (128, 128, 7, 2, 7, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 1792, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 128, 7, 2, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("minjok, jikl -> mnol", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([2, 256, 3, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (128, 2, 256, 7, 7, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.permute(t_2, (0, 2, 3, 1, 4, ))
		t_2 = torch.reshape(t_2, (128, 256, 14, 7, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 2)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (128, 256, 7, 2, 7, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 3584, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 256, 7, 2, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 3, 5, 4, ))

		# Perform contraction.
		t_3 = torch.einsum("minjok, jikl -> mnol", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_3

		return y

