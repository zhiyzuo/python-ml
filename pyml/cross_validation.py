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

def k_fold(n, k=5):
    '''
        Partition datasets for use of K-Fold Cross Validation
    '''

    indices = np.arange(n)
    np.random.shuffle(indices)
    k_folds = np.split(indices, k)
    for index in k_folds:
        te_ = np.array([index]).flatten()
        tr_ = np.array([idx for idx in k_folds if (idx != index).all()]).flatten()
        yield (tr_, te_)

