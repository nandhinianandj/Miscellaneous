function getInfo(a, callback) {
    callback(null, a);
}
var a="test";
getInfo(a, function(a){debugger;console.log(a);});
