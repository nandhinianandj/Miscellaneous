module PrimeSieves
(-- Eratosthenes_sieve
--, Euclid_sieve
--, Atkin_sieve
--, Sundaram_sieve
--, Legendre_sieve
) where


import Data.List
-- list = [2,3,5..]

--Eratosthenes_sieve :: (Num a) => a -> [a]
--Eratosthenes_sieve 2 = 2
--Eratosthenes_sieve 3 = (2:sieve 2 [2,3,5])
--Eratosthenes_sieve n = let last_prime = sieve last_prime list

--sieve :: (Integral a) => a -> [a] -> a
sieve _ [] = []
sieve 1 _ = error "1 is not a prime number"
sieve n (x:xs) = head (takeWhile (>= n) (x:xs))

--pop_multiples :: [a] -> a -> [a]
pop_multiples [] _ = []
pop_multiples (x:xs) 1 = (x:xs)
pop_multiples (x:xs) n = (x:xs) - [y | y <- [2..],y `mod` n ==0]
        
Eratosthenes_sieve 1 = error "1 is not a prime number"
Eratosthenes_sieve 2 = 2
--Eratosthenes_sieve n = Eratosthenes_sieve 
