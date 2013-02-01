-- Just code from the blog post http://stochastix.wordpress.com/2011/09/05/circular-convolution-in-haskell
--
--
circShiftR :: [a] -> [a]
circShiftR [] = []
circShiftR x = last x : init x

circShiftL :: [a] -> [a]
circShiftL [] = []
circShiftL xs = (tail xs) : [head xs]

--iterate :: (a -> a) -> a -> [a]
--iterate f x = x : iterate f (f x)
--
innerProd :: Num a => [a] -> [a] -> a
innerProd xs ys = sum(zipWith (*) xs ys)

circConv :: Num a => [a] -> [a] -> [a]
circConv xs ys = map (innerProd xs) ys
                 where
                  n = length xs
                  ys' = (circShiftR . reverse) ys
                  yss = take n (iterate circShiftR ys')

