function init() {
    var app = {};
    root = this;

    var finalCbMap = function(err, results){
    if (!err)
        console.log("final callback:", results);
    else
        console.log(err);
    }

    var finalCbReduce = function(err, results){
    if (!err)
        console.log("final callback:", results);
    else
        console.log(err);
    }

    var only_once = function(fn) {
        var called = false;
        return function() {
            if(called) throw new Error("Callback was already called");
            called = true;
            fn.apply(root, arguments);
        }
    }
    // _.each(modules, function (m) {
    //     app[m] = require('./' + m);
    // });
    

    return app;
}

module.exports = init;
