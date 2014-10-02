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

pickRandom :: [String] -> String
pickRandom [strList] = strList !! getStdRandom (randomR (1, length strList))

--getRandomQuote str = pickRandom (str)
main = do
  contents <- readFile "/home/anand/workspace/github_stuff_private/wordpress_blog_posts/pages/quotes"
  let allQuotes = lines contents
  putStr allQuotes
  putStr (allQuotes !! 1)
  let sign = pickRandom allQuotes
  putStr (allQuotes !! 1)
