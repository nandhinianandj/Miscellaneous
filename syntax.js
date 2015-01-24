function each1(arr, func, ficb) {
    var completed = 0;
    var i = 0;
    cb = function(err) {
        if (!err)
            completed +=1;
    };
    while(i!= arr.length){
        func(arr[i], cb);
        i++;
    }
    if (completed === arr.length) {
        ficb();
    }
}

var array = ["test1", "teost3", "stest4" , "oeuo", "oeuo", "ouoelg" ];
var finalCb = function(){console.log("final callback");};
// each1(array,
//         function(a, cb)  {
//                             console.log(a);
//                             cb();
// }, finalCb) ;

function eachSeries(arr, func, globalCb){
    var completed = 0;
    var localCb = function(err) {
            if(err) {
                console.log("error: ", err);
                globalCb(err);
                globalCb = function () {console.log("error");};
            }
            else {
                completed += 1;
                if (completed >= arr.length) {
                    globalCb();
                }
                else{
                    runFunc(arr[completed], localCb);
                }
            }
    };
    var runFunc = function () {
            func(arr[completed], localCb);
    }
    runFunc();
}

// eachSeries(array,
//             function(a, cb) {
//                 console.log("processing element:", a);
//                 console.log(a);
//                 cb();
// }, finalCb);

// eachSeries(null, function(a, cb) {
//                     console.log("procesing elem", a);
//                     console.log(a);
//                     cb();
//  }, finalCb);


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

var finalCbMap = function(err, results){
    if (!err)
        console.log("final callback:", results);
    else
        console.log(err);
};

function map(arr, func, ficb) {
    var completed = 0;
    var i = 0;
    var err = null;
    var newArr = [];
    cb = function(err, a) {
        if (!err)
            completed +=1;
            a;
    };
    while(i!= arr.length){
        newArr.push(func(arr[i], cb));
        i++;

    }
    ficb(err, newArr);
    //return results;
}

map(array,
    function(a, cb)  {try {
                        return a;
    } catch(e) {
        }

}, finalCbMap);

// Infinite fibonacci generator
// Generators
//
function* fibGen () {
  var current = 0, next = 1, swap
  while (true) {
    swap = current, current = next
    next = swap + next
    yield current
  }
}
