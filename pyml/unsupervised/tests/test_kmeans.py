import numpy as np
from matplotlib import pyplot as plt
from pyml.unsupervised.kmeans import KMeans

data = np.array([[1,2],[2,1],[3,2],[2,3],[1,1],[2,2],[3,3],\
                 [9,9], [10,10], [8,9], [8,8], [7,7], [10,7]])

plt.plot(data[:,0], data[:,1], 'ko')

kmeans = KMeans(2)
clusters, centers = kmeans.fit(data, True)

print centers
plt.plot(centers[:, 0], centers[:, 1], 'r+', markersize=20)

plt.show()

