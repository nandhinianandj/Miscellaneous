import System.IO
import System.Random

getLines = liftM lines . readFile
main = do
  contents <- readFile "/home/anand/workspace/my_projects/Miscellaneous/Quotes.txt"
  mapM_ putStrLn contents
