import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f8754004ce8 [label="Sum", shape=box];
    reduce_0x7f8754007440 [label="Sum", shape=box];
    reduce_0x7f8754003a98 [label="Sum", shape=box];
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
        reduce_0x7f8754004ce8;
        reduce_0x7f8754007440;
        reduce_0x7f8754003a98;
        interface_0_out_0x55dcca2d4a60;
        interface_0_out_0x55dcca2d4a88;
        interface_0_out_0x55dcca2d4ab0;
        interface_0_out_0x55dcca2d4ad8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55dcca2d4a60 [label="N", shape=none];
        interface_0_in_0x55dcca2d4ab0 [label="H", shape=none];
        interface_0_in_0x55dcd9672a70 [label="s", shape=none];
        interface_0_in_0x55dcd9672cf0 [label="s^-1*C_in", shape=none];
        interface_0_in_0x55dcd9672b10 [label="k_1", shape=none];
        interface_0_in_0x55dcca2d4ad8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x55dcd9672a38 [label="C_out", shape=none];
        interface_0_in_0x55dcd9672d08 [label="s^-1*C_in", shape=none];
        interface_0_in_0x55dcd9672a88 [label="s", shape=none];
        interface_0_in_0x55dcd9672b28 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55dcca2d4a60;
        interface_0_in_0x55dcca2d4ab0;
        interface_0_in_0x55dcd9672a70;
        interface_0_in_0x55dcd9672cf0;
        interface_0_in_0x55dcd9672b10;
        interface_0_in_0x55dcca2d4ad8;
        interface_0_in_0x55dcd9672a38;
        interface_0_in_0x55dcd9672d08;
        interface_0_in_0x55dcd9672a88;
        interface_0_in_0x55dcd9672b28;
    }
    // Op's.
    op_0x55dcd9672a00 [label="Share"];
    op_0x55dcd9672a50 [label="Share"];
    op_0x55dcd9672af0 [label="Share"];
    op_0x55dcd9672cd0 [label="Share"];
    op_0x55dcd9672ed8 [label="Expand"];
    // Dimension's.
    interface_0_in_0x55dcca2d4a60 -> interface_0_out_0x55dcca2d4a60 [label="N"];
    op_0x55dcd9672a00 -> interface_0_out_0x55dcca2d4a88 [label="C_out"];
    interface_0_in_0x55dcca2d4ab0 -> interface_0_out_0x55dcca2d4ab0 [label="H"];
    interface_0_in_0x55dcca2d4ad8 -> interface_0_out_0x55dcca2d4ad8 [label="H"];
    op_0x55dcd9672ed8 -> op_0x55dcd9672a00 [label="C_out"];
    interface_0_in_0x55dcd9672a38 -> op_0x55dcd9672a00 [label="C_out"];
    interface_0_in_0x55dcd9672a70 -> op_0x55dcd9672a50 [label="s"];
    interface_0_in_0x55dcd9672a88 -> op_0x55dcd9672a50 [label="s"];
    interface_0_in_0x55dcd9672b10 -> op_0x55dcd9672af0 [label="k_1"];
    interface_0_in_0x55dcd9672b28 -> op_0x55dcd9672af0 [label="k_1"];
    interface_0_in_0x55dcd9672cf0 -> op_0x55dcd9672cd0 [label="s^-1*C_in"];
    interface_0_in_0x55dcd9672d08 -> op_0x55dcd9672cd0 [label="s^-1*C_in"];
    op_0x55dcd9672af0 -> reduce_0x7f8754003a98 [label="k_1"];
    op_0x55dcd9672a50 -> reduce_0x7f8754004ce8 [label="s"];
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
        interface_1_out_0x55dcca2d4ab0 [label="H", shape=none];
        interface_1_out_0x55dcd9672a70 [label="s", shape=none];
        interface_1_out_0x55dcd9672cf0 [label="s^-1*C_in", shape=none];
        interface_1_out_0x55dcd9672b10 [label="k_1", shape=none];
        interface_1_out_0x55dcca2d4ad8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x55dcca2d4a60;
        interface_1_out_0x55dcca2d4ab0;
        interface_1_out_0x55dcd9672a70;
        interface_1_out_0x55dcd9672cf0;
        interface_1_out_0x55dcd9672b10;
        interface_1_out_0x55dcca2d4ad8;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55dcca2d4a60 [label="N", shape=none];
        interface_1_in_0x55dcd96cd630 [label="C_in", shape=none];
        interface_1_in_0x55dcd972beb0 [label="H", shape=none];
        interface_1_in_0x55dcca86dfc0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55dcca2d4a60;
        interface_1_in_0x55dcd96cd630;
        interface_1_in_0x55dcd972beb0;
        interface_1_in_0x55dcca86dfc0;
    }
    // Op's.
    op_0x55dcca86dfa0 [label="Shift"];
    op_0x55dcca86e030 [label="Shift"];
    op_0x55dcd9680600 [label="Unfold"];
    op_0x55dcd96cd050 [label="Split"];
    op_0x55dcd96cd5f0 [label="Split"];
    op_0x55dcd972be70 [label="Merge"];
    // Dimension's.
    interface_1_in_0x55dcca2d4a60 -> interface_1_out_0x55dcca2d4a60 [label="N"];
    op_0x55dcd96cd050 -> interface_1_out_0x55dcca2d4ab0 [label="H"];
    op_0x55dcd9680600 -> interface_1_out_0x55dcca2d4ad8 [label="H"];
    interface_1_in_0x55dcca86dfc0 -> op_0x55dcca86dfa0 [label="H"];
    op_0x55dcd972be70 -> op_0x55dcca86e030 [label="s*H"];
    op_0x55dcd96cd050 -> interface_1_out_0x55dcd9672a70 [label="s"];
    op_0x55dcd9680600 -> interface_1_out_0x55dcd9672b10 [label="k_1"];
    op_0x55dcd96cd5f0 -> interface_1_out_0x55dcd9672cf0 [label="s^-1*C_in"];
    op_0x55dcca86dfa0 -> op_0x55dcd9680600 [label="H"];
    op_0x55dcca86e030 -> op_0x55dcd96cd050 [label="s*H"];
    interface_1_in_0x55dcd96cd630 -> op_0x55dcd96cd5f0 [label="C_in"];
    interface_1_in_0x55dcd972beb0 -> op_0x55dcd972be70 [label="H"];
    op_0x55dcd96cd5f0 -> op_0x55dcd972be70 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_2 {
    label = "Input 0";
    interface_2_out_0x55dcca2d4a60 [label="N", shape=none];
    interface_2_out_0x55dcd96cd630 [label="C_in", shape=none];
    interface_2_out_0x55dcd972beb0 [label="H", shape=none];
    interface_2_out_0x55dcca86dfc0 [label="H", shape=none];
}

interface_2_out_0x55dcca2d4a60 -> interface_1_in_0x55dcca2d4a60;
interface_2_out_0x55dcd96cd630 -> interface_1_in_0x55dcd96cd630;
interface_2_out_0x55dcd972beb0 -> interface_1_in_0x55dcd972beb0;
interface_2_out_0x55dcca86dfc0 -> interface_1_in_0x55dcca86dfc0;

interface_1_out_0x55dcca2d4a60 -> interface_0_in_0x55dcca2d4a60;
interface_1_out_0x55dcca2d4ab0 -> interface_0_in_0x55dcca2d4ab0;
interface_1_out_0x55dcd9672a70 -> interface_0_in_0x55dcd9672a70;
interface_1_out_0x55dcd9672cf0 -> interface_0_in_0x55dcd9672cf0;
interface_1_out_0x55dcd9672b10 -> interface_0_in_0x55dcd9672b10;
interface_1_out_0x55dcca2d4ad8 -> interface_0_in_0x55dcca2d4ad8;

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 1";
    interface_3_out_0x55dcd9672a38 [label="C_out", shape=none];
    interface_3_out_0x55dcd9672d08 [label="s^-1*C_in", shape=none];
    interface_3_out_0x55dcd9672a88 [label="s", shape=none];
    interface_3_out_0x55dcd9672b28 [label="k_1", shape=none];
}

interface_3_out_0x55dcd9672a38 -> interface_0_in_0x55dcd9672a38;
interface_3_out_0x55dcd9672d08 -> interface_0_in_0x55dcd9672d08;
interface_3_out_0x55dcd9672a88 -> interface_0_in_0x55dcd9672a88;
interface_3_out_0x55dcd9672b28 -> interface_0_in_0x55dcd9672b28;

{
    rank = same;
    interface_2_out_0x55dcca2d4a60;
    interface_2_out_0x55dcd96cd630;
    interface_2_out_0x55dcd972beb0;
    interface_2_out_0x55dcca86dfc0;
    interface_3_out_0x55dcd9672a38;
    interface_3_out_0x55dcd9672d08;
    interface_3_out_0x55dcd9672a88;
    interface_3_out_0x55dcd9672b28;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_4_in_0x55dcca2d4a60 [label="N", shape=none];
    interface_4_in_0x55dcca2d4a88 [label="C_out", shape=none];
    interface_4_in_0x55dcca2d4ab0 [label="H", shape=none];
    interface_4_in_0x55dcca2d4ad8 [label="H", shape=none];
}
interface_0_out_0x55dcca2d4a60 -> interface_4_in_0x55dcca2d4a60;
interface_0_out_0x55dcca2d4a88 -> interface_4_in_0x55dcca2d4a88;
interface_0_out_0x55dcca2d4ab0 -> interface_4_in_0x55dcca2d4ab0;
interface_0_out_0x55dcca2d4ad8 -> interface_4_in_0x55dcca2d4ad8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 32, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("iklj -> ilkj", in_0)

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 56, 2, 32, 56, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.reshape(t_2, (1, 112, 32, 56, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1, 56, 2, 32, 56, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 3584, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 56, 2, 32, 3, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("mnjlko, iljk -> mino", t_2, in_1)

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 32, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("iklj -> ilkj", in_0)

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 28, 2, 32, 28, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.reshape(t_2, (1, 56, 32, 28, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1, 28, 2, 32, 28, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1792, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 28, 2, 32, 3, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("mnjlko, iljk -> mino", t_2, in_1)

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 64, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("iklj -> ilkj", in_0)

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 28, 2, 64, 28, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.reshape(t_2, (1, 56, 64, 28, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1, 28, 2, 64, 28, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 3584, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 28, 2, 64, 3, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("mnjlko, iljk -> mino", t_2, in_1)

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 64, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("iklj -> ilkj", in_0)

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 14, 2, 64, 14, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.reshape(t_2, (1, 28, 64, 14, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1, 14, 2, 64, 14, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1792, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 14, 2, 64, 3, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("mnjlko, iljk -> mino", t_2, in_1)

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 128, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("iklj -> ilkj", in_0)

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 14, 2, 128, 14, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.reshape(t_2, (1, 28, 128, 14, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1, 14, 2, 128, 14, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 3584, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 14, 2, 128, 3, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("mnjlko, iljk -> mino", t_2, in_1)

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 128, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("iklj -> ilkj", in_0)

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 7, 2, 128, 7, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.reshape(t_2, (1, 14, 128, 7, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1, 7, 2, 128, 7, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1792, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 7, 2, 128, 3, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("mnjlko, iljk -> mino", t_2, in_1)

		# No need to crop the output tensor.
		y = t_3

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 256, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("iklj -> ilkj", in_0)

		# [C_in]@Spliteef7ce0b7703d88a -> [s]@Merge6f1a0d6b662fae85, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 7, 2, 256, 7, ))

		# [H]@Merge6f1a0d6b662fae84, [s]@Merge6f1a0d6b662fae85 -> [s*H]@Shift594e1a6314829db7
		t_2 = torch.reshape(t_2, (1, 14, 256, 7, ))

		# [s*H]@Shift594e1a6314829db7 -> [s*H]@Split7ee86503d19bbef6
		t_2 = torch.roll(t_2, self.shift_direction, 1)

		# [s*H]@Split7ee86503d19bbef6 -> [H]@Iterator96123ba3184da39c, [s]@Shareb15a7faee0f8b868
		t_2 = torch.reshape(t_2, (1, 7, 2, 256, 7, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 3584, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 7, 2, 256, 3, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("mnjlko, iljk -> mino", t_2, in_1)

		# No need to crop the output tensor.
		y = t_3

		return y

