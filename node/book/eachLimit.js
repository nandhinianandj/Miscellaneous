
var finalCbMap = function(err, results){
    if (!err)
        console.log("final callback:", results);
    else
        console.log(err);
};

function eachLimit(arr, limit, func, ficb) {
    var completed = 0;
    var i = 0;
    cb = function(err) {
        if (!err)
            completed +=1;
    };
    while(i!= limit){
        func(arr[i], cb);
        i++;
    }
    if (completed === limit) {
        ficb();
    }
}

// eachLimit(array, 2,
//         function(a, cb)  {
//                             console.log(a);
//                             cb();
// }, finalCb) ;
//
