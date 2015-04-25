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

// eachSeries(array, setTimeOut(
//             function(a, cb) {
//                 console.log("processing element:", a);
//                 console.log(a);
//                 cb();
// },3000), finalCb);

// eachSeries(null, function(a, cb) {
//                     console.log("procesing elem", a);
//                     console.log(a);
//                     cb();
//  }, finalCb);
