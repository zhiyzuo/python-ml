import numpy as np
from pyml.dataset import banknote_authentication
from pyml.metric import accuracy, confusion_matrix
from pyml.supervised.k_nearest_neighbour import KNN

x, y = banknote_authentication.load()

knn = KNN(k=1)
knn.fit(x, y)

pred = knn.predict(x[0:10])
print confusion_matrix(y[0:10], pred)

