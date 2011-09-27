var fs = require('fs')
  ,sys = require('util');

fs.readFile('tone_data.txt',function(report){
  util.puts("oh, look the senti wordnet data:"+report);
});


