import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import csv

# def findSampleMean():
#     x = []
#     with open('/home/danielacthomas/Desktop/spring_2023/AI/assignments/cs-uy-4613/assignment1/nyc-east-river-bicycle-counts.csv', 'r') as csvfile:
#         plots = csv.reader(csvfile, delimiter = ',')
#         for row in plots:
#             x.append(int(row[10]))
#     return sum(x) / len(x)

def samplemean():

    df = pd.read_csv(r'/home/danielacthomas/Desktop/spring_2023/AI/assignments/cs-uy-4613/assignment1/nyc-east-river-bicycle-counts.csv')
    print(df)
    sample_mean = df['Total'].mean()
    print(sample_mean)

def kaggleplot():

    x = []
    y = []

    with open('/home/danielacthomas/Desktop/spring_2023/AI/assignments/cs-uy-4613/assignment1/nyc-east-river-bicycle-counts.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',')
        for row in plots:
            x.append(row[10])
            y.append(row[6])
            

    plt.bar(x, y, color = 'b', width = 0.75, label = "Frequency")
    plt.xlabel('total # of cyclists')
    plt.ylabel('frequency')
    plt.title('Frequency of Cyclists that ride on Brooklyn Birdge')
    plt.legend()
    plt.show() 

def poisson(lam):
    el, n, u = np.exp(-lam), 0, np.random.uniform(0,1)
    pp, fact, pow = el, 1, 1
    while u > pp:
        n = n + 1
        fact, pow = n*fact, lam*pow
        pp = pp + (pow/fact)*el
    return n




# df = pd.read_csv(r'/home/danielacthomas/Desktop/spring_2023/AI/assignments/cs-uy-4613/assignment1/nyc-east-river-bicycle-counts.csv')
# print(df)
# sample_mean = df['Brooklyn Bridge'].mean()
# print(sample_mean)
# #lam = mu = 2269.63

# x = np.random.poisson(2269, 211)
# results = plt.hist(x)
# plt.show()

x = np.random.poisson(2269.63, 211)
#print(x.mean()) -> 2272.3

count, bins, ignored = plt.hist(x, 14, density = True)
plt.show()
