import logging
import numpy as np
from scipy.special import expit

class LogisticRegression(object):
    '''
       Simple logsitic regression using
       Gradient Descent
       Sigmoid Function
    '''

    def __init__(self):
        self.theta = None

    def output(self, x, _append=True):
        if self.theta is None:
            logging.warning('Fit model before predictions!')
            return None

        if _append:
            _output = expit(np.dot(np.hstack((np.ones((x.shape[0], 1)), x)), self.theta))
        else:
            _output = expit(np.dot(x, self.theta))
        return _output

    def _cost_func(self, x, y):
        # x here already adds bias column
        _n, _dim = x.shape
        #print y*np.log(self.output(x, False)) + (1.-y)*(1.-np.log(self.output(x, False)))
        _cost = -1./_n * \
                ( y.reshape(_n,1)*np.log(self.output(x, False)) +\
                (1.-y.reshape(_n,1))*(np.log(1.-self.output(x, False))) ).sum()

        return _cost

    def fit(self, x, y, alpha=0.01, beta=0.1, max_iter=1000, threshold=0.02):
        '''
            alpha: learning rate
            beta: regularization rate
        '''

        # of features
        _n, _dim = x.shape
        # append bias 1
        x_ = np.hstack((np.ones((_n,1)), x))
        # initialize parameter theta
        self.theta = np.random.rand(_dim+1, 1)
        iter_, epsilon = 0, 100
        while iter_ < max_iter or epsilon > threshold:
            temp = self.output(x_, False)-y.reshape(_n, 1)
            self.theta = (1 - alpha*beta)*self.theta - alpha*(np.dot(x_.T, temp))
            epsilon = self._cost_func(x_, y)
            iter_ += 1
            print iter_, epsilon

    def predict(self, x_new, threshold=0.5):
        '''
            Default classification threshold: 0.5
        '''
        prob = self.output(x_new)
        predictions = np.where(np.where(prob>threshold, prob, 0) <= 0,\
                np.where(prob>threshold, prob, 0), 1)
        print prob
        return predictions

    def get_param(self):
        return self.theta

