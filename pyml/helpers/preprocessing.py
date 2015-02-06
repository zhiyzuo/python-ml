from operations import *
import numpy as np

def normalize(matrix, columns, method="linear"):
# input should be a numpy matrix
    normalized_matrix = np.matrix([[] for i in range(matrix.shape[1])])
    if method == "linear":
        for col in range(matrix.shape[1]):
            if col in columns:
                vector = matrix[:, col][:]
                minVal = float(min(vector))
                scale = - minVal + max(vector)
                try:
                    normalized_matrix = np.concatenate((normalized_matrix, np.array([[(vector[i, 0] - minVal)/scale] for i in range(vector.shape[0])])), axis=1)
                except ZeroDivisionError:
                    print "Maximum and minimun are the same value!"
                    continue
            else:
                normalized_matrix = np.concatenate((normalized_matrix, vector), axis=1)

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
