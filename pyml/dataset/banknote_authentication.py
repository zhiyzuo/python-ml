def load():
    import urllib2
    import numpy as np
    URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt'
    data = []

    for line in urllib2.urlopen(URL):
        data.append(map(float, line.strip().split(',')))
    data = np.asarray(data)

    return data[:, :-1], np.asarray(data[:, -1], dtype=np.uint8)

