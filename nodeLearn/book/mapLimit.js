var util = require('./util.js')
function map(arr, func, util.finalCbMap) {
    var completed = 0;
    var i = 0;
    var err = null;
    var newArr = [];
    cb = function(err, a) {
        if (!err)
            completed +=1;
            newArr.push(a);
    };
    while(i!= arr.length){
        func(arr[i],cb);
        i++;

    }
    ficb(err, newArr);
    //return results;
}
//map(array, function(a, cb) {a = a + "//";cb(null, a); }, finalCbMap);
