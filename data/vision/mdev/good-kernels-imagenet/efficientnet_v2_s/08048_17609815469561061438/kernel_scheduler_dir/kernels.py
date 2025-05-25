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
        interface_0_in_0x7fcf7c003e90 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5581660a87e0;
        interface_0_in_0x7fcf88006780;
        interface_0_in_0x7fcf88006798;
        interface_0_in_0x5581660a8830;
        interface_0_in_0x7fcf7c003e90;
    }
    // Op's.
    op_0x7fcf7c003e70 [label="Shift"];
    op_0x7fcf88006740 [label="Merge"];
    // Dimension's.
    interface_0_in_0x5581660a87e0 -> interface_0_out_0x5581660a87e0 [label="N"];
    op_0x7fcf88006740 -> interface_0_out_0x5581660a8808 [label="C_out"];
    interface_0_in_0x5581660a8830 -> interface_0_out_0x5581660a8830 [label="H"];
    op_0x7fcf7c003e70 -> interface_0_out_0x5581660a8858 [label="H"];
    interface_0_in_0x7fcf7c003e90 -> op_0x7fcf7c003e70 [label="H"];
    interface_0_in_0x7fcf88006780 -> op_0x7fcf88006740 [label="s"];
    interface_0_in_0x7fcf88006798 -> op_0x7fcf88006740 [label="s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fc7f0001de8 [label="Sum", shape=box];
    reduce_0x7fc7f0001bc0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5581660a87e0 [label="N", shape=none];
        interface_1_out_0x7fcf88006780 [label="s", shape=none];
        interface_1_out_0x7fcf88006798 [label="s^-1*C_out", shape=none];
        interface_1_out_0x5581660a8830 [label="H", shape=none];
        interface_1_out_0x7fcf7c003e90 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc7f0001de8;
        reduce_0x7fc7f0001bc0;
        interface_1_out_0x5581660a87e0;
        interface_1_out_0x7fcf88006780;
        interface_1_out_0x7fcf88006798;
        interface_1_out_0x5581660a8830;
        interface_1_out_0x7fcf7c003e90;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5581660a87e0 [label="N", shape=none];
        interface_1_in_0x7fcf88006780 [label="s", shape=none];
        interface_1_in_0x7fcf840041a0 [label="k_2", shape=none];
        interface_1_in_0x5581660a8830 [label="H", shape=none];
        interface_1_in_0x7fcf7c003e90 [label="H", shape=none];
        interface_1_in_0x7fcf58004dc0 [label="k_1^2", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x7fcbc4005698 [label="s^-1*C_out", shape=none];
        interface_1_in_0x7fcf840041b8 [label="k_2", shape=none];
        interface_1_in_0x7fcf58004dd8 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5581660a87e0;
        interface_1_in_0x7fcf88006780;
        interface_1_in_0x7fcf840041a0;
        interface_1_in_0x5581660a8830;
        interface_1_in_0x7fcf7c003e90;
        interface_1_in_0x7fcf58004dc0;
        interface_1_in_0x7fcbc4005698;
        interface_1_in_0x7fcf840041b8;
        interface_1_in_0x7fcf58004dd8;
    }
    // Op's.
    op_0x7fcbc4005660 [label="Share"];
    op_0x7fcf58004da0 [label="Share"];
    op_0x7fcf84004180 [label="Share"];
    op_0x7fcf84004718 [label="Expand"];
    // Dimension's.
    interface_1_in_0x5581660a87e0 -> interface_1_out_0x5581660a87e0 [label="N"];
    interface_1_in_0x5581660a8830 -> interface_1_out_0x5581660a8830 [label="H"];
    op_0x7fcf58004da0 -> reduce_0x7fc7f0001bc0 [label="k_1^2"];
    op_0x7fcf84004180 -> reduce_0x7fc7f0001de8 [label="k_2"];
    op_0x7fcf84004718 -> op_0x7fcbc4005660 [label="s^-1*C_out"];
    interface_1_in_0x7fcbc4005698 -> op_0x7fcbc4005660 [label="s^-1*C_out"];
    interface_1_in_0x7fcf58004dc0 -> op_0x7fcf58004da0 [label="k_1^2"];
    interface_1_in_0x7fcf58004dd8 -> op_0x7fcf58004da0 [label="k_1^2"];
    interface_1_in_0x7fcf7c003e90 -> interface_1_out_0x7fcf7c003e90 [label="H"];
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
        interface_2_out_0x7fcf840041a0 [label="k_2", shape=none];
        interface_2_out_0x5581660a8830 [label="H", shape=none];
        interface_2_out_0x7fcf7c003e90 [label="H", shape=none];
        interface_2_out_0x7fcf58004dc0 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x5581660a87e0;
        interface_2_out_0x7fcf88006780;
        interface_2_out_0x7fcf840041a0;
        interface_2_out_0x5581660a8830;
        interface_2_out_0x7fcf7c003e90;
        interface_2_out_0x7fcf58004dc0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5581660a87e0 [label="N", shape=none];
        interface_2_in_0x7fcf88006780 [label="s", shape=none];
        interface_2_in_0x7fce0006b390 [label="H", shape=none];
        interface_2_in_0x7fcf7c003e90 [label="H", shape=none];
        interface_2_in_0x7fcf58004dc0 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5581660a87e0;
        interface_2_in_0x7fcf88006780;
        interface_2_in_0x7fce0006b390;
        interface_2_in_0x7fcf7c003e90;
        interface_2_in_0x7fcf58004dc0;
    }
    // Op's.
    op_0x7fcba8009ec0 [label="Unfold"];
    op_0x7fce0006b370 [label="Shift"];
    // Dimension's.
    interface_2_in_0x5581660a87e0 -> interface_2_out_0x5581660a87e0 [label="N"];
    op_0x7fcba8009ec0 -> interface_2_out_0x5581660a8830 [label="H"];
    op_0x7fce0006b370 -> op_0x7fcba8009ec0 [label="H"];
    interface_2_in_0x7fce0006b390 -> op_0x7fce0006b370 [label="H"];
    interface_2_in_0x7fcf58004dc0 -> interface_2_out_0x7fcf58004dc0 [label="k_1^2"];
    interface_2_in_0x7fcf7c003e90 -> interface_2_out_0x7fcf7c003e90 [label="H"];
    op_0x7fcba8009ec0 -> interface_2_out_0x7fcf840041a0 [label="k_2"];
    interface_2_in_0x7fcf88006780 -> interface_2_out_0x7fcf88006780 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7fc7f0005968 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5581660a87e0 [label="N", shape=none];
        interface_3_out_0x7fcf88006780 [label="s", shape=none];
        interface_3_out_0x7fce0006b390 [label="H", shape=none];
        interface_3_out_0x7fcf7c003e90 [label="H", shape=none];
        interface_3_out_0x7fcf58004dc0 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc7f0005968;
        interface_3_out_0x5581660a87e0;
        interface_3_out_0x7fcf88006780;
        interface_3_out_0x7fce0006b390;
        interface_3_out_0x7fcf7c003e90;
        interface_3_out_0x7fcf58004dc0;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5581660a87e0 [label="N", shape=none];
        interface_3_in_0x7fcf88006780 [label="s", shape=none];
        interface_3_in_0x7fc950009e70 [label="s^-1*C_in", shape=none];
        interface_3_in_0x7fce0006b390 [label="H", shape=none];
        interface_3_in_0x7fcf7c003e90 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x7fc950009e88 [label="s^-1*C_in", shape=none];
        interface_3_in_0x7fc950008cb8 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5581660a87e0;
        interface_3_in_0x7fcf88006780;
        interface_3_in_0x7fc950009e70;
        interface_3_in_0x7fce0006b390;
        interface_3_in_0x7fcf7c003e90;
        interface_3_in_0x7fc950009e88;
        interface_3_in_0x7fc950008cb8;
    }
    // Op's.
    op_0x7fc950008c80 [label="Share"];
    op_0x7fc950009e50 [label="Share"];
    op_0x7fcf840049b8 [label="Expand"];
    // Dimension's.
    interface_3_in_0x5581660a87e0 -> interface_3_out_0x5581660a87e0 [label="N"];
    op_0x7fc950009e50 -> reduce_0x7fc7f0005968 [label="s^-1*C_in"];
    op_0x7fcf840049b8 -> op_0x7fc950008c80 [label="k_1^2"];
    interface_3_in_0x7fc950008cb8 -> op_0x7fc950008c80 [label="k_1^2"];
    interface_3_in_0x7fc950009e70 -> op_0x7fc950009e50 [label="s^-1*C_in"];
    interface_3_in_0x7fc950009e88 -> op_0x7fc950009e50 [label="s^-1*C_in"];
    interface_3_in_0x7fce0006b390 -> interface_3_out_0x7fce0006b390 [label="H"];
    op_0x7fc950008c80 -> interface_3_out_0x7fcf58004dc0 [label="k_1^2"];
    interface_3_in_0x7fcf7c003e90 -> interface_3_out_0x7fcf7c003e90 [label="H"];
    interface_3_in_0x7fcf88006780 -> interface_3_out_0x7fcf88006780 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x5581660a87e0 [label="N", shape=none];
        interface_4_out_0x7fcf88006780 [label="s", shape=none];
        interface_4_out_0x7fc950009e70 [label="s^-1*C_in", shape=none];
        interface_4_out_0x7fce0006b390 [label="H", shape=none];
        interface_4_out_0x7fcf7c003e90 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x5581660a87e0;
        interface_4_out_0x7fcf88006780;
        interface_4_out_0x7fc950009e70;
        interface_4_out_0x7fce0006b390;
        interface_4_out_0x7fcf7c003e90;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x5581660a87e0 [label="N", shape=none];
        interface_4_in_0x7fca441d0040 [label="C_in", shape=none];
        interface_4_in_0x7fce0006b390 [label="H", shape=none];
        interface_4_in_0x7fcf7c003e90 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x5581660a87e0;
        interface_4_in_0x7fca441d0040;
        interface_4_in_0x7fce0006b390;
        interface_4_in_0x7fcf7c003e90;
    }
    // Op's.
    op_0x7fca441d0000 [label="Split"];
    // Dimension's.
    interface_4_in_0x5581660a87e0 -> interface_4_out_0x5581660a87e0 [label="N"];
    op_0x7fca441d0000 -> interface_4_out_0x7fc950009e70 [label="s^-1*C_in"];
    interface_4_in_0x7fca441d0040 -> op_0x7fca441d0000 [label="C_in"];
    interface_4_in_0x7fce0006b390 -> interface_4_out_0x7fce0006b390 [label="H"];
    interface_4_in_0x7fcf7c003e90 -> interface_4_out_0x7fcf7c003e90 [label="H"];
    op_0x7fca441d0000 -> interface_4_out_0x7fcf88006780 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x5581660a87e0 [label="N", shape=none];
    interface_5_out_0x7fca441d0040 [label="C_in", shape=none];
    interface_5_out_0x7fce0006b390 [label="H", shape=none];
    interface_5_out_0x7fcf7c003e90 [label="H", shape=none];
}

interface_5_out_0x5581660a87e0 -> interface_4_in_0x5581660a87e0;
interface_5_out_0x7fca441d0040 -> interface_4_in_0x7fca441d0040;
interface_5_out_0x7fce0006b390 -> interface_4_in_0x7fce0006b390;
interface_5_out_0x7fcf7c003e90 -> interface_4_in_0x7fcf7c003e90;

interface_4_out_0x5581660a87e0 -> interface_3_in_0x5581660a87e0;
interface_4_out_0x7fcf88006780 -> interface_3_in_0x7fcf88006780;
interface_4_out_0x7fc950009e70 -> interface_3_in_0x7fc950009e70;
interface_4_out_0x7fce0006b390 -> interface_3_in_0x7fce0006b390;
interface_4_out_0x7fcf7c003e90 -> interface_3_in_0x7fcf7c003e90;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x7fc950009e88 [label="s^-1*C_in", shape=none];
    interface_6_out_0x7fc950008cb8 [label="k_1^2", shape=none];
}

interface_6_out_0x7fc950009e88 -> interface_3_in_0x7fc950009e88;
interface_6_out_0x7fc950008cb8 -> interface_3_in_0x7fc950008cb8;

interface_3_out_0x5581660a87e0 -> interface_2_in_0x5581660a87e0;
interface_3_out_0x7fcf88006780 -> interface_2_in_0x7fcf88006780;
interface_3_out_0x7fce0006b390 -> interface_2_in_0x7fce0006b390;
interface_3_out_0x7fcf7c003e90 -> interface_2_in_0x7fcf7c003e90;
interface_3_out_0x7fcf58004dc0 -> interface_2_in_0x7fcf58004dc0;

interface_2_out_0x5581660a87e0 -> interface_1_in_0x5581660a87e0;
interface_2_out_0x7fcf88006780 -> interface_1_in_0x7fcf88006780;
interface_2_out_0x7fcf840041a0 -> interface_1_in_0x7fcf840041a0;
interface_2_out_0x5581660a8830 -> interface_1_in_0x5581660a8830;
interface_2_out_0x7fcf7c003e90 -> interface_1_in_0x7fcf7c003e90;
interface_2_out_0x7fcf58004dc0 -> interface_1_in_0x7fcf58004dc0;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x7fcbc4005698 [label="s^-1*C_out", shape=none];
    interface_7_out_0x7fcf840041b8 [label="k_2", shape=none];
    interface_7_out_0x7fcf58004dd8 [label="k_1^2", shape=none];
}

interface_7_out_0x7fcbc4005698 -> interface_1_in_0x7fcbc4005698;
interface_7_out_0x7fcf840041b8 -> interface_1_in_0x7fcf840041b8;
interface_7_out_0x7fcf58004dd8 -> interface_1_in_0x7fcf58004dd8;

interface_1_out_0x5581660a87e0 -> interface_0_in_0x5581660a87e0;
interface_1_out_0x7fcf88006780 -> interface_0_in_0x7fcf88006780;
interface_1_out_0x7fcf88006798 -> interface_0_in_0x7fcf88006798;
interface_1_out_0x5581660a8830 -> interface_0_in_0x5581660a8830;
interface_1_out_0x7fcf7c003e90 -> interface_0_in_0x7fcf7c003e90;

{
    rank = same;
    interface_5_out_0x5581660a87e0;
    interface_5_out_0x7fca441d0040;
    interface_5_out_0x7fce0006b390;
    interface_5_out_0x7fcf7c003e90;
    interface_7_out_0x7fcbc4005698;
    interface_7_out_0x7fcf840041b8;
    interface_7_out_0x7fcf58004dd8;
    interface_6_out_0x7fc950009e88;
    interface_6_out_0x7fc950008cb8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x5581660a87e0 [label="N", shape=none];
    interface_8_in_0x5581660a8808 [label="C_out", shape=none];
    interface_8_in_0x5581660a8830 [label="H", shape=none];
    interface_8_in_0x5581660a8858 [label="H", shape=none];
}
interface_0_out_0x5581660a87e0 -> interface_8_in_0x5581660a87e0;
interface_0_out_0x5581660a8808 -> interface_8_in_0x5581660a8808;
interface_0_out_0x5581660a8830 -> interface_8_in_0x5581660a8830;
interface_0_out_0x5581660a8858 -> interface_8_in_0x5581660a8858;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([12, 7, 9]),
			torch.randn([12, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split69dd43e0c9ec9c4b -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share010730f7adbbf8aa
		t_3 = torch.reshape(t_3, (128, 2, 12, 112, 112, ))

		# Perform contraction.
		t_4 = torch.einsum("knjlm, ji -> knlmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift55a06fa4f7c5d730 -> [H]@Unfold820e0f3eb05a896f
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# [H]@Unfold820e0f3eb05a896f -> [H]@Iterator96123ba3184da39c, [k_2]@Sharec0d065a85569cbbe
		t_5 = torch.reshape(t_5, (128, 2, 112, 1008, ))
		t_5 = torch.nn.functional.unfold(t_5, (7, 1, ), padding=(3, 0, ))
		t_5 = torch.reshape(t_5, (128, 2, 7, 112, 112, 9, ))

		# Perform contraction.
		t_6 = torch.einsum("lokmnj, ikj -> loimn", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (128, 24, 112, 112, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([48, 7, 9]),
			torch.randn([12, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split69dd43e0c9ec9c4b -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share010730f7adbbf8aa
		t_3 = torch.reshape(t_3, (128, 2, 12, 56, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("knjlm, ji -> knlmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift55a06fa4f7c5d730 -> [H]@Unfold820e0f3eb05a896f
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# [H]@Unfold820e0f3eb05a896f -> [H]@Iterator96123ba3184da39c, [k_2]@Sharec0d065a85569cbbe
		t_5 = torch.reshape(t_5, (128, 2, 56, 504, ))
		t_5 = torch.nn.functional.unfold(t_5, (7, 1, ), padding=(3, 0, ))
		t_5 = torch.reshape(t_5, (128, 2, 7, 56, 56, 9, ))

		# Perform contraction.
		t_6 = torch.einsum("lokmnj, ikj -> loimn", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (128, 96, 56, 56, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([96, 7, 9]),
			torch.randn([24, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split69dd43e0c9ec9c4b -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share010730f7adbbf8aa
		t_3 = torch.reshape(t_3, (128, 2, 24, 56, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("knjlm, ji -> knlmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift55a06fa4f7c5d730 -> [H]@Unfold820e0f3eb05a896f
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# [H]@Unfold820e0f3eb05a896f -> [H]@Iterator96123ba3184da39c, [k_2]@Sharec0d065a85569cbbe
		t_5 = torch.reshape(t_5, (128, 2, 56, 504, ))
		t_5 = torch.nn.functional.unfold(t_5, (7, 1, ), padding=(3, 0, ))
		t_5 = torch.reshape(t_5, (128, 2, 7, 56, 56, 9, ))

		# Perform contraction.
		t_6 = torch.einsum("lokmnj, ikj -> loimn", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (128, 192, 56, 56, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([96, 7, 9]),
			torch.randn([24, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split69dd43e0c9ec9c4b -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share010730f7adbbf8aa
		t_3 = torch.reshape(t_3, (128, 2, 24, 28, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("knjlm, ji -> knlmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift55a06fa4f7c5d730 -> [H]@Unfold820e0f3eb05a896f
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# [H]@Unfold820e0f3eb05a896f -> [H]@Iterator96123ba3184da39c, [k_2]@Sharec0d065a85569cbbe
		t_5 = torch.reshape(t_5, (128, 2, 28, 252, ))
		t_5 = torch.nn.functional.unfold(t_5, (7, 1, ), padding=(3, 0, ))
		t_5 = torch.reshape(t_5, (128, 2, 7, 28, 28, 9, ))

		# Perform contraction.
		t_6 = torch.einsum("lokmnj, ikj -> loimn", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (128, 192, 28, 28, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 7, 9]),
			torch.randn([32, 9]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Split69dd43e0c9ec9c4b -> [s]@Merge03a73148aa81036c, [s^-1*C_in]@Share010730f7adbbf8aa
		t_3 = torch.reshape(t_3, (128, 2, 32, 28, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("knjlm, ji -> knlmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift55a06fa4f7c5d730 -> [H]@Unfold820e0f3eb05a896f
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# [H]@Unfold820e0f3eb05a896f -> [H]@Iterator96123ba3184da39c, [k_2]@Sharec0d065a85569cbbe
		t_5 = torch.reshape(t_5, (128, 2, 28, 252, ))
		t_5 = torch.nn.functional.unfold(t_5, (7, 1, ), padding=(3, 0, ))
		t_5 = torch.reshape(t_5, (128, 2, 7, 28, 28, 9, ))

		# Perform contraction.
		t_6 = torch.einsum("lokmnj, ikj -> loimn", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (128, 256, 28, 28, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

