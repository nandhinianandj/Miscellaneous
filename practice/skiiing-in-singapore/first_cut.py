import networkx as nx
import numpy as np

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

def main(filename='sample1.txt'):
    terrain_altitude_map = np.loadtxt(filename)
    G = nx.Graph()
    # Construct a graph with nodes as a triple (x,y, prev_node)
    for(x,y), value in np.ndenumerate(terrain_altitude_map):
        G.add_node((x,y))

        # outcoming ski-edge so curr_altitude - new_altitude = height difference
        # +1 for all edge weights for the objective function to include length of the path
        if x+1 < terrain_altitude_map.shape[0]:
            # Instead of checking for lower height just using the negative value, for now
            G.add_edge((x,y),(x+1, y),{'weight': -1 * (value - terrain_altitude_map[x+1][y] +1) })

        if y+1 < terrain_altitude_map.shape[1]:
            G.add_edge((x,y),(x, y+1), {'weight':-1 * (value - terrain_altitude_map[x][y+1] + 1) })

        # incoming ski-edge so new_altitude - curr_altitude = height difference
        if x-1 > 0:
            G.add_edge((x,y),(x-1, y), {'weight': -1 * (terrain_altitude_map[x-1][y] - value + 1)})
        if y-1 > 0:
            G.add_edge((x,y),(x, y-1), {'weight': -1 * (terrain_altitude_map[x][y-1] - value + 1)})

    ans = nx.minimum_spanning_tree(G,'weight')
    for edge in ans.edges():
        print(terrain_altitude_map[edge[0][0]][edge[0][1]] + '-')
        print(terrain_altitude_map[edge[1][0]][edge[1][1]] + '-')




if __name__ == '__main__':
    main()
