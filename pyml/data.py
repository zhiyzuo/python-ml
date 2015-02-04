from helpers import *
from helpers.exceptions import *

class Vector:
# {{{ Vector Class
    def __init__(self, vector=[]):
        self.vector = vector
        self.dimension = len(vector)
        
    def __mul__(self, anotherVector):
        try:
            if len(anotherVector) != len(self):
                raise DimensionError(self, anotherVector)
            return sum([self[i]*anotherVector[i] for i in range(self.dimension)])
        except DimensionError as e:
            print e.msg

    def __rmul__(self, anotherVector):
        return self*anotherVector

    def __imul__(self, anotherVector):
        try:
            if len(anotherVector) != len(self):
                raise DimensionError(self, anotherVector)
            self.vector = [self.vector[i] * anotherVector[i] for i in range(len(self))]
        except DimensionError as e:
            print e.msg

    def __add__(self, anotherVector):
        try:
            if len(anotherVector) != len(self):
                raise DimensionError(self, anotherVector)
            return Vector([self.vector[i] + anotherVector[i] for i in range(len(self))])
        except DimensionError as e:
            print e.msg

    def __radd__(self, anotherVector):
        return (self + anotherVector)

    def __iadd__(self, anotherVector):
        try:
            if len(anotherVector) != len(self):
                raise DimensionError(self, anotherVector)
            self.vector = [self.vector[i] + anotherVector[i] for i in range(len(self))]
        except DimensionError as e:
            print e.msg

    def __sub__(self, anotherVector):
        try:
            if len(anotherVector) != len(self):
                raise DimensionError(self, anotherVector)
            return Vector([self.vector[i] - anotherVector[i] for i in range(len(self))])
        except DimensionError as e:
            print e.msg

    def __rsub__(self, anotherVector):
        return (self - anotherVector)

    def __isub__(self, anotherVector):
        try:
            if len(anotherVector) != len(self):
                raise DimensionError(self, anotherVector)
            self.vector = [self.vector[i] - anotherVector[i] for i in range(len(self))]
        except DimensionError as e:
            print e.msg

    def __getitem__(self, index):
        try:
            return self.vector[index]
        except IndexError as e:
            print e

    def __eq__(self, anotherVector):
        for index in range(self.dimension):
            if self.vector[index] != anotherVector[index]:
                return False
        return True

    def __getslice__(self, i, j):
        try:
            return tuple(self.vector[i:j])
        except IndexError as e:
            print e

    def __len__(self):
        return self.dimension

    def __str__(self):
        return "Vector({})".format(",".join(str(element) for element in self.vector))

    def __repr__(self):
        return "Vector({})".format(",".join(str(element) for element in self.vector))

    def getDimension(self):
        return self.dimension

# }}}

#TODO
class Matrix(Vector):
# {{{ Matrix Class
    def __init__(self, data):
        self.matrix = None
# }}}

'''
class Feature:
    def __init__(self, data):
    # data should be in the form of list or numpy array
        self.features = data
        self.dimension = len(data[0])
        self.size = len(data)
    def getDimension(self):
        return self.dimension
    def getFeatures(self):
        return self.features
    def normalize(self, method="linear", columns=None):
        if columns == None:
            columns = range(0, self.dimension)
        for col in columns:
            # extract a specified column from feature space
            feature = [[sample[col]] for sample in self.features]
            feature = preprocessing.normalize(feature, method)
'''
