import System.IO
import System.Random
main = do 
  contents <- readFile "/home/anand/workspace/my_projects/Miscellaneous/Quotes.txt"
  let Quotes = split "~Aang Jie" contents
  writeFile "/home/anand/.signature" rand_quote
