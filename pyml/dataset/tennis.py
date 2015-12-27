def load():
    import urllib2
    import numpy as np
    URL = 'http://www.shatterline.com/MachineLearning/data/tennis_anyone.csv'
    data = []

    for line in urllib2.urlopen(URL):
        if 'Outlook' in line:
            continue
        data.append(line.strip().split(','))
    data = np.asarray(data)
    x = data[:, :-1]
    temp_y = np.where(data[:, -1] == 'Yes', data[:, -1], 0)
    y = np.where(temp_y=='0', temp_y, 1).astype(np.uint8)

    return x, y

