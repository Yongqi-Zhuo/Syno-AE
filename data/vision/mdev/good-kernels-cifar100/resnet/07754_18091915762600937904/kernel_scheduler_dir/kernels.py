import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7fe520007928 [label="Sum", shape=box];
    reduce_0x7fe520007a98 [label="Sum", shape=box];
    reduce_0x7fe52000f088 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x564115463120 [label="N", shape=none];
        interface_0_out_0x564115463148 [label="C_out", shape=none];
        interface_0_out_0x564115463170 [label="H", shape=none];
        interface_0_out_0x564115463198 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fe520007928;
        reduce_0x7fe520007a98;
        reduce_0x7fe52000f088;
        interface_0_out_0x564115463120;
        interface_0_out_0x564115463148;
        interface_0_out_0x564115463170;
        interface_0_out_0x564115463198;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x564115463120 [label="N", shape=none];
        interface_0_in_0x564116cece40 [label="g", shape=none];
        interface_0_in_0x564116cece90 [label="k_1", shape=none];
        interface_0_in_0x564115463170 [label="H", shape=none];
        interface_0_in_0x564115463198 [label="H", shape=none];
        interface_0_in_0x564116cecee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x564116cecdb8 [label="C_out", shape=none];
        interface_0_in_0x564116cece58 [label="g", shape=none];
        interface_0_in_0x564116cecea8 [label="k_1", shape=none];
        interface_0_in_0x564116cecef8 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x564115463120;
        interface_0_in_0x564116cece40;
        interface_0_in_0x564116cece90;
        interface_0_in_0x564115463170;
        interface_0_in_0x564115463198;
        interface_0_in_0x564116cecee0;
        interface_0_in_0x564116cecdb8;
        interface_0_in_0x564116cece58;
        interface_0_in_0x564116cecea8;
        interface_0_in_0x564116cecef8;
    }
    // Op's.
    op_0x56410b6a7858 [label="Expand"];
    op_0x564116cecd80 [label="Share"];
    op_0x564116cece20 [label="Share"];
    op_0x564116cece70 [label="Share"];
    op_0x564116cecec0 [label="Share"];
    // Dimension's.
    interface_0_in_0x564115463120 -> interface_0_out_0x564115463120 [label="N"];
    op_0x564116cecd80 -> interface_0_out_0x564115463148 [label="C_out"];
    interface_0_in_0x564115463170 -> interface_0_out_0x564115463170 [label="H"];
    interface_0_in_0x564115463198 -> interface_0_out_0x564115463198 [label="H"];
    op_0x56410b6a7858 -> op_0x564116cecd80 [label="C_out"];
    interface_0_in_0x564116cecdb8 -> op_0x564116cecd80 [label="C_out"];
    interface_0_in_0x564116cece40 -> op_0x564116cece20 [label="g"];
    interface_0_in_0x564116cece58 -> op_0x564116cece20 [label="g"];
    interface_0_in_0x564116cece90 -> op_0x564116cece70 [label="k_1"];
    interface_0_in_0x564116cecea8 -> op_0x564116cece70 [label="k_1"];
    interface_0_in_0x564116cecee0 -> op_0x564116cecec0 [label="g^-1*s^-1*C_out"];
    interface_0_in_0x564116cecef8 -> op_0x564116cecec0 [label="g^-1*s^-1*C_out"];
    op_0x564116cece20 -> reduce_0x7fe520007928 [label="g"];
    op_0x564116cece70 -> reduce_0x7fe520007a98 [label="k_1"];
    op_0x564116cecec0 -> reduce_0x7fe52000f088 [label="g^-1*s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x564115463120 [label="N", shape=none];
        interface_1_out_0x564116cece40 [label="g", shape=none];
        interface_1_out_0x564116cece90 [label="k_1", shape=none];
        interface_1_out_0x564115463170 [label="H", shape=none];
        interface_1_out_0x564115463198 [label="H", shape=none];
        interface_1_out_0x564116cecee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x564115463120;
        interface_1_out_0x564116cece40;
        interface_1_out_0x564116cece90;
        interface_1_out_0x564115463170;
        interface_1_out_0x564115463198;
        interface_1_out_0x564116cecee0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x564115463120 [label="N", shape=none];
        interface_1_in_0x564116cece40 [label="g", shape=none];
        interface_1_in_0x564115844a00 [label="H", shape=none];
        interface_1_in_0x564115463198 [label="H", shape=none];
        interface_1_in_0x564116cecee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x564115463120;
        interface_1_in_0x564116cece40;
        interface_1_in_0x564115844a00;
        interface_1_in_0x564115463198;
        interface_1_in_0x564116cecee0;
    }
    // Op's.
    op_0x5641158449e0 [label="Shift"];
    op_0x564116c68fc0 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x564115463120 -> interface_1_out_0x564115463120 [label="N"];
    op_0x564116c68fc0 -> interface_1_out_0x564115463170 [label="H"];
    interface_1_in_0x564115463198 -> interface_1_out_0x564115463198 [label="H"];
    interface_1_in_0x564115844a00 -> op_0x5641158449e0 [label="H"];
    op_0x5641158449e0 -> op_0x564116c68fc0 [label="H"];
    interface_1_in_0x564116cece40 -> interface_1_out_0x564116cece40 [label="g"];
    op_0x564116c68fc0 -> interface_1_out_0x564116cece90 [label="k_1"];
    interface_1_in_0x564116cecee0 -> interface_1_out_0x564116cecee0 [label="g^-1*s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7fe52000b990 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x564115463120 [label="N", shape=none];
        interface_2_out_0x564116cece40 [label="g", shape=none];
        interface_2_out_0x564115844a00 [label="H", shape=none];
        interface_2_out_0x564115463198 [label="H", shape=none];
        interface_2_out_0x564116cecee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7fe52000b990;
        interface_2_out_0x564115463120;
        interface_2_out_0x564116cece40;
        interface_2_out_0x564115844a00;
        interface_2_out_0x564115463198;
        interface_2_out_0x564116cecee0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x564115463120 [label="N", shape=none];
        interface_2_in_0x564116c67140 [label="C_in", shape=none];
        interface_2_in_0x564115844a00 [label="H", shape=none];
        interface_2_in_0x564115463198 [label="H", shape=none];
        interface_2_in_0x564116cecee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x564115463120;
        interface_2_in_0x564116c67140;
        interface_2_in_0x564115844a00;
        interface_2_in_0x564115463198;
        interface_2_in_0x564116cecee0;
    }
    // Op's.
    op_0x564116c67100 [label="Split"];
    // Dimension's.
    interface_2_in_0x564115463120 -> interface_2_out_0x564115463120 [label="N"];
    interface_2_in_0x564115463198 -> interface_2_out_0x564115463198 [label="H"];
    interface_2_in_0x564115844a00 -> interface_2_out_0x564115844a00 [label="H"];
    interface_2_in_0x564116c67140 -> op_0x564116c67100 [label="C_in"];
    op_0x564116c67100 -> interface_2_out_0x564116cece40 [label="g"];
    interface_2_in_0x564116cecee0 -> interface_2_out_0x564116cecee0 [label="g^-1*s^-1*C_out"];
    op_0x564116c67100 -> reduce_0x7fe52000b990 [label="g^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7fe520007ab0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x564115463120 [label="N", shape=none];
        interface_3_out_0x564116c67140 [label="C_in", shape=none];
        interface_3_out_0x564115844a00 [label="H", shape=none];
        interface_3_out_0x564115463198 [label="H", shape=none];
        interface_3_out_0x564116cecee0 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7fe520007ab0;
        interface_3_out_0x564115463120;
        interface_3_out_0x564116c67140;
        interface_3_out_0x564115844a00;
        interface_3_out_0x564115463198;
        interface_3_out_0x564116cecee0;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x564115463120 [label="N", shape=none];
        interface_3_in_0x564116ced110 [label="C_in", shape=none];
        interface_3_in_0x564115844a00 [label="H", shape=none];
        interface_3_in_0x564116ced0c0 [label="k_1", shape=none];
        interface_3_in_0x564115463198 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x564116ced128 [label="C_in", shape=none];
        interface_3_in_0x564116ced0d8 [label="k_1", shape=none];
        interface_3_in_0x564116cecf98 [label="g^-1*s^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x564115463120;
        interface_3_in_0x564116ced110;
        interface_3_in_0x564115844a00;
        interface_3_in_0x564116ced0c0;
        interface_3_in_0x564115463198;
        interface_3_in_0x564116ced128;
        interface_3_in_0x564116ced0d8;
        interface_3_in_0x564116cecf98;
    }
    // Op's.
    op_0x56410b6a7878 [label="Expand"];
    op_0x564116cecf60 [label="Share"];
    op_0x564116ced0a0 [label="Share"];
    op_0x564116ced0f0 [label="Share"];
    // Dimension's.
    interface_3_in_0x564115463120 -> interface_3_out_0x564115463120 [label="N"];
    interface_3_in_0x564115463198 -> interface_3_out_0x564115463198 [label="H"];
    interface_3_in_0x564115844a00 -> interface_3_out_0x564115844a00 [label="H"];
    op_0x564116ced0f0 -> interface_3_out_0x564116c67140 [label="C_in"];
    op_0x564116cecf60 -> interface_3_out_0x564116cecee0 [label="g^-1*s^-1*C_out"];
    op_0x56410b6a7878 -> op_0x564116cecf60 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x564116cecf98 -> op_0x564116cecf60 [label="g^-1*s^-1*C_out"];
    interface_3_in_0x564116ced0c0 -> op_0x564116ced0a0 [label="k_1"];
    interface_3_in_0x564116ced0d8 -> op_0x564116ced0a0 [label="k_1"];
    interface_3_in_0x564116ced110 -> op_0x564116ced0f0 [label="C_in"];
    interface_3_in_0x564116ced128 -> op_0x564116ced0f0 [label="C_in"];
    op_0x564116ced0a0 -> reduce_0x7fe520007ab0 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x564115463120 [label="N", shape=none];
        interface_4_out_0x564116ced110 [label="C_in", shape=none];
        interface_4_out_0x564115844a00 [label="H", shape=none];
        interface_4_out_0x564116ced0c0 [label="k_1", shape=none];
        interface_4_out_0x564115463198 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x564115463120;
        interface_4_out_0x564116ced110;
        interface_4_out_0x564115844a00;
        interface_4_out_0x564116ced0c0;
        interface_4_out_0x564115463198;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x564115463120 [label="N", shape=none];
        interface_4_in_0x564116ced110 [label="C_in", shape=none];
        interface_4_in_0x564115844a00 [label="H", shape=none];
        interface_4_in_0x564116c69068 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x564115463120;
        interface_4_in_0x564116ced110;
        interface_4_in_0x564115844a00;
        interface_4_in_0x564116c69068;
    }
    // Op's.
    op_0x564116c69040 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x564115463120 -> interface_4_out_0x564115463120 [label="N"];
    op_0x564116c69040 -> interface_4_out_0x564115463198 [label="H"];
    interface_4_in_0x564115844a00 -> interface_4_out_0x564115844a00 [label="H"];
    interface_4_in_0x564116c69068 -> op_0x564116c69040 [label="H"];
    op_0x564116c69040 -> interface_4_out_0x564116ced0c0 [label="k_1"];
    interface_4_in_0x564116ced110 -> interface_4_out_0x564116ced110 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x564115463120 [label="N", shape=none];
    interface_5_out_0x564116ced110 [label="C_in", shape=none];
    interface_5_out_0x564115844a00 [label="H", shape=none];
    interface_5_out_0x564116c69068 [label="H", shape=none];
}

interface_5_out_0x564115463120 -> interface_4_in_0x564115463120;
interface_5_out_0x564116ced110 -> interface_4_in_0x564116ced110;
interface_5_out_0x564115844a00 -> interface_4_in_0x564115844a00;
interface_5_out_0x564116c69068 -> interface_4_in_0x564116c69068;

interface_4_out_0x564115463120 -> interface_3_in_0x564115463120;
interface_4_out_0x564116ced110 -> interface_3_in_0x564116ced110;
interface_4_out_0x564115844a00 -> interface_3_in_0x564115844a00;
interface_4_out_0x564116ced0c0 -> interface_3_in_0x564116ced0c0;
interface_4_out_0x564115463198 -> interface_3_in_0x564115463198;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x564116ced128 [label="C_in", shape=none];
    interface_6_out_0x564116ced0d8 [label="k_1", shape=none];
    interface_6_out_0x564116cecf98 [label="g^-1*s^-1*C_out", shape=none];
}

interface_6_out_0x564116ced128 -> interface_3_in_0x564116ced128;
interface_6_out_0x564116ced0d8 -> interface_3_in_0x564116ced0d8;
interface_6_out_0x564116cecf98 -> interface_3_in_0x564116cecf98;

interface_3_out_0x564115463120 -> interface_2_in_0x564115463120;
interface_3_out_0x564116c67140 -> interface_2_in_0x564116c67140;
interface_3_out_0x564115844a00 -> interface_2_in_0x564115844a00;
interface_3_out_0x564115463198 -> interface_2_in_0x564115463198;
interface_3_out_0x564116cecee0 -> interface_2_in_0x564116cecee0;

interface_2_out_0x564115463120 -> interface_1_in_0x564115463120;
interface_2_out_0x564116cece40 -> interface_1_in_0x564116cece40;
interface_2_out_0x564115844a00 -> interface_1_in_0x564115844a00;
interface_2_out_0x564115463198 -> interface_1_in_0x564115463198;
interface_2_out_0x564116cecee0 -> interface_1_in_0x564116cecee0;

interface_1_out_0x564115463120 -> interface_0_in_0x564115463120;
interface_1_out_0x564116cece40 -> interface_0_in_0x564116cece40;
interface_1_out_0x564116cece90 -> interface_0_in_0x564116cece90;
interface_1_out_0x564115463170 -> interface_0_in_0x564115463170;
interface_1_out_0x564115463198 -> interface_0_in_0x564115463198;
interface_1_out_0x564116cecee0 -> interface_0_in_0x564116cecee0;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x564116cecdb8 [label="C_out", shape=none];
    interface_7_out_0x564116cece58 [label="g", shape=none];
    interface_7_out_0x564116cecea8 [label="k_1", shape=none];
    interface_7_out_0x564116cecef8 [label="g^-1*s^-1*C_out", shape=none];
}

interface_7_out_0x564116cecdb8 -> interface_0_in_0x564116cecdb8;
interface_7_out_0x564116cece58 -> interface_0_in_0x564116cece58;
interface_7_out_0x564116cecea8 -> interface_0_in_0x564116cecea8;
interface_7_out_0x564116cecef8 -> interface_0_in_0x564116cecef8;

{
    rank = same;
    interface_5_out_0x564115463120;
    interface_5_out_0x564116ced110;
    interface_5_out_0x564115844a00;
    interface_5_out_0x564116c69068;
    interface_7_out_0x564116cecdb8;
    interface_7_out_0x564116cece58;
    interface_7_out_0x564116cecea8;
    interface_7_out_0x564116cecef8;
    interface_6_out_0x564116ced128;
    interface_6_out_0x564116ced0d8;
    interface_6_out_0x564116cecf98;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x564115463120 [label="N", shape=none];
    interface_8_in_0x564115463148 [label="C_out", shape=none];
    interface_8_in_0x564115463170 [label="H", shape=none];
    interface_8_in_0x564115463198 [label="H", shape=none];
}
interface_0_out_0x564115463120 -> interface_8_in_0x564115463120;
interface_0_out_0x564115463148 -> interface_8_in_0x564115463148;
interface_0_out_0x564115463170 -> interface_8_in_0x564115463170;
interface_0_out_0x564115463198 -> interface_8_in_0x564115463198;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 32, 3, 1]),
			torch.randn([64, 3, 1]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold3df8d2eb9190e6db -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareb0cd4bf85106ab3d
		t_3 = torch.reshape(t_3, (128, 3584, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 56, 3, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, kji -> lknmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 2, 56, 56, 1, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift8e39b9031dc296c5 -> [H]@Unfold4d77c1e3da5bca44
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 32, 56, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 56, 56, 1, ))

		# Perform contraction.
		t_7 = torch.einsum("mjknol, ijkl -> mino", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 32, 3, 2]),
			torch.randn([64, 3, 2]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold3df8d2eb9190e6db -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareb0cd4bf85106ab3d
		t_3 = torch.reshape(t_3, (128, 1792, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, kji -> lknmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 2, 28, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift8e39b9031dc296c5 -> [H]@Unfold4d77c1e3da5bca44
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 32, 28, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 28, 28, 2, ))

		# Perform contraction.
		t_7 = torch.einsum("mjknol, ijkl -> mino", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 32, 3, 2]),
			torch.randn([128, 3, 2]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold3df8d2eb9190e6db -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareb0cd4bf85106ab3d
		t_3 = torch.reshape(t_3, (128, 3584, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 128, 28, 3, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, kji -> lknmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 4, 28, 28, 2, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift8e39b9031dc296c5 -> [H]@Unfold4d77c1e3da5bca44
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 32, 28, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 28, 28, 2, ))

		# Perform contraction.
		t_7 = torch.einsum("mjknol, ijkl -> mino", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 32, 3, 4]),
			torch.randn([128, 3, 4]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold3df8d2eb9190e6db -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareb0cd4bf85106ab3d
		t_3 = torch.reshape(t_3, (128, 1792, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 128, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, kji -> lknmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 4, 14, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift8e39b9031dc296c5 -> [H]@Unfold4d77c1e3da5bca44
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 32, 14, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 14, 14, 4, ))

		# Perform contraction.
		t_7 = torch.einsum("mjknol, ijkl -> mino", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 32, 3, 4]),
			torch.randn([256, 3, 4]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold3df8d2eb9190e6db -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareb0cd4bf85106ab3d
		t_3 = torch.reshape(t_3, (128, 3584, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 256, 14, 3, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, kji -> lknmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 8, 14, 14, 4, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift8e39b9031dc296c5 -> [H]@Unfold4d77c1e3da5bca44
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 32, 14, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 14, 14, 4, ))

		# Perform contraction.
		t_7 = torch.einsum("mjknol, ijkl -> mino", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 32, 3, 8]),
			torch.randn([256, 3, 8]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold3df8d2eb9190e6db -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareb0cd4bf85106ab3d
		t_3 = torch.reshape(t_3, (128, 1792, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 256, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, kji -> lknmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 8, 7, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift8e39b9031dc296c5 -> [H]@Unfold4d77c1e3da5bca44
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 32, 7, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 7, 7, 8, ))

		# Perform contraction.
		t_7 = torch.einsum("mjknol, ijkl -> mino", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 32, 3, 8]),
			torch.randn([512, 3, 8]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold3df8d2eb9190e6db -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shareb0cd4bf85106ab3d
		t_3 = torch.reshape(t_3, (128, 3584, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 512, 7, 3, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("lknjm, kji -> lknmi", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [C_in]@Splitc2d52f3525ba6cc4 -> [g]@Sharec7a8ce455b828537, [g^-1*C_in]@Reduceef9903cafc29eea1
		t_5 = torch.reshape(t_5, (128, 32, 16, 7, 7, 8, ))

		# [g^-1*C_in]@Reduce
		t_5 = torch.sum(t_5, dim=(2, ))

		# No contraction needed.
		t_6 = t_5

		# [H]@Shift8e39b9031dc296c5 -> [H]@Unfold4d77c1e3da5bca44
		t_6 = torch.roll(t_6, self.shift_direction, 2)

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 32, 7, 56, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 32, 3, 7, 7, 8, ))

		# Perform contraction.
		t_7 = torch.einsum("mjknol, ijkl -> mino", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

