# From John D. Cook http://www.johndcook.com/blog/2016/02/20/the-empty-middle-no-one-is-average/
import numpy as np

# Winning critera: minimum Euclidean distance
def euclidean_norm(x):
    return np.linalg.norm(x)

# Winning criteria: min-max
def max_norm(x):
    return max(abs(x))

n = 9
N = 3864

# Simulated normalized measurements of contestants
M = np.random.normal(size=(N, n))

euclid = np.empty(N)
maxdev = np.empty(N)
for i in range(N):
    euclid[i] = euclidean_norm(M[i,:])
    maxdev[i] = max_norm(M[i,:])

w1 = euclid.argmin()
w2 = maxdev.argmin()

print( M[w1,:] )
print( euclidean_norm(M[w1,:]) )
print( M[w2,:] )
print( max_norm(M[w2,:]) )
