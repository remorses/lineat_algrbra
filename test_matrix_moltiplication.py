import numpy as np
from funcy import rcompose, partial


a = np.array([
    [0, 2],
    [1, 0],
])

b = np.array([
    [1, -2],
    [1, 0],
])

y = np.dot(a, np.dot(b, a,))
print(y)
print(a @ b @ a)
print(rcompose(
    partial(np.dot, a, b),
    partial(np.dot, a),
)())