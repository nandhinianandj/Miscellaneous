
--filetype=cpp:expandtab:shiftwidth=2:tabstop=8:softtabstop=2

import Data.List

removeNonUppercase:: [Char] -> [Char]
removeNonUppercase st = [c |c <- st,c `elem` ['A'..'Z']]

addThree :: Int -> Int -> Int -> Int
addThree x y z = x + y + z

factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n = n * factorial (n-1)

circumference :: Float -> Float
circumference r = 2 * pi * r

lucky :: (Integral a) => a -> String
lucky 7 = "LUCKY NUMBER SEVEN!"
lucky x = "Sorry you're out of luck, pal!"

sayMe :: (Integral a) => a -> String
sayMe 1 = "One!"
sayMe 2 = "Two!"
sayMe 3 = "Three!"
sayMe x = "Not in the range of 1 and 3"

charName :: Char -> String
charName 'a' = "Anand"
charName 'b' = "Boy"
charName 'c' = "Cat"

addVectors :: (Num a) => (a,a) -> (a,a) -> (a,a)
addVectors (x1,y1) (x2,y2) = (x1 + x2, y1 + y2)

first :: (a, b, c) -> a
first (x, _, _) = x

second :: (a, b, c) -> b
second (_, y, _) = y

third :: (a,b,c) -> c
third (_, _, z) = z


tell :: (Show a) => [a] -> String
tell [] = "The list is empty"
tell (x:[]) = "The list has one element: " ++ show x
tell (x:y:[]) = "The list has two elements: " ++ show x ++ " and " ++ show y
tell (x:y:_) = "This list is two long. The first two elements are: " ++ show x ++ " and" ++ show y

length' :: (Num b) => [a] -> b
length' [] = 0
length' (_:xs) = 1 + length' xs

sum' :: (Num a) => [a] -> a
sum' x = foldl (+) 0 x

--sum' xs = foldl (\acc x -> acc +x) 0 xs
--sum' [] = 0
--sum' (x:xs) = x + sum' xs

capital :: String -> String
capital "" = "Empty string, whoops!"
capital all@(x:xs) = "The first letter of " ++ all ++ " is " ++ [x]


bmiTell :: (RealFloat a) =>a -> a -> String
bmiTell weight height
	| bmi <= 18.5	 = "You're underweight, you emo, you"
	| bmi <= 25.0    = "You're supposedly normal. I  bet you're ugly"
	| bmi <= 30.0    = "You're fat! Lose some weight, fatty"
	| otherwise      = "You're a whale, the biggest mammal"
	where (bmi, skinny, normal, fat) = (weight / height ^ 2, 18.5, 25.0, 30.0)

max' :: (Ord a) => a -> a -> a
max' a b
	| a > b		= a
	| otherwise	= b

myCompare :: (Ord a) => a -> a -> Ordering
a `myCompare` b
	| a > b		= GT
	| a == b	= EQ
	| otherwise	= LT


initials :: String -> String -> String
initials firstname lastname = [f] ++ ". " ++ [l] ++ "."
			where (f:_) = firstname
			      (l:_) = lastname


calcBmis :: (RealFloat a) => [(a,a)] -> [a]
calcBmis xs = [bmi w h|(w,h) <- xs]
	where bmi weight height = weight/height ^2



cylinder :: (RealFloat a) => a -> a -> a
cylinder r h = 
	let (sideArea, topArea) = (2 * pi * r * h, pi * r^2)
	in  sideArea + 2 * topArea

head' :: [a] -> a
head' xs = case xs of [] -> error "No head for empty lists"
		      (x:_) -> x	

describeList :: [a] -> String
describeList xs = "The list is " ++ case xs of [] -> "empty"
				 	       [x] -> "a singleton list"
					       xs -> "a long list of length " ++ show(length xs)



maximum' :: (Ord a) => [a] -> a
--maximum' [] = error "Can't find maximum of empty list"
--maximum' [x] = x
--maximum' (x:xs)
--	| x > maxTail = x
--	| otherwise = maxTail
---	where maxTail = maximum' xs

maximum' = foldr1 (\x acc -> if x > acc then x else acc)
	
replicate' :: (Num i, Ord i) => i -> a -> [a]
replicate' n x
	| n <= 0 = []
	| otherwise = x:replicate' (n-1) x

take' :: (Num i, Ord i) => i -> [a] -> [a]
take' n _
	| n <= 0 = []
take' _ []	 = []
take' n (x:xs) 	 = x : take' (n-1) xs

reverse' :: [a] -> [a]
--reverse' [] = []
--reverse' (x:xs) = reverse' xs ++ [x]
--reverse' = foldl (\acc x -> x : acc) []
reverse' = foldl (flip (:)) []

repeat' :: a -> [a]
repeat' x = x:repeat' x

zip' :: [a] -> [b] -> [(a,b)]
zip' _ [] = []
zip' [] _ = []
zip' (x:xs) (y:ys) = (x,y):zip' xs ys

elem' :: (Eq a) => a -> [a] -> Bool
elem' y ys = foldl (\acc x -> if x == y then True else False) False ys
--elem' a [] = False
--elem' a (x:xs)
--	| a == x	= True
--	| otherwise	= a `elem` xs


quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) = 
	let smallerSorted = quicksort [a | a <- xs, a <= x]
	    biggerSorted  = quicksort [a | a <- xs, a > x]
	in  smallerSorted ++ [x] ++ biggerSorted


quicksort' :: (Ord z) => [z] -> [z]
quicksort' [] = []
quicksort' (x:xs) =
	let smallerSorted = quicksort (filter (<=x) xs)
	    biggerSorted = quicksort (filter (>x) xs)
	in smallerSorted ++ [x] ++ biggerSorted


multThree :: (Num a) => a -> a -> a -> a
multThree x y z = x * y * z

compareWithHundred :: (Num a, Ord a) => a -> Ordering
compareWithHundred = compare 100


divideByTen :: (Floating a) => a -> a
divideByTen = (/10)

isUpperAlpha :: Char -> Bool
isUpperAlpha = (`elem` ['A' .. 'Z'])

applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)

zipWith' :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith' _ [] _ = []
zipWith' _ _ [] = []
zipWith' f (x:xs) (y:ys) = f x y : zipWith' f xs ys

flip' :: (a -> b -> c) -> (b -> a -> c)
flip' f = g
	where g x y = f y x

map' :: (a -> b) -> [a] -> [b]
--map' _ [] = []
--map' f (x:xs) = f x : map' f xs
--map' :: (a -> b) -> [a] -> [b]
map' f xs = foldr (\x acc -> f x : acc) [] xs

filter' :: (a -> Bool) -> [a] -> [a]
filter' p = foldr (\x acc -> if p x then x : acc else acc) []
--filter' _ [] = []
--filter' p (x:xs)
--	| p x 	= x : filter' p xs
--	| otherwise = filter' p xs

largestDivisible :: (Integral a) => a -> a -> a
largestDivisible x y = head (filter p [y,y-1 ..])
	where p y = y `mod` x  == 0

collatz_chain :: (Integral a) => a -> [a]
collatz_chain 1 = [1]
collatz_chain n
	| even n = n:collatz_chain (n `div` 2)
	| odd n = n:collatz_chain (n*3 + 1)

test_map cf x = filter (\xs -> length xs > x) (map cf [3..34])

numChainsLonger :: (Num a1, Enum a1) => (a1 -> [a]) -> Int -> Int
numChainsLonger cf x = length (filter (\xs -> length xs > x) (map cf [10,100 .. 10000]))


addThree' :: (Num a) => a -> a -> a -> a
addThree' = \x -> \y -> \z  -> x + y + z

product' :: (Num a) => [a] -> a
product' = foldr1 (*)

sqrtSums :: (Ord a,Floating a, Enum a) => a -> Int
--sqrtSums :: a -> Int
sqrtSums x = length (takeWhile (<x)(scanl1 (+) (map sqrt [1..]))) +1

--($) :: (a -> b) -> a -> b
--f $ x = f x

fn x = ceiling . negate .tan .cos .max 50 

oddSquareSum :: (Integral a) => a -> a 
--oddSquareSum  x = sum.takeWhile (<x). filter  odd .map (^2) $ [1..]
oddSquareSum x = 
	let oddSquares = filter odd $ map (^2) [1..]
	    belowLimit = takeWhile (< x) oddSquares
	in sum belowLimit

numUniques :: (Eq a) => [a] -> Int
numUniques = length . Data.List.nub

search :: (Eq a) => [a] -> [a] -> Bool
search needle haystack = 
	let nlen = length needle
	in foldl (\acc x -> if take nlen x == needle then True else acc) False (tails haystack)

--group' :: (a -> a -> Bool) -> [a] -> [[a]]
--group' f x:xs =  if (f x) then 

mybubble::(Ord a) => [a] -> [a]
mybubble ([]) = []
mybubble (x:[]) = [x]
mybubble (x:y:xs) = if x>y then y:mybubble (x:xs) else x:mybubble (y:xs)

--Loop ::[a] -> [a]
--Loop ([]) = []
--Loop (x:[]) = [x]
--Loop (x:y:xs) = if x>y then y:Loop (x:xs) else x:Loop (y:xs)


--Bubbble implementation copied from http://tech-nickel.blogspot.com/2008/10/sorting-using-haskell.html
bubble :: (Ord t) => [t] -> [t] 
bubble (a:b:c) | a < b = a : bubble (b:c)
               | otherwise = b : bubble (a:c)
bubble (a:[]) = [a] 
bubble [] = []

loop :: (Num a, Ord a) => a -> (t -> t) -> t -> t
loop count f x | count > 0 = loop (count -1) f x'
			   | otherwise = x
			   where x' = f x

bubbleSort :: (Ord a) => [a] -> [a]
bubbleSort a = loop (length a -2) bubble a
