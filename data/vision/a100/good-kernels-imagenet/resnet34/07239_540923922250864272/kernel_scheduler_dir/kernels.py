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
        interface_0_out_0x5605b0775920 [label="N", shape=none];
        interface_0_out_0x5605b0775948 [label="C_out", shape=none];
        interface_0_out_0x5605b0775970 [label="H", shape=none];
        interface_0_out_0x5605b0775998 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x5605b0775920;
        interface_0_out_0x5605b0775948;
        interface_0_out_0x5605b0775970;
        interface_0_out_0x5605b0775998;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5605b0775920 [label="N", shape=none];
        interface_0_in_0x5605b0775948 [label="C_out", shape=none];
        interface_0_in_0x5605b0775970 [label="H", shape=none];
        interface_0_in_0x5605beb89550 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5605b0775920;
        interface_0_in_0x5605b0775948;
        interface_0_in_0x5605b0775970;
        interface_0_in_0x5605beb89550;
    }
    // Op's.
    op_0x5605beb89530 [label="Shift"];
    // Dimension's.
    interface_0_in_0x5605b0775920 -> interface_0_out_0x5605b0775920 [label="N"];
    interface_0_in_0x5605b0775948 -> interface_0_out_0x5605b0775948 [label="C_out"];
    interface_0_in_0x5605b0775970 -> interface_0_out_0x5605b0775970 [label="H"];
    op_0x5605beb89530 -> interface_0_out_0x5605b0775998 [label="H"];
    interface_0_in_0x5605beb89550 -> op_0x5605beb89530 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f7a20004ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5605b0775920 [label="N", shape=none];
        interface_1_out_0x5605b0775948 [label="C_out", shape=none];
        interface_1_out_0x5605b0775970 [label="H", shape=none];
        interface_1_out_0x5605beb89550 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f7a20004ce8;
        interface_1_out_0x5605b0775920;
        interface_1_out_0x5605b0775948;
        interface_1_out_0x5605b0775970;
        interface_1_out_0x5605beb89550;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5605b0775920 [label="N", shape=none];
        interface_1_in_0x5605b0775948 [label="C_out", shape=none];
        interface_1_in_0x5605beb8abc0 [label="H", shape=none];
        interface_1_in_0x5605beb8abd8 [label="s", shape=none];
        interface_1_in_0x5605beb89550 [label="H", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5605b0775920;
        interface_1_in_0x5605b0775948;
        interface_1_in_0x5605beb8abc0;
        interface_1_in_0x5605beb8abd8;
        interface_1_in_0x5605beb89550;
    }
    // Op's.
    op_0x5605beb89590 [label="Shift"];
    op_0x5605beb89c20 [label="Split"];
    op_0x5605beb8ab80 [label="Merge"];
    // Dimension's.
    interface_1_in_0x5605b0775920 -> interface_1_out_0x5605b0775920 [label="N"];
    interface_1_in_0x5605b0775948 -> interface_1_out_0x5605b0775948 [label="C_out"];
    op_0x5605beb89c20 -> interface_1_out_0x5605b0775970 [label="H"];
    interface_1_in_0x5605beb89550 -> interface_1_out_0x5605beb89550 [label="H"];
    op_0x5605beb8ab80 -> op_0x5605beb89590 [label="s*H"];
    op_0x5605beb89590 -> op_0x5605beb89c20 [label="s*H"];
    interface_1_in_0x5605beb8abc0 -> op_0x5605beb8ab80 [label="H"];
    interface_1_in_0x5605beb8abd8 -> op_0x5605beb8ab80 [label="s"];
    op_0x5605beb89c20 -> reduce_0x7f7a20004ce8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f7a20003a98 [label="Sum", shape=box];
    reduce_0x7f7a20007948 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5605b0775920 [label="N", shape=none];
        interface_2_out_0x5605b0775948 [label="C_out", shape=none];
        interface_2_out_0x5605beb8abc0 [label="H", shape=none];
        interface_2_out_0x5605beb8abd8 [label="s", shape=none];
        interface_2_out_0x5605beb89550 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f7a20003a98;
        reduce_0x7f7a20007948;
        interface_2_out_0x5605b0775920;
        interface_2_out_0x5605b0775948;
        interface_2_out_0x5605beb8abc0;
        interface_2_out_0x5605beb8abd8;
        interface_2_out_0x5605beb89550;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5605b0775920 [label="N", shape=none];
        interface_2_in_0x5605beb88910 [label="k_1", shape=none];
        interface_2_in_0x5605beb8abc0 [label="H", shape=none];
        interface_2_in_0x5605beb888c0 [label="C_in", shape=none];
        interface_2_in_0x5605beb89550 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x5605beb88838 [label="C_out", shape=none];
        interface_2_in_0x5605beb88928 [label="k_1", shape=none];
        interface_2_in_0x5605beb889c8 [label="s", shape=none];
        interface_2_in_0x5605beb888d8 [label="C_in", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5605b0775920;
        interface_2_in_0x5605beb88910;
        interface_2_in_0x5605beb8abc0;
        interface_2_in_0x5605beb888c0;
        interface_2_in_0x5605beb89550;
        interface_2_in_0x5605beb88838;
        interface_2_in_0x5605beb88928;
        interface_2_in_0x5605beb889c8;
        interface_2_in_0x5605beb888d8;
    }
    // Op's.
    op_0x5605beb88800 [label="Share"];
    op_0x5605beb888a0 [label="Share"];
    op_0x5605beb888f0 [label="Share"];
    op_0x5605beb88990 [label="Share"];
    op_0x5605beb88cd8 [label="Expand"];
    op_0x5605beb88d18 [label="Expand"];
    // Dimension's.
    interface_2_in_0x5605b0775920 -> interface_2_out_0x5605b0775920 [label="N"];
    op_0x5605beb88800 -> interface_2_out_0x5605b0775948 [label="C_out"];
    op_0x5605beb88cd8 -> op_0x5605beb88800 [label="C_out"];
    interface_2_in_0x5605beb88838 -> op_0x5605beb88800 [label="C_out"];
    interface_2_in_0x5605beb888c0 -> op_0x5605beb888a0 [label="C_in"];
    interface_2_in_0x5605beb888d8 -> op_0x5605beb888a0 [label="C_in"];
    interface_2_in_0x5605beb88910 -> op_0x5605beb888f0 [label="k_1"];
    interface_2_in_0x5605beb88928 -> op_0x5605beb888f0 [label="k_1"];
    op_0x5605beb88d18 -> op_0x5605beb88990 [label="s"];
    interface_2_in_0x5605beb889c8 -> op_0x5605beb88990 [label="s"];
    interface_2_in_0x5605beb89550 -> interface_2_out_0x5605beb89550 [label="H"];
    interface_2_in_0x5605beb8abc0 -> interface_2_out_0x5605beb8abc0 [label="H"];
    op_0x5605beb88990 -> interface_2_out_0x5605beb8abd8 [label="s"];
    op_0x5605beb888f0 -> reduce_0x7f7a20003a98 [label="k_1"];
    op_0x5605beb888a0 -> reduce_0x7f7a20007948 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5605b0775920 [label="N", shape=none];
        interface_3_out_0x5605beb88910 [label="k_1", shape=none];
        interface_3_out_0x5605beb8abc0 [label="H", shape=none];
        interface_3_out_0x5605beb888c0 [label="C_in", shape=none];
        interface_3_out_0x5605beb89550 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x5605b0775920;
        interface_3_out_0x5605beb88910;
        interface_3_out_0x5605beb8abc0;
        interface_3_out_0x5605beb888c0;
        interface_3_out_0x5605beb89550;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5605b0775920 [label="N", shape=none];
        interface_3_in_0x5605beb888c0 [label="C_in", shape=none];
        interface_3_in_0x5605beb89550 [label="H", shape=none];
        interface_3_in_0x5605beb97ae8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5605b0775920;
        interface_3_in_0x5605beb888c0;
        interface_3_in_0x5605beb89550;
        interface_3_in_0x5605beb97ae8;
    }
    // Op's.
    op_0x5605beb97ac0 [label="Unfold"];
    // Dimension's.
    interface_3_in_0x5605b0775920 -> interface_3_out_0x5605b0775920 [label="N"];
    interface_3_in_0x5605beb888c0 -> interface_3_out_0x5605beb888c0 [label="C_in"];
    op_0x5605beb97ac0 -> interface_3_out_0x5605beb88910 [label="k_1"];
    interface_3_in_0x5605beb89550 -> interface_3_out_0x5605beb89550 [label="H"];
    op_0x5605beb97ac0 -> interface_3_out_0x5605beb8abc0 [label="H"];
    interface_3_in_0x5605beb97ae8 -> op_0x5605beb97ac0 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x5605b0775920 [label="N", shape=none];
    interface_4_out_0x5605beb888c0 [label="C_in", shape=none];
    interface_4_out_0x5605beb89550 [label="H", shape=none];
    interface_4_out_0x5605beb97ae8 [label="H", shape=none];
}

interface_4_out_0x5605b0775920 -> interface_3_in_0x5605b0775920;
interface_4_out_0x5605beb888c0 -> interface_3_in_0x5605beb888c0;
interface_4_out_0x5605beb89550 -> interface_3_in_0x5605beb89550;
interface_4_out_0x5605beb97ae8 -> interface_3_in_0x5605beb97ae8;

interface_3_out_0x5605b0775920 -> interface_2_in_0x5605b0775920;
interface_3_out_0x5605beb88910 -> interface_2_in_0x5605beb88910;
interface_3_out_0x5605beb8abc0 -> interface_2_in_0x5605beb8abc0;
interface_3_out_0x5605beb888c0 -> interface_2_in_0x5605beb888c0;
interface_3_out_0x5605beb89550 -> interface_2_in_0x5605beb89550;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x5605beb88838 [label="C_out", shape=none];
    interface_5_out_0x5605beb88928 [label="k_1", shape=none];
    interface_5_out_0x5605beb889c8 [label="s", shape=none];
    interface_5_out_0x5605beb888d8 [label="C_in", shape=none];
}

interface_5_out_0x5605beb88838 -> interface_2_in_0x5605beb88838;
interface_5_out_0x5605beb88928 -> interface_2_in_0x5605beb88928;
interface_5_out_0x5605beb889c8 -> interface_2_in_0x5605beb889c8;
interface_5_out_0x5605beb888d8 -> interface_2_in_0x5605beb888d8;

interface_2_out_0x5605b0775920 -> interface_1_in_0x5605b0775920;
interface_2_out_0x5605b0775948 -> interface_1_in_0x5605b0775948;
interface_2_out_0x5605beb8abc0 -> interface_1_in_0x5605beb8abc0;
interface_2_out_0x5605beb8abd8 -> interface_1_in_0x5605beb8abd8;
interface_2_out_0x5605beb89550 -> interface_1_in_0x5605beb89550;

interface_1_out_0x5605b0775920 -> interface_0_in_0x5605b0775920;
interface_1_out_0x5605b0775948 -> interface_0_in_0x5605b0775948;
interface_1_out_0x5605b0775970 -> interface_0_in_0x5605b0775970;
interface_1_out_0x5605beb89550 -> interface_0_in_0x5605beb89550;

{
    rank = same;
    interface_4_out_0x5605b0775920;
    interface_4_out_0x5605beb888c0;
    interface_4_out_0x5605beb89550;
    interface_4_out_0x5605beb97ae8;
    interface_5_out_0x5605beb88838;
    interface_5_out_0x5605beb88928;
    interface_5_out_0x5605beb889c8;
    interface_5_out_0x5605beb888d8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x5605b0775920 [label="N", shape=none];
    interface_6_in_0x5605b0775948 [label="C_out", shape=none];
    interface_6_in_0x5605b0775970 [label="H", shape=none];
    interface_6_in_0x5605b0775998 [label="H", shape=none];
}
interface_0_out_0x5605b0775920 -> interface_6_in_0x5605b0775920;
interface_0_out_0x5605b0775948 -> interface_6_in_0x5605b0775948;
interface_0_out_0x5605b0775970 -> interface_6_in_0x5605b0775970;
interface_0_out_0x5605b0775998 -> interface_6_in_0x5605b0775998;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 3, 2, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 56, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 56, 64, 56, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 64, 112, 56, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 64, 56, 2, 56, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 2, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 28, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 28, 64, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 128, 56, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 128, 28, 2, 28, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 2, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 28, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 28, 128, 28, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 128, 56, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 128, 28, 2, 28, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 2, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 14, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 14, 128, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 256, 28, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 256, 14, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 2, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 14, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 14, 256, 14, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 256, 28, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 256, 14, 2, 14, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 3, 2, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 7, 1792, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 7, 256, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 512, 14, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 512, 7, 2, 7, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 3, 2, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# Perform contraction.
		t_2 = torch.einsum("ijkl -> iljk", in_0)

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (1, 1, 7, 3584, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (1, 3, 7, 512, 7, ))

		# Perform contraction.
		t_3 = torch.einsum("mkojn, iklj -> mioln", t_2, in_1)

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.reshape(t_4, (1, 512, 14, 7, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 2)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (1, 512, 7, 2, 7, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(3, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 3)

		# No need to crop the output tensor.
		y = t_5

		return y

