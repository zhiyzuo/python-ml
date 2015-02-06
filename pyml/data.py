from helpers.preprocessing import *
from helpers.exceptions import *
import numpy as np

class Feature:
    def __init__(self, data):
    # data should be in the form of list or numpy matrix
        try:
            if len(data) < 1:
                raise EmptyErro
            self.features = np.asmatrix(data)
            self.dimension = len(data[0])
            self.size = len(data)
        except EmptyError as e:
            print e

    def get_dimension(self):
        return self.dimension

    def get_features(self):
        return self.features

    def get_normalized(self, columns, method="linear"):
    # return a new Feature object that is normalized
        return Feature(normalize(self.features, columns, method))
