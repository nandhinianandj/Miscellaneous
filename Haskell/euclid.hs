import Data.List
data Int = -2147483648 | -2147483647 | .... | -1 | 0 |1 | 2 | ... | 2147483647
data Point = Int Int
data Line = Point Point
data Lines = take Line
data Degree = 0 | 1 | 2 | ... | 360
data Circle = Point Line
