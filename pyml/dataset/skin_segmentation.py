def load():
    import urllib2
    import numpy as np
    URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00229/Skin_NonSkin.txt'
    data = []

    for line in urllib2.urlopen(URL):
        data.append(map(float, line.strip().split()))
    data = np.asarray(data)
    x = data[:, :-1]
    y = np.asarray(data[:, -1], dtype=np.uint8)
    y = np.where(y<2, y, 0)

    return x, y

