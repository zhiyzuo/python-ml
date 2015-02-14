# -*- coding: utf-8 -*-
import numpy as np

def euclidean_distance(x1, x2, r=2):
# {{{ Euclidean distance
    ''' Compute Euclidean distance between x1 and x2;
        Default is L2-norm
        r == 'inf' indicates L∞-Norm
    '''

    try:
        if (type(r) not in  (int, str)) or (type(x1) not in (np.ndarray, list, tuple)) or \
                (type(x1) not in (np.ndarray, list, tuple)):
            raise TypeError("Input data invalid!")
        #TODO: raise possible errors
        else:
            #  L∞-Norm 
            if r == 'inf':
                distance = 0
                for i in range(len(x1)):
                    x1i, x2i = x1[i], x2[i]
                    if distance < abs(x1i-x2i):
                        distance = abs(x1i-x2i)
            # Lr-Norm
            else:
                sumation = 0
                for i in range(len(x1)):
                    x1i, x2i = x1[i], x2[i]
                    sumation += abs(x1i-x2i)**r
                distance = float(sumation)**(1./r)
            return distance
    except TypeError as e:
        raise
# }}}
