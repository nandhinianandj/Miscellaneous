co(function* () {
      var result = yield Promise.resolve(true);
        return result;
}).then(function (value) {
  console.log(value);
}, function (err) {
      console.error(err.stack);
});

var fn = co.wrap(function* (val) {
      return yield Promise.resolve(val);
});

fn(true).then(function (val) {

});
