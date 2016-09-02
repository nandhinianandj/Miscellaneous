bruteCollatz :: Integer -> [Integer]
bruteCollatz 1 = []
bruteCollatz n
    | odd n = 3*n+1:bruteCollatz(3*n+1)
    | even n = div n 2:bruteCollatz(div n 2)

chains = [bruteCollatz x | x <- [1..]]

longest' (max_i, max_l) =
  let l = head $ dropWhile (\(i,l) -> l <= max_l) $ zip [max_i..] $ map length $ chains' max_i
  in l:longest' l



-- memoizedCollatz :: Integer -> [Integer]
-- memoizedCollatz = memoize col where
--   col 1 = []
--   col n
--     | odd n = 3*n+1:memoizedCollatz(3*n+1)
--     | even n = div n 2:memoizedCollatz(div n 2)

memoizedCollatz :: Integer -> [Integer]
memoizedCollatz = memoFix col where
      col _ 1 = []
      col f n
	| odd n = 3*n+1:f $! 3*n+1
	| even n = div n 2:f $! div n 2
