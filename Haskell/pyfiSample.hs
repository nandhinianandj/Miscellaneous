import Python

square::Int -> IO Int
square = defVV "export = lambda x:x * x"

main = do
    x <- square 7
    print x
