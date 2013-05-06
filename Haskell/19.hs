import System.IO
import System.Directory
import Data.List
import System.Random

withFile' :: FilePath -> IOMode -> (Handle -> IO a) -> IO a
withFile' path mode f = do
  handle <- openFile path mode
  result <- f handle
  hClose handle
  return result

pickRandom :: Int -> IO Int
pickRandom x = getStdRandom (randomR (1,x))

--extractRandomLine :: (Int -> IO Int)=> [[Char]] -> [Char]
extractRandomLine f str = head (drop (f (length str)) str)

main = do
  quotes_handle <- openFile "../Quotes.txt" ReadMode
  sign_handle <- openFile "/home/anand/.signature" WriteMode

  contents <- hGetContents quotes_handle
  let quotes = lines contents
      numberedQuotes = zipWith (\n line -> show n ++ "-" ++ line) [0..] quotes
      no_of_quotes = length quotes
      rand_no = pickRandom no_of_quotes

  hClose quotes_handle
  hClose sign_handle














