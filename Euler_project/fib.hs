--fibonacci_my :: Num -> [Num]
--fibonacci_my 1 = [1]
--fibonacci_my 2 = [1,1]
--fibonacci_my 3 = [2]
--fibonacci_my n = fibonacci_my n-1
--fibonacci_my n = fibonacci_my (n-1) ++ [last(fibonacci_my (n-1)) + last(fibonacci_my (n-2))]

fib_naive :: Integer -> Integer
fib_naive 0 = 0
fib_naive 1 = 1
fib_naive n = fib_naive(n-1) + fib_naive(n-2)

--fib_infinite ::
--fib_infinite n = fib_infinite!!n

fib_scan = 0:1:zipWith (+) fib_scan (tail fib_scan)

--euler_prob_2 :: Int -> Int
euler_prob_2 n = sum (takeWhile (\x -> (even x && x < n)) (fib_scan ))

--module Main where
--main :: IO()
--main = show (euler_prob_2 4000000)
