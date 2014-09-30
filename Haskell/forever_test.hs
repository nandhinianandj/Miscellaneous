import Control.Monad
import Data.Char
main = forever $ do
    putStr "Give mo some candy "
    l <- getLine
    putStrLn $ map toUpper l
