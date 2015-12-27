import numpy as np
from pyml.metric import confusion_matrix
from pyml.cross_validation import leave_one_out
from pyml.dataset import tic_tac_toe, tennis
from pyml.supervised.naive_bayes import NaiveBayes

x, y = tic_tac_toe.load()
data = np.hstack((x,y.reshape(x.shape[0],1)))
np.random.shuffle(data)
x, y = data[:, :-1], data[:, -1].flatten().astype(np.uint8)

nb = NaiveBayes((50, 0.2))

loo = leave_one_out(y.size)
cm = np.zeros((2,2))
count = 0
for tr, te in loo:
    count += 1
    x_tr, y_tr = x[tr], y[tr]
    x_te, y_te = x[te], y[te]
    nb.fit(x_tr, y_tr)
    y_pred = nb.predict(x_te)
    cm += confusion_matrix(y_te, y_pred)

print cm

