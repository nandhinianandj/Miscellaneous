{-# LANGUAGE QuasiQuotes #-}
-- ShortestPaths.hs
import Python
data Graph

square::Int -> IO Int
square = defVV "export = lambda x:x * x"

square1 :: Int -> IO Int
square1 = defVV "from numpy import square as export"

guess_type :: String -> IO String
guess_type = defVV "from mimetypes import guess_type; export = lambda x: guess_type(x)[0]"

sin_product :: Float -> Float -> IO Float
sin_product = defVVV "def export(x, y): from math import sin; return sin(x * y)"

getGraph :: [(Int, Int)] -> IO (PyObject Graph)
getGraph = defVO [str]
"import networkx
def export(xs):
    g = networkx.Graph()
    for edge in xs:
        g.add_edge(edge[0], edge[1])
    return g
|]"

shortestPath :: (Int, Int) -> PyObject Graph -> IO Int
shortestPath = defVOV [str]
"import networkx
def export(x, g):
    return int(networkx.shortest_path_length(g, x[0], x[1]))
|]"

-- main = do
--     x <- square 7
--     print x
main = do
    g <- getGraph [(1,2), (2,3), (3,4)]
    distance <- shortestPath (1, 4) g
    print distance

