import numpy as np

import matplotlib.pyplot as plt

u = np.array([0,2])
A = np.array([[0.3, -1], [-1, 5]])
mux = 0.6
sigma = 0.1

L = np.linalg.cholesky(A)


x = np.random.multivariate_normal(u, L, 1000)

#x, y = np.random.multivariate_normal(u, L, (1000,2))
# x = np.random.normal(u, L, 1000)

results = plt.hist(x)
plt.show()
# plt.scatter(x[:,0], x[:,1])
# plt.show()


