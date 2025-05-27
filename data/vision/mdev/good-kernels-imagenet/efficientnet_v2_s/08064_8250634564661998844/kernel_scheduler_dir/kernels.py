import torch
import random
"""
digraph kernel_preview {
newrank = true;

// Stage tensor.
subgraph cluster_subgraph_0 {
    label = "Subgraph 0";
    // Reductions.
    reduce_0x7f5f78003a98 [label="Sum", shape=box];
    reduce_0x7f5f78004110 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_0_out {
        label = "";
        interface_0_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_0_out_0x55f1ee7b7dc8 [label="C_out", shape=none];
        interface_0_out_0x55f1ee7b7df0 [label="H", shape=none];
        interface_0_out_0x55f1ee7b7e18 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5f78003a98;
        reduce_0x7f5f78004110;
        interface_0_out_0x55f1ee7b7da0;
        interface_0_out_0x55f1ee7b7dc8;
        interface_0_out_0x55f1ee7b7df0;
        interface_0_out_0x55f1ee7b7e18;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_0_in_0x55f1f89e2c20 [label="k_1", shape=none];
        interface_0_in_0x55f1ee7b7df0 [label="H", shape=none];
        interface_0_in_0x55f1ee7b7e18 [label="H", shape=none];
        interface_0_in_0x55f1f89e2f90 [label="k_1*k_2", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_0_in_1 {
        label = "";
        interface_0_in_0x55f1f89dd938 [label="C_out", shape=none];
        interface_0_in_0x55f1f89e2c38 [label="k_1", shape=none];
        interface_0_in_0x55f1f89e2fa8 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55f1ee7b7da0;
        interface_0_in_0x55f1f89e2c20;
        interface_0_in_0x55f1ee7b7df0;
        interface_0_in_0x55f1ee7b7e18;
        interface_0_in_0x55f1f89e2f90;
        interface_0_in_0x55f1f89dd938;
        interface_0_in_0x55f1f89e2c38;
        interface_0_in_0x55f1f89e2fa8;
    }
    // Op's.
    op_0x55f1f88b2978 [label="Expand"];
    op_0x55f1f89dd900 [label="Share"];
    op_0x55f1f89e2c00 [label="Share"];
    op_0x55f1f89e2f70 [label="Share"];
    // Dimension's.
    interface_0_in_0x55f1ee7b7da0 -> interface_0_out_0x55f1ee7b7da0 [label="N"];
    op_0x55f1f89dd900 -> interface_0_out_0x55f1ee7b7dc8 [label="C_out"];
    interface_0_in_0x55f1ee7b7df0 -> interface_0_out_0x55f1ee7b7df0 [label="H"];
    interface_0_in_0x55f1ee7b7e18 -> interface_0_out_0x55f1ee7b7e18 [label="H"];
    op_0x55f1f88b2978 -> op_0x55f1f89dd900 [label="C_out"];
    interface_0_in_0x55f1f89dd938 -> op_0x55f1f89dd900 [label="C_out"];
    interface_0_in_0x55f1f89e2c20 -> op_0x55f1f89e2c00 [label="k_1"];
    interface_0_in_0x55f1f89e2c38 -> op_0x55f1f89e2c00 [label="k_1"];
    interface_0_in_0x55f1f89e2f90 -> op_0x55f1f89e2f70 [label="k_1*k_2"];
    interface_0_in_0x55f1f89e2fa8 -> op_0x55f1f89e2f70 [label="k_1*k_2"];
    op_0x55f1f89e2c00 -> reduce_0x7f5f78003a98 [label="k_1"];
    op_0x55f1f89e2f70 -> reduce_0x7f5f78004110 [label="k_1*k_2"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_1_out_0x55f1f89e2c20 [label="k_1", shape=none];
        interface_1_out_0x55f1ee7b7df0 [label="H", shape=none];
        interface_1_out_0x55f1ee7b7e18 [label="H", shape=none];
        interface_1_out_0x55f1f89e2f90 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        interface_1_out_0x55f1ee7b7da0;
        interface_1_out_0x55f1f89e2c20;
        interface_1_out_0x55f1ee7b7df0;
        interface_1_out_0x55f1ee7b7e18;
        interface_1_out_0x55f1f89e2f90;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_1_in_0x55f1f88a62e8 [label="H", shape=none];
        interface_1_in_0x55f1ee7b7e18 [label="H", shape=none];
        interface_1_in_0x55f1f89e2f90 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55f1ee7b7da0;
        interface_1_in_0x55f1f88a62e8;
        interface_1_in_0x55f1ee7b7e18;
        interface_1_in_0x55f1f89e2f90;
    }
    // Op's.
    op_0x55f1f88a62c0 [label="Unfold"];
    // Dimension's.
    interface_1_in_0x55f1ee7b7da0 -> interface_1_out_0x55f1ee7b7da0 [label="N"];
    op_0x55f1f88a62c0 -> interface_1_out_0x55f1ee7b7df0 [label="H"];
    interface_1_in_0x55f1ee7b7e18 -> interface_1_out_0x55f1ee7b7e18 [label="H"];
    interface_1_in_0x55f1f88a62e8 -> op_0x55f1f88a62c0 [label="H"];
    op_0x55f1f88a62c0 -> interface_1_out_0x55f1f89e2c20 [label="k_1"];
    interface_1_in_0x55f1f89e2f90 -> interface_1_out_0x55f1f89e2f90 [label="k_1*k_2"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    reduce_0x7f5f78007668 [label="Sum", shape=box];
    reduce_0x7f5f78003ee8 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_2_out_0x55f1f88a62e8 [label="H", shape=none];
        interface_2_out_0x55f1ee7b7e18 [label="H", shape=none];
        interface_2_out_0x55f1f89e2f90 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5f78007668;
        reduce_0x7f5f78003ee8;
        interface_2_out_0x55f1ee7b7da0;
        interface_2_out_0x55f1f88a62e8;
        interface_2_out_0x55f1ee7b7e18;
        interface_2_out_0x55f1f89e2f90;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_2_in_0x55f1f89e2d10 [label="s^-1*C_in", shape=none];
        interface_2_in_0x55f1f88a62e8 [label="H", shape=none];
        interface_2_in_0x55f1f89e2d60 [label="k_2", shape=none];
        interface_2_in_0x55f1ee7b7e18 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_2_in_1 {
        label = "";
        interface_2_in_0x55f1f89e2d28 [label="s^-1*C_in", shape=none];
        interface_2_in_0x55f1f89e2d78 [label="k_2", shape=none];
        interface_2_in_0x55f1f89e2ff8 [label="k_1*k_2", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55f1ee7b7da0;
        interface_2_in_0x55f1f89e2d10;
        interface_2_in_0x55f1f88a62e8;
        interface_2_in_0x55f1f89e2d60;
        interface_2_in_0x55f1ee7b7e18;
        interface_2_in_0x55f1f89e2d28;
        interface_2_in_0x55f1f89e2d78;
        interface_2_in_0x55f1f89e2ff8;
    }
    // Op's.
    op_0x55f1f88b2ad8 [label="Expand"];
    op_0x55f1f89e2cf0 [label="Share"];
    op_0x55f1f89e2d40 [label="Share"];
    op_0x55f1f89e2fc0 [label="Share"];
    // Dimension's.
    interface_2_in_0x55f1ee7b7da0 -> interface_2_out_0x55f1ee7b7da0 [label="N"];
    interface_2_in_0x55f1ee7b7e18 -> interface_2_out_0x55f1ee7b7e18 [label="H"];
    interface_2_in_0x55f1f88a62e8 -> interface_2_out_0x55f1f88a62e8 [label="H"];
    interface_2_in_0x55f1f89e2d10 -> op_0x55f1f89e2cf0 [label="s^-1*C_in"];
    interface_2_in_0x55f1f89e2d28 -> op_0x55f1f89e2cf0 [label="s^-1*C_in"];
    interface_2_in_0x55f1f89e2d60 -> op_0x55f1f89e2d40 [label="k_2"];
    interface_2_in_0x55f1f89e2d78 -> op_0x55f1f89e2d40 [label="k_2"];
    op_0x55f1f89e2fc0 -> interface_2_out_0x55f1f89e2f90 [label="k_1*k_2"];
    op_0x55f1f88b2ad8 -> op_0x55f1f89e2fc0 [label="k_1*k_2"];
    interface_2_in_0x55f1f89e2ff8 -> op_0x55f1f89e2fc0 [label="k_1*k_2"];
    op_0x55f1f89e2d40 -> reduce_0x7f5f78003ee8 [label="k_2"];
    op_0x55f1f89e2cf0 -> reduce_0x7f5f78007668 [label="s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_3_out_0x55f1f89e2d10 [label="s^-1*C_in", shape=none];
        interface_3_out_0x55f1f88a62e8 [label="H", shape=none];
        interface_3_out_0x55f1f89e2d60 [label="k_2", shape=none];
        interface_3_out_0x55f1ee7b7e18 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_out_0x55f1ee7b7da0;
        interface_3_out_0x55f1f89e2d10;
        interface_3_out_0x55f1f88a62e8;
        interface_3_out_0x55f1f89e2d60;
        interface_3_out_0x55f1ee7b7e18;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_3_in_0x55f1f89e2d10 [label="s^-1*C_in", shape=none];
        interface_3_in_0x55f1f88a62e8 [label="H", shape=none];
        interface_3_in_0x55f1eba3e550 [label="H", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55f1ee7b7da0;
        interface_3_in_0x55f1f89e2d10;
        interface_3_in_0x55f1f88a62e8;
        interface_3_in_0x55f1eba3e550;
    }
    // Op's.
    op_0x55f1eba3e530 [label="Shift"];
    op_0x55f1f88a61c0 [label="Unfold"];
    // Dimension's.
    interface_3_in_0x55f1eba3e550 -> op_0x55f1eba3e530 [label="H"];
    interface_3_in_0x55f1ee7b7da0 -> interface_3_out_0x55f1ee7b7da0 [label="N"];
    op_0x55f1f88a61c0 -> interface_3_out_0x55f1ee7b7e18 [label="H"];
    op_0x55f1eba3e530 -> op_0x55f1f88a61c0 [label="H"];
    interface_3_in_0x55f1f88a62e8 -> interface_3_out_0x55f1f88a62e8 [label="H"];
    interface_3_in_0x55f1f89e2d10 -> interface_3_out_0x55f1f89e2d10 [label="s^-1*C_in"];
    op_0x55f1f88a61c0 -> interface_3_out_0x55f1f89e2d60 [label="k_2"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    reduce_0x7f5f78004e58 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x55f1ee7b7da0 [label="N", shape=none];
        interface_4_out_0x55f1f89e2d10 [label="s^-1*C_in", shape=none];
        interface_4_out_0x55f1f88a62e8 [label="H", shape=none];
        interface_4_out_0x55f1eba3e550 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f5f78004e58;
        interface_4_out_0x55f1ee7b7da0;
        interface_4_out_0x55f1f89e2d10;
        interface_4_out_0x55f1f88a62e8;
        interface_4_out_0x55f1eba3e550;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x55f1ee7b7da0 [label="N", shape=none];
        interface_4_in_0x55f1f8a07730 [label="C_in", shape=none];
        interface_4_in_0x55f1f88a62e8 [label="H", shape=none];
        interface_4_in_0x55f1eba3e550 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x55f1ee7b7da0;
        interface_4_in_0x55f1f8a07730;
        interface_4_in_0x55f1f88a62e8;
        interface_4_in_0x55f1eba3e550;
    }
    // Op's.
    op_0x55f1f8a076f0 [label="Split"];
    // Dimension's.
    interface_4_in_0x55f1eba3e550 -> interface_4_out_0x55f1eba3e550 [label="H"];
    interface_4_in_0x55f1ee7b7da0 -> interface_4_out_0x55f1ee7b7da0 [label="N"];
    interface_4_in_0x55f1f88a62e8 -> interface_4_out_0x55f1f88a62e8 [label="H"];
    op_0x55f1f8a076f0 -> interface_4_out_0x55f1f89e2d10 [label="s^-1*C_in"];
    interface_4_in_0x55f1f8a07730 -> op_0x55f1f8a076f0 [label="C_in"];
    op_0x55f1f8a076f0 -> reduce_0x7f5f78004e58 [label="s"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x55f1ee7b7da0 [label="N", shape=none];
    interface_5_out_0x55f1f8a07730 [label="C_in", shape=none];
    interface_5_out_0x55f1f88a62e8 [label="H", shape=none];
    interface_5_out_0x55f1eba3e550 [label="H", shape=none];
}

interface_5_out_0x55f1ee7b7da0 -> interface_4_in_0x55f1ee7b7da0;
interface_5_out_0x55f1f8a07730 -> interface_4_in_0x55f1f8a07730;
interface_5_out_0x55f1f88a62e8 -> interface_4_in_0x55f1f88a62e8;
interface_5_out_0x55f1eba3e550 -> interface_4_in_0x55f1eba3e550;

interface_4_out_0x55f1ee7b7da0 -> interface_3_in_0x55f1ee7b7da0;
interface_4_out_0x55f1f89e2d10 -> interface_3_in_0x55f1f89e2d10;
interface_4_out_0x55f1f88a62e8 -> interface_3_in_0x55f1f88a62e8;
interface_4_out_0x55f1eba3e550 -> interface_3_in_0x55f1eba3e550;

interface_3_out_0x55f1ee7b7da0 -> interface_2_in_0x55f1ee7b7da0;
interface_3_out_0x55f1f89e2d10 -> interface_2_in_0x55f1f89e2d10;
interface_3_out_0x55f1f88a62e8 -> interface_2_in_0x55f1f88a62e8;
interface_3_out_0x55f1f89e2d60 -> interface_2_in_0x55f1f89e2d60;
interface_3_out_0x55f1ee7b7e18 -> interface_2_in_0x55f1ee7b7e18;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 2";
    interface_6_out_0x55f1f89e2d28 [label="s^-1*C_in", shape=none];
    interface_6_out_0x55f1f89e2d78 [label="k_2", shape=none];
    interface_6_out_0x55f1f89e2ff8 [label="k_1*k_2", shape=none];
}

interface_6_out_0x55f1f89e2d28 -> interface_2_in_0x55f1f89e2d28;
interface_6_out_0x55f1f89e2d78 -> interface_2_in_0x55f1f89e2d78;
interface_6_out_0x55f1f89e2ff8 -> interface_2_in_0x55f1f89e2ff8;

interface_2_out_0x55f1ee7b7da0 -> interface_1_in_0x55f1ee7b7da0;
interface_2_out_0x55f1f88a62e8 -> interface_1_in_0x55f1f88a62e8;
interface_2_out_0x55f1ee7b7e18 -> interface_1_in_0x55f1ee7b7e18;
interface_2_out_0x55f1f89e2f90 -> interface_1_in_0x55f1f89e2f90;

interface_1_out_0x55f1ee7b7da0 -> interface_0_in_0x55f1ee7b7da0;
interface_1_out_0x55f1f89e2c20 -> interface_0_in_0x55f1f89e2c20;
interface_1_out_0x55f1ee7b7df0 -> interface_0_in_0x55f1ee7b7df0;
interface_1_out_0x55f1ee7b7e18 -> interface_0_in_0x55f1ee7b7e18;
interface_1_out_0x55f1f89e2f90 -> interface_0_in_0x55f1f89e2f90;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 1";
    interface_7_out_0x55f1f89dd938 [label="C_out", shape=none];
    interface_7_out_0x55f1f89e2c38 [label="k_1", shape=none];
    interface_7_out_0x55f1f89e2fa8 [label="k_1*k_2", shape=none];
}

interface_7_out_0x55f1f89dd938 -> interface_0_in_0x55f1f89dd938;
interface_7_out_0x55f1f89e2c38 -> interface_0_in_0x55f1f89e2c38;
interface_7_out_0x55f1f89e2fa8 -> interface_0_in_0x55f1f89e2fa8;

{
    rank = same;
    interface_5_out_0x55f1ee7b7da0;
    interface_5_out_0x55f1f8a07730;
    interface_5_out_0x55f1f88a62e8;
    interface_5_out_0x55f1eba3e550;
    interface_7_out_0x55f1f89dd938;
    interface_7_out_0x55f1f89e2c38;
    interface_7_out_0x55f1f89e2fa8;
    interface_6_out_0x55f1f89e2d28;
    interface_6_out_0x55f1f89e2d78;
    interface_6_out_0x55f1f89e2ff8;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x55f1ee7b7da0 [label="N", shape=none];
    interface_8_in_0x55f1ee7b7dc8 [label="C_out", shape=none];
    interface_8_in_0x55f1ee7b7df0 [label="H", shape=none];
    interface_8_in_0x55f1ee7b7e18 [label="H", shape=none];
}
interface_0_out_0x55f1ee7b7da0 -> interface_8_in_0x55f1ee7b7da0;
interface_0_out_0x55f1ee7b7dc8 -> interface_8_in_0x55f1ee7b7dc8;
interface_0_out_0x55f1ee7b7df0 -> interface_8_in_0x55f1ee7b7df0;
interface_0_out_0x55f1ee7b7e18 -> interface_8_in_0x55f1ee7b7e18;

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

