def load():
    import urllib2
    import numpy as np
    URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/tic-tac-toe/tic-tac-toe.data'
    data = []

    for line in urllib2.urlopen(URL):
        data.append(line.strip().split(','))
    data = np.asarray(data)
    x = data[:, :-1]
    temp_y = np.where(data[:, -1] == 'positive', data[:, -1], 0)
    y = np.where(temp_y=='0', temp_y, 1).astype(np.uint8)

    return x, y

