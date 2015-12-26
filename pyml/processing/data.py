# -*- coding: utf-8 -*-
import numpy as np

class Feature:
# {{{ Feature Class
    def __init__(self, data, header=np.array([])):
    # data should be in the form of list or numpy matrix
        try:
            if len(data) < 1:
                raise EmptyError

            self.feature_space = np.asmatrix(data)
            self.dimension = len(data[0])
            self.size = len(data)

            if len(header) < 1:
                self.header = np.array(["x{}".format(i) for i in range(self.dimension)])
            else:
                self.header = np.asarray(header)

        except EmptyError as e:
            raise

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
        return Feature(discretize(self.feature_space, columns, bins))
# }}}

class Target:
# {{{ Target Class
    def __init__(self, targets, header=np.array([])):
    # target should be a column
        try:
            if len(targets) < 1:
                raise EmptyError

            self.targets = np.asmatrix(targets)
            self.size = self.targets[0].size
            self.dimension = self.targets.shape[0]

            if len(header) < 1:
                self.header = np.array(["target" for i in range(self.dimension)])
            elif len(header) != self.dimension:
                raise DimensionError
            elif type(header) in [list, np.ndarray]:
                self.header = np.asarray(header)
            else:
                self.header = np.asarray([header])

        except EmptyError:
            raise

        except DimensionError:
            raise


    def get_header(self):
        return self.header[:]

    def get(self, columns=None):
        try:
            if columns == None:
                return self.targets[:]
            elif type(columns) == int:
                return self.targets[:, columns]
            elif type(columns) == np.ndarray or type(columns) == list:
                return np.column_stack(self.targets[:, col] for col in columns)
            else:
                raise TypeError
        except TypeError:
            print "Please either enter an integer or array for specified columns of this Target object!"

    def get_discretized(self, columns, bins=None):
    # return a new Target object whose specified columns are discretized
        if bins == None:
            bins = [math.sqrt(self.size) for i in range(self.size)]
        elif type(bins) == int:
            bins = [bins for i in range(self.size)]
        return Target(discretize(self.targets, columns, bins), self.header)
# }}}
