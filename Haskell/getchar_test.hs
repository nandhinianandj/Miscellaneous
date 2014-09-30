import Control.Monad
main = do
    c <- getChar
    when (c /= ' ') $ do
        putChar c
        main
--main = do
--    c <- getChar
--    if c /= ' '
--        then do
--            putChar c
--            main
--        else return()
