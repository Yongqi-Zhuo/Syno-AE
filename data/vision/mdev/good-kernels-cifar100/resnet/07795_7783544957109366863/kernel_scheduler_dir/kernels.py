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
        interface_2_in_0x55e87a5aa7d0 [label="H", shape=none];
        interface_2_in_0x55e87a6382f0 [label="H", shape=none];
        interface_2_in_0x55e87a635fa0 [label="C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x55e87a635fb8 [label="C_out", shape=none];
        interface_2_in_0x55e87b370458 [label="s", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55e87a596460;
        interface_2_in_0x55e87a5aa7d0;
        interface_2_in_0x55e87a6382f0;
        interface_2_in_0x55e87a635fa0;
        interface_2_in_0x55e87a635fb8;
        interface_2_in_0x55e87b370458;
    }
    // Op's.
    op_0x55e87a635f80 [label="Share"];
    op_0x55e87b370420 [label="Share"];
    op_0x55e87b7ebcf8 [label="Expand"];
    // Dimension's.
    interface_2_in_0x55e87a596460 -> interface_2_out_0x55e87a596460 [label="N"];
    op_0x55e87a635f80 -> interface_2_out_0x55e87a596488 [label="C_out"];
    interface_2_in_0x55e87a5aa7d0 -> interface_2_out_0x55e87a5aa7d0 [label="H"];
    interface_2_in_0x55e87a635fa0 -> op_0x55e87a635f80 [label="C_out"];
    interface_2_in_0x55e87a635fb8 -> op_0x55e87a635f80 [label="C_out"];
    interface_2_in_0x55e87a6382f0 -> interface_2_out_0x55e87a6382f0 [label="H"];
    op_0x55e87b370420 -> interface_2_out_0x55e87a638308 [label="s"];
    op_0x55e87b7ebcf8 -> op_0x55e87b370420 [label="s"];
    interface_2_in_0x55e87b370458 -> op_0x55e87b370420 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7f3e54005c48 [label="Sum", shape=box];
    reduce_0x7f3e54001998 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55e87a596460 [label="N", shape=none];
        interface_3_out_0x55e87a5aa7d0 [label="H", shape=none];
        interface_3_out_0x55e87a6382f0 [label="H", shape=none];
        interface_3_out_0x55e87a635fa0 [label="C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7f3e54005c48;
        reduce_0x7f3e54001998;
        interface_3_out_0x55e87a596460;
        interface_3_out_0x55e87a5aa7d0;
        interface_3_out_0x55e87a6382f0;
        interface_3_out_0x55e87a635fa0;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55e87a596460 [label="N", shape=none];
        interface_3_in_0x55e87b370210 [label="C_in", shape=none];
        interface_3_in_0x55e87a5aa7d0 [label="H", shape=none];
        interface_3_in_0x55e87a6382f0 [label="H", shape=none];
        interface_3_in_0x55e87b36fea0 [label="k_1", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x55e87b370228 [label="C_in", shape=none];
        interface_3_in_0x55e87b36feb8 [label="k_1", shape=none];
        interface_3_in_0x55e87b3704a8 [label="C_out", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55e87a596460;
        interface_3_in_0x55e87b370210;
        interface_3_in_0x55e87a5aa7d0;
        interface_3_in_0x55e87a6382f0;
        interface_3_in_0x55e87b36fea0;
        interface_3_in_0x55e87b370228;
        interface_3_in_0x55e87b36feb8;
        interface_3_in_0x55e87b3704a8;
    }
    // Op's.
    op_0x55e87b36fe80 [label="Share"];
    op_0x55e87b3701f0 [label="Share"];
    op_0x55e87b370470 [label="Share"];
    op_0x55e87b7ebd18 [label="Expand"];
    // Dimension's.
    interface_3_in_0x55e87a596460 -> interface_3_out_0x55e87a596460 [label="N"];
    interface_3_in_0x55e87a5aa7d0 -> interface_3_out_0x55e87a5aa7d0 [label="H"];
    op_0x55e87b370470 -> interface_3_out_0x55e87a635fa0 [label="C_out"];
    interface_3_in_0x55e87a6382f0 -> interface_3_out_0x55e87a6382f0 [label="H"];
    interface_3_in_0x55e87b36fea0 -> op_0x55e87b36fe80 [label="k_1"];
    interface_3_in_0x55e87b36feb8 -> op_0x55e87b36fe80 [label="k_1"];
    interface_3_in_0x55e87b370210 -> op_0x55e87b3701f0 [label="C_in"];
    interface_3_in_0x55e87b370228 -> op_0x55e87b3701f0 [label="C_in"];
    op_0x55e87b7ebd18 -> op_0x55e87b370470 [label="C_out"];
    interface_3_in_0x55e87b3704a8 -> op_0x55e87b370470 [label="C_out"];
    op_0x55e87b36fe80 -> reduce_0x7f3e54001998 [label="k_1"];
    op_0x55e87b3701f0 -> reduce_0x7f3e54005c48 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x55e87a596460 [label="N", shape=none];
        interface_4_out_0x55e87b370210 [label="C_in", shape=none];
        interface_4_out_0x55e87a5aa7d0 [label="H", shape=none];
        interface_4_out_0x55e87a6382f0 [label="H", shape=none];
        interface_4_out_0x55e87b36fea0 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x55e87a596460;
        interface_4_out_0x55e87b370210;
        interface_4_out_0x55e87a5aa7d0;
        interface_4_out_0x55e87a6382f0;
        interface_4_out_0x55e87b36fea0;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x55e87a596460 [label="N", shape=none];
        interface_4_in_0x55e87b370210 [label="C_in", shape=none];
        interface_4_in_0x55e87a5aa7d0 [label="H", shape=none];
        interface_4_in_0x7f4330020028 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x55e87a596460;
        interface_4_in_0x55e87b370210;
        interface_4_in_0x55e87a5aa7d0;
        interface_4_in_0x7f4330020028;
    }
    // Op's.
    op_0x7f4330020000 [label="Unfold"];
    // Dimension's.
    interface_4_in_0x55e87a596460 -> interface_4_out_0x55e87a596460 [label="N"];
    interface_4_in_0x55e87a5aa7d0 -> interface_4_out_0x55e87a5aa7d0 [label="H"];
    op_0x7f4330020000 -> interface_4_out_0x55e87a6382f0 [label="H"];
    op_0x7f4330020000 -> interface_4_out_0x55e87b36fea0 [label="k_1"];
    interface_4_in_0x55e87b370210 -> interface_4_out_0x55e87b370210 [label="C_in"];
    interface_4_in_0x7f4330020028 -> op_0x7f4330020000 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x55e87a596460 [label="N", shape=none];
    interface_5_out_0x55e87b370210 [label="C_in", shape=none];
    interface_5_out_0x55e87a5aa7d0 [label="H", shape=none];
    interface_5_out_0x7f4330020028 [label="H", shape=none];
}

interface_5_out_0x55e87a596460 -> interface_4_in_0x55e87a596460;
interface_5_out_0x55e87b370210 -> interface_4_in_0x55e87b370210;
interface_5_out_0x55e87a5aa7d0 -> interface_4_in_0x55e87a5aa7d0;
interface_5_out_0x7f4330020028 -> interface_4_in_0x7f4330020028;

interface_4_out_0x55e87a596460 -> interface_3_in_0x55e87a596460;
interface_4_out_0x55e87b370210 -> interface_3_in_0x55e87b370210;
interface_4_out_0x55e87a5aa7d0 -> interface_3_in_0x55e87a5aa7d0;
interface_4_out_0x55e87a6382f0 -> interface_3_in_0x55e87a6382f0;
interface_4_out_0x55e87b36fea0 -> interface_3_in_0x55e87b36fea0;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x55e87b370228 [label="C_in", shape=none];
    interface_6_out_0x55e87b36feb8 [label="k_1", shape=none];
    interface_6_out_0x55e87b3704a8 [label="C_out", shape=none];
}

interface_6_out_0x55e87b370228 -> interface_3_in_0x55e87b370228;
interface_6_out_0x55e87b36feb8 -> interface_3_in_0x55e87b36feb8;
interface_6_out_0x55e87b3704a8 -> interface_3_in_0x55e87b3704a8;

interface_3_out_0x55e87a596460 -> interface_2_in_0x55e87a596460;
interface_3_out_0x55e87a5aa7d0 -> interface_2_in_0x55e87a5aa7d0;
interface_3_out_0x55e87a6382f0 -> interface_2_in_0x55e87a6382f0;
interface_3_out_0x55e87a635fa0 -> interface_2_in_0x55e87a635fa0;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x55e87a635fb8 [label="C_out", shape=none];
    interface_7_out_0x55e87b370458 [label="s", shape=none];
}

interface_7_out_0x55e87a635fb8 -> interface_2_in_0x55e87a635fb8;
interface_7_out_0x55e87b370458 -> interface_2_in_0x55e87b370458;

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
    interface_5_out_0x55e87a596460;
    interface_5_out_0x55e87b370210;
    interface_5_out_0x55e87a5aa7d0;
    interface_5_out_0x7f4330020028;
    interface_7_out_0x55e87a635fb8;
    interface_7_out_0x55e87b370458;
    interface_6_out_0x55e87b370228;
    interface_6_out_0x55e87b36feb8;
    interface_6_out_0x55e87b3704a8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x55e87a596460 [label="N", shape=none];
    interface_8_in_0x55e87a596488 [label="C_out", shape=none];
    interface_8_in_0x55e87a5964b0 [label="H", shape=none];
    interface_8_in_0x55e87a5964d8 [label="H", shape=none];
}
interface_0_out_0x55e87a596460 -> interface_8_in_0x55e87a596460;
interface_0_out_0x55e87a596488 -> interface_8_in_0x55e87a596488;
interface_0_out_0x55e87a5964b0 -> interface_8_in_0x55e87a5964b0;
interface_0_out_0x55e87a5964d8 -> interface_8_in_0x55e87a5964d8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([64, 2]),
			torch.randn([64, 3, 64]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (128, 3584, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 56, 3, 56, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmni, jik -> lmnk", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("klmi, ij -> klmij", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, ))
		t_6 = torch.reshape(t_6, (128, 56, 64, 112, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (128, 56, 64, 56, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 2]),
			torch.randn([64, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (128, 1792, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 64, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmni, jik -> lmnk", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("klmi, ij -> klmij", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, ))
		t_6 = torch.reshape(t_6, (128, 28, 128, 56, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (128, 28, 128, 28, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([128, 2]),
			torch.randn([128, 3, 128]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (128, 3584, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 128, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmni, jik -> lmnk", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("klmi, ij -> klmij", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, ))
		t_6 = torch.reshape(t_6, (128, 28, 128, 56, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (128, 28, 128, 28, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 2]),
			torch.randn([128, 3, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (128, 1792, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 128, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmni, jik -> lmnk", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("klmi, ij -> klmij", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, ))
		t_6 = torch.reshape(t_6, (128, 14, 256, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (128, 14, 256, 14, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_4(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([256, 2]),
			torch.randn([256, 3, 256]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (128, 3584, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 256, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmni, jik -> lmnk", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("klmi, ij -> klmij", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, ))
		t_6 = torch.reshape(t_6, (128, 14, 256, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (128, 14, 256, 14, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_5(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 2]),
			torch.randn([256, 3, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (128, 1792, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 256, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmni, jik -> lmnk", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("klmi, ij -> klmij", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, ))
		t_6 = torch.reshape(t_6, (128, 7, 512, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (128, 7, 512, 7, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_6(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([512, 2]),
			torch.randn([512, 3, 512]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [H]@Unfold9ee82d943ec7d29d -> [H]@Merge5f50103ea583163b, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (128, 3584, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 512, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("ljmni, jik -> lmnk", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("klmi, ij -> klmij", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 1, 3, 2, 4, ))
		t_6 = torch.reshape(t_6, (128, 7, 512, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (128, 7, 512, 7, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# No contraction needed.
		t_7 = t_6

		# [H]@Shift6b179c72f0c6dbad -> [H]@Iteratorb0a1def4ad5784ec
		t_7 = torch.roll(t_7, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_7 = torch.permute(t_7, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_7

		return y

