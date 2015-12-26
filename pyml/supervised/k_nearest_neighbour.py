class KNN(object):
    '''
        k Nearest Neighbour
        12/26: Majority vote ONLY at this moment
    '''

    def __init__(self, k=3, p=2):
        # p: p-norm
        self.k = k
        self.p = p

    def fit(self, data, target):
        # data is pyml Data object
        self.data = data
        self.target = target

    def predict(self, unknown_data):
        # unknown data is just the feature space
        import numpy as np
        from scipy.stats import mode
        from scipy.spatial.distance import cdist

        unknown_data = np.asarray(unknown_data)

        dist_mat = cdist(unknown_data, self.data, 'minkowski', self.p)
        sorted_mat = np.argsort(np.argsort(dist_mat))

        predictions = np.zeros(unknown_data.shape[0])
        for index in range(sorted_mat.shape[0]):
            _nn_index = [idx for idx in range(sorted_mat[index, :].shape[0]) if  sorted_mat[index, idx] < self.k]
            _class = [self.target[idx] for idx in _nn_index]
            predictions[index] = mode(_class)[0][0]
        return predictions

