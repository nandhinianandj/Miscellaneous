def whileLoop {
    var i = 1
    while(i <= 3) {
        println(i)
        i += 1
        }
    }

// whileLoop

def forLoop {
    println("for loop in java style iteration")
    for(i <- 0 until args.length) {
        println(args(i))
        }
    }
//forLoop


def rubyStyleForLoop {
    println("for loop using Ruby-Style iteration")
    args.foreach { arg =>
        println(arg)
        }
    }

// rubyStyleForLoop

// ranges
val range = 0 until 10 // exclusive
val range2 = 0 to 10 // inclusive

val range1 = (0 to 10) by 2
val range3 = (10 to 0) by -1
val charrange = 'a' to 'e'

//tuples
val person = ("Elvis", "Presley")
println(person._1)
println(person._2)

//Classes
class Person(firstName: String, lastName: String)
val gump = new Person("Forrest", "Gump")

class Compass {

    val directions = List("north", "south", "east", "west")
    var bearing = 0
    print("Initial bearing:")
    println(directions)

    def direction() = directions(bearing)

    def inform(turnDirection: String) {
        println("Turning" + turnDirection + ". Now bearing " + directions)
        }

    def turnRight() {
        bearing = (bearing + 1) % directions.size
        inform("right")
        }

    def turnLeft() {
        bearing = (bearing + (directions.size - 1)) % directions.size
        inform("left")
        }
    }

val myCompass = new Compass
myCompass.turnRight
myCompass.turnRight

myCompass.turnLeft
myCompass.turnLeft
myCompass.turnLeft





