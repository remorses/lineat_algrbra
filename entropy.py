import numpy as np


def entropy(probabilities):
    H = sum(p * np.log2(1/p,) for p in probabilities)
    return H

def discrete_probabilities(labels):
    symbols, counts = np.unique(labels, return_counts=True)
    probabilities = counts / len(labels)
    return probabilities
 

def relative_entropy(p, q):
    return entropy(p) - sum(p * np.log2(q) for p, q in zip(p, q))

labels = [0, 0, 0, 0, 1, 1, 1, 1,]
p1 = discrete_probabilities(labels)
H = entropy(p1)
print(H)

print(relative_entropy([2, 1], [1, 1]))