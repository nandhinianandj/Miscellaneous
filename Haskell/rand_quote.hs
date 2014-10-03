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
pickRandom [strList] = do
    index <- getStdRandom (randomR (0, length strList))
    putStr index
    strList !! fromIntegral index

main = do
  contents <- readFile "/home/anand/workspace/github_stuff_private/wordpress_blog_posts/pages/quotes"
  let allQuotes = lines contents
  let sign = pickRandom allQuotes
  putStr (sign)
