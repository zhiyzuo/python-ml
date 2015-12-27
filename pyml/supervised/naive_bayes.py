class NaiveBayes(object):
    '''
        Naive implementation for 
        Naive Bayes XD
    '''

    def __init__(self, correction=(0,0)):
        # TODO: add correction
        self.correction = correction

    def fit(self, x, y):
        import numpy as np
        # get class dependent info

        # filter class
        _n, _dim = x.shape
        self._dim = _dim
        c0_index = np.where(y==0)[0]
        c1_index = np.where(y==1)[0]
        x0, y0 = x[c0_index], y[c0_index]
        x1, y1 = x[c1_index], y[c1_index]
        _n_0 = x0.shape[0]
        _n_1 = x1.shape[0]
        self.c0 = _n_0/float(_n)
        self.c1 = _n_1/float(_n)

        c0_info = []
        c1_info = []

        for j in range(_dim):
            x0j, x1j = x0[:,j], x1[:,j]
            _unique_j = np.unique(x[:,j])
            c0_info.append(dict.fromkeys(_unique_j))
            c1_info.append(dict.fromkeys(_unique_j))
            for _item in _unique_j:
                c0_info[-1][_item] = (x0j == _item).sum()/float(_n_0)
                c1_info[-1][_item] = (x1j == _item).sum()/float(_n_1)

        self.c0_info = np.array(c0_info)
        self.c1_info = np.array(c1_info)

    def predict(self, x_new):
        import numpy as np
        predictions = np.zeros(x_new.shape[0])
        for i in range(x_new.shape[0]):
            x_ = x_new[i]
            # use log
            pc1 = np.log(self.c1) + sum([np.log(self.c1_info[j][x_[j]]) for j in range(self._dim)])
            pc0 = np.log(self.c0) + sum([np.log(self.c0_info[j][x_[j]]) for j in range(self._dim)])
            if pc1 > pc0:
                predictions[i] = 1
        return predictions


