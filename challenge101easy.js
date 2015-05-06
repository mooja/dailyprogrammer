function hasUniqueDigits(year) {
  var digitsset = new Set(year);
  return digitsset.size == year.length;
}

function numUniqueYears(lo, hi) {
  var counter = 0;
  for(var i = lo; i <= hi; i++) {
    if (hasUniqueDigits(i.toString())) {
      counter++;
    }
  }
  return counter;
}

console.log(hasUniqueDigits("2015"));
console.log(hasUniqueDigits("2002"));
console.log(numUniqueYears(1980, 1987));
