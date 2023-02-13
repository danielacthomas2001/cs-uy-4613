import numpy as np
import matplotlib.pyplot as plt



lam1 = 1
lam2 = 3
lam3 = 4
mu = 4
queue = []
nextArrival = np.random.poisson(lam1)
nextService = nextArrival + np.random.poisson(mu)
num_of_samples = 0
while (num_of_samples < 1000):
    while(nextArrival < nextService):
        queue.append(nextArrival)
        nextArrival += np.random.poisson(lam1)
    a = queue.pop()
    waiting_time = nextService - a
    if (len(queue ) != 0):
        nextService += np.random.poisson(mu)
    else:
        nextService = nextArrival + np.random.poisson(mu)
    num_of_samples += 1
num_of_samples = 0
queue = []
nextArrival = np.random.poisson(lam2)
nextService = nextArrival + np.random.poisson(mu)
while (num_of_samples < 1000):
    while(nextArrival < nextService):
        queue.append(nextArrival)
        nextArrival += np.random.poisson(lam2)
    a = queue.pop()
    waiting_time = nextService - a
    if (len(queue)!= 0):
        nextService += np.random.poisson(mu)
    else:
        nextService = nextArrival + np.random.poisson(mu)
    num_of_samples += 1


num_of_samples = 0
queue = []
nextArrival = np.random.poisson(lam3)
nextService = nextArrival + np.random.poisson(mu)
while (num_of_samples < 1000):
    while(nextArrival < nextService):
        queue.append(nextArrival)
        nextArrival += np.random.poisson(lam3)
    a = queue.pop()
    waiting_time = nextService - a
    if (len(queue)!= 0):
        nextService += np.random.poisson(mu)
    else:
        nextService = nextArrival + np.random.poisson(mu)
    num_of_samples += 1

for i in range(3):
    plt.hist(queue)
plt.xlabel('Time')
plt.ylabel('# of requests waiting in queue')
plt.show()
    
'''
need to plot the # of requests that are waiting in the
queue as a func of time.

'''



# time = 1000
# mu = 4
# lam = [1,3,4]
# length = np.zeros(len(lam), time)
# nextArrival = np.random.poisson(lam[0])
# num_of_samples = 0
# while(num_of_samples < 1000):
#     while(nextArrival < mu):


# while (num_of_samples < 1000):
#     while nextArrival < ...:

#     a = 
    
