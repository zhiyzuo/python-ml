def load():
    import urllib2
    import numpy as np
    URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00291/airfoil_self_noise.dat'
    data = []

    for line in urllib2.urlopen(URL):
        data.append(line.strip().split())
    data = np.asarray(data)
    x = data[:, :-1].astype(float)
    y = data[:,-1].astype(float)

    return x, y

