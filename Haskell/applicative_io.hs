import Control.Applicative

-- myAction = do
--     a <- getLine
--     b <- getLine
--     return $ a ++ b
myAction :: IO String
myAction = (++) <$> getLine <*> getLine

main = myAction
