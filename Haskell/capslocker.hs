--import Control.Monad
--import Data.Char
--
--main = forever $ do
--    putStr "Give me some input:\n"
--    l <- getLine
--    putStrLn $ map toUpper l
import Data.Char
main = do
    contents <- getContents
    putStr (map toUpper contents)
