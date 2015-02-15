# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random

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
        plt.hist(samples, bins=np.sqrt(n))
        plt.title("Beta Histogram")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()

    return samples
