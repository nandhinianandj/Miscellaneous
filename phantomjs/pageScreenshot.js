var page = require('webpage').create();
page.open('http://facedetect.aang.in', function() {
  page.render('facedetectIndex.png');
  phantom.exit();
});
