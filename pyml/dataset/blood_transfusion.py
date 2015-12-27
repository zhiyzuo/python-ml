def load():
    import urllib2
    import numpy as np
    URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/blood-transfusion/transfusion.data'
    data = []

    for line in urllib2.urlopen(URL):
        if "R" in line:
            continue
        data.append(map(float, line.strip().split(',')))
    data = np.asarray(data)

    return data[:, :-1], np.asarray(data[:, -1], dtype=np.uint8)

