sol :: [[Int]]
sol = [ [ witness (build i j) | j <- [0..heightGame] ]
                              | i <- [0..heightGame] ]
  where
    build i j     = (i * heightRegion) + (i `div` heightRegion) + j
    witness       = (`mod` heightGame) . (+ 1)
    heightRegion  = 3
    heightGame    = heightRegion^2
