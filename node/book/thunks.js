
var Thunk = require('../thunks.js')();
var fs = require('fs');

var size = Thunk.thunkify(fs.stat);


// generator
// Thunk(function* () {
//
//   // sequential
//     console.log(yield size('.gitignore'));
//       console.log(yield size('thunks.js'));
//         console.log(yield size('package.json'));
//
//         })(function* (error, res) {
//           //parallel
//             console.log(yield [size('.gitignore'), size('thunks.js'), size('package.json')]);
//             })();
//
