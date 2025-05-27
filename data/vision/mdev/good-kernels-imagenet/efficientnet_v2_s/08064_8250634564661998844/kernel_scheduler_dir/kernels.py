import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7ef0e4001a98 [label="Sum", shape=box];
    reduce_0x7ef0e4002110 [label="Sum", shape=box];
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
        reduce_0x7ef0e4001a98;
        reduce_0x7ef0e4002110;
        interface_0_out_0x5596d7788c60;
        interface_0_out_0x5596d7788c88;
        interface_0_out_0x5596d7788cb0;
        interface_0_out_0x5596d7788cd8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5596d7788c60 [label="N", shape=none];
        interface_0_in_0x5596d7875490 [label="k_1", shape=none];
        interface_0_in_0x5596d7788cb0 [label="H", shape=none];
        interface_0_in_0x5596d7788cd8 [label="H", shape=none];
        interface_0_in_0x5596d787bb80 [label="k_1*k_2", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x5596d7875138 [label="C_out", shape=none];
        interface_0_in_0x5596d78754a8 [label="k_1", shape=none];
        interface_0_in_0x5596d787bb98 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5596d7788c60;
        interface_0_in_0x5596d7875490;
        interface_0_in_0x5596d7788cb0;
        interface_0_in_0x5596d7788cd8;
        interface_0_in_0x5596d787bb80;
        interface_0_in_0x5596d7875138;
        interface_0_in_0x5596d78754a8;
        interface_0_in_0x5596d787bb98;
    }
    // Op's.
    op_0x5596d7875100 [label="Share"];
    op_0x5596d7875470 [label="Share"];
    op_0x5596d7875618 [label="Expand"];
    op_0x5596d787bb60 [label="Share"];
    // Dimension's.
    interface_0_in_0x5596d7788c60 -> interface_0_out_0x5596d7788c60 [label="N"];
    op_0x5596d7875100 -> interface_0_out_0x5596d7788c88 [label="C_out"];
    interface_0_in_0x5596d7788cb0 -> interface_0_out_0x5596d7788cb0 [label="H"];
    interface_0_in_0x5596d7788cd8 -> interface_0_out_0x5596d7788cd8 [label="H"];
    op_0x5596d7875618 -> op_0x5596d7875100 [label="C_out"];
    interface_0_in_0x5596d7875138 -> op_0x5596d7875100 [label="C_out"];
    interface_0_in_0x5596d7875490 -> op_0x5596d7875470 [label="k_1"];
    interface_0_in_0x5596d78754a8 -> op_0x5596d7875470 [label="k_1"];
    interface_0_in_0x5596d787bb80 -> op_0x5596d787bb60 [label="k_1*k_2"];
    interface_0_in_0x5596d787bb98 -> op_0x5596d787bb60 [label="k_1*k_2"];
    op_0x5596d7875470 -> reduce_0x7ef0e4001a98 [label="k_1"];
    op_0x5596d787bb60 -> reduce_0x7ef0e4002110 [label="k_1*k_2"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5596d7788c60 [label="N", shape=none];
        interface_1_out_0x5596d7875490 [label="k_1", shape=none];
        interface_1_out_0x5596d7788cb0 [label="H", shape=none];
        interface_1_out_0x5596d7788cd8 [label="H", shape=none];
        interface_1_out_0x5596d787bb80 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x5596d7788c60;
        interface_1_out_0x5596d7875490;
        interface_1_out_0x5596d7788cb0;
        interface_1_out_0x5596d7788cd8;
        interface_1_out_0x5596d787bb80;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5596d7788c60 [label="N", shape=none];
        interface_1_in_0x5596d7879568 [label="H", shape=none];
        interface_1_in_0x5596d7788cd8 [label="H", shape=none];
        interface_1_in_0x5596d787bb80 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5596d7788c60;
        interface_1_in_0x5596d7879568;
        interface_1_in_0x5596d7788cd8;
        interface_1_in_0x5596d787bb80;
    }
    // Op's.
    op_0x5596d7879540 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x5596d7788c60 -> interface_1_out_0x5596d7788c60 [label="N"];
    op_0x5596d7879540 -> interface_1_out_0x5596d7788cb0 [label="H"];
    interface_1_in_0x5596d7788cd8 -> interface_1_out_0x5596d7788cd8 [label="H"];
    op_0x5596d7879540 -> interface_1_out_0x5596d7875490 [label="k_1"];
    interface_1_in_0x5596d7879568 -> op_0x5596d7879540 [label="H"];
    interface_1_in_0x5596d787bb80 -> interface_1_out_0x5596d787bb80 [label="k_1*k_2"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7ef0e4005768 [label="Sum", shape=box];
    reduce_0x7ef0e4001ee8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5596d7788c60 [label="N", shape=none];
        interface_2_out_0x5596d7879568 [label="H", shape=none];
        interface_2_out_0x5596d7788cd8 [label="H", shape=none];
        interface_2_out_0x5596d787bb80 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        reduce_0x7ef0e4005768;
        reduce_0x7ef0e4001ee8;
        interface_2_out_0x5596d7788c60;
        interface_2_out_0x5596d7879568;
        interface_2_out_0x5596d7788cd8;
        interface_2_out_0x5596d787bb80;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5596d7788c60 [label="N", shape=none];
        interface_2_in_0x5596d7875350 [label="s^-1*C_in", shape=none];
        interface_2_in_0x5596d7879568 [label="H", shape=none];
        interface_2_in_0x5596d78753a0 [label="k_2", shape=none];
        interface_2_in_0x5596d7788cd8 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x5596d7875368 [label="s^-1*C_in", shape=none];
        interface_2_in_0x5596d78753b8 [label="k_2", shape=none];
        interface_2_in_0x5596d787bbe8 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5596d7788c60;
        interface_2_in_0x5596d7875350;
        interface_2_in_0x5596d7879568;
        interface_2_in_0x5596d78753a0;
        interface_2_in_0x5596d7788cd8;
        interface_2_in_0x5596d7875368;
        interface_2_in_0x5596d78753b8;
        interface_2_in_0x5596d787bbe8;
    }
    // Op's.
    op_0x5596d7875330 [label="Share"];
    op_0x5596d7875380 [label="Share"];
    op_0x5596d7875738 [label="Expand"];
    op_0x5596d787bbb0 [label="Share"];
    // Dimension's.
    interface_2_in_0x5596d7788c60 -> interface_2_out_0x5596d7788c60 [label="N"];
    interface_2_in_0x5596d7788cd8 -> interface_2_out_0x5596d7788cd8 [label="H"];
    interface_2_in_0x5596d7875350 -> op_0x5596d7875330 [label="s^-1*C_in"];
    interface_2_in_0x5596d7875368 -> op_0x5596d7875330 [label="s^-1*C_in"];
    interface_2_in_0x5596d78753a0 -> op_0x5596d7875380 [label="k_2"];
    interface_2_in_0x5596d78753b8 -> op_0x5596d7875380 [label="k_2"];
    interface_2_in_0x5596d7879568 -> interface_2_out_0x5596d7879568 [label="H"];
    op_0x5596d787bbb0 -> interface_2_out_0x5596d787bb80 [label="k_1*k_2"];
    op_0x5596d7875738 -> op_0x5596d787bbb0 [label="k_1*k_2"];
    interface_2_in_0x5596d787bbe8 -> op_0x5596d787bbb0 [label="k_1*k_2"];
    op_0x5596d7875380 -> reduce_0x7ef0e4001ee8 [label="k_2"];
    op_0x5596d7875330 -> reduce_0x7ef0e4005768 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5596d7788c60 [label="N", shape=none];
        interface_3_out_0x5596d7875350 [label="s^-1*C_in", shape=none];
        interface_3_out_0x5596d7879568 [label="H", shape=none];
        interface_3_out_0x5596d78753a0 [label="k_2", shape=none];
        interface_3_out_0x5596d7788cd8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5596d7788c60;
        interface_3_out_0x5596d7875350;
        interface_3_out_0x5596d7879568;
        interface_3_out_0x5596d78753a0;
        interface_3_out_0x5596d7788cd8;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5596d7788c60 [label="N", shape=none];
        interface_3_in_0x5596d7875350 [label="s^-1*C_in", shape=none];
        interface_3_in_0x5596d7879568 [label="H", shape=none];
        interface_3_in_0x5596d7875f00 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5596d7788c60;
        interface_3_in_0x5596d7875350;
        interface_3_in_0x5596d7879568;
        interface_3_in_0x5596d7875f00;
    }
    // Op's.
    op_0x5596d7875ee0 [label="Shift"];
    op_0x5596d7879440 [label="Unfold"];
    // Dimension's.
    interface_3_in_0x5596d7788c60 -> interface_3_out_0x5596d7788c60 [label="N"];
    op_0x5596d7879440 -> interface_3_out_0x5596d7788cd8 [label="H"];
    interface_3_in_0x5596d7875350 -> interface_3_out_0x5596d7875350 [label="s^-1*C_in"];
    op_0x5596d7879440 -> interface_3_out_0x5596d78753a0 [label="k_2"];
    interface_3_in_0x5596d7875f00 -> op_0x5596d7875ee0 [label="H"];
    op_0x5596d7875ee0 -> op_0x5596d7879440 [label="H"];
    interface_3_in_0x5596d7879568 -> interface_3_out_0x5596d7879568 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    reduce_0x7ef0e4002e58 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x5596d7788c60 [label="N", shape=none];
        interface_4_out_0x5596d7875350 [label="s^-1*C_in", shape=none];
        interface_4_out_0x5596d7879568 [label="H", shape=none];
        interface_4_out_0x5596d7875f00 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7ef0e4002e58;
        interface_4_out_0x5596d7788c60;
        interface_4_out_0x5596d7875350;
        interface_4_out_0x5596d7879568;
        interface_4_out_0x5596d7875f00;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x5596d7788c60 [label="N", shape=none];
        interface_4_in_0x5596d7882840 [label="C_in", shape=none];
        interface_4_in_0x5596d7879568 [label="H", shape=none];
        interface_4_in_0x5596d7875f00 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x5596d7788c60;
        interface_4_in_0x5596d7882840;
        interface_4_in_0x5596d7879568;
        interface_4_in_0x5596d7875f00;
    }
    // Op's.
    op_0x5596d7882800 [label="Split"];
    // Dimension's.
    interface_4_in_0x5596d7788c60 -> interface_4_out_0x5596d7788c60 [label="N"];
    op_0x5596d7882800 -> interface_4_out_0x5596d7875350 [label="s^-1*C_in"];
    interface_4_in_0x5596d7875f00 -> interface_4_out_0x5596d7875f00 [label="H"];
    interface_4_in_0x5596d7879568 -> interface_4_out_0x5596d7879568 [label="H"];
    interface_4_in_0x5596d7882840 -> op_0x5596d7882800 [label="C_in"];
    op_0x5596d7882800 -> reduce_0x7ef0e4002e58 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x5596d7788c60 [label="N", shape=none];
    interface_5_out_0x5596d7882840 [label="C_in", shape=none];
    interface_5_out_0x5596d7879568 [label="H", shape=none];
    interface_5_out_0x5596d7875f00 [label="H", shape=none];
}

interface_5_out_0x5596d7788c60 -> interface_4_in_0x5596d7788c60;
interface_5_out_0x5596d7882840 -> interface_4_in_0x5596d7882840;
interface_5_out_0x5596d7879568 -> interface_4_in_0x5596d7879568;
interface_5_out_0x5596d7875f00 -> interface_4_in_0x5596d7875f00;

interface_4_out_0x5596d7788c60 -> interface_3_in_0x5596d7788c60;
interface_4_out_0x5596d7875350 -> interface_3_in_0x5596d7875350;
interface_4_out_0x5596d7879568 -> interface_3_in_0x5596d7879568;
interface_4_out_0x5596d7875f00 -> interface_3_in_0x5596d7875f00;

interface_3_out_0x5596d7788c60 -> interface_2_in_0x5596d7788c60;
interface_3_out_0x5596d7875350 -> interface_2_in_0x5596d7875350;
interface_3_out_0x5596d7879568 -> interface_2_in_0x5596d7879568;
interface_3_out_0x5596d78753a0 -> interface_2_in_0x5596d78753a0;
interface_3_out_0x5596d7788cd8 -> interface_2_in_0x5596d7788cd8;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x5596d7875368 [label="s^-1*C_in", shape=none];
    interface_6_out_0x5596d78753b8 [label="k_2", shape=none];
    interface_6_out_0x5596d787bbe8 [label="k_1*k_2", shape=none];
}

interface_6_out_0x5596d7875368 -> interface_2_in_0x5596d7875368;
interface_6_out_0x5596d78753b8 -> interface_2_in_0x5596d78753b8;
interface_6_out_0x5596d787bbe8 -> interface_2_in_0x5596d787bbe8;

interface_2_out_0x5596d7788c60 -> interface_1_in_0x5596d7788c60;
interface_2_out_0x5596d7879568 -> interface_1_in_0x5596d7879568;
interface_2_out_0x5596d7788cd8 -> interface_1_in_0x5596d7788cd8;
interface_2_out_0x5596d787bb80 -> interface_1_in_0x5596d787bb80;

interface_1_out_0x5596d7788c60 -> interface_0_in_0x5596d7788c60;
interface_1_out_0x5596d7875490 -> interface_0_in_0x5596d7875490;
interface_1_out_0x5596d7788cb0 -> interface_0_in_0x5596d7788cb0;
interface_1_out_0x5596d7788cd8 -> interface_0_in_0x5596d7788cd8;
interface_1_out_0x5596d787bb80 -> interface_0_in_0x5596d787bb80;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x5596d7875138 [label="C_out", shape=none];
    interface_7_out_0x5596d78754a8 [label="k_1", shape=none];
    interface_7_out_0x5596d787bb98 [label="k_1*k_2", shape=none];
}

interface_7_out_0x5596d7875138 -> interface_0_in_0x5596d7875138;
interface_7_out_0x5596d78754a8 -> interface_0_in_0x5596d78754a8;
interface_7_out_0x5596d787bb98 -> interface_0_in_0x5596d787bb98;

{
    rank = same;
    interface_5_out_0x5596d7788c60;
    interface_5_out_0x5596d7882840;
    interface_5_out_0x5596d7879568;
    interface_5_out_0x5596d7875f00;
    interface_7_out_0x5596d7875138;
    interface_7_out_0x5596d78754a8;
    interface_7_out_0x5596d787bb98;
    interface_6_out_0x5596d7875368;
    interface_6_out_0x5596d78753b8;
    interface_6_out_0x5596d787bbe8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x5596d7788c60 [label="N", shape=none];
    interface_8_in_0x5596d7788c88 [label="C_out", shape=none];
    interface_8_in_0x5596d7788cb0 [label="H", shape=none];
    interface_8_in_0x5596d7788cd8 [label="H", shape=none];
}
interface_0_out_0x5596d7788c60 -> interface_8_in_0x5596d7788c60;
interface_0_out_0x5596d7788c88 -> interface_8_in_0x5596d7788c88;
interface_0_out_0x5596d7788cb0 -> interface_8_in_0x5596d7788cb0;
interface_0_out_0x5596d7788cd8 -> interface_8_in_0x5596d7788cd8;

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

