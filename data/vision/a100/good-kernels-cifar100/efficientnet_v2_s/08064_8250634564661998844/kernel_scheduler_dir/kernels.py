import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7fc7f0001998 [label="Sum", shape=box];
    reduce_0x7fc7f0002010 [label="Sum", shape=box];
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
        reduce_0x7fc7f0001998;
        reduce_0x7fc7f0002010;
        interface_0_out_0x5581660a87e0;
        interface_0_out_0x5581660a8808;
        interface_0_out_0x5581660a8830;
        interface_0_out_0x5581660a8858;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5581660a87e0 [label="N", shape=none];
        interface_0_in_0x7fcf84004330 [label="k_1", shape=none];
        interface_0_in_0x5581660a8830 [label="H", shape=none];
        interface_0_in_0x5581660a8858 [label="H", shape=none];
        interface_0_in_0x7fcf58004af0 [label="k_1*k_2", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x7fcf84003f38 [label="C_out", shape=none];
        interface_0_in_0x7fcf84004348 [label="k_1", shape=none];
        interface_0_in_0x7fcf58004b08 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5581660a87e0;
        interface_0_in_0x7fcf84004330;
        interface_0_in_0x5581660a8830;
        interface_0_in_0x5581660a8858;
        interface_0_in_0x7fcf58004af0;
        interface_0_in_0x7fcf84003f38;
        interface_0_in_0x7fcf84004348;
        interface_0_in_0x7fcf58004b08;
    }
    // Op's.
    op_0x7fcf58004ad0 [label="Share"];
    op_0x7fcf84003f00 [label="Share"];
    op_0x7fcf84004310 [label="Share"];
    op_0x7fcf84004638 [label="Expand"];
    // Dimension's.
    interface_0_in_0x5581660a87e0 -> interface_0_out_0x5581660a87e0 [label="N"];
    op_0x7fcf84003f00 -> interface_0_out_0x5581660a8808 [label="C_out"];
    interface_0_in_0x5581660a8830 -> interface_0_out_0x5581660a8830 [label="H"];
    interface_0_in_0x5581660a8858 -> interface_0_out_0x5581660a8858 [label="H"];
    op_0x7fcf84004310 -> reduce_0x7fc7f0001998 [label="k_1"];
    op_0x7fcf58004ad0 -> reduce_0x7fc7f0002010 [label="k_1*k_2"];
    interface_0_in_0x7fcf58004af0 -> op_0x7fcf58004ad0 [label="k_1*k_2"];
    interface_0_in_0x7fcf58004b08 -> op_0x7fcf58004ad0 [label="k_1*k_2"];
    op_0x7fcf84004638 -> op_0x7fcf84003f00 [label="C_out"];
    interface_0_in_0x7fcf84003f38 -> op_0x7fcf84003f00 [label="C_out"];
    interface_0_in_0x7fcf84004330 -> op_0x7fcf84004310 [label="k_1"];
    interface_0_in_0x7fcf84004348 -> op_0x7fcf84004310 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5581660a87e0 [label="N", shape=none];
        interface_1_out_0x7fcf84004330 [label="k_1", shape=none];
        interface_1_out_0x5581660a8830 [label="H", shape=none];
        interface_1_out_0x5581660a8858 [label="H", shape=none];
        interface_1_out_0x7fcf58004af0 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x5581660a87e0;
        interface_1_out_0x7fcf84004330;
        interface_1_out_0x5581660a8830;
        interface_1_out_0x5581660a8858;
        interface_1_out_0x7fcf58004af0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5581660a87e0 [label="N", shape=none];
        interface_1_in_0x7fcba8009ce8 [label="H", shape=none];
        interface_1_in_0x5581660a8858 [label="H", shape=none];
        interface_1_in_0x7fcf58004af0 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5581660a87e0;
        interface_1_in_0x7fcba8009ce8;
        interface_1_in_0x5581660a8858;
        interface_1_in_0x7fcf58004af0;
    }
    // Op's.
    op_0x7fcba8009cc0 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x5581660a87e0 -> interface_1_out_0x5581660a87e0 [label="N"];
    op_0x7fcba8009cc0 -> interface_1_out_0x5581660a8830 [label="H"];
    interface_1_in_0x5581660a8858 -> interface_1_out_0x5581660a8858 [label="H"];
    interface_1_in_0x7fcba8009ce8 -> op_0x7fcba8009cc0 [label="H"];
    interface_1_in_0x7fcf58004af0 -> interface_1_out_0x7fcf58004af0 [label="k_1*k_2"];
    op_0x7fcba8009cc0 -> interface_1_out_0x7fcf84004330 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7fc7f0005968 [label="Sum", shape=box];
    reduce_0x7fc7f0001de8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5581660a87e0 [label="N", shape=none];
        interface_2_out_0x7fcba8009ce8 [label="H", shape=none];
        interface_2_out_0x5581660a8858 [label="H", shape=none];
        interface_2_out_0x7fcf58004af0 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc7f0005968;
        reduce_0x7fc7f0001de8;
        interface_2_out_0x5581660a87e0;
        interface_2_out_0x7fcba8009ce8;
        interface_2_out_0x5581660a8858;
        interface_2_out_0x7fcf58004af0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5581660a87e0 [label="N", shape=none];
        interface_2_in_0x7fc950009e70 [label="s^-1*C_in", shape=none];
        interface_2_in_0x7fcba8009ce8 [label="H", shape=none];
        interface_2_in_0x7fceec0418f0 [label="k_2", shape=none];
        interface_2_in_0x5581660a8858 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x7fc950009e88 [label="s^-1*C_in", shape=none];
        interface_2_in_0x7fceec041908 [label="k_2", shape=none];
        interface_2_in_0x7fc950008bc8 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5581660a87e0;
        interface_2_in_0x7fc950009e70;
        interface_2_in_0x7fcba8009ce8;
        interface_2_in_0x7fceec0418f0;
        interface_2_in_0x5581660a8858;
        interface_2_in_0x7fc950009e88;
        interface_2_in_0x7fceec041908;
        interface_2_in_0x7fc950008bc8;
    }
    // Op's.
    op_0x7fc950008b90 [label="Share"];
    op_0x7fc950009e50 [label="Share"];
    op_0x7fceec0418d0 [label="Share"];
    op_0x7fcf84004978 [label="Expand"];
    // Dimension's.
    interface_2_in_0x5581660a87e0 -> interface_2_out_0x5581660a87e0 [label="N"];
    interface_2_in_0x5581660a8858 -> interface_2_out_0x5581660a8858 [label="H"];
    op_0x7fceec0418d0 -> reduce_0x7fc7f0001de8 [label="k_2"];
    op_0x7fc950009e50 -> reduce_0x7fc7f0005968 [label="s^-1*C_in"];
    op_0x7fcf84004978 -> op_0x7fc950008b90 [label="k_1*k_2"];
    interface_2_in_0x7fc950008bc8 -> op_0x7fc950008b90 [label="k_1*k_2"];
    interface_2_in_0x7fc950009e70 -> op_0x7fc950009e50 [label="s^-1*C_in"];
    interface_2_in_0x7fc950009e88 -> op_0x7fc950009e50 [label="s^-1*C_in"];
    interface_2_in_0x7fcba8009ce8 -> interface_2_out_0x7fcba8009ce8 [label="H"];
    interface_2_in_0x7fceec0418f0 -> op_0x7fceec0418d0 [label="k_2"];
    interface_2_in_0x7fceec041908 -> op_0x7fceec0418d0 [label="k_2"];
    op_0x7fc950008b90 -> interface_2_out_0x7fcf58004af0 [label="k_1*k_2"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5581660a87e0 [label="N", shape=none];
        interface_3_out_0x7fc950009e70 [label="s^-1*C_in", shape=none];
        interface_3_out_0x7fcba8009ce8 [label="H", shape=none];
        interface_3_out_0x7fceec0418f0 [label="k_2", shape=none];
        interface_3_out_0x5581660a8858 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5581660a87e0;
        interface_3_out_0x7fc950009e70;
        interface_3_out_0x7fcba8009ce8;
        interface_3_out_0x7fceec0418f0;
        interface_3_out_0x5581660a8858;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5581660a87e0 [label="N", shape=none];
        interface_3_in_0x7fc950009e70 [label="s^-1*C_in", shape=none];
        interface_3_in_0x7fcba8009ce8 [label="H", shape=none];
        interface_3_in_0x7fce0006ce30 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5581660a87e0;
        interface_3_in_0x7fc950009e70;
        interface_3_in_0x7fcba8009ce8;
        interface_3_in_0x7fce0006ce30;
    }
    // Op's.
    op_0x7fc6f00255c0 [label="Unfold"];
    op_0x7fce0006ce10 [label="Shift"];
    // Dimension's.
    interface_3_in_0x5581660a87e0 -> interface_3_out_0x5581660a87e0 [label="N"];
    op_0x7fc6f00255c0 -> interface_3_out_0x5581660a8858 [label="H"];
    op_0x7fce0006ce10 -> op_0x7fc6f00255c0 [label="H"];
    interface_3_in_0x7fc950009e70 -> interface_3_out_0x7fc950009e70 [label="s^-1*C_in"];
    interface_3_in_0x7fcba8009ce8 -> interface_3_out_0x7fcba8009ce8 [label="H"];
    interface_3_in_0x7fce0006ce30 -> op_0x7fce0006ce10 [label="H"];
    op_0x7fc6f00255c0 -> interface_3_out_0x7fceec0418f0 [label="k_2"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    reduce_0x7fc7f0002f58 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x5581660a87e0 [label="N", shape=none];
        interface_4_out_0x7fc950009e70 [label="s^-1*C_in", shape=none];
        interface_4_out_0x7fcba8009ce8 [label="H", shape=none];
        interface_4_out_0x7fce0006ce30 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fc7f0002f58;
        interface_4_out_0x5581660a87e0;
        interface_4_out_0x7fc950009e70;
        interface_4_out_0x7fcba8009ce8;
        interface_4_out_0x7fce0006ce30;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x5581660a87e0 [label="N", shape=none];
        interface_4_in_0x7fca444b2d80 [label="C_in", shape=none];
        interface_4_in_0x7fcba8009ce8 [label="H", shape=none];
        interface_4_in_0x7fce0006ce30 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x5581660a87e0;
        interface_4_in_0x7fca444b2d80;
        interface_4_in_0x7fcba8009ce8;
        interface_4_in_0x7fce0006ce30;
    }
    // Op's.
    op_0x7fca444b2d40 [label="Split"];
    // Dimension's.
    interface_4_in_0x5581660a87e0 -> interface_4_out_0x5581660a87e0 [label="N"];
    op_0x7fca444b2d40 -> reduce_0x7fc7f0002f58 [label="s"];
    op_0x7fca444b2d40 -> interface_4_out_0x7fc950009e70 [label="s^-1*C_in"];
    interface_4_in_0x7fca444b2d80 -> op_0x7fca444b2d40 [label="C_in"];
    interface_4_in_0x7fcba8009ce8 -> interface_4_out_0x7fcba8009ce8 [label="H"];
    interface_4_in_0x7fce0006ce30 -> interface_4_out_0x7fce0006ce30 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x5581660a87e0 [label="N", shape=none];
    interface_5_out_0x7fca444b2d80 [label="C_in", shape=none];
    interface_5_out_0x7fcba8009ce8 [label="H", shape=none];
    interface_5_out_0x7fce0006ce30 [label="H", shape=none];
}

interface_5_out_0x5581660a87e0 -> interface_4_in_0x5581660a87e0;
interface_5_out_0x7fca444b2d80 -> interface_4_in_0x7fca444b2d80;
interface_5_out_0x7fcba8009ce8 -> interface_4_in_0x7fcba8009ce8;
interface_5_out_0x7fce0006ce30 -> interface_4_in_0x7fce0006ce30;

interface_4_out_0x5581660a87e0 -> interface_3_in_0x5581660a87e0;
interface_4_out_0x7fc950009e70 -> interface_3_in_0x7fc950009e70;
interface_4_out_0x7fcba8009ce8 -> interface_3_in_0x7fcba8009ce8;
interface_4_out_0x7fce0006ce30 -> interface_3_in_0x7fce0006ce30;

interface_3_out_0x5581660a87e0 -> interface_2_in_0x5581660a87e0;
interface_3_out_0x7fc950009e70 -> interface_2_in_0x7fc950009e70;
interface_3_out_0x7fcba8009ce8 -> interface_2_in_0x7fcba8009ce8;
interface_3_out_0x7fceec0418f0 -> interface_2_in_0x7fceec0418f0;
interface_3_out_0x5581660a8858 -> interface_2_in_0x5581660a8858;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x7fc950009e88 [label="s^-1*C_in", shape=none];
    interface_6_out_0x7fceec041908 [label="k_2", shape=none];
    interface_6_out_0x7fc950008bc8 [label="k_1*k_2", shape=none];
}

interface_6_out_0x7fc950009e88 -> interface_2_in_0x7fc950009e88;
interface_6_out_0x7fceec041908 -> interface_2_in_0x7fceec041908;
interface_6_out_0x7fc950008bc8 -> interface_2_in_0x7fc950008bc8;

interface_2_out_0x5581660a87e0 -> interface_1_in_0x5581660a87e0;
interface_2_out_0x7fcba8009ce8 -> interface_1_in_0x7fcba8009ce8;
interface_2_out_0x5581660a8858 -> interface_1_in_0x5581660a8858;
interface_2_out_0x7fcf58004af0 -> interface_1_in_0x7fcf58004af0;

interface_1_out_0x5581660a87e0 -> interface_0_in_0x5581660a87e0;
interface_1_out_0x7fcf84004330 -> interface_0_in_0x7fcf84004330;
interface_1_out_0x5581660a8830 -> interface_0_in_0x5581660a8830;
interface_1_out_0x5581660a8858 -> interface_0_in_0x5581660a8858;
interface_1_out_0x7fcf58004af0 -> interface_0_in_0x7fcf58004af0;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x7fcf84003f38 [label="C_out", shape=none];
    interface_7_out_0x7fcf84004348 [label="k_1", shape=none];
    interface_7_out_0x7fcf58004b08 [label="k_1*k_2", shape=none];
}

interface_7_out_0x7fcf84003f38 -> interface_0_in_0x7fcf84003f38;
interface_7_out_0x7fcf84004348 -> interface_0_in_0x7fcf84004348;
interface_7_out_0x7fcf58004b08 -> interface_0_in_0x7fcf58004b08;

{
    rank = same;
    interface_5_out_0x5581660a87e0;
    interface_5_out_0x7fca444b2d80;
    interface_5_out_0x7fcba8009ce8;
    interface_5_out_0x7fce0006ce30;
    interface_7_out_0x7fcf84003f38;
    interface_7_out_0x7fcf84004348;
    interface_7_out_0x7fcf58004b08;
    interface_6_out_0x7fc950009e88;
    interface_6_out_0x7fceec041908;
    interface_6_out_0x7fc950008bc8;
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
		t_3 = torch.reshape(t_3, (128, 2, 12, 112, 112, ))

		# [s]@Reduce
		t_3 = torch.sum(t_3, dim=(1, ))

		# No contraction needed.
		t_4 = t_3

		# [H]@Shift9a938b886027bd1c -> [H]@Unfold411df36b3e389f9b
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [H]@Unfold411df36b3e389f9b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Share537524b85569cbbe
		t_4 = torch.reshape(t_4, (128, 1344, 112, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (7, 1, ), padding=(3, 0, ))
		t_4 = torch.reshape(t_4, (128, 12, 112, 7, 112, ))

		# Perform contraction.
		t_5 = torch.einsum("ljnkm, jki -> lnmi", t_4, in_2)

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 1, 112, 2352, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 3, 112, 112, 21, ))

		# Perform contraction.
		t_7 = torch.einsum("lkmni, jki -> ljmn", t_6, in_1)

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
		t_3 = torch.reshape(t_3, (128, 2, 12, 56, 56, ))

		# [s]@Reduce
		t_3 = torch.sum(t_3, dim=(1, ))

		# No contraction needed.
		t_4 = t_3

		# [H]@Shift9a938b886027bd1c -> [H]@Unfold411df36b3e389f9b
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [H]@Unfold411df36b3e389f9b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Share537524b85569cbbe
		t_4 = torch.reshape(t_4, (128, 672, 56, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (7, 1, ), padding=(3, 0, ))
		t_4 = torch.reshape(t_4, (128, 12, 56, 7, 56, ))

		# Perform contraction.
		t_5 = torch.einsum("ljnkm, jki -> lnmi", t_4, in_2)

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 1, 56, 1176, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 3, 56, 56, 21, ))

		# Perform contraction.
		t_7 = torch.einsum("lkmni, jki -> ljmn", t_6, in_1)

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
		t_3 = torch.reshape(t_3, (128, 2, 24, 56, 56, ))

		# [s]@Reduce
		t_3 = torch.sum(t_3, dim=(1, ))

		# No contraction needed.
		t_4 = t_3

		# [H]@Shift9a938b886027bd1c -> [H]@Unfold411df36b3e389f9b
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [H]@Unfold411df36b3e389f9b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Share537524b85569cbbe
		t_4 = torch.reshape(t_4, (128, 1344, 56, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (7, 1, ), padding=(3, 0, ))
		t_4 = torch.reshape(t_4, (128, 24, 56, 7, 56, ))

		# Perform contraction.
		t_5 = torch.einsum("ljnkm, jki -> lnmi", t_4, in_2)

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 1, 56, 1176, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 3, 56, 56, 21, ))

		# Perform contraction.
		t_7 = torch.einsum("lkmni, jki -> ljmn", t_6, in_1)

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
		t_3 = torch.reshape(t_3, (128, 2, 24, 28, 28, ))

		# [s]@Reduce
		t_3 = torch.sum(t_3, dim=(1, ))

		# No contraction needed.
		t_4 = t_3

		# [H]@Shift9a938b886027bd1c -> [H]@Unfold411df36b3e389f9b
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [H]@Unfold411df36b3e389f9b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Share537524b85569cbbe
		t_4 = torch.reshape(t_4, (128, 672, 28, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (7, 1, ), padding=(3, 0, ))
		t_4 = torch.reshape(t_4, (128, 24, 28, 7, 28, ))

		# Perform contraction.
		t_5 = torch.einsum("ljnkm, jki -> lnmi", t_4, in_2)

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 1, 28, 588, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 3, 28, 28, 21, ))

		# Perform contraction.
		t_7 = torch.einsum("lkmni, jki -> ljmn", t_6, in_1)

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
		t_3 = torch.reshape(t_3, (128, 2, 32, 28, 28, ))

		# [s]@Reduce
		t_3 = torch.sum(t_3, dim=(1, ))

		# No contraction needed.
		t_4 = t_3

		# [H]@Shift9a938b886027bd1c -> [H]@Unfold411df36b3e389f9b
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [H]@Unfold411df36b3e389f9b -> [H]@Iteratorb0a1def4ad5784ec, [k_2]@Share537524b85569cbbe
		t_4 = torch.reshape(t_4, (128, 896, 28, 1, ))
		t_4 = torch.nn.functional.unfold(t_4, (7, 1, ), padding=(3, 0, ))
		t_4 = torch.reshape(t_4, (128, 32, 28, 7, 28, ))

		# Perform contraction.
		t_5 = torch.einsum("ljnkm, jki -> lnmi", t_4, in_2)

		# No contraction needed.
		t_6 = t_5

		# [H]@Unfold4d77c1e3da5bca44 -> [H]@Iterator96123ba3184da39c, [k_1]@Share26cfa48d169008e4
		t_6 = torch.reshape(t_6, (128, 1, 28, 588, ))
		t_6 = torch.nn.functional.unfold(t_6, (3, 1, ), padding=(1, 0, ))
		t_6 = torch.reshape(t_6, (128, 3, 28, 28, 21, ))

		# Perform contraction.
		t_7 = torch.einsum("lkmni, jki -> ljmn", t_6, in_1)

		# No need to crop the output tensor.
		y = t_7

		return y

