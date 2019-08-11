import typing
import numpy as np

a = np.array([
    [3, 1],
    [0, 2],
])

res: typing.Tuple[np.array] = np.linalg.eig(a)
e, v = res
for i, vector in enumerate(v.T):
    print(f'eigenvector {vector} with stretch {e[i]}')