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
        interface_0_in_0x5581660a8830 [label="H", shape=none];
        interface_0_in_0x5581660a8858 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5581660a87e0;
        interface_0_in_0x7fcf88006780;
        interface_0_in_0x7fcf88006798;
        interface_0_in_0x5581660a8830;
        interface_0_in_0x5581660a8858;
    }
    // Op's.
    op_0x7fcf88006740 [label="Merge"];
    // Dimension's.
    interface_0_in_0x5581660a87e0 -> interface_0_out_0x5581660a87e0 [label="N"];
    op_0x7fcf88006740 -> interface_0_out_0x5581660a8808 [label="C_out"];
    interface_0_in_0x5581660a8830 -> interface_0_out_0x5581660a8830 [label="H"];
    interface_0_in_0x5581660a8858 -> interface_0_out_0x5581660a8858 [label="H"];
    interface_0_in_0x7fcf88006780 -> op_0x7fcf88006740 [label="s"];
    interface_0_in_0x7fcf88006798 -> op_0x7fcf88006740 [label="s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fc7f0001bc0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5581660a87e0 [label="N", shape=none];
        interface_1_out_0x7fcf88006780 [label="s", shape=none];
        interface_1_out_0x7fcf88006798 [label="s^-1*C_out", shape=none];
        interface_1_out_0x5581660a8830 [label="H", shape=none];
        interface_1_out_0x5581660a8858 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc7f0001bc0;
        interface_1_out_0x5581660a87e0;
        interface_1_out_0x7fcf88006780;
        interface_1_out_0x7fcf88006798;
        interface_1_out_0x5581660a8830;
        interface_1_out_0x5581660a8858;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5581660a87e0 [label="N", shape=none];
        interface_1_in_0x7fcf88006780 [label="s", shape=none];
        interface_1_in_0x5581660a8830 [label="H", shape=none];
        interface_1_in_0x5581660a8858 [label="H", shape=none];
        interface_1_in_0x7fcf58004dc0 [label="k_1^2", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x7fcbc4005698 [label="s^-1*C_out", shape=none];
        interface_1_in_0x7fcf58004dd8 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5581660a87e0;
        interface_1_in_0x7fcf88006780;
        interface_1_in_0x5581660a8830;
        interface_1_in_0x5581660a8858;
        interface_1_in_0x7fcf58004dc0;
        interface_1_in_0x7fcbc4005698;
        interface_1_in_0x7fcf58004dd8;
    }
    // Op's.
    op_0x7fcbc4005660 [label="Share"];
    op_0x7fcf58004da0 [label="Share"];
    op_0x7fcf84004718 [label="Expand"];
    // Dimension's.
    interface_1_in_0x5581660a87e0 -> interface_1_out_0x5581660a87e0 [label="N"];
    interface_1_in_0x5581660a8830 -> interface_1_out_0x5581660a8830 [label="H"];
    interface_1_in_0x5581660a8858 -> interface_1_out_0x5581660a8858 [label="H"];
    op_0x7fcf58004da0 -> reduce_0x7fc7f0001bc0 [label="k_1^2"];
    op_0x7fcf84004718 -> op_0x7fcbc4005660 [label="s^-1*C_out"];
    interface_1_in_0x7fcbc4005698 -> op_0x7fcbc4005660 [label="s^-1*C_out"];
    interface_1_in_0x7fcf58004dc0 -> op_0x7fcf58004da0 [label="k_1^2"];
    interface_1_in_0x7fcf58004dd8 -> op_0x7fcf58004da0 [label="k_1^2"];
    interface_1_in_0x7fcf88006780 -> interface_1_out_0x7fcf88006780 [label="s"];
    op_0x7fcbc4005660 -> interface_1_out_0x7fcf88006798 [label="s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7fc7f0005968 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5581660a87e0 [label="N", shape=none];
        interface_2_out_0x7fcf88006780 [label="s", shape=none];
        interface_2_out_0x5581660a8830 [label="H", shape=none];
        interface_2_out_0x5581660a8858 [label="H", shape=none];
        interface_2_out_0x7fcf58004dc0 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc7f0005968;
        interface_2_out_0x5581660a87e0;
        interface_2_out_0x7fcf88006780;
        interface_2_out_0x5581660a8830;
        interface_2_out_0x5581660a8858;
        interface_2_out_0x7fcf58004dc0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5581660a87e0 [label="N", shape=none];
        interface_2_in_0x7fccc8013fd0 [label="C_in", shape=none];
        interface_2_in_0x5581660a8830 [label="H", shape=none];
        interface_2_in_0x5581660a8858 [label="H", shape=none];
        interface_2_in_0x7fcf58004dc0 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5581660a87e0;
        interface_2_in_0x7fccc8013fd0;
        interface_2_in_0x5581660a8830;
        interface_2_in_0x5581660a8858;
        interface_2_in_0x7fcf58004dc0;
    }
    // Op's.
    op_0x7fccc8013f90 [label="Split"];
    // Dimension's.
    interface_2_in_0x5581660a87e0 -> interface_2_out_0x5581660a87e0 [label="N"];
    interface_2_in_0x5581660a8830 -> interface_2_out_0x5581660a8830 [label="H"];
    interface_2_in_0x5581660a8858 -> interface_2_out_0x5581660a8858 [label="H"];
    op_0x7fccc8013f90 -> reduce_0x7fc7f0005968 [label="s^-1*C_in"];
    interface_2_in_0x7fccc8013fd0 -> op_0x7fccc8013f90 [label="C_in"];
    interface_2_in_0x7fcf58004dc0 -> interface_2_out_0x7fcf58004dc0 [label="k_1^2"];
    op_0x7fccc8013f90 -> interface_2_out_0x7fcf88006780 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5581660a87e0 [label="N", shape=none];
        interface_3_out_0x7fccc8013fd0 [label="C_in", shape=none];
        interface_3_out_0x5581660a8830 [label="H", shape=none];
        interface_3_out_0x5581660a8858 [label="H", shape=none];
        interface_3_out_0x7fcf58004dc0 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5581660a87e0;
        interface_3_out_0x7fccc8013fd0;
        interface_3_out_0x5581660a8830;
        interface_3_out_0x5581660a8858;
        interface_3_out_0x7fcf58004dc0;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5581660a87e0 [label="N", shape=none];
        interface_3_in_0x7fcad00a24c0 [label="C_in", shape=none];
        interface_3_in_0x5581660a8858 [label="H", shape=none];
        interface_3_in_0x5581660a8830 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x7fcad00a24d8 [label="C_in", shape=none];
        interface_3_in_0x7fc950008cb8 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5581660a87e0;
        interface_3_in_0x7fcad00a24c0;
        interface_3_in_0x5581660a8858;
        interface_3_in_0x5581660a8830;
        interface_3_in_0x7fcad00a24d8;
        interface_3_in_0x7fc950008cb8;
    }
    // Op's.
    op_0x7fc950008c80 [label="Share"];
    op_0x7fcad00a24a0 [label="Share"];
    op_0x7fcf840049b8 [label="Expand"];
    // Dimension's.
    interface_3_in_0x5581660a87e0 -> interface_3_out_0x5581660a87e0 [label="N"];
    interface_3_in_0x5581660a8830 -> interface_3_out_0x5581660a8830 [label="H"];
    interface_3_in_0x5581660a8858 -> interface_3_out_0x5581660a8858 [label="H"];
    op_0x7fcf840049b8 -> op_0x7fc950008c80 [label="k_1^2"];
    interface_3_in_0x7fc950008cb8 -> op_0x7fc950008c80 [label="k_1^2"];
    interface_3_in_0x7fcad00a24c0 -> op_0x7fcad00a24a0 [label="C_in"];
    interface_3_in_0x7fcad00a24d8 -> op_0x7fcad00a24a0 [label="C_in"];
    op_0x7fcad00a24a0 -> interface_3_out_0x7fccc8013fd0 [label="C_in"];
    op_0x7fc950008c80 -> interface_3_out_0x7fcf58004dc0 [label="k_1^2"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x5581660a87e0 [label="N", shape=none];
    interface_4_out_0x7fcad00a24c0 [label="C_in", shape=none];
    interface_4_out_0x5581660a8858 [label="H", shape=none];
    interface_4_out_0x5581660a8830 [label="H", shape=none];
}

interface_4_out_0x5581660a87e0 -> interface_3_in_0x5581660a87e0;
interface_4_out_0x7fcad00a24c0 -> interface_3_in_0x7fcad00a24c0;
interface_4_out_0x5581660a8858 -> interface_3_in_0x5581660a8858;
interface_4_out_0x5581660a8830 -> interface_3_in_0x5581660a8830;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 2";
    interface_5_out_0x7fcad00a24d8 [label="C_in", shape=none];
    interface_5_out_0x7fc950008cb8 [label="k_1^2", shape=none];
}

interface_5_out_0x7fcad00a24d8 -> interface_3_in_0x7fcad00a24d8;
interface_5_out_0x7fc950008cb8 -> interface_3_in_0x7fc950008cb8;

interface_3_out_0x5581660a87e0 -> interface_2_in_0x5581660a87e0;
interface_3_out_0x7fccc8013fd0 -> interface_2_in_0x7fccc8013fd0;
interface_3_out_0x5581660a8830 -> interface_2_in_0x5581660a8830;
interface_3_out_0x5581660a8858 -> interface_2_in_0x5581660a8858;
interface_3_out_0x7fcf58004dc0 -> interface_2_in_0x7fcf58004dc0;

interface_2_out_0x5581660a87e0 -> interface_1_in_0x5581660a87e0;
interface_2_out_0x7fcf88006780 -> interface_1_in_0x7fcf88006780;
interface_2_out_0x5581660a8830 -> interface_1_in_0x5581660a8830;
interface_2_out_0x5581660a8858 -> interface_1_in_0x5581660a8858;
interface_2_out_0x7fcf58004dc0 -> interface_1_in_0x7fcf58004dc0;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 1";
    interface_6_out_0x7fcbc4005698 [label="s^-1*C_out", shape=none];
    interface_6_out_0x7fcf58004dd8 [label="k_1^2", shape=none];
}

interface_6_out_0x7fcbc4005698 -> interface_1_in_0x7fcbc4005698;
interface_6_out_0x7fcf58004dd8 -> interface_1_in_0x7fcf58004dd8;

interface_1_out_0x5581660a87e0 -> interface_0_in_0x5581660a87e0;
interface_1_out_0x7fcf88006780 -> interface_0_in_0x7fcf88006780;
interface_1_out_0x7fcf88006798 -> interface_0_in_0x7fcf88006798;
interface_1_out_0x5581660a8830 -> interface_0_in_0x5581660a8830;
interface_1_out_0x5581660a8858 -> interface_0_in_0x5581660a8858;

{
    rank = same;
    interface_4_out_0x5581660a87e0;
    interface_4_out_0x7fcad00a24c0;
    interface_4_out_0x5581660a8858;
    interface_4_out_0x5581660a8830;
    interface_6_out_0x7fcbc4005698;
    interface_6_out_0x7fcf58004dd8;
    interface_5_out_0x7fcad00a24d8;
    interface_5_out_0x7fc950008cb8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_7_in_0x5581660a87e0 [label="N", shape=none];
    interface_7_in_0x5581660a8808 [label="C_out", shape=none];
    interface_7_in_0x5581660a8830 [label="H", shape=none];
    interface_7_in_0x5581660a8858 [label="H", shape=none];
}
interface_0_out_0x5581660a87e0 -> interface_7_in_0x5581660a87e0;
interface_0_out_0x5581660a8808 -> interface_7_in_0x5581660a8808;
interface_0_out_0x5581660a8830 -> interface_7_in_0x5581660a8830;
interface_0_out_0x5581660a8858 -> interface_7_in_0x5581660a8858;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([12, 9]),
			torch.randn([24, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("kjml, ji -> kjlmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [C_in]@Split75a539c6b0ba4a63 -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Reducee9b9071fb9943ecb
		t_4 = torch.reshape(t_4, (128, 2, 12, 112, 112, 9, ))

		# [s^-1*C_in]@Reduce
		t_4 = torch.sum(t_4, dim=(2, ))

		# Perform contraction.
		t_5 = torch.einsum("knlmj, ij -> knilm", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_6 = torch.reshape(t_6, (128, 24, 112, 112, ))

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([48, 9]),
			torch.randn([24, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("kjml, ji -> kjlmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [C_in]@Split75a539c6b0ba4a63 -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Reducee9b9071fb9943ecb
		t_4 = torch.reshape(t_4, (128, 2, 12, 56, 56, 9, ))

		# [s^-1*C_in]@Reduce
		t_4 = torch.sum(t_4, dim=(2, ))

		# Perform contraction.
		t_5 = torch.einsum("knlmj, ij -> knilm", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_6 = torch.reshape(t_6, (128, 96, 56, 56, ))

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([96, 9]),
			torch.randn([48, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("kjml, ji -> kjlmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [C_in]@Split75a539c6b0ba4a63 -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Reducee9b9071fb9943ecb
		t_4 = torch.reshape(t_4, (128, 2, 24, 56, 56, 9, ))

		# [s^-1*C_in]@Reduce
		t_4 = torch.sum(t_4, dim=(2, ))

		# Perform contraction.
		t_5 = torch.einsum("knlmj, ij -> knilm", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_6 = torch.reshape(t_6, (128, 192, 56, 56, ))

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([96, 9]),
			torch.randn([48, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("kjml, ji -> kjlmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [C_in]@Split75a539c6b0ba4a63 -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Reducee9b9071fb9943ecb
		t_4 = torch.reshape(t_4, (128, 2, 24, 28, 28, 9, ))

		# [s^-1*C_in]@Reduce
		t_4 = torch.sum(t_4, dim=(2, ))

		# Perform contraction.
		t_5 = torch.einsum("knlmj, ij -> knilm", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_6 = torch.reshape(t_6, (128, 192, 28, 28, ))

		# No need to crop the output tensor.
		y = t_6

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 9]),
			torch.randn([64, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# Perform contraction.
		t_3 = torch.einsum("kjml, ji -> kjlmi", in_0, in_2)

		# No contraction needed.
		t_4 = t_3

		# [C_in]@Split75a539c6b0ba4a63 -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Reducee9b9071fb9943ecb
		t_4 = torch.reshape(t_4, (128, 2, 32, 28, 28, 9, ))

		# [s^-1*C_in]@Reduce
		t_4 = torch.sum(t_4, dim=(2, ))

		# Perform contraction.
		t_5 = torch.einsum("knlmj, ij -> knilm", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_6 = torch.reshape(t_6, (128, 256, 28, 28, ))

		# No need to crop the output tensor.
		y = t_6

		return y

