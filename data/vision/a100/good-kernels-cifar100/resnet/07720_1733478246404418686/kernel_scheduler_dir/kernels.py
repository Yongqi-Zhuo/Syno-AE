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
        interface_0_out_0x55e87a596460 [label="N", shape=none];
        interface_0_out_0x55e87a596488 [label="C_out", shape=none];
        interface_0_out_0x55e87a5964b0 [label="H", shape=none];
        interface_0_out_0x55e87a5964d8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55e87a596460;
        interface_0_out_0x55e87a596488;
        interface_0_out_0x55e87a5964b0;
        interface_0_out_0x55e87a5964d8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55e87a596460 [label="N", shape=none];
        interface_0_in_0x55e87a5aa7d0 [label="H", shape=none];
        interface_0_in_0x55e87a596488 [label="C_out", shape=none];
        interface_0_in_0x55e87a5964b0 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55e87a596460;
        interface_0_in_0x55e87a5aa7d0;
        interface_0_in_0x55e87a596488;
        interface_0_in_0x55e87a5964b0;
    }
    // Op's.
    op_0x55e87a5aa7b0 [label="Shift"];
    // Dimension's.
    interface_0_in_0x55e87a596460 -> interface_0_out_0x55e87a596460 [label="N"];
    interface_0_in_0x55e87a596488 -> interface_0_out_0x55e87a596488 [label="C_out"];
    interface_0_in_0x55e87a5964b0 -> interface_0_out_0x55e87a5964b0 [label="H"];
    op_0x55e87a5aa7b0 -> interface_0_out_0x55e87a5964d8 [label="H"];
    interface_0_in_0x55e87a5aa7d0 -> op_0x55e87a5aa7b0 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f3e54002de8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55e87a596460 [label="N", shape=none];
        interface_1_out_0x55e87a5aa7d0 [label="H", shape=none];
        interface_1_out_0x55e87a596488 [label="C_out", shape=none];
        interface_1_out_0x55e87a5964b0 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f3e54002de8;
        interface_1_out_0x55e87a596460;
        interface_1_out_0x55e87a5aa7d0;
        interface_1_out_0x55e87a596488;
        interface_1_out_0x55e87a5964b0;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55e87a596460 [label="N", shape=none];
        interface_1_in_0x55e87a5aa7d0 [label="H", shape=none];
        interface_1_in_0x55e87a6382f0 [label="H", shape=none];
        interface_1_in_0x55e87a596488 [label="C_out", shape=none];
        interface_1_in_0x55e87a638308 [label="s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55e87a596460;
        interface_1_in_0x55e87a5aa7d0;
        interface_1_in_0x55e87a6382f0;
        interface_1_in_0x55e87a596488;
        interface_1_in_0x55e87a638308;
    }
    // Op's.
    op_0x55e87a6382b0 [label="Merge"];
    op_0x55e87a6617a0 [label="Split"];
    op_0x55e87b24a520 [label="Shift"];
    // Dimension's.
    interface_1_in_0x55e87a596460 -> interface_1_out_0x55e87a596460 [label="N"];
    interface_1_in_0x55e87a596488 -> interface_1_out_0x55e87a596488 [label="C_out"];
    op_0x55e87a6617a0 -> interface_1_out_0x55e87a5964b0 [label="H"];
    interface_1_in_0x55e87a5aa7d0 -> interface_1_out_0x55e87a5aa7d0 [label="H"];
    interface_1_in_0x55e87a6382f0 -> op_0x55e87a6382b0 [label="H"];
    interface_1_in_0x55e87a638308 -> op_0x55e87a6382b0 [label="s"];
    op_0x55e87b24a520 -> op_0x55e87a6617a0 [label="s*H"];
    op_0x55e87a6382b0 -> op_0x55e87b24a520 [label="s*H"];
    op_0x55e87a6617a0 -> reduce_0x7f3e54002de8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f3e54005c48 [label="Sum", shape=box];
    reduce_0x7f3e54001998 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55e87a596460 [label="N", shape=none];
        interface_2_out_0x55e87a5aa7d0 [label="H", shape=none];
        interface_2_out_0x55e87a6382f0 [label="H", shape=none];
        interface_2_out_0x55e87a596488 [label="C_out", shape=none];
        interface_2_out_0x55e87a638308 [label="s", shape=none];
    }
    {
        rank = same;
        reduce_0x7f3e54005c48;
        reduce_0x7f3e54001998;
        interface_2_out_0x55e87a596460;
        interface_2_out_0x55e87a5aa7d0;
        interface_2_out_0x55e87a6382f0;
        interface_2_out_0x55e87a596488;
        interface_2_out_0x55e87a638308;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55e87a596460 [label="N", shape=none];
        interface_2_in_0x55e87a652980 [label="C_in", shape=none];
        interface_2_in_0x55e87a5aa7d0 [label="H", shape=none];
        interface_2_in_0x55e87a6382f0 [label="H", shape=none];
        interface_2_in_0x7f44e0004480 [label="k_1", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x55e87a652998 [label="C_in", shape=none];
        interface_2_in_0x7f44e0004498 [label="k_1", shape=none];
        interface_2_in_0x55e87b370458 [label="s", shape=none];
        interface_2_in_0x55e87a635fb8 [label="C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55e87a596460;
        interface_2_in_0x55e87a652980;
        interface_2_in_0x55e87a5aa7d0;
        interface_2_in_0x55e87a6382f0;
        interface_2_in_0x7f44e0004480;
        interface_2_in_0x55e87a652998;
        interface_2_in_0x7f44e0004498;
        interface_2_in_0x55e87b370458;
        interface_2_in_0x55e87a635fb8;
    }
    // Op's.
    op_0x55e87a5a9eb8 [label="Expand"];
    op_0x55e87a635f80 [label="Share"];
    op_0x55e87a652960 [label="Share"];
    op_0x55e87b370420 [label="Share"];
    op_0x55e87b7ebcf8 [label="Expand"];
    op_0x7f44e0004460 [label="Share"];
    // Dimension's.
    interface_2_in_0x55e87a596460 -> interface_2_out_0x55e87a596460 [label="N"];
    op_0x55e87a635f80 -> interface_2_out_0x55e87a596488 [label="C_out"];
    interface_2_in_0x55e87a5aa7d0 -> interface_2_out_0x55e87a5aa7d0 [label="H"];
    op_0x55e87a5a9eb8 -> op_0x55e87a635f80 [label="C_out"];
    interface_2_in_0x55e87a635fb8 -> op_0x55e87a635f80 [label="C_out"];
    interface_2_in_0x55e87a6382f0 -> interface_2_out_0x55e87a6382f0 [label="H"];
    op_0x55e87b370420 -> interface_2_out_0x55e87a638308 [label="s"];
    interface_2_in_0x55e87a652980 -> op_0x55e87a652960 [label="C_in"];
    interface_2_in_0x55e87a652998 -> op_0x55e87a652960 [label="C_in"];
    op_0x55e87b7ebcf8 -> op_0x55e87b370420 [label="s"];
    interface_2_in_0x55e87b370458 -> op_0x55e87b370420 [label="s"];
    op_0x7f44e0004460 -> reduce_0x7f3e54001998 [label="k_1"];
    op_0x55e87a652960 -> reduce_0x7f3e54005c48 [label="C_in"];
    interface_2_in_0x7f44e0004480 -> op_0x7f44e0004460 [label="k_1"];
    interface_2_in_0x7f44e0004498 -> op_0x7f44e0004460 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55e87a596460 [label="N", shape=none];
        interface_3_out_0x55e87a652980 [label="C_in", shape=none];
        interface_3_out_0x55e87a5aa7d0 [label="H", shape=none];
        interface_3_out_0x55e87a6382f0 [label="H", shape=none];
        interface_3_out_0x7f44e0004480 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x55e87a596460;
        interface_3_out_0x55e87a652980;
        interface_3_out_0x55e87a5aa7d0;
        interface_3_out_0x55e87a6382f0;
        interface_3_out_0x7f44e0004480;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55e87a596460 [label="N", shape=none];
        interface_3_in_0x55e87a652980 [label="C_in", shape=none];
        interface_3_in_0x55e87a5aa7d0 [label="H", shape=none];
        interface_3_in_0x55e87bba7328 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55e87a596460;
        interface_3_in_0x55e87a652980;
        interface_3_in_0x55e87a5aa7d0;
        interface_3_in_0x55e87bba7328;
    }
    // Op's.
    op_0x55e87bba7300 [label="Unfold"];
    // Dimension's.
    interface_3_in_0x55e87a596460 -> interface_3_out_0x55e87a596460 [label="N"];
    interface_3_in_0x55e87a5aa7d0 -> interface_3_out_0x55e87a5aa7d0 [label="H"];
    op_0x55e87bba7300 -> interface_3_out_0x55e87a6382f0 [label="H"];
    interface_3_in_0x55e87a652980 -> interface_3_out_0x55e87a652980 [label="C_in"];
    interface_3_in_0x55e87bba7328 -> op_0x55e87bba7300 [label="H"];
    op_0x55e87bba7300 -> interface_3_out_0x7f44e0004480 [label="k_1"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x55e87a596460 [label="N", shape=none];
    interface_4_out_0x55e87a652980 [label="C_in", shape=none];
    interface_4_out_0x55e87a5aa7d0 [label="H", shape=none];
    interface_4_out_0x55e87bba7328 [label="H", shape=none];
}

interface_4_out_0x55e87a596460 -> interface_3_in_0x55e87a596460;
interface_4_out_0x55e87a652980 -> interface_3_in_0x55e87a652980;
interface_4_out_0x55e87a5aa7d0 -> interface_3_in_0x55e87a5aa7d0;
interface_4_out_0x55e87bba7328 -> interface_3_in_0x55e87bba7328;

interface_3_out_0x55e87a596460 -> interface_2_in_0x55e87a596460;
interface_3_out_0x55e87a652980 -> interface_2_in_0x55e87a652980;
interface_3_out_0x55e87a5aa7d0 -> interface_2_in_0x55e87a5aa7d0;
interface_3_out_0x55e87a6382f0 -> interface_2_in_0x55e87a6382f0;
interface_3_out_0x7f44e0004480 -> interface_2_in_0x7f44e0004480;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x55e87a652998 [label="C_in", shape=none];
    interface_5_out_0x7f44e0004498 [label="k_1", shape=none];
    interface_5_out_0x55e87b370458 [label="s", shape=none];
    interface_5_out_0x55e87a635fb8 [label="C_out", shape=none];
}

interface_5_out_0x55e87a652998 -> interface_2_in_0x55e87a652998;
interface_5_out_0x7f44e0004498 -> interface_2_in_0x7f44e0004498;
interface_5_out_0x55e87b370458 -> interface_2_in_0x55e87b370458;
interface_5_out_0x55e87a635fb8 -> interface_2_in_0x55e87a635fb8;

interface_2_out_0x55e87a596460 -> interface_1_in_0x55e87a596460;
interface_2_out_0x55e87a5aa7d0 -> interface_1_in_0x55e87a5aa7d0;
interface_2_out_0x55e87a6382f0 -> interface_1_in_0x55e87a6382f0;
interface_2_out_0x55e87a596488 -> interface_1_in_0x55e87a596488;
interface_2_out_0x55e87a638308 -> interface_1_in_0x55e87a638308;

interface_1_out_0x55e87a596460 -> interface_0_in_0x55e87a596460;
interface_1_out_0x55e87a5aa7d0 -> interface_0_in_0x55e87a5aa7d0;
interface_1_out_0x55e87a596488 -> interface_0_in_0x55e87a596488;
interface_1_out_0x55e87a5964b0 -> interface_0_in_0x55e87a5964b0;

{
    rank = same;
    interface_4_out_0x55e87a596460;
    interface_4_out_0x55e87a652980;
    interface_4_out_0x55e87a5aa7d0;
    interface_4_out_0x55e87bba7328;
    interface_5_out_0x55e87a652998;
    interface_5_out_0x7f44e0004498;
    interface_5_out_0x55e87b370458;
    interface_5_out_0x55e87a635fb8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x55e87a596460 [label="N", shape=none];
    interface_6_in_0x55e87a596488 [label="C_out", shape=none];
    interface_6_in_0x55e87a5964b0 [label="H", shape=none];
    interface_6_in_0x55e87a5964d8 [label="H", shape=none];
}
interface_0_out_0x55e87a596460 -> interface_6_in_0x55e87a596460;
interface_0_out_0x55e87a596488 -> interface_6_in_0x55e87a596488;
interface_0_out_0x55e87a5964b0 -> interface_6_in_0x55e87a5964b0;
interface_0_out_0x55e87a5964d8 -> interface_6_in_0x55e87a5964d8;

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

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 3584, 56, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 64, 56, 3, 56, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mjnol, jlki -> mnoki", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.permute(t_4, (0, 1, 3, 2, 4, ))
		t_4 = torch.reshape(t_4, (128, 56, 64, 112, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 56, 64, 56, 2, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 3, 2, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 1792, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 64, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mjnol, jlki -> mnoki", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.permute(t_4, (0, 1, 3, 2, 4, ))
		t_4 = torch.reshape(t_4, (128, 28, 128, 56, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 28, 128, 28, 2, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 2, 3, 1, ))

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

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 3584, 28, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 128, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mjnol, jlki -> mnoki", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.permute(t_4, (0, 1, 3, 2, 4, ))
		t_4 = torch.reshape(t_4, (128, 28, 128, 56, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 28, 128, 28, 2, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 3, 2, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 1792, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 128, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mjnol, jlki -> mnoki", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.permute(t_4, (0, 1, 3, 2, 4, ))
		t_4 = torch.reshape(t_4, (128, 14, 256, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 14, 256, 14, 2, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 2, 3, 1, ))

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

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 3584, 14, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 256, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mjnol, jlki -> mnoki", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.permute(t_4, (0, 1, 3, 2, 4, ))
		t_4 = torch.reshape(t_4, (128, 14, 256, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 14, 256, 14, 2, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 3, 2, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 1792, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 256, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mjnol, jlki -> mnoki", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.permute(t_4, (0, 1, 3, 2, 4, ))
		t_4 = torch.reshape(t_4, (128, 7, 512, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 7, 512, 7, 2, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 2, 3, 1, ))

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

		# No contraction needed.
		t_2 = in_0

		# [H]@Unfold9ee82d948cf711ad -> [H]@Merge5f50103ea583163b, [k_1]@Share26cfa48d169008e4
		t_2 = torch.reshape(t_2, (128, 3584, 7, 1, ))
		t_2 = torch.nn.functional.unfold(t_2, (3, 1, ), padding=(1, 0, ))
		t_2 = torch.reshape(t_2, (128, 512, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_2 = torch.permute(t_2, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_3 = torch.einsum("mjnol, jlki -> mnoki", t_2, in_1)

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# No contraction needed.
		t_4 = t_3

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_4 = torch.permute(t_4, (0, 1, 3, 2, 4, ))
		t_4 = torch.reshape(t_4, (128, 7, 512, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_4 = torch.roll(t_4, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_4 = torch.reshape(t_4, (128, 7, 512, 7, 2, ))

		# [s]@Reduce
		t_4 = torch.sum(t_4, dim=(4, ))

		# No contraction needed.
		t_5 = t_4

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_5 = torch.roll(t_5, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_5

		return y

