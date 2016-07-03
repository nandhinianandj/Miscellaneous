import numpy as np
terrain_map = np.loadtxt('test_play.txt')

# This is a graph search problem with 4 edges coming out of all vertices(well except the corner
# ones)
# Clearly, from the description they assume the starting point is anywhere and they can
# teleport(:-) to
# it.

# Heuristic 1: Don't search all of the starting points cut it down to half
# Heuristic 2: Even among the half of the starting points prune down the paths that lead to quick
# ends(i.e, the matrix index bounds)


def starting_indexes(nparray, threshold=500):
    ind =
    ix = np.inldx(x.ravel()
    return np.where(nparray >= threshold)
