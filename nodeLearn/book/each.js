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
