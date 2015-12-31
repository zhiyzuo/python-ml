class KMeans(object):
    '''
        K Means Clustering 
        Random Initilization ONLY at this moment
    '''

    def __init__(self, k=3, p=2, max_iter=1000):
        self.k = k
        self.p = p
        self.max_iter = max_iter

    def _update_centers(self, data, clusters, _dim):
        import numpy as np
        centers = np.zeros((self.k, _dim))
        for k in range(self.k):
            k_indices = np.where(clusters==k)[0]
            cluster_k = data[k_indices]
            centers[k] = np.mean(cluster_k, 0)
        return centers
    
    def fit(self, data, return_center=False):
        import numpy as np
        from scipy.spatial.distance import cdist
        # random init
        _n, _dim = data.shape
        clusters = np.random.choice(range(self.k), _n, True)

        centers = self._update_centers(data, clusters, _dim)
        _new_centers = np.copy(centers)

        iter_ = 0
        while iter_ < self.max_iter:
            print iter_, [item for item in _new_centers]
            if iter_ > 0 and _new_centers is not None and np.allclose(_new_centers, centers):
                # converge
                break
            centers = np.copy(_new_centers)

            # update 
            dist_mat = cdist(data, centers, 'minkowski', self.p)
            sorted_mat = np.argsort(np.argsort(dist_mat))
            clusters = np.where(sorted_mat==0)[1]

            _new_centers = self._update_centers(data, clusters, _dim)
            iter_ += 1

        if return_center:
            return clusters, centers
        else:
            return clusters

