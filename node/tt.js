function* genFn() {
    console.log("look ma i was suspended");
}

var g = genFn()
setTimeout(function() {
    g.next()
},2000);
