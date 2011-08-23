import System.IO
import System.Random

getLines = liftM lines . readFile

pickRandom :: x -> IO Int
pickRandom x = getStdRandom (randomR (1,x))

main = do
  contents <- readFile "/home/anand/workspace/my_projects/Miscellaneous/Quotes.txt"
  mapM_ putStrLn contents
