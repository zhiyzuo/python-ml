# -*- coding: utf-8 -*-
import numpy as np
from pyml.utils.exceptions import *

def cosine_distance(v1,v2):
# {{{ Cosine distance
    ''' Input objects should be two vectors;
        Compute cosine distance (angle) between v1 and v2;
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
            den = np.sqrt(v1.dot(v1)) * np.sqrt(v2.dot(v2))
            num = np.dot(v1, v2)
            distance = (np.arccos(float(num)/den))*180/np.pi
            return distance
    except:
        raise
# }}}
