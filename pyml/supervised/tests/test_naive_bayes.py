import numpy as np
from pyml.metric import confusion_matrix
from pyml.cross_validation import leave_one_out
from pyml.dataset import tic_tac_toe, tennis
from pyml.supervised.naive_bayes import NaiveBayes

x, y = tennis.load()
#x, y = data[:1000, :-1], data[:1000, -1].flatten()

nb = NaiveBayes()

nb.fit(x[:13], y[:13])

y_pred = nb.predict(x[13:])

print confusion_matrix(y[13:], y_pred)
