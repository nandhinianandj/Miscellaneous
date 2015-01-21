var moment = require('moment-timezone');
var mz = moment.tz._zones
function reverseLookupTZ(offset, cb) {
    for (var tz in mz) {
        if (offset in mz[tz].offsets){
            console.log(tz);
            cb(tz);
        }

    }
    cb(-1, offset);
}

function offsetSecs2tz (offsetSecs) {
    return new Promise(function (resolve, reject) {
        reverseLookupTZ(offsetSecs,
            function(err, res){
                if(err) {
                    reject(err);
                    }
                resolve(res);
        });
    });
}
var b = offsetSecs2tz(0);
b.then(function(val) {console.log(val);});
