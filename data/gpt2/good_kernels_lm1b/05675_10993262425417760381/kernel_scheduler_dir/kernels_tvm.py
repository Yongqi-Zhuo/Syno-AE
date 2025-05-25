import tvm
from tvm import relax, te
from tvm.relax import BlockBuilder
from typing import List
import numpy as np

def weights(H_in: int = -1, N: int = -1, seq_len: int = -1, g: int = 32, k_1: int = 2, k_2: int = 5, t: int = 3, ) -> List[relax.Constant]:
	in_1: relax.Constant = relax.const(np.random.normal(size=(k_1 ** 3 * t ** 2, H_in // k_1, H_in // k_1 ** 4 // t,)).astype("float32"))
	return [in_1]

def build(bb: BlockBuilder, in_0: relax.Expr, in_1: relax.Expr, H_in: int = -1, N: int = -1, seq_len: int = -1, g: int = 32, k_1: int = 2, k_2: int = 5, t: int = 3, ) -> relax.Var:
	assert H_in > 0 and N > 0 and seq_len > 0 and g > 0 and k_1 > 0 and k_2 > 0 and t > 0
	def build_subgraph_3(in_0: te.Tensor, in_1: te.Tensor) -> te.Tensor:
		ri_0 = te.reduce_axis((0, H_in // k_1), "ri_0")
		return te.compute(
			(N, seq_len, k_1 ** 3 * t ** 2, k_1, H_in // k_1 ** 4 // t,),
			lambda i_0, i_1, i_2, i_3, i_4:
				te.sum(
					in_0[i_0, i_1, i_3 * (H_in // k_1) + ri_0] * in_1[i_2, ri_0, i_4],
					axis=[ri_0],
				),
			name="subgraph_3",
		)
	def build_subgraph_2(in_0: te.Tensor) -> te.Tensor:
		return te.compute(
			(N, seq_len, H_in * t,),
			lambda i_0, i_1, i_2:
				in_0[i_0, i_1, te.floordiv(i_2, H_in // k_1 ** 3 // t), te.floordiv(te.floormod(i_2, H_in // k_1 ** 3 // t), H_in // k_1 ** 4 // t), te.floormod(te.floormod(i_2, H_in // k_1 ** 3 // t), H_in // k_1 ** 4 // t)],
			name="subgraph_2",
		)
	subgraph_3 = bb.emit_te(build_subgraph_3, in_0, in_1)
	subgraph_2 = bb.emit_te(build_subgraph_2, subgraph_3)
	return subgraph_2
