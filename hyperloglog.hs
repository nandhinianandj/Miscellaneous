import Data.Hashable

getInp    ::  IO Char

putInp    ::  Char -> IO ()

main      :: IO ()
main      = do c <- getInp
                putInp c
