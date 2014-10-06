module BST
( Tree
, singleton
, treeInsert
, treeElem
, fmap
) where

data Tree a = EmptyTree | Node a (Tree a) (Tree a) deriving (Show, Read, Eq)

singleton :: a -> Tree a
singleton x = Node x EmptyTree EmptyTree

treeInsert :: (Ord a)=> a -> Tree a -> Tree a
treeInsert x EmptyTree = singleton x
treeInsert x (Node a left right)
    | x == a = Node x left right
    | x < a  = Node a (treeInsert x left) right
    | x > a  = Node a left (treeInsert x right)


treeElem :: (Ord a) => a -> Tree a -> Bool
treeElem x EmptyTree = False
treeElem x (Node a left right)
    | x == a = True
    | x < a = treeElem x left
    | x > a = treeElem x right

data Options = {test :: String}
--class Functor f where
--    fmap :: (a -> b) -> f a -> f b
--instance Functor [] where
--    fmap = map
--instance Functor Maybe where
--    fmap f (Just x) = Just (f x)
--    fmap f Nothing = Nothing
--
--instance Functor Tree where
--    fmap f EmptyTree = EmptyTree
--    fmap f (Node x leftsub rightsub)
--
--instance Functor (Either a) where
--    fmap f (Right x) = Right (f x)
--    fmap f (Left x) = Left x
--
--data Either a b = Left a | Right b
--
--instance Functor Tree where
--    fmap f EmptyTree = EmptyTree
--    fmap f (Node x leftsub rightsub) = Node (f x) (fmap f leftsub) (fmap f rightsub)
--
--instance Functor (Either a) where
--    fmap f (Right x) = Right (f x)
--    fmap f (Left x) Left (f x)
--
-- data Either a b = Left a | Right b
--
--
--


