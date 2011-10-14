lastButOne :: [a] -> a
lastButOne [] = error "empty list"
lastButOne [_] = error "list size is one"
lastButOne x = head (drop (length x -2) x)
