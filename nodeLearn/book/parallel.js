
function parallel(tasksArr, finalcb){
    var allResults = {};
    var completed = 0;
    tasksArr.forEach(function(task, i) {
        tasksArr[i](function(err, result) {
            console.log("callback for function:" + i);
            console.log(allResults);
            if(err){
                finalcb(err, allResults);
                return;
            }
            else {
                if(completed === tasksArr.length) {
                    finalcb(err, allResults);
                }
                else{
                    allResults[i] = result;
                    completed++;
                }
            }
        });
    });
}


// parallel([
//     function(callback){
//         setTimeout(function(){
//                 callback(null, 'one');
//             }, 200);
//         },
//     function(callback){
//         setTimeout(function(){
//                 callback(null, 'two');
//             }, 100);
//         }
//     ],
//     // optional callback
//     function(err, results){
//         console.log(results);
//         // the results array will equal ['one','two'] even though
//         // the second function had a shorter timeout.
//     });

