
var number = 42
var opposite = true
var string = "the answer is {number}"
var regex = /answer is (\d+)/

# Functions:
var square = do |x| x * x

# Arrays:
var list = [1, 2, 3, 4, 5]

# Objects:
var math =
    square: square
        cube: do |x| x * math.square(x)
            rand: do Math.random

# Array comprehensions:
var cubes = (math.cube num for num in list)

# Implicit calling:
math.rand.toFixed 2
