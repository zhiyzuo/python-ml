# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random

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
        plt.hist(samples, bins=np.sqrt(n))
        plt.title("Gamma Histogram")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()

    return samples

