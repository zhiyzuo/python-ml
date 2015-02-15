# -*- coding: utf-8 -*-
import numpy as np

'''
Page Rank Algorithm for Graph
** Page, Lawrence, et al. "The PageRank citation ranking: Bringing order to the web." (1999). **
'''

#TODO
def _power_iteration(r, M, random=True, beta=0.8):
    '''
    default: Google Formulation and beta=0.8
    '''
