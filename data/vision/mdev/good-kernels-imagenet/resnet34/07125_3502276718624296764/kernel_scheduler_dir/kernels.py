import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f722c002ce8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x55e98c3f5ac0 [label="N", shape=none];
        interface_0_out_0x55e98c3f5ae8 [label="C_out", shape=none];
        interface_0_out_0x55e98c3f5b10 [label="H", shape=none];
        interface_0_out_0x55e98c3f5b38 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f722c002ce8;
        interface_0_out_0x55e98c3f5ac0;
        interface_0_out_0x55e98c3f5ae8;
        interface_0_out_0x55e98c3f5b10;
        interface_0_out_0x55e98c3f5b38;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55e98c3f5ac0 [label="N", shape=none];
        interface_0_in_0x55e98a0f75f0 [label="H", shape=none];
        interface_0_in_0x55e98c3f5b38 [label="H", shape=none];
        interface_0_in_0x55e98c3f5ae8 [label="C_out", shape=none];
        interface_0_in_0x55e98c4701b8 [label="s", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55e98c3f5ac0;
        interface_0_in_0x55e98a0f75f0;
        interface_0_in_0x55e98c3f5b38;
        interface_0_in_0x55e98c3f5ae8;
        interface_0_in_0x55e98c4701b8;
    }
    // Op's.
    op_0x55e98a0f7570 [label="Shift"];
    op_0x55e98a0f75d0 [label="Shift"];
    op_0x55e98c470160 [label="Merge"];
    op_0x55e98c472960 [label="Split"];
    // Dimension's.
    op_0x55e98c470160 -> op_0x55e98a0f7570 [label="s*H"];
    interface_0_in_0x55e98a0f75f0 -> op_0x55e98a0f75d0 [label="H"];
    interface_0_in_0x55e98c3f5ac0 -> interface_0_out_0x55e98c3f5ac0 [label="N"];
    interface_0_in_0x55e98c3f5ae8 -> interface_0_out_0x55e98c3f5ae8 [label="C_out"];
    op_0x55e98c472960 -> interface_0_out_0x55e98c3f5b10 [label="H"];
    interface_0_in_0x55e98c3f5b38 -> interface_0_out_0x55e98c3f5b38 [label="H"];
    op_0x55e98a0f75d0 -> op_0x55e98c470160 [label="H"];
    interface_0_in_0x55e98c4701b8 -> op_0x55e98c470160 [label="s"];
    op_0x55e98a0f7570 -> op_0x55e98c472960 [label="s*H"];
    op_0x55e98c472960 -> reduce_0x7f722c002ce8 [label="s"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55e98c3f5ac0 [label="N", shape=none];
        interface_1_out_0x55e98a0f75f0 [label="H", shape=none];
        interface_1_out_0x55e98c3f5b38 [label="H", shape=none];
        interface_1_out_0x55e98c3f5ae8 [label="C_out", shape=none];
        interface_1_out_0x55e98c4701b8 [label="s", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x55e98c3f5ac0;
        interface_1_out_0x55e98a0f75f0;
        interface_1_out_0x55e98c3f5b38;
        interface_1_out_0x55e98c3f5ae8;
        interface_1_out_0x55e98c4701b8;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55e98c3f5ac0 [label="N", shape=none];
        interface_1_in_0x55e98a0f75f0 [label="H", shape=none];
        interface_1_in_0x55e98c3f5b38 [label="H", shape=none];
        interface_1_in_0x55e98c54dda0 [label="C_out", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55e98c54ddb8 [label="C_out", shape=none];
        interface_1_in_0x55e98c47ddb8 [label="s", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55e98c3f5ac0;
        interface_1_in_0x55e98a0f75f0;
        interface_1_in_0x55e98c3f5b38;
        interface_1_in_0x55e98c54dda0;
        interface_1_in_0x55e98c54ddb8;
        interface_1_in_0x55e98c47ddb8;
    }
    // Op's.
    op_0x55e98a159698 [label="Expand"];
    op_0x55e98c47dd80 [label="Share"];
    op_0x55e98c54dd80 [label="Share"];
    // Dimension's.
    interface_1_in_0x55e98a0f75f0 -> interface_1_out_0x55e98a0f75f0 [label="H"];
    interface_1_in_0x55e98c3f5ac0 -> interface_1_out_0x55e98c3f5ac0 [label="N"];
    op_0x55e98c54dd80 -> interface_1_out_0x55e98c3f5ae8 [label="C_out"];
    interface_1_in_0x55e98c3f5b38 -> interface_1_out_0x55e98c3f5b38 [label="H"];
    op_0x55e98c47dd80 -> interface_1_out_0x55e98c4701b8 [label="s"];
    op_0x55e98a159698 -> op_0x55e98c47dd80 [label="s"];
    interface_1_in_0x55e98c47ddb8 -> op_0x55e98c47dd80 [label="s"];
    interface_1_in_0x55e98c54dda0 -> op_0x55e98c54dd80 [label="C_out"];
    interface_1_in_0x55e98c54ddb8 -> op_0x55e98c54dd80 [label="C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f722c005b48 [label="Sum", shape=box];
    reduce_0x7f722c001a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55e98c3f5ac0 [label="N", shape=none];
        interface_2_out_0x55e98a0f75f0 [label="H", shape=none];
        interface_2_out_0x55e98c3f5b38 [label="H", shape=none];
        interface_2_out_0x55e98c54dda0 [label="C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7f722c005b48;
        reduce_0x7f722c001a98;
        interface_2_out_0x55e98c3f5ac0;
        interface_2_out_0x55e98a0f75f0;
        interface_2_out_0x55e98c3f5b38;
        interface_2_out_0x55e98c54dda0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55e98c3f5ac0 [label="N", shape=none];
        interface_2_in_0x55e98c47de40 [label="C_in", shape=none];
        interface_2_in_0x55e98a0f75f0 [label="H", shape=none];
        interface_2_in_0x55e98c3f5b38 [label="H", shape=none];
        interface_2_in_0x55e98c47de90 [label="k_1", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x55e98c47de58 [label="C_in", shape=none];
        interface_2_in_0x55e98c47dea8 [label="k_1", shape=none];
        interface_2_in_0x55e98c47de08 [label="C_out", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55e98c3f5ac0;
        interface_2_in_0x55e98c47de40;
        interface_2_in_0x55e98a0f75f0;
        interface_2_in_0x55e98c3f5b38;
        interface_2_in_0x55e98c47de90;
        interface_2_in_0x55e98c47de58;
        interface_2_in_0x55e98c47dea8;
        interface_2_in_0x55e98c47de08;
    }
    // Op's.
    op_0x55e98a1596b8 [label="Expand"];
    op_0x55e98c47ddd0 [label="Share"];
    op_0x55e98c47de20 [label="Share"];
    op_0x55e98c47de70 [label="Share"];
    // Dimension's.
    interface_2_in_0x55e98a0f75f0 -> interface_2_out_0x55e98a0f75f0 [label="H"];
    interface_2_in_0x55e98c3f5ac0 -> interface_2_out_0x55e98c3f5ac0 [label="N"];
    interface_2_in_0x55e98c3f5b38 -> interface_2_out_0x55e98c3f5b38 [label="H"];
    op_0x55e98a1596b8 -> op_0x55e98c47ddd0 [label="C_out"];
    interface_2_in_0x55e98c47de08 -> op_0x55e98c47ddd0 [label="C_out"];
    interface_2_in_0x55e98c47de40 -> op_0x55e98c47de20 [label="C_in"];
    interface_2_in_0x55e98c47de58 -> op_0x55e98c47de20 [label="C_in"];
    interface_2_in_0x55e98c47de90 -> op_0x55e98c47de70 [label="k_1"];
    interface_2_in_0x55e98c47dea8 -> op_0x55e98c47de70 [label="k_1"];
    op_0x55e98c47ddd0 -> interface_2_out_0x55e98c54dda0 [label="C_out"];
    op_0x55e98c47de70 -> reduce_0x7f722c001a98 [label="k_1"];
    op_0x55e98c47de20 -> reduce_0x7f722c005b48 [label="C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55e98c3f5ac0 [label="N", shape=none];
        interface_3_out_0x55e98c47de40 [label="C_in", shape=none];
        interface_3_out_0x55e98a0f75f0 [label="H", shape=none];
        interface_3_out_0x55e98c3f5b38 [label="H", shape=none];
        interface_3_out_0x55e98c47de90 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x55e98c3f5ac0;
        interface_3_out_0x55e98c47de40;
        interface_3_out_0x55e98a0f75f0;
        interface_3_out_0x55e98c3f5b38;
        interface_3_out_0x55e98c47de90;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55e98c3f5ac0 [label="N", shape=none];
        interface_3_in_0x55e98c47de40 [label="C_in", shape=none];
        interface_3_in_0x55e98a0f75f0 [label="H", shape=none];
        interface_3_in_0x55e98a0f7f68 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55e98c3f5ac0;
        interface_3_in_0x55e98c47de40;
        interface_3_in_0x55e98a0f75f0;
        interface_3_in_0x55e98a0f7f68;
    }
    // Op's.
    op_0x55e98a0f7f40 [label="Unfold"];
    // Dimension's.
    interface_3_in_0x55e98a0f75f0 -> interface_3_out_0x55e98a0f75f0 [label="H"];
    interface_3_in_0x55e98a0f7f68 -> op_0x55e98a0f7f40 [label="H"];
    interface_3_in_0x55e98c3f5ac0 -> interface_3_out_0x55e98c3f5ac0 [label="N"];
    op_0x55e98a0f7f40 -> interface_3_out_0x55e98c3f5b38 [label="H"];
    interface_3_in_0x55e98c47de40 -> interface_3_out_0x55e98c47de40 [label="C_in"];
    op_0x55e98a0f7f40 -> interface_3_out_0x55e98c47de90 [label="k_1"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x55e98c3f5ac0 [label="N", shape=none];
    interface_4_out_0x55e98c47de40 [label="C_in", shape=none];
    interface_4_out_0x55e98a0f75f0 [label="H", shape=none];
    interface_4_out_0x55e98a0f7f68 [label="H", shape=none];
}

interface_4_out_0x55e98c3f5ac0 -> interface_3_in_0x55e98c3f5ac0;
interface_4_out_0x55e98c47de40 -> interface_3_in_0x55e98c47de40;
interface_4_out_0x55e98a0f75f0 -> interface_3_in_0x55e98a0f75f0;
interface_4_out_0x55e98a0f7f68 -> interface_3_in_0x55e98a0f7f68;

interface_3_out_0x55e98c3f5ac0 -> interface_2_in_0x55e98c3f5ac0;
interface_3_out_0x55e98c47de40 -> interface_2_in_0x55e98c47de40;
interface_3_out_0x55e98a0f75f0 -> interface_2_in_0x55e98a0f75f0;
interface_3_out_0x55e98c3f5b38 -> interface_2_in_0x55e98c3f5b38;
interface_3_out_0x55e98c47de90 -> interface_2_in_0x55e98c47de90;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 2";
    interface_5_out_0x55e98c47de58 [label="C_in", shape=none];
    interface_5_out_0x55e98c47dea8 [label="k_1", shape=none];
    interface_5_out_0x55e98c47de08 [label="C_out", shape=none];
}

interface_5_out_0x55e98c47de58 -> interface_2_in_0x55e98c47de58;
interface_5_out_0x55e98c47dea8 -> interface_2_in_0x55e98c47dea8;
interface_5_out_0x55e98c47de08 -> interface_2_in_0x55e98c47de08;

interface_2_out_0x55e98c3f5ac0 -> interface_1_in_0x55e98c3f5ac0;
interface_2_out_0x55e98a0f75f0 -> interface_1_in_0x55e98a0f75f0;
interface_2_out_0x55e98c3f5b38 -> interface_1_in_0x55e98c3f5b38;
interface_2_out_0x55e98c54dda0 -> interface_1_in_0x55e98c54dda0;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 1";
    interface_6_out_0x55e98c54ddb8 [label="C_out", shape=none];
    interface_6_out_0x55e98c47ddb8 [label="s", shape=none];
}

interface_6_out_0x55e98c54ddb8 -> interface_1_in_0x55e98c54ddb8;
interface_6_out_0x55e98c47ddb8 -> interface_1_in_0x55e98c47ddb8;

interface_1_out_0x55e98c3f5ac0 -> interface_0_in_0x55e98c3f5ac0;
interface_1_out_0x55e98a0f75f0 -> interface_0_in_0x55e98a0f75f0;
interface_1_out_0x55e98c3f5b38 -> interface_0_in_0x55e98c3f5b38;
interface_1_out_0x55e98c3f5ae8 -> interface_0_in_0x55e98c3f5ae8;
interface_1_out_0x55e98c4701b8 -> interface_0_in_0x55e98c4701b8;

{
    rank = same;
    interface_4_out_0x55e98c3f5ac0;
    interface_4_out_0x55e98c47de40;
    interface_4_out_0x55e98a0f75f0;
    interface_4_out_0x55e98a0f7f68;
    interface_6_out_0x55e98c54ddb8;
    interface_6_out_0x55e98c47ddb8;
    interface_5_out_0x55e98c47de58;
    interface_5_out_0x55e98c47dea8;
    interface_5_out_0x55e98c47de08;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_7_in_0x55e98c3f5ac0 [label="N", shape=none];
    interface_7_in_0x55e98c3f5ae8 [label="C_out", shape=none];
    interface_7_in_0x55e98c3f5b10 [label="H", shape=none];
    interface_7_in_0x55e98c3f5b38 [label="H", shape=none];
}
interface_0_out_0x55e98c3f5ac0 -> interface_7_in_0x55e98c3f5ac0;
interface_0_out_0x55e98c3f5ae8 -> interface_7_in_0x55e98c3f5ae8;
interface_0_out_0x55e98c3f5b10 -> interface_7_in_0x55e98c3f5b10;
interface_0_out_0x55e98c3f5b38 -> interface_7_in_0x55e98c3f5b38;

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

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 3584, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 56, 3, 56, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlnk, jki -> mlni", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("lkmj, ji -> lkmji", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftb8e66ea4c8ed4afc -> [H]@Merge5f50103ea583163b
		t_6 = torch.roll(t_6, self.shift_direction, 1)

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 2, 3, 1, 4, ))
		t_6 = torch.reshape(t_6, (1024, 56, 64, 112, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 56, 64, 56, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_6

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

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 1792, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 64, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlnk, jki -> mlni", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("lkmj, ji -> lkmji", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftb8e66ea4c8ed4afc -> [H]@Merge5f50103ea583163b
		t_6 = torch.roll(t_6, self.shift_direction, 1)

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 2, 3, 1, 4, ))
		t_6 = torch.reshape(t_6, (1024, 28, 128, 56, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 28, 128, 28, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_6

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

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 3584, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlnk, jki -> mlni", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("lkmj, ji -> lkmji", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftb8e66ea4c8ed4afc -> [H]@Merge5f50103ea583163b
		t_6 = torch.roll(t_6, self.shift_direction, 1)

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 2, 3, 1, 4, ))
		t_6 = torch.reshape(t_6, (1024, 28, 128, 56, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 28, 128, 28, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_6

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

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 1792, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 128, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlnk, jki -> mlni", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("lkmj, ji -> lkmji", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftb8e66ea4c8ed4afc -> [H]@Merge5f50103ea583163b
		t_6 = torch.roll(t_6, self.shift_direction, 1)

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 2, 3, 1, 4, ))
		t_6 = torch.reshape(t_6, (1024, 14, 256, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 14, 256, 14, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_6

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

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 3584, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 256, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlnk, jki -> mlni", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("lkmj, ji -> lkmji", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftb8e66ea4c8ed4afc -> [H]@Merge5f50103ea583163b
		t_6 = torch.roll(t_6, self.shift_direction, 1)

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 2, 3, 1, 4, ))
		t_6 = torch.reshape(t_6, (1024, 14, 256, 28, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 14, 256, 14, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_6

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

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 1792, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 256, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlnk, jki -> mlni", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("lkmj, ji -> lkmji", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftb8e66ea4c8ed4afc -> [H]@Merge5f50103ea583163b
		t_6 = torch.roll(t_6, self.shift_direction, 1)

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 2, 3, 1, 4, ))
		t_6 = torch.reshape(t_6, (1024, 7, 512, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 7, 512, 7, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_6

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

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_3 = torch.reshape(t_3, (1024, 3584, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1024, 512, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 1, 2, 4, 3, ))

		# Perform contraction.
		t_4 = torch.einsum("mjlnk, jki -> mlni", t_3, in_2)

		# Perform contraction.
		t_5 = torch.einsum("lkmj, ji -> lkmji", t_4, in_1)

		# No contraction needed.
		t_6 = t_5

		# [H]@Shiftb8e66ea4c8ed4afc -> [H]@Merge5f50103ea583163b
		t_6 = torch.roll(t_6, self.shift_direction, 1)

		# [H]@Merge5f50103ea583163b, [s]@Merge5f50103ea5831638 -> [s*H]@Shift3c9c8e9d3c84cb9b
		t_6 = torch.permute(t_6, (0, 2, 3, 1, 4, ))
		t_6 = torch.reshape(t_6, (1024, 7, 512, 14, ))

		# [s*H]@Shift3c9c8e9d3c84cb9b -> [s*H]@Splitdb1af055f999951a
		t_6 = torch.roll(t_6, self.shift_direction, 3)

		# [s*H]@Splitdb1af055f999951a -> [H]@Iterator96123ba3184da39c, [s]@Reduced95c644a3c072d9a
		t_6 = torch.reshape(t_6, (1024, 7, 512, 7, 2, ))

		# [s]@Reduce
		t_6 = torch.sum(t_6, dim=(4, ))

		# Permute to match the output of this subgraph.
		t_6 = torch.permute(t_6, (0, 2, 3, 1, ))

		# No need to crop the output tensor.
		y = t_6

		return y

