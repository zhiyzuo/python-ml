# -*- coding: utf-8 -*-
import numpy as np
from pyml.utils.exceptions import *

def hamming_distance(v1,v2):
# {{{ Hamming distance
    ''' Input objects should be two vectors;
        Return the number of different elements in two vectors;
    '''

    try:
        if (type(v1) not in (np.ndarray, list, tuple)) or (type(v2) not in (np.ndarray, list, tuple)):
            raise TypeError("Input data invalid!")
        elif len(v1) != len(v2):
            raise DimensionError
        elif len(v1) == 0:
            raise EmptyError
        #TODO: raise possible errors
        else:
            v1, v2 = np.array(v1), np.array(v2)
            distance = 0
            for i in range(len(v1)):
                e1, e2 = v1[i], v2[i]
                if e1 != e2:
                    distance += 1
            return distance
    except:
        raise
# }}}
