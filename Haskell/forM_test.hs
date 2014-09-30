import Control.Monad

main = do
    colors <- forM [1,2,3,5] (\a -> do
        putStrLn $ "Which color do you associate with number " ++ show a ++ "?"
        color <- getLine
        return color)
    putStrLn "The colors you chose are :"
    mapM_ putStrLn colors


