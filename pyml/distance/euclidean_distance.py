# -*- coding: utf-8 -*-
import numpy as np
from pyml.utils.exceptions import *

def euclidean_distance(p1, p2, r=2):
# {{{ Euclidean distance
    ''' Input objects should be two points;
        Compute Euclidean distance between p1 and p2;
        Default is L2-norm
        r == 'inf' indicates L∞-Norm
    '''

    try:
        if (type(r) not in  (int, str)) or (type(p1) not in (np.ndarray, list, tuple)) or \
                (type(p2) not in (np.ndarray, list, tuple)):
            raise TypeError("Input data invalid!")
        #TODO: raise possible errors
        elif len(p1) != len(p2):
            raise DimensionError
        elif len(p1) == 0:
            raise EmptyError
        else:
            #  L∞-Norm 
            if r == 'inf':
                distance = 0
                for i in range(len(p1)):
                    p1i, p2i = p1[i], p2[i]
                    if distance < abs(p1i-p2i):
                        distance = abs(p1i-p2i)
            # Lr-Norm
            else:
                sumation = 0
                for i in range(len(p1)):
                    p1i, p2i = p1[i], p2[i]
                    sumation += abs(p1i-p2i)**r
                distance = float(sumation)**(1./r)
            return distance
    except:
        raise
# }}}
