import networkx as nx
import numpy as np
from skimage import novice
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
# 1000x1000)  That's huge not sure a straightforward search can be done.

# Ok that was wrong on multiple levels.. one:no need for that 4x component the matrix logically
# encodes both the vertices and the edge weights contain the possible edges from any direction so
# the edge weights will take care of it.


# Mistake 2: Minimal spanning tree algorithm won't work, because it necessitates all vertices are
# covered.. So will need heuristic search and may be dynamic programming  for this one.

# We might need to trim the
# graph with Heuristics before attempting:

# Heuristic 1: Don't search all of the starting points cut it down to half
# Heuristic 2: Even among the half of the starting points prune down the paths that lead to quick
# ends(i.e, the matrix index bounds)

# Heuristic 1:
def filtered_heights(nparray, low_threshold=0.5):
    return np.where(nparray >= (1-low_threshold)*nparray.max())

def starting_positions(nparray, heightList):
    #TODO: Look for an efficient way to find these indexes
    res = list()
    for (x,y) , value in np.ndenumerate(nparray):
        if value in heightList:
            res.appnd((x,y))
    return res
#Heurisitc 2:
# Create a probability matrix with peak at the center element
# Hmm. may be that heurisitic is wrong.
def prob_matrix(size=(1000,1000)):
    mat = np.zeros(size)

def graph_mst_method(filename='sample1.txt'):
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
    agraph_ans = nx.nx_agraph.to_agraph(ans)
    agraph_ans.layout(prog='dot')
    png = agraph_ans.draw('answer.png')
    #filename = agraph_ans.render(filename='img/answer')

    from bokeh.plotting import figure, show
    image = novice.open('answer.png')
    p = figure((0, image.shape[0]),(0, image.shape[1]))
    p.image(image=image)
    show(p)
    for edge in ans.edges():
        print(edge, G[edge[0]][edge[1]]['weight'])
        print(str(terrain_altitude_map[edge[0][0]][edge[0][1]]) + '-' + str(terrain_altitude_map[edge[1][0]][edge[1][1]]))


def main(filename='sample1.txt'):
    terrain_altitude_map = np.loadtxt(filename)
    x_idx, y_idx = filtered_heights(terrain_altitude_map, low_threshold=0.5)
    starting_indices = list(zip(x_idx, y_idx))
    print(starting_indices)
    G = nx.Graph()
    for(x,y), value in np.ndenumerate(terrain_altitude_map):
        G.add_node((x,y))
        if x+1 < terrain_altitude_map.shape[0]:
            # Instead of checking for lower height just using the negative value, for now
            G.add_edge((x,y),(x+1, y),{'weight': -1 * (value - terrain_altitude_map[x+1][y] +1) })
        if y+1 < terrain_altitude_map.shape[1]:
            G.add_edge((x,y),(x, y+1), {'weight':-1 * (value - terrain_altitude_map[x][y+1] + 1) })
        if x-1 > 0:
            G.add_edge((x,y),(x-1, y), {'weight': -1 * (terrain_altitude_map[x-1][y] - value + 1)})
        if y-1 > 0:
            G.add_edge((x,y),(x, y-1), {'weight': -1 * (terrain_altitude_map[x][y-1] - value + 1)})

    for idx in starting_indices:
        depth_first_search(G, start=idx)

def greedy_search(altitude_graph, start):
    from collections import deque
    neighbors = G.neighbors_iter
    visited = set([start])

    queue = deque([(start, neighbors(start))])
    while queue:
        parent, children = queue[0]
        try:
            child = next(children)
            if child not in visited:
                yield parent, child
                visited.add(child)
                queue.append((child, neighbors[child]))
        except Exception
    pass

def depth_first_search(altitude_graph, start):
    pass

def breadh_fist
if __name__ == '__main__':
    main()
