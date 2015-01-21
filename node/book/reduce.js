var intArray = [1, 2, 3, 4, 5];
var err = null;

function reduce(init, arr, func, ficb) {
    var accum = init;
    var idx = 0;
    var localCb = function(err, result) {
        if (err)
            throw(err);
        else {
            accum = result;
            idx +=1;
            if (idx >= arr.length) {
                ficb(null, accum);
            }
            else
                runFunc();
        }
    };
    var runFunc = function (){
        func(accum, arr[idx], localCb);
    }
    runFunc();
}


// reduce(4, intArray,
//         function(elem1, elem2,  cb) {
//             setTimeout( function() {
//                 cb(err, elem1+elem2);
//         }, 400);},
//         finalCbReduce);
