import numpy as np

def leave_one_out(n):
    '''
        Partition datasets using Leave One Out (loo)

        Return training indices and testing indices
    '''
    indices = np.arange(n)

    for index in indices:
        te_ = np.array([index])
        tr_ = np.array([idx for idx in indices if idx != index])
        yield (tr_, te_)

def k_fold(data, k=5):
    pass

