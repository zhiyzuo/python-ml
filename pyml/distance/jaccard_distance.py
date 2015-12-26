# -*- coding: utf-8 -*-
import numpy as np

def jaccard_distance(s1, s2):
# {{{ Euclidean distance
    ''' Input objects should be two sets; 
        Compute Jaccard distance between s1 and s2;
    '''

    try:
        if (type(s1) not in (np.ndarray, list, tuple, set)) or (type(s2) not in (np.ndarray, list, tuple, set)):
            raise TypeError("Input data invalid!")
        #TODO: raise possible errors
        else:
            s1, s2 = set(s1), set(s2)
            jaccard_similarity = float(len((s1.intersection(s2))))/len((s1.union(s2)))
            return (1 - jaccard_similarity)
    except TypeError as e:
        raise
# }}}
