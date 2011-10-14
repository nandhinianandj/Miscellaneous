--fibonacci :: Num -> [Num]
fibonacci 1 = [1]
fibonacci 2 = [1,1]
--fibonacci 3 = [2]
--fibonacci n = fibonacci n-1
fibonacci n = fibonacci (n-1) ++ [last(fibonacci (n-1)) + last(fibonacci (n-2))]

--euler_prob_2 :: Int -> Int
euler_prob_2 n = sum (takeWhile (\x -> x < n) (fibonacci n))

--module Main where
--main :: IO()
--main = show (euler_prob_2 4000000)
