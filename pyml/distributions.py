import random
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def GammaFunc(x):
    return math.gamma(x)

def BetaFunc(alphas=[1,1,1]):
    alpha0 = sum(alphas)
    denominator = float(GammaFunc(alpha0))
    nominator = 0
    for alpha in alphas:
        nominator *= GammaFunc(alpha)

    return nominator/denominator


def Gaussian(n=1000, mu=0, sigma=1, plot=False):
    ''' Generate a Gaussian Distribution;
        Default: #points is 1000;
                 Standard Normal Distribution;
    '''

    samples = []
    for i in range(n):
        sample = random.gauss(mu, sigma)
        samples.append(sample)

    if plot:
        plt.hist(samples, bins=math.sqrt(n))
        plt.title("Gaussian Histogram")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()

    return samples

def Beta(n=1000, alpha=1, beta=1, plot=False):
    ''' Generate a Beta Distribution;
        Default: #points is 1000;
                 Uniform Distribution;
    '''

    samples = []
    for i in range(n):
        sample = random.betavariate(alpha, beta)
        samples.append(sample)

    if plot:
        plt.hist(samples, bins=math.sqrt(n))
        plt.title("Beta Histogram")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()

    return samples

def Gamma(n=1000, alpha=1, beta=1, plot=False):
    ''' Generate a Gamma Distribution;
        Default: #points is 1000;
                 f(x) = exp(-x);
    '''

    samples = []
    for i in range(n):
        sample = random.gammavariate(alpha, beta)
        samples.append(sample)

    if plot:
        plt.hist(samples, bins=math.sqrt(n))
        plt.title("Gamma Histogram")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()

    return samples

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
