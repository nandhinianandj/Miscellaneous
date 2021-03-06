# From John D. Cook http://www.johndcook.com/blog/2016/02/20/the-empty-middle-no-one-is-average/
import numpy as np
import pandas as pd

# Winning critera: minimum Euclidean distance
def euclidean_norm(x):
    return np.linalg.norm(x)

# Winning criteria: min-max
def max_norm(x):
    return max(abs(x))

# Assumptions involved:
# a, The features are all independent(unlikely)
# b, Sampling was not biased, but uniform
# c, Sampling was representative

# Number of features
n = 9
# Sample size
#N = 3864
N = 5000

newDf = pd.DataFrame(columns=['feature_counts', 'Euclidean_Dist', 'least_deviation_4m_average'])
for each in map(lambda x: x+1, range(n)):
    # Simulated normalized measurements of contestants
    M = np.random.normal(size=(N, each))

    euclid = np.empty(N)
    maxdev = np.empty(N)
    for i in range(N):
        euclid[i] = euclidean_norm(M[i,:])
        maxdev[i] = max_norm(M[i,:])

    w1 = euclid.argmin()
    w2 = maxdev.argmin()

    print("No. of Features")
    print(n)
    print("Euclidean distance winner's attributes")
    print("Distance")
    euclidean_dist = M[w1,:]
    print( euclidean_dist )
    print("Attributes")
    euclidean_normal = euclidean_norm(M[w1,:])
    print(euclidean_normal)
    print("least deviation from average winner's attributes")
    print( M[w2,:] )
    max_normal = max_norm(M[w2,:])
    print(max_normal)
    newDf.loc[each] = [each, euclidean_normal, max_normal]

import pdb; pdb.set_trace()
print(newDf)
