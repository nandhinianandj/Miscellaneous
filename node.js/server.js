var http = require("http");
var url = require("url");

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

function start(route,handle) {
  function onRequest(request,response) {
    var postData = "";
    var pathname = url.parse(request.url).pathname;
    print_word_on_console("Request recieved for " + pathname);
    route(handle,pathname,response,request);
  }

  http.createServer(onRequest).listen(8888);

  console.log("server started")
}
exports.start = start


