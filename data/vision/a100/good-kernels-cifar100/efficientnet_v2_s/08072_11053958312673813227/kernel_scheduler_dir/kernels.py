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
        interface_0_out_0x5581660a87e0 [label="N", shape=none];
        interface_0_out_0x5581660a8808 [label="C_out", shape=none];
        interface_0_out_0x5581660a8830 [label="H", shape=none];
        interface_0_out_0x5581660a8858 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x5581660a87e0;
        interface_0_out_0x5581660a8808;
        interface_0_out_0x5581660a8830;
        interface_0_out_0x5581660a8858;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5581660a87e0 [label="N", shape=none];
        interface_0_in_0x7fcf88006780 [label="s", shape=none];
        interface_0_in_0x7fcf88006798 [label="s^-1*C_out", shape=none];
        interface_0_in_0x7fcf7c003e60 [label="H", shape=none];
        interface_0_in_0x5581660a8858 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5581660a87e0;
        interface_0_in_0x7fcf88006780;
        interface_0_in_0x7fcf88006798;
        interface_0_in_0x7fcf7c003e60;
        interface_0_in_0x5581660a8858;
    }
    // Op's.
    op_0x7fcf7c003e40 [label="Shift"];
    op_0x7fcf88006740 [label="Merge"];
    // Dimension's.
    interface_0_in_0x5581660a87e0 -> interface_0_out_0x5581660a87e0 [label="N"];
    op_0x7fcf88006740 -> interface_0_out_0x5581660a8808 [label="C_out"];
    op_0x7fcf7c003e40 -> interface_0_out_0x5581660a8830 [label="H"];
    interface_0_in_0x5581660a8858 -> interface_0_out_0x5581660a8858 [label="H"];
    interface_0_in_0x7fcf7c003e60 -> op_0x7fcf7c003e40 [label="H"];
    interface_0_in_0x7fcf88006780 -> op_0x7fcf88006740 [label="s"];
    interface_0_in_0x7fcf88006798 -> op_0x7fcf88006740 [label="s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fc7f0005968 [label="Sum", shape=box];
    reduce_0x7fc7f0001de8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5581660a87e0 [label="N", shape=none];
        interface_1_out_0x7fcf88006780 [label="s", shape=none];
        interface_1_out_0x7fcf88006798 [label="s^-1*C_out", shape=none];
        interface_1_out_0x7fcf7c003e60 [label="H", shape=none];
        interface_1_out_0x5581660a8858 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc7f0005968;
        reduce_0x7fc7f0001de8;
        interface_1_out_0x5581660a87e0;
        interface_1_out_0x7fcf88006780;
        interface_1_out_0x7fcf88006798;
        interface_1_out_0x7fcf7c003e60;
        interface_1_out_0x5581660a8858;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5581660a87e0 [label="N", shape=none];
        interface_1_in_0x7fcf88006780 [label="s", shape=none];
        interface_1_in_0x7fcf58004aa0 [label="s^-1*C_in", shape=none];
        interface_1_in_0x7fcf7c003e60 [label="H", shape=none];
        interface_1_in_0x7fcf840041a0 [label="k_2", shape=none];
        interface_1_in_0x5581660a8858 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x7fcf58004ab8 [label="s^-1*C_in", shape=none];
        interface_1_in_0x7fcbc4005698 [label="s^-1*C_out", shape=none];
        interface_1_in_0x7fcf840041b8 [label="k_2", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5581660a87e0;
        interface_1_in_0x7fcf88006780;
        interface_1_in_0x7fcf58004aa0;
        interface_1_in_0x7fcf7c003e60;
        interface_1_in_0x7fcf840041a0;
        interface_1_in_0x5581660a8858;
        interface_1_in_0x7fcf58004ab8;
        interface_1_in_0x7fcbc4005698;
        interface_1_in_0x7fcf840041b8;
    }
    // Op's.
    op_0x7fcbc4005660 [label="Share"];
    op_0x7fcf58004a80 [label="Share"];
    op_0x7fcf84004180 [label="Share"];
    op_0x7fcf84004718 [label="Expand"];
    // Dimension's.
    interface_1_in_0x5581660a87e0 -> interface_1_out_0x5581660a87e0 [label="N"];
    interface_1_in_0x5581660a8858 -> interface_1_out_0x5581660a8858 [label="H"];
    op_0x7fcf84004180 -> reduce_0x7fc7f0001de8 [label="k_2"];
    op_0x7fcf58004a80 -> reduce_0x7fc7f0005968 [label="s^-1*C_in"];
    op_0x7fcf84004718 -> op_0x7fcbc4005660 [label="s^-1*C_out"];
    interface_1_in_0x7fcbc4005698 -> op_0x7fcbc4005660 [label="s^-1*C_out"];
    interface_1_in_0x7fcf58004aa0 -> op_0x7fcf58004a80 [label="s^-1*C_in"];
    interface_1_in_0x7fcf58004ab8 -> op_0x7fcf58004a80 [label="s^-1*C_in"];
    interface_1_in_0x7fcf7c003e60 -> interface_1_out_0x7fcf7c003e60 [label="H"];
    interface_1_in_0x7fcf840041a0 -> op_0x7fcf84004180 [label="k_2"];
    interface_1_in_0x7fcf840041b8 -> op_0x7fcf84004180 [label="k_2"];
    interface_1_in_0x7fcf88006780 -> interface_1_out_0x7fcf88006780 [label="s"];
    op_0x7fcbc4005660 -> interface_1_out_0x7fcf88006798 [label="s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5581660a87e0 [label="N", shape=none];
        interface_2_out_0x7fcf88006780 [label="s", shape=none];
        interface_2_out_0x7fcf58004aa0 [label="s^-1*C_in", shape=none];
        interface_2_out_0x7fcf7c003e60 [label="H", shape=none];
        interface_2_out_0x7fcf840041a0 [label="k_2", shape=none];
        interface_2_out_0x5581660a8858 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x5581660a87e0;
        interface_2_out_0x7fcf88006780;
        interface_2_out_0x7fcf58004aa0;
        interface_2_out_0x7fcf7c003e60;
        interface_2_out_0x7fcf840041a0;
        interface_2_out_0x5581660a8858;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5581660a87e0 [label="N", shape=none];
        interface_2_in_0x7fcf68048c70 [label="C_in", shape=none];
        interface_2_in_0x7fcf7c003e60 [label="H", shape=none];
        interface_2_in_0x7fcba8009f28 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5581660a87e0;
        interface_2_in_0x7fcf68048c70;
        interface_2_in_0x7fcf7c003e60;
        interface_2_in_0x7fcba8009f28;
    }
    // Op's.
    op_0x7fcba8009f00 [label="Unfold"];
    op_0x7fcf68048c30 [label="Split"];
    // Dimension's.
    interface_2_in_0x5581660a87e0 -> interface_2_out_0x5581660a87e0 [label="N"];
    op_0x7fcba8009f00 -> interface_2_out_0x5581660a8858 [label="H"];
    interface_2_in_0x7fcba8009f28 -> op_0x7fcba8009f00 [label="H"];
    op_0x7fcf68048c30 -> interface_2_out_0x7fcf58004aa0 [label="s^-1*C_in"];
    interface_2_in_0x7fcf68048c70 -> op_0x7fcf68048c30 [label="C_in"];
    interface_2_in_0x7fcf7c003e60 -> interface_2_out_0x7fcf7c003e60 [label="H"];
    op_0x7fcba8009f00 -> interface_2_out_0x7fcf840041a0 [label="k_2"];
    op_0x7fcf68048c30 -> interface_2_out_0x7fcf88006780 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_3 {
    label = "Input 0";
    interface_3_out_0x5581660a87e0 [label="N", shape=none];
    interface_3_out_0x7fcf68048c70 [label="C_in", shape=none];
    interface_3_out_0x7fcf7c003e60 [label="H", shape=none];
    interface_3_out_0x7fcba8009f28 [label="H", shape=none];
}

interface_3_out_0x5581660a87e0 -> interface_2_in_0x5581660a87e0;
interface_3_out_0x7fcf68048c70 -> interface_2_in_0x7fcf68048c70;
interface_3_out_0x7fcf7c003e60 -> interface_2_in_0x7fcf7c003e60;
interface_3_out_0x7fcba8009f28 -> interface_2_in_0x7fcba8009f28;

interface_2_out_0x5581660a87e0 -> interface_1_in_0x5581660a87e0;
interface_2_out_0x7fcf88006780 -> interface_1_in_0x7fcf88006780;
interface_2_out_0x7fcf58004aa0 -> interface_1_in_0x7fcf58004aa0;
interface_2_out_0x7fcf7c003e60 -> interface_1_in_0x7fcf7c003e60;
interface_2_out_0x7fcf840041a0 -> interface_1_in_0x7fcf840041a0;
interface_2_out_0x5581660a8858 -> interface_1_in_0x5581660a8858;

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 1";
    interface_4_out_0x7fcf58004ab8 [label="s^-1*C_in", shape=none];
    interface_4_out_0x7fcbc4005698 [label="s^-1*C_out", shape=none];
    interface_4_out_0x7fcf840041b8 [label="k_2", shape=none];
}

interface_4_out_0x7fcf58004ab8 -> interface_1_in_0x7fcf58004ab8;
interface_4_out_0x7fcbc4005698 -> interface_1_in_0x7fcbc4005698;
interface_4_out_0x7fcf840041b8 -> interface_1_in_0x7fcf840041b8;

interface_1_out_0x5581660a87e0 -> interface_0_in_0x5581660a87e0;
interface_1_out_0x7fcf88006780 -> interface_0_in_0x7fcf88006780;
interface_1_out_0x7fcf88006798 -> interface_0_in_0x7fcf88006798;
interface_1_out_0x7fcf7c003e60 -> interface_0_in_0x7fcf7c003e60;
interface_1_out_0x5581660a8858 -> interface_0_in_0x5581660a8858;

{
    rank = same;
    interface_3_out_0x5581660a87e0;
    interface_3_out_0x7fcf68048c70;
    interface_3_out_0x7fcf7c003e60;
    interface_3_out_0x7fcba8009f28;
    interface_4_out_0x7fcf58004ab8;
    interface_4_out_0x7fcbc4005698;
    interface_4_out_0x7fcf840041b8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_5_in_0x5581660a87e0 [label="N", shape=none];
    interface_5_in_0x5581660a8808 [label="C_out", shape=none];
    interface_5_in_0x5581660a8830 [label="H", shape=none];
    interface_5_in_0x5581660a8858 [label="H", shape=none];
}
interface_0_out_0x5581660a87e0 -> interface_5_in_0x5581660a87e0;
interface_0_out_0x5581660a8808 -> interface_5_in_0x5581660a8808;
interface_0_out_0x5581660a8830 -> interface_5_in_0x5581660a8830;
interface_0_out_0x5581660a8858 -> interface_5_in_0x5581660a8858;

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
		t_2 = torch.reshape(t_2, (128, 2, 12, 112, 112, ))

		# [H]@Unfold411df364a19ddc8b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Sharec0d065a85569cbbe
		t_2 = torch.reshape(t_2, (128, 2688, 112, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (7, 1, ), padding=(3, 0, ))
		t_2 = torch.reshape(t_2, (128, 2, 12, 112, 7, 112, ))

		# Perform contraction.
		t_3 = torch.einsum("lojnkm, jik -> loinm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (128, 24, 112, 112, ))

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
		t_2 = torch.reshape(t_2, (128, 2, 12, 56, 56, ))

		# [H]@Unfold411df364a19ddc8b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Sharec0d065a85569cbbe
		t_2 = torch.reshape(t_2, (128, 1344, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (7, 1, ), padding=(3, 0, ))
		t_2 = torch.reshape(t_2, (128, 2, 12, 56, 7, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("lojnkm, jik -> loinm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (128, 96, 56, 56, ))

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
		t_2 = torch.reshape(t_2, (128, 2, 24, 56, 56, ))

		# [H]@Unfold411df364a19ddc8b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Sharec0d065a85569cbbe
		t_2 = torch.reshape(t_2, (128, 2688, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (7, 1, ), padding=(3, 0, ))
		t_2 = torch.reshape(t_2, (128, 2, 24, 56, 7, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("lojnkm, jik -> loinm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (128, 192, 56, 56, ))

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
		t_2 = torch.reshape(t_2, (128, 2, 24, 28, 28, ))

		# [H]@Unfold411df364a19ddc8b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Sharec0d065a85569cbbe
		t_2 = torch.reshape(t_2, (128, 1344, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (7, 1, ), padding=(3, 0, ))
		t_2 = torch.reshape(t_2, (128, 2, 24, 28, 7, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("lojnkm, jik -> loinm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (128, 192, 28, 28, ))

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
		t_2 = torch.reshape(t_2, (128, 2, 32, 28, 28, ))

		# [H]@Unfold411df364a19ddc8b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Sharec0d065a85569cbbe
		t_2 = torch.reshape(t_2, (128, 1792, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (7, 1, ), padding=(3, 0, ))
		t_2 = torch.reshape(t_2, (128, 2, 32, 28, 7, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("lojnkm, jik -> loinm", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_4 = torch.reshape(t_4, (128, 256, 28, 28, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# No need to crop the output tensor.
		y = t_4

		return y

