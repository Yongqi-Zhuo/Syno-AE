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
        interface_0_out_0x55ceeb214920 [label="N", shape=none];
        interface_0_out_0x55ceeb214948 [label="C_out", shape=none];
        interface_0_out_0x55ceeb214970 [label="H", shape=none];
        interface_0_out_0x55ceeb214998 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_out_0x55ceeb214920;
        interface_0_out_0x55ceeb214948;
        interface_0_out_0x55ceeb214970;
        interface_0_out_0x55ceeb214998;
    }
    // Input 0.
    subgraph cluster_subgraph_0_in_0 {
        label = "";
        interface_0_in_0x55ceeb214920 [label="N", shape=none];
        interface_0_in_0x55ceeec84fe0 [label="g", shape=none];
        interface_0_in_0x55ceeec84ff8 [label="g^-1*C_out", shape=none];
        interface_0_in_0x55ceeb214970 [label="H", shape=none];
        interface_0_in_0x55ceeb214998 [label="H", shape=none];
    }
    {
        rank = same;
        interface_0_in_0x55ceeb214920;
        interface_0_in_0x55ceeec84fe0;
        interface_0_in_0x55ceeec84ff8;
        interface_0_in_0x55ceeb214970;
        interface_0_in_0x55ceeb214998;
    }
    // Op's.
    op_0x55ceeec84fa0 [label="Merge"];
    // Dimension's.
    interface_0_in_0x55ceeb214920 -> interface_0_out_0x55ceeb214920 [label="N"];
    op_0x55ceeec84fa0 -> interface_0_out_0x55ceeb214948 [label="C_out"];
    interface_0_in_0x55ceeb214970 -> interface_0_out_0x55ceeb214970 [label="H"];
    interface_0_in_0x55ceeb214998 -> interface_0_out_0x55ceeb214998 [label="H"];
    interface_0_in_0x55ceeec84fe0 -> op_0x55ceeec84fa0 [label="g"];
    interface_0_in_0x55ceeec84ff8 -> op_0x55ceeec84fa0 [label="g^-1*C_out"];
}

// Stage tensor.
subgraph cluster_subgraph_1 {
    label = "Subgraph 1";
    // Reductions.
    reduce_0x7f854c005820 [label="Sum", shape=box];
    reduce_0x7f854c001a98 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_1_out {
        label = "";
        interface_1_out_0x55ceeb214920 [label="N", shape=none];
        interface_1_out_0x55ceeec84fe0 [label="g", shape=none];
        interface_1_out_0x55ceeec84ff8 [label="g^-1*C_out", shape=none];
        interface_1_out_0x55ceeb214970 [label="H", shape=none];
        interface_1_out_0x55ceeb214998 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f854c005820;
        reduce_0x7f854c001a98;
        interface_1_out_0x55ceeb214920;
        interface_1_out_0x55ceeec84fe0;
        interface_1_out_0x55ceeec84ff8;
        interface_1_out_0x55ceeb214970;
        interface_1_out_0x55ceeb214998;
    }
    // Input 0.
    subgraph cluster_subgraph_1_in_0 {
        label = "";
        interface_1_in_0x55ceeb214920 [label="N", shape=none];
        interface_1_in_0x55ceeec84ff8 [label="g^-1*C_out", shape=none];
        interface_1_in_0x55ceeecdddf0 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x55ceeb214970 [label="H", shape=none];
        interface_1_in_0x55ceeecdde40 [label="k_1", shape=none];
        interface_1_in_0x55ceeb214998 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_1_in_1 {
        label = "";
        interface_1_in_0x55ceeec83018 [label="g", shape=none];
        interface_1_in_0x55ceeecdde08 [label="g^-1*s^-1*C_in", shape=none];
        interface_1_in_0x55ceeecdde58 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_1_in_0x55ceeb214920;
        interface_1_in_0x55ceeec84ff8;
        interface_1_in_0x55ceeecdddf0;
        interface_1_in_0x55ceeb214970;
        interface_1_in_0x55ceeecdde40;
        interface_1_in_0x55ceeb214998;
        interface_1_in_0x55ceeec83018;
        interface_1_in_0x55ceeecdde08;
        interface_1_in_0x55ceeecdde58;
    }
    // Op's.
    op_0x55ceeec82fe0 [label="Share"];
    op_0x55ceeec831f8 [label="Expand"];
    op_0x55ceeecdddd0 [label="Share"];
    op_0x55ceeecdde20 [label="Share"];
    // Dimension's.
    interface_1_in_0x55ceeb214920 -> interface_1_out_0x55ceeb214920 [label="N"];
    interface_1_in_0x55ceeb214970 -> interface_1_out_0x55ceeb214970 [label="H"];
    interface_1_in_0x55ceeb214998 -> interface_1_out_0x55ceeb214998 [label="H"];
    op_0x55ceeec831f8 -> op_0x55ceeec82fe0 [label="g"];
    interface_1_in_0x55ceeec83018 -> op_0x55ceeec82fe0 [label="g"];
    op_0x55ceeec82fe0 -> interface_1_out_0x55ceeec84fe0 [label="g"];
    interface_1_in_0x55ceeec84ff8 -> interface_1_out_0x55ceeec84ff8 [label="g^-1*C_out"];
    interface_1_in_0x55ceeecdddf0 -> op_0x55ceeecdddd0 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x55ceeecdde08 -> op_0x55ceeecdddd0 [label="g^-1*s^-1*C_in"];
    interface_1_in_0x55ceeecdde40 -> op_0x55ceeecdde20 [label="k_1"];
    interface_1_in_0x55ceeecdde58 -> op_0x55ceeecdde20 [label="k_1"];
    op_0x55ceeecdde20 -> reduce_0x7f854c001a98 [label="k_1"];
    op_0x55ceeecdddd0 -> reduce_0x7f854c005820 [label="g^-1*s^-1*C_in"];
}

// Stage tensor.
subgraph cluster_subgraph_2 {
    label = "Subgraph 2";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_2_out {
        label = "";
        interface_2_out_0x55ceeb214920 [label="N", shape=none];
        interface_2_out_0x55ceeec84ff8 [label="g^-1*C_out", shape=none];
        interface_2_out_0x55ceeecdddf0 [label="g^-1*s^-1*C_in", shape=none];
        interface_2_out_0x55ceeb214970 [label="H", shape=none];
        interface_2_out_0x55ceeecdde40 [label="k_1", shape=none];
        interface_2_out_0x55ceeb214998 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_out_0x55ceeb214920;
        interface_2_out_0x55ceeec84ff8;
        interface_2_out_0x55ceeecdddf0;
        interface_2_out_0x55ceeb214970;
        interface_2_out_0x55ceeecdde40;
        interface_2_out_0x55ceeb214998;
    }
    // Input 0.
    subgraph cluster_subgraph_2_in_0 {
        label = "";
        interface_2_in_0x55ceeb214920 [label="N", shape=none];
        interface_2_in_0x55ceeec84ff8 [label="g^-1*C_out", shape=none];
        interface_2_in_0x55ceeecdddf0 [label="g^-1*s^-1*C_in", shape=none];
        interface_2_in_0x55ceeb214970 [label="H", shape=none];
        interface_2_in_0x55ceeec91968 [label="H", shape=none];
    }
    {
        rank = same;
        interface_2_in_0x55ceeb214920;
        interface_2_in_0x55ceeec84ff8;
        interface_2_in_0x55ceeecdddf0;
        interface_2_in_0x55ceeb214970;
        interface_2_in_0x55ceeec91968;
    }
    // Op's.
    op_0x55ceeec91940 [label="Unfold"];
    // Dimension's.
    interface_2_in_0x55ceeb214920 -> interface_2_out_0x55ceeb214920 [label="N"];
    interface_2_in_0x55ceeb214970 -> interface_2_out_0x55ceeb214970 [label="H"];
    op_0x55ceeec91940 -> interface_2_out_0x55ceeb214998 [label="H"];
    interface_2_in_0x55ceeec84ff8 -> interface_2_out_0x55ceeec84ff8 [label="g^-1*C_out"];
    interface_2_in_0x55ceeec91968 -> op_0x55ceeec91940 [label="H"];
    interface_2_in_0x55ceeecdddf0 -> interface_2_out_0x55ceeecdddf0 [label="g^-1*s^-1*C_in"];
    op_0x55ceeec91940 -> interface_2_out_0x55ceeecdde40 [label="k_1"];
}

// Stage tensor.
subgraph cluster_subgraph_3 {
    label = "Subgraph 3";
    // Reductions.
    reduce_0x7f854c002f10 [label="Sum", shape=box];
    reduce_0x7f854c001ab0 [label="Sum", shape=box];
    // Output.
    subgraph cluster_subgraph_3_out {
        label = "";
        interface_3_out_0x55ceeb214920 [label="N", shape=none];
        interface_3_out_0x55ceeec84ff8 [label="g^-1*C_out", shape=none];
        interface_3_out_0x55ceeecdddf0 [label="g^-1*s^-1*C_in", shape=none];
        interface_3_out_0x55ceeb214970 [label="H", shape=none];
        interface_3_out_0x55ceeec91968 [label="H", shape=none];
    }
    {
        rank = same;
        reduce_0x7f854c002f10;
        reduce_0x7f854c001ab0;
        interface_3_out_0x55ceeb214920;
        interface_3_out_0x55ceeec84ff8;
        interface_3_out_0x55ceeecdddf0;
        interface_3_out_0x55ceeb214970;
        interface_3_out_0x55ceeec91968;
    }
    // Input 0.
    subgraph cluster_subgraph_3_in_0 {
        label = "";
        interface_3_in_0x55ceeb214920 [label="N", shape=none];
        interface_3_in_0x55ceeec82d80 [label="g*s", shape=none];
        interface_3_in_0x55ceeecdddf0 [label="g^-1*s^-1*C_in", shape=none];
        interface_3_in_0x55ceeec82dd0 [label="k_1", shape=none];
        interface_3_in_0x55ceeb214970 [label="H", shape=none];
        interface_3_in_0x55ceeec91968 [label="H", shape=none];
    }
    // Input 1.
    subgraph cluster_subgraph_3_in_1 {
        label = "";
        interface_3_in_0x55ceeec82e88 [label="g^-1*C_out", shape=none];
        interface_3_in_0x55ceeec82d98 [label="g*s", shape=none];
        interface_3_in_0x55ceeec82de8 [label="k_1", shape=none];
    }
    {
        rank = same;
        interface_3_in_0x55ceeb214920;
        interface_3_in_0x55ceeec82d80;
        interface_3_in_0x55ceeecdddf0;
        interface_3_in_0x55ceeec82dd0;
        interface_3_in_0x55ceeb214970;
        interface_3_in_0x55ceeec91968;
        interface_3_in_0x55ceeec82e88;
        interface_3_in_0x55ceeec82d98;
        interface_3_in_0x55ceeec82de8;
    }
    // Op's.
    op_0x55ceeec82d60 [label="Share"];
    op_0x55ceeec82db0 [label="Share"];
    op_0x55ceeec82e50 [label="Share"];
    op_0x55ceeec831b8 [label="Expand"];
    // Dimension's.
    interface_3_in_0x55ceeb214920 -> interface_3_out_0x55ceeb214920 [label="N"];
    interface_3_in_0x55ceeb214970 -> interface_3_out_0x55ceeb214970 [label="H"];
    interface_3_in_0x55ceeec82d80 -> op_0x55ceeec82d60 [label="g*s"];
    interface_3_in_0x55ceeec82d98 -> op_0x55ceeec82d60 [label="g*s"];
    interface_3_in_0x55ceeec82dd0 -> op_0x55ceeec82db0 [label="k_1"];
    interface_3_in_0x55ceeec82de8 -> op_0x55ceeec82db0 [label="k_1"];
    op_0x55ceeec831b8 -> op_0x55ceeec82e50 [label="g^-1*C_out"];
    interface_3_in_0x55ceeec82e88 -> op_0x55ceeec82e50 [label="g^-1*C_out"];
    op_0x55ceeec82e50 -> interface_3_out_0x55ceeec84ff8 [label="g^-1*C_out"];
    interface_3_in_0x55ceeec91968 -> interface_3_out_0x55ceeec91968 [label="H"];
    interface_3_in_0x55ceeecdddf0 -> interface_3_out_0x55ceeecdddf0 [label="g^-1*s^-1*C_in"];
    op_0x55ceeec82db0 -> reduce_0x7f854c001ab0 [label="k_1"];
    op_0x55ceeec82d60 -> reduce_0x7f854c002f10 [label="g*s"];
}

// Stage tensor.
subgraph cluster_subgraph_4 {
    label = "Subgraph 4";
    // Reductions.
    // Output.
    subgraph cluster_subgraph_4_out {
        label = "";
        interface_4_out_0x55ceeb214920 [label="N", shape=none];
        interface_4_out_0x55ceeec82d80 [label="g*s", shape=none];
        interface_4_out_0x55ceeecdddf0 [label="g^-1*s^-1*C_in", shape=none];
        interface_4_out_0x55ceeec82dd0 [label="k_1", shape=none];
        interface_4_out_0x55ceeb214970 [label="H", shape=none];
        interface_4_out_0x55ceeec91968 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_out_0x55ceeb214920;
        interface_4_out_0x55ceeec82d80;
        interface_4_out_0x55ceeecdddf0;
        interface_4_out_0x55ceeec82dd0;
        interface_4_out_0x55ceeb214970;
        interface_4_out_0x55ceeec91968;
    }
    // Input 0.
    subgraph cluster_subgraph_4_in_0 {
        label = "";
        interface_4_in_0x55ceeb214920 [label="N", shape=none];
        interface_4_in_0x55ceeecc2400 [label="C_in", shape=none];
        interface_4_in_0x55ceeec83aa0 [label="H", shape=none];
        interface_4_in_0x55ceeec91968 [label="H", shape=none];
    }
    {
        rank = same;
        interface_4_in_0x55ceeb214920;
        interface_4_in_0x55ceeecc2400;
        interface_4_in_0x55ceeec83aa0;
        interface_4_in_0x55ceeec91968;
    }
    // Op's.
    op_0x55ceeec83a80 [label="Shift"];
    op_0x55ceeec917c0 [label="Unfold"];
    op_0x55ceeecc23c0 [label="Split"];
    // Dimension's.
    interface_4_in_0x55ceeb214920 -> interface_4_out_0x55ceeb214920 [label="N"];
    op_0x55ceeec917c0 -> interface_4_out_0x55ceeb214970 [label="H"];
    op_0x55ceeecc23c0 -> interface_4_out_0x55ceeec82d80 [label="g*s"];
    op_0x55ceeec917c0 -> interface_4_out_0x55ceeec82dd0 [label="k_1"];
    interface_4_in_0x55ceeec83aa0 -> op_0x55ceeec83a80 [label="H"];
    op_0x55ceeec83a80 -> op_0x55ceeec917c0 [label="H"];
    interface_4_in_0x55ceeec91968 -> interface_4_out_0x55ceeec91968 [label="H"];
    interface_4_in_0x55ceeecc2400 -> op_0x55ceeecc23c0 [label="C_in"];
    op_0x55ceeecc23c0 -> interface_4_out_0x55ceeecdddf0 [label="g^-1*s^-1*C_in"];
}

// Input tensor.
subgraph cluster_subgraph_5 {
    label = "Input 0";
    interface_5_out_0x55ceeb214920 [label="N", shape=none];
    interface_5_out_0x55ceeecc2400 [label="C_in", shape=none];
    interface_5_out_0x55ceeec83aa0 [label="H", shape=none];
    interface_5_out_0x55ceeec91968 [label="H", shape=none];
}

interface_5_out_0x55ceeb214920 -> interface_4_in_0x55ceeb214920;
interface_5_out_0x55ceeecc2400 -> interface_4_in_0x55ceeecc2400;
interface_5_out_0x55ceeec83aa0 -> interface_4_in_0x55ceeec83aa0;
interface_5_out_0x55ceeec91968 -> interface_4_in_0x55ceeec91968;

interface_4_out_0x55ceeb214920 -> interface_3_in_0x55ceeb214920;
interface_4_out_0x55ceeec82d80 -> interface_3_in_0x55ceeec82d80;
interface_4_out_0x55ceeecdddf0 -> interface_3_in_0x55ceeecdddf0;
interface_4_out_0x55ceeec82dd0 -> interface_3_in_0x55ceeec82dd0;
interface_4_out_0x55ceeb214970 -> interface_3_in_0x55ceeb214970;
interface_4_out_0x55ceeec91968 -> interface_3_in_0x55ceeec91968;

// Input tensor.
subgraph cluster_subgraph_6 {
    label = "Input 1";
    interface_6_out_0x55ceeec82e88 [label="g^-1*C_out", shape=none];
    interface_6_out_0x55ceeec82d98 [label="g*s", shape=none];
    interface_6_out_0x55ceeec82de8 [label="k_1", shape=none];
}

interface_6_out_0x55ceeec82e88 -> interface_3_in_0x55ceeec82e88;
interface_6_out_0x55ceeec82d98 -> interface_3_in_0x55ceeec82d98;
interface_6_out_0x55ceeec82de8 -> interface_3_in_0x55ceeec82de8;

interface_3_out_0x55ceeb214920 -> interface_2_in_0x55ceeb214920;
interface_3_out_0x55ceeec84ff8 -> interface_2_in_0x55ceeec84ff8;
interface_3_out_0x55ceeecdddf0 -> interface_2_in_0x55ceeecdddf0;
interface_3_out_0x55ceeb214970 -> interface_2_in_0x55ceeb214970;
interface_3_out_0x55ceeec91968 -> interface_2_in_0x55ceeec91968;

interface_2_out_0x55ceeb214920 -> interface_1_in_0x55ceeb214920;
interface_2_out_0x55ceeec84ff8 -> interface_1_in_0x55ceeec84ff8;
interface_2_out_0x55ceeecdddf0 -> interface_1_in_0x55ceeecdddf0;
interface_2_out_0x55ceeb214970 -> interface_1_in_0x55ceeb214970;
interface_2_out_0x55ceeecdde40 -> interface_1_in_0x55ceeecdde40;
interface_2_out_0x55ceeb214998 -> interface_1_in_0x55ceeb214998;

// Input tensor.
subgraph cluster_subgraph_7 {
    label = "Input 2";
    interface_7_out_0x55ceeec83018 [label="g", shape=none];
    interface_7_out_0x55ceeecdde08 [label="g^-1*s^-1*C_in", shape=none];
    interface_7_out_0x55ceeecdde58 [label="k_1", shape=none];
}

interface_7_out_0x55ceeec83018 -> interface_1_in_0x55ceeec83018;
interface_7_out_0x55ceeecdde08 -> interface_1_in_0x55ceeecdde08;
interface_7_out_0x55ceeecdde58 -> interface_1_in_0x55ceeecdde58;

interface_1_out_0x55ceeb214920 -> interface_0_in_0x55ceeb214920;
interface_1_out_0x55ceeec84fe0 -> interface_0_in_0x55ceeec84fe0;
interface_1_out_0x55ceeec84ff8 -> interface_0_in_0x55ceeec84ff8;
interface_1_out_0x55ceeb214970 -> interface_0_in_0x55ceeb214970;
interface_1_out_0x55ceeb214998 -> interface_0_in_0x55ceeb214998;

{
    rank = same;
    interface_5_out_0x55ceeb214920;
    interface_5_out_0x55ceeecc2400;
    interface_5_out_0x55ceeec83aa0;
    interface_5_out_0x55ceeec91968;
    interface_6_out_0x55ceeec82e88;
    interface_6_out_0x55ceeec82d98;
    interface_6_out_0x55ceeec82de8;
    interface_7_out_0x55ceeec83018;
    interface_7_out_0x55ceeecdde08;
    interface_7_out_0x55ceeecdde58;
}
subgraph cluster_subgraph_output {
    label = "Output";
    interface_8_in_0x55ceeb214920 [label="N", shape=none];
    interface_8_in_0x55ceeb214948 [label="C_out", shape=none];
    interface_8_in_0x55ceeb214970 [label="H", shape=none];
    interface_8_in_0x55ceeb214998 [label="H", shape=none];
}
interface_0_out_0x55ceeb214920 -> interface_8_in_0x55ceeb214920;
interface_0_out_0x55ceeb214948 -> interface_8_in_0x55ceeb214948;
interface_0_out_0x55ceeb214970 -> interface_8_in_0x55ceeb214970;
interface_0_out_0x55ceeb214998 -> interface_8_in_0x55ceeb214998;

}

"""
class kernel_generated_0(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([4, 64, 3]),
			torch.randn([32, 2, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Splitfaea1e47551cefb0 -> [g*s]@Share8fb28f0c9326f917, [g^-1*s^-1*C_in]@Share5d155fcebfb4fc10
		t_3 = torch.reshape(t_3, (1, 64, 2, 56, 56, ))

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_3 = torch.roll(t_3, self.shift_direction, 3)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (1, 128, 56, 56, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 2, 3, 56, 56, ))

		# Perform contraction.
		t_4 = torch.einsum("liojmn, kij -> lkomn", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_5 = torch.reshape(t_5, (1, 448, 56, 1, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (1, 4, 2, 56, 3, 56, ))

		# Perform contraction.
		t_6 = torch.einsum("lojmkn, ijk -> liomn", t_5, in_2)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 128, 56, 56, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_1(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([8, 64, 3]),
			torch.randn([32, 4, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Splitfaea1e47551cefb0 -> [g*s]@Share8fb28f0c9326f917, [g^-1*s^-1*C_in]@Share5d155fcebfb4fc10
		t_3 = torch.reshape(t_3, (1, 64, 4, 28, 28, ))

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_3 = torch.roll(t_3, self.shift_direction, 3)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (1, 256, 28, 28, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 4, 3, 28, 28, ))

		# Perform contraction.
		t_4 = torch.einsum("liojmn, kij -> lkomn", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_5 = torch.reshape(t_5, (1, 896, 28, 1, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (1, 8, 4, 28, 3, 28, ))

		# Perform contraction.
		t_6 = torch.einsum("lojmkn, ijk -> liomn", t_5, in_2)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 256, 28, 28, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_2(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([16, 64, 3]),
			torch.randn([32, 8, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Splitfaea1e47551cefb0 -> [g*s]@Share8fb28f0c9326f917, [g^-1*s^-1*C_in]@Share5d155fcebfb4fc10
		t_3 = torch.reshape(t_3, (1, 64, 8, 14, 14, ))

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_3 = torch.roll(t_3, self.shift_direction, 3)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (1, 512, 14, 14, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 8, 3, 14, 14, ))

		# Perform contraction.
		t_4 = torch.einsum("liojmn, kij -> lkomn", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_5 = torch.reshape(t_5, (1, 1792, 14, 1, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (1, 16, 8, 14, 3, 14, ))

		# Perform contraction.
		t_6 = torch.einsum("lojmkn, ijk -> liomn", t_5, in_2)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 512, 14, 14, ))

		# No need to crop the output tensor.
		y = t_7

		return y

class kernel_generated_3(torch.nn.Module):
	def __init__(self, i):
		super().__init__()
		self.id = i
		self.shift_direction = (random.random() > 0.5) * 2 - 1
		self.weights = torch.nn.ParameterList([
			torch.randn([32, 64, 3]),
			torch.randn([32, 16, 3]),
		])

	def forward(self, x):
		# No need to pad the input tensor.
		in_0 = x

		in_1 = self.weights[0]
		in_2 = self.weights[1]

		# No contraction needed.
		t_3 = in_0

		# [C_in]@Splitfaea1e47551cefb0 -> [g*s]@Share8fb28f0c9326f917, [g^-1*s^-1*C_in]@Share5d155fcebfb4fc10
		t_3 = torch.reshape(t_3, (1, 64, 16, 7, 7, ))

		# [H]@Shift50434f3e383b3310 -> [H]@Unfold87ed2fb8f6552d8f
		t_3 = torch.roll(t_3, self.shift_direction, 3)

		# [H]@Unfold87ed2fb8f6552d8f -> [H]@Iterator96123ba3184da39c, [k_1]@Share02da0a485106ab3d
		t_3 = torch.reshape(t_3, (1, 1024, 7, 7, ))
		t_3 = torch.nn.functional.unfold(t_3, (3, 1, ), padding=(1, 0, ))
		t_3 = torch.reshape(t_3, (1, 64, 16, 3, 7, 7, ))

		# Perform contraction.
		t_4 = torch.einsum("liojmn, kij -> lkomn", t_3, in_1)

		# No contraction needed.
		t_5 = t_4

		# [H]@Unfold0063bc82bd8ddf70 -> [H]@Iteratorb0a1def4ad5784ec, [k_1]@Shared4e0659d169008e4
		t_5 = torch.reshape(t_5, (1, 3584, 7, 1, ))
		t_5 = torch.nn.functional.unfold(t_5, (3, 1, ), padding=(1, 0, ))
		t_5 = torch.reshape(t_5, (1, 32, 16, 7, 3, 7, ))

		# Perform contraction.
		t_6 = torch.einsum("lojmkn, ijk -> liomn", t_5, in_2)

		# No contraction needed.
		t_7 = t_6

		# [g]@Merge402ce7fe20a0a5fb, [g^-1*C_out]@Merge402ce7fe20a0a5f8 -> [C_out]@Iteratorc7f8eb87a5a0a9e0
		t_7 = torch.reshape(t_7, (1, 1024, 7, 7, ))

		# No need to crop the output tensor.
		y = t_7

		return y

