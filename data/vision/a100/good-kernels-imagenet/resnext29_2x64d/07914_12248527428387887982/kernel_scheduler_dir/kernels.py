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
        interface_0_out_0x55ceeb214920 [label="N", shape=none];
        interface_0_out_0x55ceeb214948 [label="C_out", shape=none];
        interface_0_out_0x55ceeb214970 [label="H", shape=none];
        interface_0_out_0x55ceeb214998 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55ceeb214920;
        interface_0_out_0x55ceeb214948;
        interface_0_out_0x55ceeb214970;
        interface_0_out_0x55ceeb214998;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55ceeb214920 [label="N", shape=none];
        interface_0_in_0x55ceeec84f70 [label="s", shape=none];
        interface_0_in_0x55ceeec84f88 [label="s^-1*C_out", shape=none];
        interface_0_in_0x55ceeec839e0 [label="H", shape=none];
        interface_0_in_0x55ceeb214998 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55ceeb214920;
        interface_0_in_0x55ceeec84f70;
        interface_0_in_0x55ceeec84f88;
        interface_0_in_0x55ceeec839e0;
        interface_0_in_0x55ceeb214998;
    }
    // Op's.
    op_0x55ceeec839c0 [label="Shift"];
    op_0x55ceeec84f30 [label="Merge"];
    // Dimension's.
    interface_0_in_0x55ceeb214920 -> interface_0_out_0x55ceeb214920 [label="N"];
    op_0x55ceeec84f30 -> interface_0_out_0x55ceeb214948 [label="C_out"];
    op_0x55ceeec839c0 -> interface_0_out_0x55ceeb214970 [label="H"];
    interface_0_in_0x55ceeb214998 -> interface_0_out_0x55ceeb214998 [label="H"];
    interface_0_in_0x55ceeec839e0 -> op_0x55ceeec839c0 [label="H"];
    interface_0_in_0x55ceeec84f70 -> op_0x55ceeec84f30 [label="s"];
    interface_0_in_0x55ceeec84f88 -> op_0x55ceeec84f30 [label="s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f854c0058d8 [label="Sum", shape=box];
    reduce_0x7f854c001a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55ceeb214920 [label="N", shape=none];
        interface_1_out_0x55ceeec84f70 [label="s", shape=none];
        interface_1_out_0x55ceeec84f88 [label="s^-1*C_out", shape=none];
        interface_1_out_0x55ceeec839e0 [label="H", shape=none];
        interface_1_out_0x55ceeb214998 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f854c0058d8;
        reduce_0x7f854c001a98;
        interface_1_out_0x55ceeb214920;
        interface_1_out_0x55ceeec84f70;
        interface_1_out_0x55ceeec84f88;
        interface_1_out_0x55ceeec839e0;
        interface_1_out_0x55ceeb214998;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55ceeb214920 [label="N", shape=none];
        interface_1_in_0x55ceeec84f70 [label="s", shape=none];
        interface_1_in_0x55ceeec82bf0 [label="s^-1*C_in", shape=none];
        interface_1_in_0x55ceeec839e0 [label="H", shape=none];
        interface_1_in_0x55ceeec82c40 [label="k_1", shape=none];
        interface_1_in_0x55ceeb214998 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55ceeec82c08 [label="s^-1*C_in", shape=none];
        interface_1_in_0x55ceeec82ca8 [label="s^-1*C_out", shape=none];
        interface_1_in_0x55ceeec82c58 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55ceeb214920;
        interface_1_in_0x55ceeec84f70;
        interface_1_in_0x55ceeec82bf0;
        interface_1_in_0x55ceeec839e0;
        interface_1_in_0x55ceeec82c40;
        interface_1_in_0x55ceeb214998;
        interface_1_in_0x55ceeec82c08;
        interface_1_in_0x55ceeec82ca8;
        interface_1_in_0x55ceeec82c58;
    }
    // Op's.
    op_0x55ceeec82bd0 [label="Share"];
    op_0x55ceeec82c20 [label="Share"];
    op_0x55ceeec82c70 [label="Share"];
    op_0x55ceeec83158 [label="Expand"];
    // Dimension's.
    interface_1_in_0x55ceeb214920 -> interface_1_out_0x55ceeb214920 [label="N"];
    interface_1_in_0x55ceeb214998 -> interface_1_out_0x55ceeb214998 [label="H"];
    interface_1_in_0x55ceeec82bf0 -> op_0x55ceeec82bd0 [label="s^-1*C_in"];
    interface_1_in_0x55ceeec82c08 -> op_0x55ceeec82bd0 [label="s^-1*C_in"];
    interface_1_in_0x55ceeec82c40 -> op_0x55ceeec82c20 [label="k_1"];
    interface_1_in_0x55ceeec82c58 -> op_0x55ceeec82c20 [label="k_1"];
    op_0x55ceeec83158 -> op_0x55ceeec82c70 [label="s^-1*C_out"];
    interface_1_in_0x55ceeec82ca8 -> op_0x55ceeec82c70 [label="s^-1*C_out"];
    interface_1_in_0x55ceeec839e0 -> interface_1_out_0x55ceeec839e0 [label="H"];
    interface_1_in_0x55ceeec84f70 -> interface_1_out_0x55ceeec84f70 [label="s"];
    op_0x55ceeec82c70 -> interface_1_out_0x55ceeec84f88 [label="s^-1*C_out"];
    op_0x55ceeec82c20 -> reduce_0x7f854c001a98 [label="k_1"];
    op_0x55ceeec82bd0 -> reduce_0x7f854c0058d8 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55ceeb214920 [label="N", shape=none];
        interface_2_out_0x55ceeec84f70 [label="s", shape=none];
        interface_2_out_0x55ceeec82bf0 [label="s^-1*C_in", shape=none];
        interface_2_out_0x55ceeec839e0 [label="H", shape=none];
        interface_2_out_0x55ceeec82c40 [label="k_1", shape=none];
        interface_2_out_0x55ceeb214998 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x55ceeb214920;
        interface_2_out_0x55ceeec84f70;
        interface_2_out_0x55ceeec82bf0;
        interface_2_out_0x55ceeec839e0;
        interface_2_out_0x55ceeec82c40;
        interface_2_out_0x55ceeb214998;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55ceeb214920 [label="N", shape=none];
        interface_2_in_0x55ceeec84c00 [label="C_in", shape=none];
        interface_2_in_0x55ceeec839e0 [label="H", shape=none];
        interface_2_in_0x55ceeec83a40 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55ceeb214920;
        interface_2_in_0x55ceeec84c00;
        interface_2_in_0x55ceeec839e0;
        interface_2_in_0x55ceeec83a40;
    }
    // Op's.
    op_0x55ceeec83a20 [label="Shift"];
    op_0x55ceeec84bc0 [label="Split"];
    op_0x55ceeec91700 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x55ceeb214920 -> interface_2_out_0x55ceeb214920 [label="N"];
    op_0x55ceeec91700 -> interface_2_out_0x55ceeb214998 [label="H"];
    op_0x55ceeec84bc0 -> interface_2_out_0x55ceeec82bf0 [label="s^-1*C_in"];
    op_0x55ceeec91700 -> interface_2_out_0x55ceeec82c40 [label="k_1"];
    interface_2_in_0x55ceeec839e0 -> interface_2_out_0x55ceeec839e0 [label="H"];
    interface_2_in_0x55ceeec83a40 -> op_0x55ceeec83a20 [label="H"];
    interface_2_in_0x55ceeec84c00 -> op_0x55ceeec84bc0 [label="C_in"];
    op_0x55ceeec84bc0 -> interface_2_out_0x55ceeec84f70 [label="s"];
    op_0x55ceeec83a20 -> op_0x55ceeec91700 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x55ceeb214920 [label="N", shape=none];
    interface_3_out_0x55ceeec84c00 [label="C_in", shape=none];
    interface_3_out_0x55ceeec839e0 [label="H", shape=none];
    interface_3_out_0x55ceeec83a40 [label="H", shape=none];
}

interface_3_out_0x55ceeb214920 -> interface_2_in_0x55ceeb214920;
interface_3_out_0x55ceeec84c00 -> interface_2_in_0x55ceeec84c00;
interface_3_out_0x55ceeec839e0 -> interface_2_in_0x55ceeec839e0;
interface_3_out_0x55ceeec83a40 -> interface_2_in_0x55ceeec83a40;

interface_2_out_0x55ceeb214920 -> interface_1_in_0x55ceeb214920;
interface_2_out_0x55ceeec84f70 -> interface_1_in_0x55ceeec84f70;
interface_2_out_0x55ceeec82bf0 -> interface_1_in_0x55ceeec82bf0;
interface_2_out_0x55ceeec839e0 -> interface_1_in_0x55ceeec839e0;
interface_2_out_0x55ceeec82c40 -> interface_1_in_0x55ceeec82c40;
interface_2_out_0x55ceeb214998 -> interface_1_in_0x55ceeb214998;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x55ceeec82c08 [label="s^-1*C_in", shape=none];
    interface_4_out_0x55ceeec82ca8 [label="s^-1*C_out", shape=none];
    interface_4_out_0x55ceeec82c58 [label="k_1", shape=none];
}

interface_4_out_0x55ceeec82c08 -> interface_1_in_0x55ceeec82c08;
interface_4_out_0x55ceeec82ca8 -> interface_1_in_0x55ceeec82ca8;
interface_4_out_0x55ceeec82c58 -> interface_1_in_0x55ceeec82c58;

interface_1_out_0x55ceeb214920 -> interface_0_in_0x55ceeb214920;
interface_1_out_0x55ceeec84f70 -> interface_0_in_0x55ceeec84f70;
interface_1_out_0x55ceeec84f88 -> interface_0_in_0x55ceeec84f88;
interface_1_out_0x55ceeec839e0 -> interface_0_in_0x55ceeec839e0;
interface_1_out_0x55ceeb214998 -> interface_0_in_0x55ceeb214998;

{
    rank = same;
    interface_3_out_0x55ceeb214920;
    interface_3_out_0x55ceeec84c00;
    interface_3_out_0x55ceeec839e0;
    interface_3_out_0x55ceeec83a40;
    interface_4_out_0x55ceeec82c08;
    interface_4_out_0x55ceeec82ca8;
    interface_4_out_0x55ceeec82c58;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x55ceeb214920 [label="N", shape=none];
    interface_5_in_0x55ceeb214948 [label="C_out", shape=none];
    interface_5_in_0x55ceeb214970 [label="H", shape=none];
    interface_5_in_0x55ceeb214998 [label="H", shape=none];
}
interface_0_out_0x55ceeb214920 -> interface_5_in_0x55ceeb214920;
interface_0_out_0x55ceeb214948 -> interface_5_in_0x55ceeb214948;
interface_0_out_0x55ceeb214970 -> interface_5_in_0x55ceeb214970;
interface_0_out_0x55ceeb214998 -> interface_5_in_0x55ceeb214998;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 64, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 64, 56, 56, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 7168, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 64, 56, 3, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("loinjm, ikj -> loknm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 128, 56, 56, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 128, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 128, 28, 28, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 7168, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 128, 28, 3, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("loinjm, ikj -> loknm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 256, 28, 28, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 256, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 256, 14, 14, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 7168, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 256, 14, 3, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("loinjm, ikj -> loknm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 512, 14, 14, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 512, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 512, 7, 7, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_2 = torch.roll(t_2, self.shift_direction, 4)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 7168, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 512, 7, 3, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("loinjm, ikj -> loknm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 1024, 7, 7, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_4

		return y

