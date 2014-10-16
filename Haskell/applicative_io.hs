import Control.Applicative

-- myAction = do
--     a <- getLine
--     b <- getLine
--     return $ a ++ b
myAction :: IO String
myAction = (++) <$> getLine <*> getLine

sequenceA :: (Applicative f) => [f a] -> f [a]
sequenceA [] = pure []
sequenceA (x:xs) = (:) <$> X <*> sequenceA xs

main = myAction
