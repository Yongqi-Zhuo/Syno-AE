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
        interface_0_out_0x5604185d74e0 [label="N", shape=none];
        interface_0_out_0x5604185d7508 [label="C_out", shape=none];
        interface_0_out_0x5604185d7530 [label="H", shape=none];
        interface_0_out_0x5604185d7558 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x5604185d74e0;
        interface_0_out_0x5604185d7508;
        interface_0_out_0x5604185d7530;
        interface_0_out_0x5604185d7558;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5604185d74e0 [label="N", shape=none];
        interface_0_in_0x560419919800 [label="s", shape=none];
        interface_0_in_0x560419919818 [label="s^-1*C_out", shape=none];
        interface_0_in_0x5604185d7530 [label="H", shape=none];
        interface_0_in_0x560419917fd0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5604185d74e0;
        interface_0_in_0x560419919800;
        interface_0_in_0x560419919818;
        interface_0_in_0x5604185d7530;
        interface_0_in_0x560419917fd0;
    }
    // Op's.
    op_0x560419917fb0 [label="Shift"];
    op_0x5604199197c0 [label="Merge"];
    // Dimension's.
    interface_0_in_0x5604185d74e0 -> interface_0_out_0x5604185d74e0 [label="N"];
    op_0x5604199197c0 -> interface_0_out_0x5604185d7508 [label="C_out"];
    interface_0_in_0x5604185d7530 -> interface_0_out_0x5604185d7530 [label="H"];
    op_0x560419917fb0 -> interface_0_out_0x5604185d7558 [label="H"];
    interface_0_in_0x560419917fd0 -> op_0x560419917fb0 [label="H"];
    interface_0_in_0x560419919800 -> op_0x5604199197c0 [label="s"];
    interface_0_in_0x560419919818 -> op_0x5604199197c0 [label="s^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fc32c003ee8 [label="Sum", shape=box];
    reduce_0x7fc32c003cc0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5604185d74e0 [label="N", shape=none];
        interface_1_out_0x560419919800 [label="s", shape=none];
        interface_1_out_0x560419919818 [label="s^-1*C_out", shape=none];
        interface_1_out_0x5604185d7530 [label="H", shape=none];
        interface_1_out_0x560419917fd0 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc32c003ee8;
        reduce_0x7fc32c003cc0;
        interface_1_out_0x5604185d74e0;
        interface_1_out_0x560419919800;
        interface_1_out_0x560419919818;
        interface_1_out_0x5604185d7530;
        interface_1_out_0x560419917fd0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5604185d74e0 [label="N", shape=none];
        interface_1_in_0x560419919800 [label="s", shape=none];
        interface_1_in_0x56041991c9c0 [label="k_2", shape=none];
        interface_1_in_0x5604185d7530 [label="H", shape=none];
        interface_1_in_0x560419917fd0 [label="H", shape=none];
        interface_1_in_0x560419917340 [label="k_1^2", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x5604199173a8 [label="s^-1*C_out", shape=none];
        interface_1_in_0x56041991c9d8 [label="k_2", shape=none];
        interface_1_in_0x560419917358 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5604185d74e0;
        interface_1_in_0x560419919800;
        interface_1_in_0x56041991c9c0;
        interface_1_in_0x5604185d7530;
        interface_1_in_0x560419917fd0;
        interface_1_in_0x560419917340;
        interface_1_in_0x5604199173a8;
        interface_1_in_0x56041991c9d8;
        interface_1_in_0x560419917358;
    }
    // Op's.
    op_0x560419917320 [label="Share"];
    op_0x560419917370 [label="Share"];
    op_0x560419917778 [label="Expand"];
    op_0x56041991c9a0 [label="Share"];
    // Dimension's.
    interface_1_in_0x5604185d74e0 -> interface_1_out_0x5604185d74e0 [label="N"];
    interface_1_in_0x5604185d7530 -> interface_1_out_0x5604185d7530 [label="H"];
    interface_1_in_0x560419917340 -> op_0x560419917320 [label="k_1^2"];
    interface_1_in_0x560419917358 -> op_0x560419917320 [label="k_1^2"];
    op_0x560419917778 -> op_0x560419917370 [label="s^-1*C_out"];
    interface_1_in_0x5604199173a8 -> op_0x560419917370 [label="s^-1*C_out"];
    interface_1_in_0x560419917fd0 -> interface_1_out_0x560419917fd0 [label="H"];
    interface_1_in_0x560419919800 -> interface_1_out_0x560419919800 [label="s"];
    op_0x560419917370 -> interface_1_out_0x560419919818 [label="s^-1*C_out"];
    interface_1_in_0x56041991c9c0 -> op_0x56041991c9a0 [label="k_2"];
    interface_1_in_0x56041991c9d8 -> op_0x56041991c9a0 [label="k_2"];
    op_0x560419917320 -> reduce_0x7fc32c003cc0 [label="k_1^2"];
    op_0x56041991c9a0 -> reduce_0x7fc32c003ee8 [label="k_2"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5604185d74e0 [label="N", shape=none];
        interface_2_out_0x560419919800 [label="s", shape=none];
        interface_2_out_0x56041991c9c0 [label="k_2", shape=none];
        interface_2_out_0x5604185d7530 [label="H", shape=none];
        interface_2_out_0x560419917fd0 [label="H", shape=none];
        interface_2_out_0x560419917340 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x5604185d74e0;
        interface_2_out_0x560419919800;
        interface_2_out_0x56041991c9c0;
        interface_2_out_0x5604185d7530;
        interface_2_out_0x560419917fd0;
        interface_2_out_0x560419917340;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5604185d74e0 [label="N", shape=none];
        interface_2_in_0x560419919800 [label="s", shape=none];
        interface_2_in_0x560419918210 [label="H", shape=none];
        interface_2_in_0x560419917fd0 [label="H", shape=none];
        interface_2_in_0x560419917340 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5604185d74e0;
        interface_2_in_0x560419919800;
        interface_2_in_0x560419918210;
        interface_2_in_0x560419917fd0;
        interface_2_in_0x560419917340;
    }
    // Op's.
    op_0x5604199181f0 [label="Shift"];
    op_0x560419919b80 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x5604185d74e0 -> interface_2_out_0x5604185d74e0 [label="N"];
    op_0x560419919b80 -> interface_2_out_0x5604185d7530 [label="H"];
    interface_2_in_0x560419917340 -> interface_2_out_0x560419917340 [label="k_1^2"];
    interface_2_in_0x560419917fd0 -> interface_2_out_0x560419917fd0 [label="H"];
    interface_2_in_0x560419918210 -> op_0x5604199181f0 [label="H"];
    interface_2_in_0x560419919800 -> interface_2_out_0x560419919800 [label="s"];
    op_0x5604199181f0 -> op_0x560419919b80 [label="H"];
    op_0x560419919b80 -> interface_2_out_0x56041991c9c0 [label="k_2"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7fc32c007668 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5604185d74e0 [label="N", shape=none];
        interface_3_out_0x560419919800 [label="s", shape=none];
        interface_3_out_0x560419918210 [label="H", shape=none];
        interface_3_out_0x560419917fd0 [label="H", shape=none];
        interface_3_out_0x560419917340 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc32c007668;
        interface_3_out_0x5604185d74e0;
        interface_3_out_0x560419919800;
        interface_3_out_0x560419918210;
        interface_3_out_0x560419917fd0;
        interface_3_out_0x560419917340;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5604185d74e0 [label="N", shape=none];
        interface_3_in_0x560419919800 [label="s", shape=none];
        interface_3_in_0x56041991ca10 [label="s^-1*C_in", shape=none];
        interface_3_in_0x560419918210 [label="H", shape=none];
        interface_3_in_0x560419917fd0 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x56041991ca28 [label="s^-1*C_in", shape=none];
        interface_3_in_0x560419917498 [label="k_1^2", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5604185d74e0;
        interface_3_in_0x560419919800;
        interface_3_in_0x56041991ca10;
        interface_3_in_0x560419918210;
        interface_3_in_0x560419917fd0;
        interface_3_in_0x56041991ca28;
        interface_3_in_0x560419917498;
    }
    // Op's.
    op_0x560419917460 [label="Share"];
    op_0x5604199177b8 [label="Expand"];
    op_0x56041991c9f0 [label="Share"];
    // Dimension's.
    interface_3_in_0x5604185d74e0 -> interface_3_out_0x5604185d74e0 [label="N"];
    op_0x560419917460 -> interface_3_out_0x560419917340 [label="k_1^2"];
    op_0x5604199177b8 -> op_0x560419917460 [label="k_1^2"];
    interface_3_in_0x560419917498 -> op_0x560419917460 [label="k_1^2"];
    interface_3_in_0x560419917fd0 -> interface_3_out_0x560419917fd0 [label="H"];
    interface_3_in_0x560419918210 -> interface_3_out_0x560419918210 [label="H"];
    interface_3_in_0x560419919800 -> interface_3_out_0x560419919800 [label="s"];
    interface_3_in_0x56041991ca10 -> op_0x56041991c9f0 [label="s^-1*C_in"];
    interface_3_in_0x56041991ca28 -> op_0x56041991c9f0 [label="s^-1*C_in"];
    op_0x56041991c9f0 -> reduce_0x7fc32c007668 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x5604185d74e0 [label="N", shape=none];
        interface_4_out_0x560419919800 [label="s", shape=none];
        interface_4_out_0x56041991ca10 [label="s^-1*C_in", shape=none];
        interface_4_out_0x560419918210 [label="H", shape=none];
        interface_4_out_0x560419917fd0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x5604185d74e0;
        interface_4_out_0x560419919800;
        interface_4_out_0x56041991ca10;
        interface_4_out_0x560419918210;
        interface_4_out_0x560419917fd0;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x5604185d74e0 [label="N", shape=none];
        interface_4_in_0x56041991fd60 [label="C_in", shape=none];
        interface_4_in_0x560419918210 [label="H", shape=none];
        interface_4_in_0x560419917fd0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x5604185d74e0;
        interface_4_in_0x56041991fd60;
        interface_4_in_0x560419918210;
        interface_4_in_0x560419917fd0;
    }
    // Op's.
    op_0x56041991fd20 [label="Split"];
    // Dimension's.
    interface_4_in_0x5604185d74e0 -> interface_4_out_0x5604185d74e0 [label="N"];
    interface_4_in_0x560419917fd0 -> interface_4_out_0x560419917fd0 [label="H"];
    interface_4_in_0x560419918210 -> interface_4_out_0x560419918210 [label="H"];
    op_0x56041991fd20 -> interface_4_out_0x560419919800 [label="s"];
    op_0x56041991fd20 -> interface_4_out_0x56041991ca10 [label="s^-1*C_in"];
    interface_4_in_0x56041991fd60 -> op_0x56041991fd20 [label="C_in"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x5604185d74e0 [label="N", shape=none];
    interface_5_out_0x56041991fd60 [label="C_in", shape=none];
    interface_5_out_0x560419918210 [label="H", shape=none];
    interface_5_out_0x560419917fd0 [label="H", shape=none];
}

interface_5_out_0x5604185d74e0 -> interface_4_in_0x5604185d74e0;
interface_5_out_0x56041991fd60 -> interface_4_in_0x56041991fd60;
interface_5_out_0x560419918210 -> interface_4_in_0x560419918210;
interface_5_out_0x560419917fd0 -> interface_4_in_0x560419917fd0;

interface_4_out_0x5604185d74e0 -> interface_3_in_0x5604185d74e0;
interface_4_out_0x560419919800 -> interface_3_in_0x560419919800;
interface_4_out_0x56041991ca10 -> interface_3_in_0x56041991ca10;
interface_4_out_0x560419918210 -> interface_3_in_0x560419918210;
interface_4_out_0x560419917fd0 -> interface_3_in_0x560419917fd0;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x56041991ca28 [label="s^-1*C_in", shape=none];
    interface_6_out_0x560419917498 [label="k_1^2", shape=none];
}

interface_6_out_0x56041991ca28 -> interface_3_in_0x56041991ca28;
interface_6_out_0x560419917498 -> interface_3_in_0x560419917498;

interface_3_out_0x5604185d74e0 -> interface_2_in_0x5604185d74e0;
interface_3_out_0x560419919800 -> interface_2_in_0x560419919800;
interface_3_out_0x560419918210 -> interface_2_in_0x560419918210;
interface_3_out_0x560419917fd0 -> interface_2_in_0x560419917fd0;
interface_3_out_0x560419917340 -> interface_2_in_0x560419917340;

interface_2_out_0x5604185d74e0 -> interface_1_in_0x5604185d74e0;
interface_2_out_0x560419919800 -> interface_1_in_0x560419919800;
interface_2_out_0x56041991c9c0 -> interface_1_in_0x56041991c9c0;
interface_2_out_0x5604185d7530 -> interface_1_in_0x5604185d7530;
interface_2_out_0x560419917fd0 -> interface_1_in_0x560419917fd0;
interface_2_out_0x560419917340 -> interface_1_in_0x560419917340;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x5604199173a8 [label="s^-1*C_out", shape=none];
    interface_7_out_0x56041991c9d8 [label="k_2", shape=none];
    interface_7_out_0x560419917358 [label="k_1^2", shape=none];
}

interface_7_out_0x5604199173a8 -> interface_1_in_0x5604199173a8;
interface_7_out_0x56041991c9d8 -> interface_1_in_0x56041991c9d8;
interface_7_out_0x560419917358 -> interface_1_in_0x560419917358;

interface_1_out_0x5604185d74e0 -> interface_0_in_0x5604185d74e0;
interface_1_out_0x560419919800 -> interface_0_in_0x560419919800;
interface_1_out_0x560419919818 -> interface_0_in_0x560419919818;
interface_1_out_0x5604185d7530 -> interface_0_in_0x5604185d7530;
interface_1_out_0x560419917fd0 -> interface_0_in_0x560419917fd0;

{
    rank = same;
    interface_5_out_0x5604185d74e0;
    interface_5_out_0x56041991fd60;
    interface_5_out_0x560419918210;
    interface_5_out_0x560419917fd0;
    interface_7_out_0x5604199173a8;
    interface_7_out_0x56041991c9d8;
    interface_7_out_0x560419917358;
    interface_6_out_0x56041991ca28;
    interface_6_out_0x560419917498;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x5604185d74e0 [label="N", shape=none];
    interface_8_in_0x5604185d7508 [label="C_out", shape=none];
    interface_8_in_0x5604185d7530 [label="H", shape=none];
    interface_8_in_0x5604185d7558 [label="H", shape=none];
}
interface_0_out_0x5604185d74e0 -> interface_8_in_0x5604185d74e0;
interface_0_out_0x5604185d7508 -> interface_8_in_0x5604185d7508;
interface_0_out_0x5604185d7530 -> interface_8_in_0x5604185d7530;
interface_0_out_0x5604185d7558 -> interface_8_in_0x5604185d7558;

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
		t_3 = torch.reshape(t_3, (1, 2, 12, 112, 112, ))

		# Perform contraction.
		t_4 = torch.einsum("knjml, ji -> knmli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift55a06fa4f7c5d730 -> [H]@Unfold820e0f3eb05a896f
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# [H]@Unfold820e0f3eb05a896f -> [H]@Iterator96123ba3184da39c, [k_2]@Sharec0d065a85569cbbe
		t_5 = torch.reshape(t_5, (1, 2, 112, 1008, ))
		t_5 = torch.nn.functional.unfold(t_5, (7, 1, ), padding=(3, 0, ))
		t_5 = torch.reshape(t_5, (1, 2, 7, 112, 112, 9, ))

		# Perform contraction.
		t_6 = torch.einsum("lokmni, jki -> lojmn", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 24, 112, 112, ))

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
		t_3 = torch.reshape(t_3, (1, 2, 12, 56, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("knjml, ji -> knmli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift55a06fa4f7c5d730 -> [H]@Unfold820e0f3eb05a896f
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# [H]@Unfold820e0f3eb05a896f -> [H]@Iterator96123ba3184da39c, [k_2]@Sharec0d065a85569cbbe
		t_5 = torch.reshape(t_5, (1, 2, 56, 504, ))
		t_5 = torch.nn.functional.unfold(t_5, (7, 1, ), padding=(3, 0, ))
		t_5 = torch.reshape(t_5, (1, 2, 7, 56, 56, 9, ))

		# Perform contraction.
		t_6 = torch.einsum("lokmni, jki -> lojmn", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 96, 56, 56, ))

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
		t_3 = torch.reshape(t_3, (1, 2, 24, 56, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("knjml, ji -> knmli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift55a06fa4f7c5d730 -> [H]@Unfold820e0f3eb05a896f
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# [H]@Unfold820e0f3eb05a896f -> [H]@Iterator96123ba3184da39c, [k_2]@Sharec0d065a85569cbbe
		t_5 = torch.reshape(t_5, (1, 2, 56, 504, ))
		t_5 = torch.nn.functional.unfold(t_5, (7, 1, ), padding=(3, 0, ))
		t_5 = torch.reshape(t_5, (1, 2, 7, 56, 56, 9, ))

		# Perform contraction.
		t_6 = torch.einsum("lokmni, jki -> lojmn", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 192, 56, 56, ))

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
		t_3 = torch.reshape(t_3, (1, 2, 24, 28, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("knjml, ji -> knmli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift55a06fa4f7c5d730 -> [H]@Unfold820e0f3eb05a896f
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# [H]@Unfold820e0f3eb05a896f -> [H]@Iterator96123ba3184da39c, [k_2]@Sharec0d065a85569cbbe
		t_5 = torch.reshape(t_5, (1, 2, 28, 252, ))
		t_5 = torch.nn.functional.unfold(t_5, (7, 1, ), padding=(3, 0, ))
		t_5 = torch.reshape(t_5, (1, 2, 7, 28, 28, 9, ))

		# Perform contraction.
		t_6 = torch.einsum("lokmni, jki -> lojmn", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 192, 28, 28, ))

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
		t_3 = torch.reshape(t_3, (1, 2, 32, 28, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("knjml, ji -> knmli", t_3, in_2)

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift55a06fa4f7c5d730 -> [H]@Unfold820e0f3eb05a896f
		t_5 = torch.roll(t_5, self.shift_direction, 2)

		# [H]@Unfold820e0f3eb05a896f -> [H]@Iterator96123ba3184da39c, [k_2]@Sharec0d065a85569cbbe
		t_5 = torch.reshape(t_5, (1, 2, 28, 252, ))
		t_5 = torch.nn.functional.unfold(t_5, (7, 1, ), padding=(3, 0, ))
		t_5 = torch.reshape(t_5, (1, 2, 7, 28, 28, 9, ))

		# Perform contraction.
		t_6 = torch.einsum("lokmni, jki -> lojmn", t_5, in_1)

		# No contraction needed.
		t_7 = t_6

		# [s]@Merge03a73148aa81036c, [s^-1*C_out]@Merge03a73148aa81036f -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 256, 28, 28, ))

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_7

		return y

