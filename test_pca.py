import random
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

M = np.array([
    np.random.normal(size=4),
    np.random.poisson(size=4),
    np.random.normal(size=4),
    np.random.poisson(size=4),
    np.random.logistic(size=4),
    np.random.normal(size=4),
    np.random.poisson(size=4),
    np.random.logistic(size=4),
    np.random.poisson(size=4),
    np.random.poisson(size=4),
    np.random.normal(size=4),
    np.random.logistic(size=4),
    np.random.poisson(size=4),
    np.random.poisson(size=4),
    np.random.logistic(size=4),
])

np.

print(M.shape)

def depca(sample):
    x_mean = np.mean(M, axis=0)
    x_stds = np.std(M, axis=0)
    x_cov = np.cov((M - x_mean).T)
    e, v = np.linalg.eig(x_cov)
    
    # e_list = e.tolist()
    # e_list.sort(reverse=True)
    # plt.clf()
    # plt.bar(np.arange(e.shape[0]), e_list, align='center')
    # plt.draw()
    # plt.savefig('evals.png')
    
    sample = x_mean + np.dot(v, (sample * e).T).T
    return sample

sample = M[0]
print(sample)

pca = PCA()
pca.fit(M)
pcated = pca.transform([sample])
print(pcated)

sample = depca(pcated)
print(sample)

def draw_bo():
    plt.clf()
    for i, sample in enumerate(range(M.shape[0])):
        sample = M[i, :]
        pca_sample = pca(sample)
        plt.scatter(sample[0], sample[1], color='red')
        plt.scatter(pca_sample[0], pca_sample[1], color='blue')
    plt.draw()
    plt.savefig('scatter.png')