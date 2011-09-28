function start() {
  console.log("Request handler start was started");
  function sleep(milliSeconds) {
    var startTime = new Date().getTime();
    while (new Date().getTime() < startTime + milliSeconds);
  }
  sleep(10000);
  return "Hello from start"
}

function upload() {
  console.log("Request handler upload was started");
  return "Hello from upload"
}

exports.start = start;
exports.upload = upload;
