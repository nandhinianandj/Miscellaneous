import Data.List
data Int = -2147483648 | -2147483647 | .... | -1 | 0 |1 | 2 | ... | 2147483647
data Point = Int Int
data LineSegment = Point Point
data Lines = take Point
data Degree = 0 | 1 | 2 | ... | 360
data Circle = Point Line

-- Add restriced line segment for capturing the circle constraint
-- Add constraint for right-angle/90 degrees
