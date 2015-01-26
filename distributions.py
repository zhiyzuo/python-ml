import random
import math
import matplotlib.pyplot as plt

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
