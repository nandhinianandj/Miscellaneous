import System.IO
import System.Directory
import Data.List

withFile' :: FilePath -> IOMode -> (Handle -> IO a) -> IO a
withFile' path mode f = do
  handle <- openFile path mode
  result <- f handle
  hClose handle
  return result

main = do
  handle <- openFile "../Quotes.txt" ReadMode
  handle <- openFile "/home/anand/.signature" WriteMode

  contents <- hGetContents handle
  let quotes = lines contents
      numberedQuotes = zipWith (\n line -> show n ++ "-" ++ line) [0..] quotes
      no_of_quotes = length quotes

  putStr $ unlines quotes
  hClose handle














