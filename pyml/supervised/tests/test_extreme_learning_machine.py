import numpy as np
from pyml.metric import mse, rmse
from pyml.cross_validation import leave_one_out
from pyml.dataset import airfoil_self_noise
from pyml.supervised.extreme_learning_machine import ELM

x, y = airfoil_self_noise.load()
data = np.hstack((x,y.reshape(x.shape[0],1)))
np.random.shuffle(data)
x, y = data[:, :-1], data[:, -1].flatten().astype(np.uint8)

elm = ELM(n=200)

elm.fit(x[:1400], y[:1400])
y_pred = elm.predict(x[1400:])
for i in range(y_pred.size):
    print y[1400:][i], y_pred[i]

print mse(y[1400:], y_pred)
print rmse(y[1400:], y_pred)


