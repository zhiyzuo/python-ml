# -*- coding: utf-8 -*-
import numpy as np

class Data(object):
# {{{ Feature Class
    def __init__(self, data, target):
    # data should be in the form of list or numpy matrix

        self.data = np.asmatrix(data)
        self.target = np.asarray(target)
        self.dimension = self.data.shape

    def get_data(self):
        return np.copy(self.data)

    def get_target(self):
        return np.copy(self.target)
    
    def update_data(self, new_data):
        self.data = np.asmatrix(new_data)

    def update_target(self, new_target):
        self.target = np.asarray(new_target)

    def get_dimension(self):
        return self.dimension
    
    def __repr__(self):
        return 'pyml.Data object'

    def __str__(self):
        return 'pyml.Data object: shape (%d, %d)' %(self.dimension[0], self.dimension[1])

# }}}

