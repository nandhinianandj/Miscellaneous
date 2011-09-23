fibonacci :: Int -> Int
fibonacci 1 = 1
fibonacci 2 = 2
fibonacci n = fibonacci n + fibonacci n-1

euler_prob_2 :: Int -> Int
euler_prob_2 n =
                let y = takeWhile (fibonacci x < n) x <- [1..]
                sum ([xs|xs <- x,xs `mod` 2 == 0])

