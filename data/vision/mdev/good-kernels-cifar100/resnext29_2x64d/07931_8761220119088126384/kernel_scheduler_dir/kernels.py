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
        interface_0_out_0x5621811c9b40 [label="N", shape=none];
        interface_0_out_0x5621811c9b68 [label="C_out", shape=none];
        interface_0_out_0x5621811c9b90 [label="H", shape=none];
        interface_0_out_0x5621811c9bb8 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x5621811c9b40;
        interface_0_out_0x5621811c9b68;
        interface_0_out_0x5621811c9b90;
        interface_0_out_0x5621811c9bb8;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x5621811c9b40 [label="N", shape=none];
        interface_0_in_0x7fd5ec008180 [label="g", shape=none];
        interface_0_in_0x7fd5ec005160 [label="H", shape=none];
        interface_0_in_0x5621811c9bb8 [label="H", shape=none];
        interface_0_in_0x7fd5ec008198 [label="g^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x5621811c9b40;
        interface_0_in_0x7fd5ec008180;
        interface_0_in_0x7fd5ec005160;
        interface_0_in_0x5621811c9bb8;
        interface_0_in_0x7fd5ec008198;
    }
    // Op's.
    op_0x7fd5ec005140 [label="Shift"];
    op_0x7fd5ec008140 [label="Merge"];
    // Dimension's.
    interface_0_in_0x5621811c9b40 -> interface_0_out_0x5621811c9b40 [label="N"];
    op_0x7fd5ec008140 -> interface_0_out_0x5621811c9b68 [label="C_out"];
    op_0x7fd5ec005140 -> interface_0_out_0x5621811c9b90 [label="H"];
    interface_0_in_0x5621811c9bb8 -> interface_0_out_0x5621811c9bb8 [label="H"];
    interface_0_in_0x7fd5ec005160 -> op_0x7fd5ec005140 [label="H"];
    interface_0_in_0x7fd5ec008180 -> op_0x7fd5ec008140 [label="g"];
    interface_0_in_0x7fd5ec008198 -> op_0x7fd5ec008140 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7fce640019b0 [label="Sum", shape=box];
    reduce_0x7fce64005a20 [label="Sum", shape=box];
    reduce_0x7fce64001998 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x5621811c9b40 [label="N", shape=none];
        interface_1_out_0x7fd5ec008180 [label="g", shape=none];
        interface_1_out_0x7fd5ec005160 [label="H", shape=none];
        interface_1_out_0x5621811c9bb8 [label="H", shape=none];
        interface_1_out_0x7fd5ec008198 [label="g^-1*C_out", shape=none];
    }
    {
        rank = same;
        reduce_0x7fce640019b0;
        reduce_0x7fce64005a20;
        reduce_0x7fce64001998;
        interface_1_out_0x5621811c9b40;
        interface_1_out_0x7fd5ec008180;
        interface_1_out_0x7fd5ec005160;
        interface_1_out_0x5621811c9bb8;
        interface_1_out_0x7fd5ec008198;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x5621811c9b40 [label="N", shape=none];
        interface_1_in_0x7fd4bc004a60 [label="g", shape=none];
        interface_1_in_0x7fd0e400cde0 [label="k_1", shape=none];
        interface_1_in_0x7fd5e0004800 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x7fd5ec005160 [label="H", shape=none];
        interface_1_in_0x5621811c9bb8 [label="H", shape=none];
        interface_1_in_0x7fd5e00045d0 [label="k_1", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x7fd4bc004a78 [label="g", shape=none];
        interface_1_in_0x7fd0e400cdf8 [label="k_1", shape=none];
        interface_1_in_0x7fd5e0004818 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x7fd5e00045e8 [label="k_1", shape=none];
        interface_1_in_0x7fd4bc004b18 [label="g^-1*C_out", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x5621811c9b40;
        interface_1_in_0x7fd4bc004a60;
        interface_1_in_0x7fd0e400cde0;
        interface_1_in_0x7fd5e0004800;
        interface_1_in_0x7fd5ec005160;
        interface_1_in_0x5621811c9bb8;
        interface_1_in_0x7fd5e00045d0;
        interface_1_in_0x7fd4bc004a78;
        interface_1_in_0x7fd0e400cdf8;
        interface_1_in_0x7fd5e0004818;
        interface_1_in_0x7fd5e00045e8;
        interface_1_in_0x7fd4bc004b18;
    }
    // Op's.
    op_0x7fd0e400cdc0 [label="Share"];
    op_0x7fd4bc004a40 [label="Share"];
    op_0x7fd4bc004ae0 [label="Share"];
    op_0x7fd5e00045b0 [label="Share"];
    op_0x7fd5e00047e0 [label="Share"];
    op_0x7fd5e0004a78 [label="Expand"];
    // Dimension's.
    interface_1_in_0x5621811c9b40 -> interface_1_out_0x5621811c9b40 [label="N"];
    interface_1_in_0x5621811c9bb8 -> interface_1_out_0x5621811c9bb8 [label="H"];
    op_0x7fd5e00045b0 -> reduce_0x7fce64001998 [label="k_1"];
    op_0x7fd0e400cdc0 -> reduce_0x7fce640019b0 [label="k_1"];
    op_0x7fd5e00047e0 -> reduce_0x7fce64005a20 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x7fd0e400cde0 -> op_0x7fd0e400cdc0 [label="k_1"];
    interface_1_in_0x7fd0e400cdf8 -> op_0x7fd0e400cdc0 [label="k_1"];
    interface_1_in_0x7fd4bc004a60 -> op_0x7fd4bc004a40 [label="g"];
    interface_1_in_0x7fd4bc004a78 -> op_0x7fd4bc004a40 [label="g"];
    op_0x7fd5e0004a78 -> op_0x7fd4bc004ae0 [label="g^-1*C_out"];
    interface_1_in_0x7fd4bc004b18 -> op_0x7fd4bc004ae0 [label="g^-1*C_out"];
    interface_1_in_0x7fd5e00045d0 -> op_0x7fd5e00045b0 [label="k_1"];
    interface_1_in_0x7fd5e00045e8 -> op_0x7fd5e00045b0 [label="k_1"];
    interface_1_in_0x7fd5e0004800 -> op_0x7fd5e00047e0 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x7fd5e0004818 -> op_0x7fd5e00047e0 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x7fd5ec005160 -> interface_1_out_0x7fd5ec005160 [label="H"];
    op_0x7fd4bc004a40 -> interface_1_out_0x7fd5ec008180 [label="g"];
    op_0x7fd4bc004ae0 -> interface_1_out_0x7fd5ec008198 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x5621811c9b40 [label="N", shape=none];
        interface_2_out_0x7fd4bc004a60 [label="g", shape=none];
        interface_2_out_0x7fd0e400cde0 [label="k_1", shape=none];
        interface_2_out_0x7fd5e0004800 [label="g^-1*s^-1*C_in", shape=none];
        interface_2_out_0x7fd5ec005160 [label="H", shape=none];
        interface_2_out_0x5621811c9bb8 [label="H", shape=none];
        interface_2_out_0x7fd5e00045d0 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x5621811c9b40;
        interface_2_out_0x7fd4bc004a60;
        interface_2_out_0x7fd0e400cde0;
        interface_2_out_0x7fd5e0004800;
        interface_2_out_0x7fd5ec005160;
        interface_2_out_0x5621811c9bb8;
        interface_2_out_0x7fd5e00045d0;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x5621811c9b40 [label="N", shape=none];
        interface_2_in_0x7fd2416b5c60 [label="s^-1*C_in", shape=none];
        interface_2_in_0x7fd5ec005160 [label="H", shape=none];
        interface_2_in_0x7fd348031840 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x5621811c9b40;
        interface_2_in_0x7fd2416b5c60;
        interface_2_in_0x7fd5ec005160;
        interface_2_in_0x7fd348031840;
    }
    // Op's.
    op_0x7fd2416b5c20 [label="Split"];
    op_0x7fd268007540 [label="Unfold"];
    op_0x7fd348031820 [label="Shift"];
    op_0x7fd5c006bf80 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x5621811c9b40 -> interface_2_out_0x5621811c9b40 [label="N"];
    op_0x7fd268007540 -> interface_2_out_0x5621811c9bb8 [label="H"];
    op_0x7fd5c006bf80 -> interface_2_out_0x7fd0e400cde0 [label="k_1"];
    interface_2_in_0x7fd2416b5c60 -> op_0x7fd2416b5c20 [label="s^-1*C_in"];
    op_0x7fd348031820 -> op_0x7fd268007540 [label="H"];
    interface_2_in_0x7fd348031840 -> op_0x7fd348031820 [label="H"];
    op_0x7fd5c006bf80 -> interface_2_out_0x7fd4bc004a60 [label="g"];
    op_0x7fd2416b5c20 -> op_0x7fd5c006bf80 [label="g"];
    op_0x7fd268007540 -> interface_2_out_0x7fd5e00045d0 [label="k_1"];
    op_0x7fd2416b5c20 -> interface_2_out_0x7fd5e0004800 [label="g^-1*s^-1*C_in"];
    interface_2_in_0x7fd5ec005160 -> interface_2_out_0x7fd5ec005160 [label="H"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7fce64002f58 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x5621811c9b40 [label="N", shape=none];
        interface_3_out_0x7fd2416b5c60 [label="s^-1*C_in", shape=none];
        interface_3_out_0x7fd5ec005160 [label="H", shape=none];
        interface_3_out_0x7fd348031840 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7fce64002f58;
        interface_3_out_0x5621811c9b40;
        interface_3_out_0x7fd2416b5c60;
        interface_3_out_0x7fd5ec005160;
        interface_3_out_0x7fd348031840;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x5621811c9b40 [label="N", shape=none];
        interface_3_in_0x7fd4629d2710 [label="C_in", shape=none];
        interface_3_in_0x7fd5ec005160 [label="H", shape=none];
        interface_3_in_0x7fd348031840 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x5621811c9b40;
        interface_3_in_0x7fd4629d2710;
        interface_3_in_0x7fd5ec005160;
        interface_3_in_0x7fd348031840;
    }
    // Op's.
    op_0x7fd4629d26d0 [label="Split"];
    // Dimension's.
    interface_3_in_0x5621811c9b40 -> interface_3_out_0x5621811c9b40 [label="N"];
    op_0x7fd4629d26d0 -> reduce_0x7fce64002f58 [label="s"];
    op_0x7fd4629d26d0 -> interface_3_out_0x7fd2416b5c60 [label="s^-1*C_in"];
    interface_3_in_0x7fd348031840 -> interface_3_out_0x7fd348031840 [label="H"];
    interface_3_in_0x7fd4629d2710 -> op_0x7fd4629d26d0 [label="C_in"];
    interface_3_in_0x7fd5ec005160 -> interface_3_out_0x7fd5ec005160 [label="H"];
}

// Input tensor.
subgraph cluster_subgraph_4 {
    label = "Input 0";
    interface_4_out_0x5621811c9b40 [label="N", shape=none];
    interface_4_out_0x7fd4629d2710 [label="C_in", shape=none];
    interface_4_out_0x7fd5ec005160 [label="H", shape=none];
    interface_4_out_0x7fd348031840 [label="H", shape=none];
}

interface_4_out_0x5621811c9b40 -> interface_3_in_0x5621811c9b40;
interface_4_out_0x7fd4629d2710 -> interface_3_in_0x7fd4629d2710;
interface_4_out_0x7fd5ec005160 -> interface_3_in_0x7fd5ec005160;
interface_4_out_0x7fd348031840 -> interface_3_in_0x7fd348031840;

interface_3_out_0x5621811c9b40 -> interface_2_in_0x5621811c9b40;
interface_3_out_0x7fd2416b5c60 -> interface_2_in_0x7fd2416b5c60;
interface_3_out_0x7fd5ec005160 -> interface_2_in_0x7fd5ec005160;
interface_3_out_0x7fd348031840 -> interface_2_in_0x7fd348031840;

interface_2_out_0x5621811c9b40 -> interface_1_in_0x5621811c9b40;
interface_2_out_0x7fd4bc004a60 -> interface_1_in_0x7fd4bc004a60;
interface_2_out_0x7fd0e400cde0 -> interface_1_in_0x7fd0e400cde0;
interface_2_out_0x7fd5e0004800 -> interface_1_in_0x7fd5e0004800;
interface_2_out_0x7fd5ec005160 -> interface_1_in_0x7fd5ec005160;
interface_2_out_0x5621811c9bb8 -> interface_1_in_0x5621811c9bb8;
interface_2_out_0x7fd5e00045d0 -> interface_1_in_0x7fd5e00045d0;

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 1";
    interface_5_out_0x7fd4bc004a78 [label="g", shape=none];
    interface_5_out_0x7fd0e400cdf8 [label="k_1", shape=none];
    interface_5_out_0x7fd5e0004818 [label="g^-1*s^-1*C_in", shape=none];
    interface_5_out_0x7fd5e00045e8 [label="k_1", shape=none];
    interface_5_out_0x7fd4bc004b18 [label="g^-1*C_out", shape=none];
}

interface_5_out_0x7fd4bc004a78 -> interface_1_in_0x7fd4bc004a78;
interface_5_out_0x7fd0e400cdf8 -> interface_1_in_0x7fd0e400cdf8;
interface_5_out_0x7fd5e0004818 -> interface_1_in_0x7fd5e0004818;
interface_5_out_0x7fd5e00045e8 -> interface_1_in_0x7fd5e00045e8;
interface_5_out_0x7fd4bc004b18 -> interface_1_in_0x7fd4bc004b18;

interface_1_out_0x5621811c9b40 -> interface_0_in_0x5621811c9b40;
interface_1_out_0x7fd5ec008180 -> interface_0_in_0x7fd5ec008180;
interface_1_out_0x7fd5ec005160 -> interface_0_in_0x7fd5ec005160;
interface_1_out_0x5621811c9bb8 -> interface_0_in_0x5621811c9bb8;
interface_1_out_0x7fd5ec008198 -> interface_0_in_0x7fd5ec008198;

{
    rank = same;
    interface_4_out_0x5621811c9b40;
    interface_4_out_0x7fd4629d2710;
    interface_4_out_0x7fd5ec005160;
    interface_4_out_0x7fd348031840;
    interface_5_out_0x7fd4bc004a78;
    interface_5_out_0x7fd0e400cdf8;
    interface_5_out_0x7fd5e0004818;
    interface_5_out_0x7fd5e00045e8;
    interface_5_out_0x7fd4bc004b18;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_6_in_0x5621811c9b40 [label="N", shape=none];
    interface_6_in_0x5621811c9b68 [label="C_out", shape=none];
    interface_6_in_0x5621811c9b90 [label="H", shape=none];
    interface_6_in_0x5621811c9bb8 [label="H", shape=none];
}
interface_0_out_0x5621811c9b40 -> interface_6_in_0x5621811c9b40;
interface_0_out_0x5621811c9b68 -> interface_6_in_0x5621811c9b68;
interface_0_out_0x5621811c9b90 -> interface_6_in_0x5621811c9b90;
interface_0_out_0x5621811c9bb8 -> interface_6_in_0x5621811c9bb8;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 2, 3, 4]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Splita06ce4f8f1aa614a -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Split313fe4f50bf9d419
		t_2 = torch.reshape(t_2, (128, 2, 64, 56, 56, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [s^-1*C_in]@Split313fe4f50bf9d419 -> [g]@Unfold00a2b12a52289aa2, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (128, 32, 2, 56, 56, ))

		# [g]@Unfold00a2b12a52289aa2 -> [g]@Share3ccf867b1ad85e4e, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (128, 1, 32, 6272, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 3, 32, 2, 56, 56, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_3 = torch.roll(t_3, self.shift_direction, 5)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (128, 10752, 56, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 3, 32, 2, 56, 3, 56, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 2, 1, 3, 4, 6, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("njimpol, jimlk -> njpok", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_5 = torch.permute(t_5, (0, 2, 3, 1, 4, ))
		t_5 = torch.reshape(t_5, (128, 56, 56, 128, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 4, 3, 8]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Splita06ce4f8f1aa614a -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Split313fe4f50bf9d419
		t_2 = torch.reshape(t_2, (128, 2, 128, 28, 28, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [s^-1*C_in]@Split313fe4f50bf9d419 -> [g]@Unfold00a2b12a52289aa2, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (128, 32, 4, 28, 28, ))

		# [g]@Unfold00a2b12a52289aa2 -> [g]@Share3ccf867b1ad85e4e, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (128, 1, 32, 3136, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 3, 32, 4, 28, 28, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_3 = torch.roll(t_3, self.shift_direction, 5)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (128, 10752, 28, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 3, 32, 4, 28, 3, 28, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 2, 1, 3, 4, 6, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("njimpol, jimlk -> njpok", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_5 = torch.permute(t_5, (0, 2, 3, 1, 4, ))
		t_5 = torch.reshape(t_5, (128, 28, 28, 256, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 8, 3, 16]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Splita06ce4f8f1aa614a -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Split313fe4f50bf9d419
		t_2 = torch.reshape(t_2, (128, 2, 256, 14, 14, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [s^-1*C_in]@Split313fe4f50bf9d419 -> [g]@Unfold00a2b12a52289aa2, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (128, 32, 8, 14, 14, ))

		# [g]@Unfold00a2b12a52289aa2 -> [g]@Share3ccf867b1ad85e4e, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (128, 1, 32, 1568, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 3, 32, 8, 14, 14, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_3 = torch.roll(t_3, self.shift_direction, 5)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (128, 10752, 14, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 3, 32, 8, 14, 3, 14, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 2, 1, 3, 4, 6, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("njimpol, jimlk -> njpok", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_5 = torch.permute(t_5, (0, 2, 3, 1, 4, ))
		t_5 = torch.reshape(t_5, (128, 14, 14, 512, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_5

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 3, 16, 3, 32]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]

		# No contraction needed.
		t_2 = in_0

		# [C_in]@Splita06ce4f8f1aa614a -> [s]@Reduced95c644a3c072d9a, [s^-1*C_in]@Split313fe4f50bf9d419
		t_2 = torch.reshape(t_2, (128, 2, 512, 7, 7, ))

		# [s]@Reduce
		t_2 = torch.sum(t_2, dim=(1, ))

		# No contraction needed.
		t_3 = t_2

		# [s^-1*C_in]@Split313fe4f50bf9d419 -> [g]@Unfold00a2b12a52289aa2, [g^-1*s^-1*C_in]@Share77b21cfebfb4fc10
		t_3 = torch.reshape(t_3, (128, 32, 16, 7, 7, ))

		# [g]@Unfold00a2b12a52289aa2 -> [g]@Share3ccf867b1ad85e4e, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (128, 1, 32, 784, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 3, 32, 16, 7, 7, ))

		# [H]@Shiftdbd5b2e652804221 -> [H]@Unfold0063bc810b9e1e60
		t_3 = torch.roll(t_3, self.shift_direction, 5)

		# [H]@Unfold0063bc810b9e1e60 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Share26cfa48d169008e4
		t_3 = torch.reshape(t_3, (128, 10752, 7, 1, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (128, 3, 32, 16, 7, 3, 7, ))

		# Permute to match the output of this subgraph.
		t_3 = torch.permute(t_3, (0, 2, 1, 3, 4, 6, 5, ))

		# Perform contraction.
		t_4 = torch.einsum("njimpol, jimlk -> njpok", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_5 = torch.permute(t_5, (0, 2, 3, 1, 4, ))
		t_5 = torch.reshape(t_5, (128, 7, 7, 1024, ))

		# [H]@Shift41a433c05e30b91d -> [H]@Iterator96123ba3184da39c
		t_5 = torch.roll(t_5, self.shift_direction, 1)

		# Permute to match the output of this subgraph.
		t_5 = torch.permute(t_5, (0, 3, 1, 2, ))

		# No need to crop the output tensor.
		y = t_5

		return y

