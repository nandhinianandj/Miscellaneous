var _ = require('lodash');

var run = function* () {
      console.log("Starting")
        var file = yield readFile("./async.js") // [1]
          console.log(file.toString())
}
var testgen = function* () {
    var a = [0, 2 , 3, 42];
    _.each(a, function(ea,i) {
                yield ;
                        });
}

var fib = function* fibGen () {
      var current = 0, next = 1, swap
        while (true) {
                swap = current, current = next
                    next = swap + next
                        yield current
                          }
}

console.log(testgen().next());
// console.log(fib().next());
// console.log(fib().next());
