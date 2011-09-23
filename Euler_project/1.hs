sum_multiples_x :: Int -> Int -> Int
sum_multiples_x 0 _ = 0
sum_multiples_x x n = sum([xs|xs <- [1..n],((xs `mod` x) == 0)])

euler_prob_1 :: Int -> Int
euler_prob_1 n = sum_multiples_x 3 n + sum_multiples_x 5 n - sum_multiples_x 15 n

