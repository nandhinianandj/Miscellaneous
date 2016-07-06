import numpy as np
terrain_map = np.loadtxt('sample1.txt')

# This is a graph search problem with 4 edges coming out of all vertices(well except the corner
# ones)
# Clearly, from the description they assume the starting point is anywhere and they can
# teleport(:-) to
# it.

# From a optimization point of view, the challenge is to maximize sum of height differences in the
# path taken and length of the path. That translates in the graph theory world to maximal spanning
# tree problem.
# The challenge though is the height difference at a given position depends on which position you
# came in from. So to represent this in a graph we'll need 4 x (input matrix size in this case
# 1000x1000)  That's huge not sure a straightforward search can be done. We might need to trim the
# graph with Heuristics before attempting:

# Heuristic 1: Don't search all of the starting points cut it down to half
# Heuristic 2: Even among the half of the starting points prune down the paths that lead to quick
# ends(i.e, the matrix index bounds)

# Heuristic 1:
def starting_positions(nparray, threshold=0.5):
    return np.where(nparray >= threshold*nparray.max())

#Heurisitc 2:
# Create a probability matrix with peak at the center element
# Hmm. may be that heurisitic is wrong.
def prob_matrix(size=(1000,1000)):
    mat = np.zeros(size)
    for
