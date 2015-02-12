import matplotlib.pyplot as plt
import numpy as np
import random

def Dirichlet(n=1000, alphas=[1,1,1]):

    ''' Generate a Dirichlet Distribution;
        Default: #points is 1000;
                 plot 3-dim space;
                 2-dim simplex with uniform distribution;
    '''

    dim = len(alphas)
    samples = np.array([([None] * dim) for row in xrange(n)])

    for i in range(n):
        for j in range(dim): 
            alpha = alphas[j]
            samples[i, j] = random.gammavariate(alpha, 1)
        samples[i, :] = samples[i, :]/sum(samples[i, :])


    if dim==3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(samples[:, 0], samples[:, 1] , samples[:, 2])
        plt.show()

    return samples
