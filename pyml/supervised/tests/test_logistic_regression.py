import numpy as np
from pyml.metric import confusion_matrix
from pyml.cross_validation import leave_one_out
from pyml.dataset import skin_segmentation
from pyml.supervised.logistic_regression import LogisticRegression

x, y = skin_segmentation.load()
data = np.hstack((x,y.reshape(x.shape[0],1)))
np.random.shuffle(data)
x, y = data[:, :-1], data[:, -1].flatten()

logReg = LogisticRegression()

loo = leave_one_out(y.size)
cm = np.zeros((2,2))
for tr, te in loo:
    x_tr, y_tr = x[tr], y[tr]
    x_te, y_te = x[te], y[te]
    logReg.fit(x_tr, y_tr)
    y_pred = logReg.predict(x_te)
    cm += confusion_matrix(y_te, y_pred)

print cm


