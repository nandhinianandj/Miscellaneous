import System.IO
import System.Random
import Data.List

-- Copied from an answer in stackoverflow
splitByDelimiter :: Char -> String -> [String]
splitByDelimiter = unfoldr .splitSingle

splitSingle :: Char -> String -> Maybe (String, String)
splitSingle _ [] = Nothing
splitSingle delimiter xs =
  let (ys, zs) = break (== delimiter) xs in
  Just (ys, drop 1 zs)

--getLines = liftM lines . readFile

--pickRandom :: (Num (([a]->Int) ->[String] ->(Int,Int)))
pickRandom x = randomRIO (0,length x) >>= return .(x !!)

--getRandomQuote str = pickRandom (str)
main = do
  contents <- readFile "/home/anand/workspace/my_projects/Miscellaneous/Quotes.txt"
  let delimit = "~Aang Jie"
--  let quotes = splitByDelimiter delimit contents
  let quotes = lines contents
  let sign = pickRandom quotes
  sign
