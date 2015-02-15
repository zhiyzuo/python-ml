# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random

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
        plt.hist(samples, bins=np.sqrt(n))
        plt.title("Gaussian Histogram")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()

    return samples

