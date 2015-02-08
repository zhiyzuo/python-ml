from operations import *
import numpy as np
import math

def normalize(matrix, columns, method="linear"):
# {{{ normalize
    normalized_matrix = np.matrix([[] for i in range(matrix.shape[0])])
    if method == "linear":
        for col in range(matrix.shape[1]):
            vector = matrix[:, col][:]
            if col in columns:
                minVal = float(min(vector))
                scale = - minVal + max(vector).item()
                try:
                    normalized_vector = np.array([[(vector[i, 0] - minVal)/scale] for i in range(vector.shape[0])])
                    normalized_matrix = np.column_stack((normalized_matrix, normalized_vector))
                except ZeroDivisionError:
                    print "Maximum and minimun are the same value!"
            else:
               normalized_matrix = np.column_stack((normalized_matrix, vector))

    '''
        #TODO: feels not right
    elif method.lower() =="z" or method.lower() == "z-transform":
        for col in columns:
            vector = matrix[:, col]
            meanVal = mean(vector)
            stdVal = std(vector)
            try:
                return [(xi - meanVal)/stdVal for xi in vector]
            except ZeroDivisionError:
                print "All points are of the same value!"
                return
    '''

    return normalized_matrix
# }}}

def discretize(matrix, columns, bins):
# {{{ discretize
    discretized_matrix = np.matrix([[] for i in range(matrix.shape[0])])
    for col in range(matrix.shape[1]):
        vector = matrix[:, col][:]
        if col in columns:
            bin_ = int(math.ceil(bins[col]))
            bins_ = np.linspace(vector.min(), vector.max(), bin_)
            discretized_vector = np.digitize(np.transpose(np.asarray(vector))[0], bins_)
            discretized_matrix = np.column_stack((discretized_matrix, discretized_vector))
        else:
            discretized_matrix = np.column_stack((discretized_matrix, vector))
    return discretized_matrix
# }}}
