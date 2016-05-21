#!/usr/bin/env node

// Daily Programmer Challenge 213 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/34rxkc/20150504_challenge_213_easy_pronouncing_hex/

// 21 May 2016


var lower_byte_names = {
  0x0: 'bitey',
  0x1: 'one',
  0x2: 'two',
  0x3: 'three',
  0x4: 'four',
  0x5: 'five',
  0x6: 'six',
  0x7: 'seven',
  0x8: 'eight',
  0x9: 'nine',
  0xA: 'ay',
  0xB: 'bee',
  0xC: 'cee',
  0xD: 'dee',
  0xE: 'eee',
  0xF: 'eff',
}

var upper_byte_names = {
  0x0: '',
  0x1: 'eleventy',
  0x2: 'twenty',
  0x3: 'thirty',
  0x4: 'fourty',
  0x5: 'fifty',
  0x6: 'sixty',
  0x7: 'seventy',
  0x8: 'eightty',
  0x9: 'ninety',
  0xA: 'atta',
  0xB: 'bibbity',
  0xC: 'city',
  0xD: 'dickety',
  0xE: 'ebbity',
  0xF: 'fleventy',
}

var div = (x, y) => Math.floor(x / y);

// humanizes numbers 0-15
function humanize_byte(n) {
  var words = [];
  var uppername = upper_byte_names[div(n, 0x10)];
  var lowername = lower_byte_names[n % 16];

  if(uppername)
    words.push(uppername+'-'+lowername);
  else
    words.push(lowername)

  return words.join(' ');
}

// humanizes number 0-255
function humanize_hex(n) {
  var result = [];

  var first_byte = div(n, 0x0100);
  if (first_byte > 0) {
    var fb_text = humanize_byte(first_byte);
    result.push(fb_text);

    var endswith_bitey = fb_text.slice(-6) == '-bitey';
    if(!(endswith_bitey))
      result.push('bitey');
  }

  var second_byte = n % 0x0100;
  var sb_text = humanize_byte(second_byte);
  result.push(sb_text);
  return result.join(' ');
}

console.log(humanize_hex(0xBBBB));
console.log(humanize_hex(0xF5));
console.log(humanize_hex(0xB3));
console.log(humanize_hex(0xE4));
console.log(humanize_hex(0xBBBB));
console.log(humanize_hex(0xA0C9));
