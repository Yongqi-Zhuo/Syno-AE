import tvm
from tvm import relax, te
from tvm.relax import BlockBuilder
from typing import List
import numpy as np

def weights(C_in: int = -1, C_out: int = -1, H: int = -1, N: int = -1, g: int = 32, k_1: int = 3, k_2: int = 7, s: int = 2, ) -> List[relax.Constant]:
	in_1: relax.Constant = relax.const(np.random.normal(size=(C_out // s, k_1 ** 2,)).astype("float32"))
	in_2: relax.Constant = relax.const(np.random.normal(size=(C_in, k_1 ** 2,)).astype("float32"))
	return [in_1, in_2]

def build(bb: BlockBuilder, in_0: relax.Expr, in_1: relax.Expr, in_2: relax.Expr, C_in: int = -1, C_out: int = -1, H: int = -1, N: int = -1, g: int = 32, k_1: int = 3, k_2: int = 7, s: int = 2, ) -> relax.Var:
	assert C_in > 0 and C_out > 0 and H > 0 and N > 0 and g > 0 and k_1 > 0 and k_2 > 0 and s > 0
	def build_subgraph_5(in_0: te.Tensor, in_1: te.Tensor) -> te.Tensor:
		ri_0 = te.reduce_axis((0, C_in // s), "ri_0")
		return te.compute(
			(N, s, H, H, k_1 ** 2,),
			lambda i_0, i_1, i_2, i_3, i_4:
				te.sum(
					in_0[i_0, i_1 * (C_in // s) + ri_0, i_3, i_2] * in_1[i_1 * (C_in // s) + ri_0, i_4],
					axis=[ri_0],
				),
			name="subgraph_5",
		)
	def build_subgraph_4(in_0: te.Tensor, in_1: te.Tensor) -> te.Tensor:
		ri_0 = te.reduce_axis((0, k_1 ** 2), "ri_0")
		return te.compute(
			(N, s, C_out // s, H, H,),
			lambda i_0, i_1, i_2, i_3, i_4:
				te.sum(
					in_0[i_0, i_1, i_3, i_4, ri_0] * in_1[i_2, ri_0],
					axis=[ri_0],
				),
			name="subgraph_4",
		)
	def build_subgraph_3(in_0: te.Tensor) -> te.Tensor:
		return te.compute(
			(N, C_out, H, H,),
			lambda i_0, i_1, i_2, i_3:
				in_0[i_0, te.floordiv(i_1, C_out // s), te.floormod(i_1, C_out // s), i_2, i_3],
			name="subgraph_3",
		)
	subgraph_5 = bb.emit_te(build_subgraph_5, in_0, in_2)
	subgraph_4 = bb.emit_te(build_subgraph_4, subgraph_5, in_1)
	subgraph_3 = bb.emit_te(build_subgraph_3, subgraph_4)
	return subgraph_3
