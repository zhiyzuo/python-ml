import numpy as np

def mse(y_true, y_pred):
    '''
        For regression models
    '''

    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    return ((y_true-y_pred)**2).sum()

def rmse(y_true, y_pred):
    return np.sqrt(mse(y_true, y_pred))

def accuracy(y_true, y_pred):
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    return sum(y_true == y_pred)/float(y_true.size)


def confusion_matrix(y_true, y_pred):
    '''
          TP   FP
        
          FN   TN
    '''

    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    conf_mat = np.zeros((2,2))
    for i in range(y_true.size):
        true, pred = y_true[i], y_pred[i]
        if true == pred:
            if true:
                conf_mat[0,0] += 1
            else:
                conf_mat[1,1] += 1
        else:
            if true:
                conf_mat[1,0] += 1
            else:
                conf_mat[0,1] += 1

    return conf_mat


