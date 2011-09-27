var http = require("http");
var response= http.response;

function response_say(word,response)
  {
    response.write(word);
  }

function print_word_on_webpage(say,value,request,response)
{
  console.log("Request received");
  response.writeHead(200,{"Content-Type":"text/plain"});

  say(value,response);
  response.end();
}

function print_word_on_console(word)
{
  console.log(word)
  }

function start() {
  function onRequest(request,response) {
  print_word_on_console("Request recieved");
  response.writeHead(200,{"Content-Type":"text/plain"});
  response_say("Hello, javascript",response);
  response.end()
  }

  http.createServer(onRequest).listen(8888);

  console.log("server started")
}
exports.start = start


