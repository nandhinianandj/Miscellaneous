import System.IO
import System.Random

--getLines = liftM lines . readFile

--pickRandom :: (Num (([a]->Int) ->[String] ->(Int,Int)))
pickRandom x = randomRIO (0,length x) >>= return .(x !!)

--getRandomQuote str = pickRandom (str)
main = do
  contents <- readFile "/home/anand/workspace/my_projects/Miscellaneous/Quotes.txt"
  let quotes = lines contents
  let sign = pickRandom quotes
  sign
