mean :: Double -> Double -> Double
mean n m = go 0 0 n
    where 
        go :: Double -> Int -> Double -> Double
        go s|x|x > m = s/fromIntegral |
            |otherwise = go (s +x)(l+1)(x+1)


geom_mean :: Double -> Double -> Double
geom_mean n m = go 0 0 n
    where 
        go :: Double -> Int -> Double -> Double
        go s|x|x > m = s/fromIntegral |
            |otherwise = go (s +x)(l+1)(x+1)
main = do 
    [d] <- map read `fmap` getArgs
    printf "%f\n" mean (1 d)
