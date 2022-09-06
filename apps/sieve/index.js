function notDivide(a) {
  return function (b) {
    return b % a > 0;
  };
}

function _sieve(xs) {
  if (!xs || xs.length <= 1) {
    return xs;
  }
  var p = xs[0],
      ys = xs.filter(notDivide(p));

  return [p].concat(_sieve(ys));
}

function sieve(limit) {
  var sqrt = Math.floor(Math.sqrt(limit)),
      xs = [],
      i = 3,
      step = 2;

  while (i <= limit) {
    xs.push(i);
    i = i + step;
  }

  return _sieve(xs);
}

console.log(sieve(1000));
