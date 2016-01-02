class ELM(object):
    '''
        Implementation of simple ELM
        Use Sigmoid function ONLY at this moment
    '''

    def __init__(self, n=100):
        # number of hidden neurons
        self.n = n

    def fit(self, data, target):
        import numpy as np
        from scipy.special import expit

        self.a = np.random.rand(self.n, data.shape[1])*2 - 1
        self.b = np.random.rand(self.n, 1)
        H = expit(np.dot(self.a, data.T) + self.b)
        self.beta = np.dot(np.linalg.pinv(H.T), target)

    def predict(self, unknown_data, threshold=0):
        import numpy as np
        from scipy.special import expit

        H_test = expit(np.dot(self.a, unknown_data.T) + self.b)
        output = np.dot(H_test.T, self.beta)
        predictions = np.array([1 if item > threshold else 0 for item in output])
        return predictions

