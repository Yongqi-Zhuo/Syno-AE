import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7fc32c003a98 [label="Sum", shape=box];
    reduce_0x7fc32c004110 [label="Sum", shape=box];
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
        reduce_0x7fc32c003a98;
        reduce_0x7fc32c004110;
        interface_0_out_0x5604185d74e0;
        interface_0_out_0x5604185d7508;
        interface_0_out_0x5604185d7530;
        interface_0_out_0x5604185d7558;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5604185d74e0 [label="N", shape=none];
        interface_0_in_0x56041991c920 [label="k_1", shape=none];
        interface_0_in_0x5604185d7530 [label="H", shape=none];
        interface_0_in_0x5604185d7558 [label="H", shape=none];
        interface_0_in_0x56041991cc90 [label="k_1*k_2", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x5604199172b8 [label="C_out", shape=none];
        interface_0_in_0x56041991c938 [label="k_1", shape=none];
        interface_0_in_0x56041991cca8 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5604185d74e0;
        interface_0_in_0x56041991c920;
        interface_0_in_0x5604185d7530;
        interface_0_in_0x5604185d7558;
        interface_0_in_0x56041991cc90;
        interface_0_in_0x5604199172b8;
        interface_0_in_0x56041991c938;
        interface_0_in_0x56041991cca8;
    }
    // Op's.
    op_0x560419917280 [label="Share"];
    op_0x560419917758 [label="Expand"];
    op_0x56041991c900 [label="Share"];
    op_0x56041991cc70 [label="Share"];
    // Dimension's.
    interface_0_in_0x5604185d74e0 -> interface_0_out_0x5604185d74e0 [label="N"];
    op_0x560419917280 -> interface_0_out_0x5604185d7508 [label="C_out"];
    interface_0_in_0x5604185d7530 -> interface_0_out_0x5604185d7530 [label="H"];
    interface_0_in_0x5604185d7558 -> interface_0_out_0x5604185d7558 [label="H"];
    op_0x560419917758 -> op_0x560419917280 [label="C_out"];
    interface_0_in_0x5604199172b8 -> op_0x560419917280 [label="C_out"];
    interface_0_in_0x56041991c920 -> op_0x56041991c900 [label="k_1"];
    interface_0_in_0x56041991c938 -> op_0x56041991c900 [label="k_1"];
    interface_0_in_0x56041991cc90 -> op_0x56041991cc70 [label="k_1*k_2"];
    interface_0_in_0x56041991cca8 -> op_0x56041991cc70 [label="k_1*k_2"];
    op_0x56041991c900 -> reduce_0x7fc32c003a98 [label="k_1"];
    op_0x56041991cc70 -> reduce_0x7fc32c004110 [label="k_1*k_2"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5604185d74e0 [label="N", shape=none];
        interface_1_out_0x56041991c920 [label="k_1", shape=none];
        interface_1_out_0x5604185d7530 [label="H", shape=none];
        interface_1_out_0x5604185d7558 [label="H", shape=none];
        interface_1_out_0x56041991cc90 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x5604185d74e0;
        interface_1_out_0x56041991c920;
        interface_1_out_0x5604185d7530;
        interface_1_out_0x5604185d7558;
        interface_1_out_0x56041991cc90;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5604185d74e0 [label="N", shape=none];
        interface_1_in_0x560419919c68 [label="H", shape=none];
        interface_1_in_0x5604185d7558 [label="H", shape=none];
        interface_1_in_0x56041991cc90 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5604185d74e0;
        interface_1_in_0x560419919c68;
        interface_1_in_0x5604185d7558;
        interface_1_in_0x56041991cc90;
    }
    // Op's.
    op_0x560419919c40 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x5604185d74e0 -> interface_1_out_0x5604185d74e0 [label="N"];
    op_0x560419919c40 -> interface_1_out_0x5604185d7530 [label="H"];
    interface_1_in_0x5604185d7558 -> interface_1_out_0x5604185d7558 [label="H"];
    interface_1_in_0x560419919c68 -> op_0x560419919c40 [label="H"];
    op_0x560419919c40 -> interface_1_out_0x56041991c920 [label="k_1"];
    interface_1_in_0x56041991cc90 -> interface_1_out_0x56041991cc90 [label="k_1*k_2"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7fc32c007668 [label="Sum", shape=box];
    reduce_0x7fc32c003ee8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5604185d74e0 [label="N", shape=none];
        interface_2_out_0x560419919c68 [label="H", shape=none];
        interface_2_out_0x5604185d7558 [label="H", shape=none];
        interface_2_out_0x56041991cc90 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc32c007668;
        reduce_0x7fc32c003ee8;
        interface_2_out_0x5604185d74e0;
        interface_2_out_0x560419919c68;
        interface_2_out_0x5604185d7558;
        interface_2_out_0x56041991cc90;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5604185d74e0 [label="N", shape=none];
        interface_2_in_0x56041991ca10 [label="s^-1*C_in", shape=none];
        interface_2_in_0x560419919c68 [label="H", shape=none];
        interface_2_in_0x56041991ca60 [label="k_2", shape=none];
        interface_2_in_0x5604185d7558 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x56041991ca28 [label="s^-1*C_in", shape=none];
        interface_2_in_0x56041991ca78 [label="k_2", shape=none];
        interface_2_in_0x56041991ccf8 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5604185d74e0;
        interface_2_in_0x56041991ca10;
        interface_2_in_0x560419919c68;
        interface_2_in_0x56041991ca60;
        interface_2_in_0x5604185d7558;
        interface_2_in_0x56041991ca28;
        interface_2_in_0x56041991ca78;
        interface_2_in_0x56041991ccf8;
    }
    // Op's.
    op_0x5604199178b8 [label="Expand"];
    op_0x56041991c9f0 [label="Share"];
    op_0x56041991ca40 [label="Share"];
    op_0x56041991ccc0 [label="Share"];
    // Dimension's.
    interface_2_in_0x5604185d74e0 -> interface_2_out_0x5604185d74e0 [label="N"];
    interface_2_in_0x5604185d7558 -> interface_2_out_0x5604185d7558 [label="H"];
    interface_2_in_0x560419919c68 -> interface_2_out_0x560419919c68 [label="H"];
    interface_2_in_0x56041991ca10 -> op_0x56041991c9f0 [label="s^-1*C_in"];
    interface_2_in_0x56041991ca28 -> op_0x56041991c9f0 [label="s^-1*C_in"];
    interface_2_in_0x56041991ca60 -> op_0x56041991ca40 [label="k_2"];
    interface_2_in_0x56041991ca78 -> op_0x56041991ca40 [label="k_2"];
    op_0x56041991ccc0 -> interface_2_out_0x56041991cc90 [label="k_1*k_2"];
    op_0x5604199178b8 -> op_0x56041991ccc0 [label="k_1*k_2"];
    interface_2_in_0x56041991ccf8 -> op_0x56041991ccc0 [label="k_1*k_2"];
    op_0x56041991ca40 -> reduce_0x7fc32c003ee8 [label="k_2"];
    op_0x56041991c9f0 -> reduce_0x7fc32c007668 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5604185d74e0 [label="N", shape=none];
        interface_3_out_0x56041991ca10 [label="s^-1*C_in", shape=none];
        interface_3_out_0x560419919c68 [label="H", shape=none];
        interface_3_out_0x56041991ca60 [label="k_2", shape=none];
        interface_3_out_0x5604185d7558 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5604185d74e0;
        interface_3_out_0x56041991ca10;
        interface_3_out_0x560419919c68;
        interface_3_out_0x56041991ca60;
        interface_3_out_0x5604185d7558;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5604185d74e0 [label="N", shape=none];
        interface_3_in_0x56041991ca10 [label="s^-1*C_in", shape=none];
        interface_3_in_0x560419919c68 [label="H", shape=none];
        interface_3_in_0x560419918150 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5604185d74e0;
        interface_3_in_0x56041991ca10;
        interface_3_in_0x560419919c68;
        interface_3_in_0x560419918150;
    }
    // Op's.
    op_0x560419918130 [label="Shift"];
    op_0x560419919b40 [label="Unfold"];
    // Dimension's.
    interface_3_in_0x5604185d74e0 -> interface_3_out_0x5604185d74e0 [label="N"];
    op_0x560419919b40 -> interface_3_out_0x5604185d7558 [label="H"];
    interface_3_in_0x560419918150 -> op_0x560419918130 [label="H"];
    op_0x560419918130 -> op_0x560419919b40 [label="H"];
    interface_3_in_0x560419919c68 -> interface_3_out_0x560419919c68 [label="H"];
    interface_3_in_0x56041991ca10 -> interface_3_out_0x56041991ca10 [label="s^-1*C_in"];
    op_0x560419919b40 -> interface_3_out_0x56041991ca60 [label="k_2"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    reduce_0x7fc32c004e58 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x5604185d74e0 [label="N", shape=none];
        interface_4_out_0x56041991ca10 [label="s^-1*C_in", shape=none];
        interface_4_out_0x560419919c68 [label="H", shape=none];
        interface_4_out_0x560419918150 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc32c004e58;
        interface_4_out_0x5604185d74e0;
        interface_4_out_0x56041991ca10;
        interface_4_out_0x560419919c68;
        interface_4_out_0x560419918150;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x5604185d74e0 [label="N", shape=none];
        interface_4_in_0x5604199469b0 [label="C_in", shape=none];
        interface_4_in_0x560419919c68 [label="H", shape=none];
        interface_4_in_0x560419918150 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x5604185d74e0;
        interface_4_in_0x5604199469b0;
        interface_4_in_0x560419919c68;
        interface_4_in_0x560419918150;
    }
    // Op's.
    op_0x560419946970 [label="Split"];
    // Dimension's.
    interface_4_in_0x5604185d74e0 -> interface_4_out_0x5604185d74e0 [label="N"];
    interface_4_in_0x560419918150 -> interface_4_out_0x560419918150 [label="H"];
    interface_4_in_0x560419919c68 -> interface_4_out_0x560419919c68 [label="H"];
    op_0x560419946970 -> interface_4_out_0x56041991ca10 [label="s^-1*C_in"];
    interface_4_in_0x5604199469b0 -> op_0x560419946970 [label="C_in"];
    op_0x560419946970 -> reduce_0x7fc32c004e58 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x5604185d74e0 [label="N", shape=none];
    interface_5_out_0x5604199469b0 [label="C_in", shape=none];
    interface_5_out_0x560419919c68 [label="H", shape=none];
    interface_5_out_0x560419918150 [label="H", shape=none];
}

interface_5_out_0x5604185d74e0 -> interface_4_in_0x5604185d74e0;
interface_5_out_0x5604199469b0 -> interface_4_in_0x5604199469b0;
interface_5_out_0x560419919c68 -> interface_4_in_0x560419919c68;
interface_5_out_0x560419918150 -> interface_4_in_0x560419918150;

interface_4_out_0x5604185d74e0 -> interface_3_in_0x5604185d74e0;
interface_4_out_0x56041991ca10 -> interface_3_in_0x56041991ca10;
interface_4_out_0x560419919c68 -> interface_3_in_0x560419919c68;
interface_4_out_0x560419918150 -> interface_3_in_0x560419918150;

interface_3_out_0x5604185d74e0 -> interface_2_in_0x5604185d74e0;
interface_3_out_0x56041991ca10 -> interface_2_in_0x56041991ca10;
interface_3_out_0x560419919c68 -> interface_2_in_0x560419919c68;
interface_3_out_0x56041991ca60 -> interface_2_in_0x56041991ca60;
interface_3_out_0x5604185d7558 -> interface_2_in_0x5604185d7558;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x56041991ca28 [label="s^-1*C_in", shape=none];
    interface_6_out_0x56041991ca78 [label="k_2", shape=none];
    interface_6_out_0x56041991ccf8 [label="k_1*k_2", shape=none];
}

interface_6_out_0x56041991ca28 -> interface_2_in_0x56041991ca28;
interface_6_out_0x56041991ca78 -> interface_2_in_0x56041991ca78;
interface_6_out_0x56041991ccf8 -> interface_2_in_0x56041991ccf8;

interface_2_out_0x5604185d74e0 -> interface_1_in_0x5604185d74e0;
interface_2_out_0x560419919c68 -> interface_1_in_0x560419919c68;
interface_2_out_0x5604185d7558 -> interface_1_in_0x5604185d7558;
interface_2_out_0x56041991cc90 -> interface_1_in_0x56041991cc90;

interface_1_out_0x5604185d74e0 -> interface_0_in_0x5604185d74e0;
interface_1_out_0x56041991c920 -> interface_0_in_0x56041991c920;
interface_1_out_0x5604185d7530 -> interface_0_in_0x5604185d7530;
interface_1_out_0x5604185d7558 -> interface_0_in_0x5604185d7558;
interface_1_out_0x56041991cc90 -> interface_0_in_0x56041991cc90;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x5604199172b8 [label="C_out", shape=none];
    interface_7_out_0x56041991c938 [label="k_1", shape=none];
    interface_7_out_0x56041991cca8 [label="k_1*k_2", shape=none];
}

interface_7_out_0x5604199172b8 -> interface_0_in_0x5604199172b8;
interface_7_out_0x56041991c938 -> interface_0_in_0x56041991c938;
interface_7_out_0x56041991cca8 -> interface_0_in_0x56041991cca8;

{
    rank = same;
    interface_5_out_0x5604185d74e0;
    interface_5_out_0x5604199469b0;
    interface_5_out_0x560419919c68;
    interface_5_out_0x560419918150;
    interface_7_out_0x5604199172b8;
    interface_7_out_0x56041991c938;
    interface_7_out_0x56041991cca8;
    interface_6_out_0x56041991ca28;
    interface_6_out_0x56041991ca78;
    interface_6_out_0x56041991ccf8;
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
			torch.randn([24, 3, 21]),
			torch.randn([12, 7, 21]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Splitcfaed96900632d48 -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Share010730f7adbbf8aa
		t_3 = torch.reshape(t_3, (1, 2, 12, 112, 112, ))

		# [s]@Reduce
		t_3 = torch.sum(t_3, dim=(1, ))

		# No contraction needed.
		t_4 = t_3

		# [H]@Shift9a938b886027bd1c -> [H]@Unfold411df36b3e389f9b
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [H]@Unfold411df36b3e389f9b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Share537524b85569cbbe
		t_4 = torch.reshape(t_4, (1, 1344, 112, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (7, 1, ), padding=(3, 0, ))
		t_4 = torch.reshape(t_4, (1, 12, 112, 7, 112, ))

		# Perform contraction.
		t_5 = torch.einsum("linjm, ijk -> lnmk", t_4, in_2)

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 1, 112, 2352, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 3, 112, 112, 21, ))

		# Perform contraction.
		t_7 = torch.einsum("ljmnk, ijk -> limn", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([96, 3, 21]),
			torch.randn([12, 7, 21]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Splitcfaed96900632d48 -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Share010730f7adbbf8aa
		t_3 = torch.reshape(t_3, (1, 2, 12, 56, 56, ))

		# [s]@Reduce
		t_3 = torch.sum(t_3, dim=(1, ))

		# No contraction needed.
		t_4 = t_3

		# [H]@Shift9a938b886027bd1c -> [H]@Unfold411df36b3e389f9b
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [H]@Unfold411df36b3e389f9b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Share537524b85569cbbe
		t_4 = torch.reshape(t_4, (1, 672, 56, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (7, 1, ), padding=(3, 0, ))
		t_4 = torch.reshape(t_4, (1, 12, 56, 7, 56, ))

		# Perform contraction.
		t_5 = torch.einsum("linjm, ijk -> lnmk", t_4, in_2)

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 1, 56, 1176, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 3, 56, 56, 21, ))

		# Perform contraction.
		t_7 = torch.einsum("ljmnk, ijk -> limn", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([192, 3, 21]),
			torch.randn([24, 7, 21]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Splitcfaed96900632d48 -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Share010730f7adbbf8aa
		t_3 = torch.reshape(t_3, (1, 2, 24, 56, 56, ))

		# [s]@Reduce
		t_3 = torch.sum(t_3, dim=(1, ))

		# No contraction needed.
		t_4 = t_3

		# [H]@Shift9a938b886027bd1c -> [H]@Unfold411df36b3e389f9b
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [H]@Unfold411df36b3e389f9b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Share537524b85569cbbe
		t_4 = torch.reshape(t_4, (1, 1344, 56, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (7, 1, ), padding=(3, 0, ))
		t_4 = torch.reshape(t_4, (1, 24, 56, 7, 56, ))

		# Perform contraction.
		t_5 = torch.einsum("linjm, ijk -> lnmk", t_4, in_2)

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 1, 56, 1176, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 3, 56, 56, 21, ))

		# Perform contraction.
		t_7 = torch.einsum("ljmnk, ijk -> limn", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([192, 3, 21]),
			torch.randn([24, 7, 21]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Splitcfaed96900632d48 -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Share010730f7adbbf8aa
		t_3 = torch.reshape(t_3, (1, 2, 24, 28, 28, ))

		# [s]@Reduce
		t_3 = torch.sum(t_3, dim=(1, ))

		# No contraction needed.
		t_4 = t_3

		# [H]@Shift9a938b886027bd1c -> [H]@Unfold411df36b3e389f9b
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [H]@Unfold411df36b3e389f9b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Share537524b85569cbbe
		t_4 = torch.reshape(t_4, (1, 672, 28, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (7, 1, ), padding=(3, 0, ))
		t_4 = torch.reshape(t_4, (1, 24, 28, 7, 28, ))

		# Perform contraction.
		t_5 = torch.einsum("linjm, ijk -> lnmk", t_4, in_2)

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 1, 28, 588, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 3, 28, 28, 21, ))

		# Perform contraction.
		t_7 = torch.einsum("ljmnk, ijk -> limn", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 21]),
			torch.randn([32, 7, 21]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Splitcfaed96900632d48 -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Share010730f7adbbf8aa
		t_3 = torch.reshape(t_3, (1, 2, 32, 28, 28, ))

		# [s]@Reduce
		t_3 = torch.sum(t_3, dim=(1, ))

		# No contraction needed.
		t_4 = t_3

		# [H]@Shift9a938b886027bd1c -> [H]@Unfold411df36b3e389f9b
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [H]@Unfold411df36b3e389f9b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Share537524b85569cbbe
		t_4 = torch.reshape(t_4, (1, 896, 28, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (7, 1, ), padding=(3, 0, ))
		t_4 = torch.reshape(t_4, (1, 32, 28, 7, 28, ))

		# Perform contraction.
		t_5 = torch.einsum("linjm, ijk -> lnmk", t_4, in_2)

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (1, 1, 28, 588, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (1, 3, 28, 28, 21, ))

		# Perform contraction.
		t_7 = torch.einsum("ljmnk, ijk -> limn", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

