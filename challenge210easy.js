#!/usr/bin/env node

// input
var x = 100, y = 42;

// function to pad binary numbers to 32 bits
var zpad = (s, size) => {
    while(s.length < size)
      s = '0' + s;
    return s;
}

// string xor function
var sxor = (xs, ys) => {
   var result = [];
   for(var i in xs) 
       result.push(xs[i] == ys[i] ? '0' : '1');
   return result.join('');
}

// convert decimals to binary strings
var xbin = zpad(x.toString(2), 32);
var ybin = zpad(y.toString(2), 32);
var xor_bin = sxor(xbin, ybin);

// 0's in xored are compatible bits, 1's are opposites
var add = (a, b) => a + b;
var nbits_opposite = xor_bin.split('')
  .map(s => parseInt(s))
  .reduce(add, 0);
var nbits_compatible = 32 - nbits_opposite;
var percent_compatible = Math.floor((nbits_compatible / 32)*100)

// xoring '1'*32 with another number flips all the second's bits
var ones = '1'.repeat(32);
var x_opp = parseInt(sxor(xbin, ones), 2);
var y_opp = parseInt(sxor(ybin, ones), 2);

// may change the way we output later
var output = s => console.log(s);
output(`${x} and ${y} are ${percent_compatible}% compatible`);
output(`${x} should avoid ${x_opp}`);
output(`${y} should avoid ${y_opp}`);
