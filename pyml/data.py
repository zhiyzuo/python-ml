from helpers.preprocessing import *
from helpers.exceptions import *
import numpy as np
import math

class Feature:
# {{{ Feature Class
    def __init__(self, data, header=np.array([])):
    # data should be in the form of list or numpy matrix
        try:
            if len(data) < 1:
                raise EmptyErro

            self.feature_space = np.asmatrix(data)
            self.dimension = len(data[0])
            self.size = len(data)

            if len(header) < 1:
                self.header = np.array(["x{}".format(i) for i in range(self.dimension)])
            else:
                self.header = np.asarray(header)

        except EmptyError as e:
            print e

    def get_header(self):
        return tuple(self.header[:])

    def get_dimension(self):
        return self.dimension

    def get_feature_space(self):
        return self.feature_space[:]

    def get_normalized(self, columns, method="linear"):
    # return a new Feature object that is normalized
        return Feature(normalize(self.feature_space, columns, method))

    def get_discretized(self, columns, bins=None):
    # return a new Feature object whose specified columns are discretized
        if bins == None:
            bins = [math.sqrt(self.size) for col in columns]
        return Feature(discretize(self.feature_space, columns, bins=[math.sqrt(self.size) for col in columns]))
# }}}

'''
class Target:
# {{{ Target Class
    def __init__(self, target, header=np.array([])):
    # target should be a column
        try:
            if len(data) < 1:
                raise EmptyErro

            self.target = target
            self.size = len(data)

            if len(header) < 1:
                self.header = np.array(["target"])
            else:
                self.header = np.asarray(header)

        except EmptyError as e:
            print e

    def get_header(self):
        return tuple(self.header[:])

    def get_dimension(self):
        return self.dimension

    def get(self):
        return self.target[:]

    #TODO
    def get_discretized(self, bins=math.sqrt(self.size)):
    # return a new Target object that is discretized
        return
# }}}
'''
