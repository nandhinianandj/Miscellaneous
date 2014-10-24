module Graph
( Graph
, singleton
, graphInsert
, graphElem
, fmap
) where

data Edge a b = Node a Node b deriving(Show, Read, Eq)
data Graph Node Edge = EmptyGraph | Graph a

singleton :: a -> Graph a
singleton x = Node x EmptyGraph EmptyGraph

graphInsert :: (Ord a)=> a -> Graph a -> Graph a
graphInsert x EmptyGraph = singleton x
graphInsert x (Node a left right)
    | x == a = Node x left right
    | x < a  = Node a (graphInsert x left) right
    | x > a  = Node a left (graphInsert x right)


graphElem :: (Ord a) => a -> Graph a -> Bool
graphElem x EmptyGraph = False
graphElem x (Node a left right)
    | x == a = True
    | x < a = graphElem x left
    | x > a = graphElem x right



