threes = cycle ["", "", "Fizz"]
fives = cycle ["","","","","Buzz"]

fizzbuzz = zipWith (++) threes fives

main = putStr (unlines fizzbuzz)
