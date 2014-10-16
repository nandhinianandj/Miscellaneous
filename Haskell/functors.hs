--main = do
--        line <- getLine
--        let line' = reverse line
--        putStrLn $ "You said " ++ line' ++ " backwards!"
--        putStrLn $ "Yes, you said" ++ line' ++ "backwards"

-- main = do
--         line <- fmap reverse getLine
--         putStrLn $ "You said " ++ line ++ " backwards!"
--         putStrLn $ "Yes, you said" ++ line ++ "backwards"
--import Data.Char
--import Data.List
--
--main = do line <- fmap (intersperse '-' . reverse . map toUpper) getLine
--          putStrLn line
--data Test a = Test a
--
--instance Functor Test where
--    fmap f (Just x) = Just (f x)
--    fmap f Nothing = Nothing
--

data CMaybe a = CNothing | CJust Int a deriving (Show)

instance Functor CMaybe where
    fmap f CNothing = CNothing
    fmap f (CJust counter x) = CJust (counter+1) (f x)
