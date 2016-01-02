import numpy as np
from pyml.metric import confusion_matrix
from pyml.cross_validation import leave_one_out
from pyml.dataset import banknote_authentication
from pyml.supervised.extreme_learning_machine import ELM

x, y = banknote_authentication.load()

elm = ELM()

loo = leave_one_out(y.size)
cm = np.zeros((2,2))
for tr, te in loo:
    x_tr, y_tr = x[tr], y[tr]
    x_te, y_te = x[te], y[te]
    elm.fit(x_tr, y_tr)
    y_pred = elm.predict(x_te)
    cm += confusion_matrix(y_te, y_pred)

print cm


