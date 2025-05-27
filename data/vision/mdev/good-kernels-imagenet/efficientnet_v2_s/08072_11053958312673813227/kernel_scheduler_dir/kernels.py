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
        interface_0_out_0x5596d7788c60 [label="N", shape=none];
        interface_0_out_0x5596d7788c88 [label="C_out", shape=none];
        interface_0_out_0x5596d7788cb0 [label="H", shape=none];
        interface_0_out_0x5596d7788cd8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x5596d7788c60;
        interface_0_out_0x5596d7788c88;
        interface_0_out_0x5596d7788cb0;
        interface_0_out_0x5596d7788cd8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5596d7788c60 [label="N", shape=none];
        interface_0_in_0x5596d7877780 [label="s", shape=none];
        interface_0_in_0x5596d7877798 [label="s^-1*C_out", shape=none];
        interface_0_in_0x5596d7875ea0 [label="H", shape=none];
        interface_0_in_0x5596d7788cd8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5596d7788c60;
        interface_0_in_0x5596d7877780;
        interface_0_in_0x5596d7877798;
        interface_0_in_0x5596d7875ea0;
        interface_0_in_0x5596d7788cd8;
    }
    // Op's.
    op_0x5596d7875e80 [label="Shift"];
    op_0x5596d7877740 [label="Merge"];
    // Dimension's.
    interface_0_in_0x5596d7788c60 -> interface_0_out_0x5596d7788c60 [label="N"];
    op_0x5596d7877740 -> interface_0_out_0x5596d7788c88 [label="C_out"];
    op_0x5596d7875e80 -> interface_0_out_0x5596d7788cb0 [label="H"];
    interface_0_in_0x5596d7788cd8 -> interface_0_out_0x5596d7788cd8 [label="H"];
    interface_0_in_0x5596d7875ea0 -> op_0x5596d7875e80 [label="H"];
    interface_0_in_0x5596d7877780 -> op_0x5596d7877740 [label="s"];
    interface_0_in_0x5596d7877798 -> op_0x5596d7877740 [label="s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7ef0e4005768 [label="Sum", shape=box];
    reduce_0x7ef0e4001ee8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5596d7788c60 [label="N", shape=none];
        interface_1_out_0x5596d7877780 [label="s", shape=none];
        interface_1_out_0x5596d7877798 [label="s^-1*C_out", shape=none];
        interface_1_out_0x5596d7875ea0 [label="H", shape=none];
        interface_1_out_0x5596d7788cd8 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7ef0e4005768;
        reduce_0x7ef0e4001ee8;
        interface_1_out_0x5596d7788c60;
        interface_1_out_0x5596d7877780;
        interface_1_out_0x5596d7877798;
        interface_1_out_0x5596d7875ea0;
        interface_1_out_0x5596d7788cd8;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5596d7788c60 [label="N", shape=none];
        interface_1_in_0x5596d7877780 [label="s", shape=none];
        interface_1_in_0x5596d7875170 [label="s^-1*C_in", shape=none];
        interface_1_in_0x5596d7875ea0 [label="H", shape=none];
        interface_1_in_0x5596d78751c0 [label="k_2", shape=none];
        interface_1_in_0x5596d7788cd8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x5596d7875188 [label="s^-1*C_in", shape=none];
        interface_1_in_0x5596d7875278 [label="s^-1*C_out", shape=none];
        interface_1_in_0x5596d78751d8 [label="k_2", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5596d7788c60;
        interface_1_in_0x5596d7877780;
        interface_1_in_0x5596d7875170;
        interface_1_in_0x5596d7875ea0;
        interface_1_in_0x5596d78751c0;
        interface_1_in_0x5596d7788cd8;
        interface_1_in_0x5596d7875188;
        interface_1_in_0x5596d7875278;
        interface_1_in_0x5596d78751d8;
    }
    // Op's.
    op_0x5596d7875150 [label="Share"];
    op_0x5596d78751a0 [label="Share"];
    op_0x5596d7875240 [label="Share"];
    op_0x5596d7875638 [label="Expand"];
    // Dimension's.
    interface_1_in_0x5596d7788c60 -> interface_1_out_0x5596d7788c60 [label="N"];
    interface_1_in_0x5596d7788cd8 -> interface_1_out_0x5596d7788cd8 [label="H"];
    interface_1_in_0x5596d7875170 -> op_0x5596d7875150 [label="s^-1*C_in"];
    interface_1_in_0x5596d7875188 -> op_0x5596d7875150 [label="s^-1*C_in"];
    interface_1_in_0x5596d78751c0 -> op_0x5596d78751a0 [label="k_2"];
    interface_1_in_0x5596d78751d8 -> op_0x5596d78751a0 [label="k_2"];
    op_0x5596d7875638 -> op_0x5596d7875240 [label="s^-1*C_out"];
    interface_1_in_0x5596d7875278 -> op_0x5596d7875240 [label="s^-1*C_out"];
    interface_1_in_0x5596d7875ea0 -> interface_1_out_0x5596d7875ea0 [label="H"];
    interface_1_in_0x5596d7877780 -> interface_1_out_0x5596d7877780 [label="s"];
    op_0x5596d7875240 -> interface_1_out_0x5596d7877798 [label="s^-1*C_out"];
    op_0x5596d78751a0 -> reduce_0x7ef0e4001ee8 [label="k_2"];
    op_0x5596d7875150 -> reduce_0x7ef0e4005768 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5596d7788c60 [label="N", shape=none];
        interface_2_out_0x5596d7877780 [label="s", shape=none];
        interface_2_out_0x5596d7875170 [label="s^-1*C_in", shape=none];
        interface_2_out_0x5596d7875ea0 [label="H", shape=none];
        interface_2_out_0x5596d78751c0 [label="k_2", shape=none];
        interface_2_out_0x5596d7788cd8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x5596d7788c60;
        interface_2_out_0x5596d7877780;
        interface_2_out_0x5596d7875170;
        interface_2_out_0x5596d7875ea0;
        interface_2_out_0x5596d78751c0;
        interface_2_out_0x5596d7788cd8;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5596d7788c60 [label="N", shape=none];
        interface_2_in_0x5596d7882fc0 [label="C_in", shape=none];
        interface_2_in_0x5596d7875ea0 [label="H", shape=none];
        interface_2_in_0x5596d7879628 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5596d7788c60;
        interface_2_in_0x5596d7882fc0;
        interface_2_in_0x5596d7875ea0;
        interface_2_in_0x5596d7879628;
    }
    // Op's.
    op_0x5596d7879600 [label="Unfold"];
    op_0x5596d7882f80 [label="Split"];
    // Dimension's.
    interface_2_in_0x5596d7788c60 -> interface_2_out_0x5596d7788c60 [label="N"];
    op_0x5596d7879600 -> interface_2_out_0x5596d7788cd8 [label="H"];
    op_0x5596d7882f80 -> interface_2_out_0x5596d7875170 [label="s^-1*C_in"];
    op_0x5596d7879600 -> interface_2_out_0x5596d78751c0 [label="k_2"];
    interface_2_in_0x5596d7875ea0 -> interface_2_out_0x5596d7875ea0 [label="H"];
    op_0x5596d7882f80 -> interface_2_out_0x5596d7877780 [label="s"];
    interface_2_in_0x5596d7879628 -> op_0x5596d7879600 [label="H"];
    interface_2_in_0x5596d7882fc0 -> op_0x5596d7882f80 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x5596d7788c60 [label="N", shape=none];
    interface_3_out_0x5596d7882fc0 [label="C_in", shape=none];
    interface_3_out_0x5596d7875ea0 [label="H", shape=none];
    interface_3_out_0x5596d7879628 [label="H", shape=none];
}

interface_3_out_0x5596d7788c60 -> interface_2_in_0x5596d7788c60;
interface_3_out_0x5596d7882fc0 -> interface_2_in_0x5596d7882fc0;
interface_3_out_0x5596d7875ea0 -> interface_2_in_0x5596d7875ea0;
interface_3_out_0x5596d7879628 -> interface_2_in_0x5596d7879628;

interface_2_out_0x5596d7788c60 -> interface_1_in_0x5596d7788c60;
interface_2_out_0x5596d7877780 -> interface_1_in_0x5596d7877780;
interface_2_out_0x5596d7875170 -> interface_1_in_0x5596d7875170;
interface_2_out_0x5596d7875ea0 -> interface_1_in_0x5596d7875ea0;
interface_2_out_0x5596d78751c0 -> interface_1_in_0x5596d78751c0;
interface_2_out_0x5596d7788cd8 -> interface_1_in_0x5596d7788cd8;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x5596d7875188 [label="s^-1*C_in", shape=none];
    interface_4_out_0x5596d7875278 [label="s^-1*C_out", shape=none];
    interface_4_out_0x5596d78751d8 [label="k_2", shape=none];
}

interface_4_out_0x5596d7875188 -> interface_1_in_0x5596d7875188;
interface_4_out_0x5596d7875278 -> interface_1_in_0x5596d7875278;
interface_4_out_0x5596d78751d8 -> interface_1_in_0x5596d78751d8;

interface_1_out_0x5596d7788c60 -> interface_0_in_0x5596d7788c60;
interface_1_out_0x5596d7877780 -> interface_0_in_0x5596d7877780;
interface_1_out_0x5596d7877798 -> interface_0_in_0x5596d7877798;
interface_1_out_0x5596d7875ea0 -> interface_0_in_0x5596d7875ea0;
interface_1_out_0x5596d7788cd8 -> interface_0_in_0x5596d7788cd8;

{
    rank = same;
    interface_3_out_0x5596d7788c60;
    interface_3_out_0x5596d7882fc0;
    interface_3_out_0x5596d7875ea0;
    interface_3_out_0x5596d7879628;
    interface_4_out_0x5596d7875188;
    interface_4_out_0x5596d7875278;
    interface_4_out_0x5596d78751d8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x5596d7788c60 [label="N", shape=none];
    interface_5_in_0x5596d7788c88 [label="C_out", shape=none];
    interface_5_in_0x5596d7788cb0 [label="H", shape=none];
    interface_5_in_0x5596d7788cd8 [label="H", shape=none];
}
interface_0_out_0x5596d7788c60 -> interface_5_in_0x5596d7788c60;
interface_0_out_0x5596d7788c88 -> interface_5_in_0x5596d7788c88;
interface_0_out_0x5596d7788cb0 -> interface_5_in_0x5596d7788cb0;
interface_0_out_0x5596d7788cd8 -> interface_5_in_0x5596d7788cd8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([12, 12, 7]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 12, 112, 112, ))

		# [H]@Unfold411df364a19ddc8b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Sharec0d065a85569cbbe
		t_2 = torch.reshape(t_2, (1, 2688, 112, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (7, 1, ), padding=(3, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 12, 112, 7, 112, ))

		# Perform contraction.
		t_3 = torch.einsum("loinjm, ikj -> loknm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 24, 112, 112, ))

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
			torch.randn([12, 48, 7]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 12, 56, 56, ))

		# [H]@Unfold411df364a19ddc8b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Sharec0d065a85569cbbe
		t_2 = torch.reshape(t_2, (1, 1344, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (7, 1, ), padding=(3, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 12, 56, 7, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("loinjm, ikj -> loknm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 96, 56, 56, ))

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
			torch.randn([24, 96, 7]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 24, 56, 56, ))

		# [H]@Unfold411df364a19ddc8b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Sharec0d065a85569cbbe
		t_2 = torch.reshape(t_2, (1, 2688, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (7, 1, ), padding=(3, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 24, 56, 7, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("loinjm, ikj -> loknm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 192, 56, 56, ))

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
			torch.randn([24, 96, 7]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 24, 28, 28, ))

		# [H]@Unfold411df364a19ddc8b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Sharec0d065a85569cbbe
		t_2 = torch.reshape(t_2, (1, 1344, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (7, 1, ), padding=(3, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 24, 28, 7, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("loinjm, ikj -> loknm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (1, 192, 28, 28, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_4

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 128, 7]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Split69dd43e05c8c5ddb -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share8de6f167adbbf8aa
		t_2 = torch.reshape(t_2, (1, 2, 32, 28, 28, ))

		# [H]@Unfold411df364a19ddc8b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Sharec0d065a85569cbbe
		t_2 = torch.reshape(t_2, (1, 1792, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (7, 1, ), padding=(3, 0, ))
		t_2 = torch.reshape(t_2, (1, 2, 32, 28, 7, 28, ))

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

