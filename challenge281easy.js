#!/usr/bin/env node

// Daily Programmer Challenge 281 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/504rdh/20160829_challenge_281_easy_something_about_bases/

// 01 September 2016


function highestBase(num) {
  const radixes = '123456789abcdefghijklmnopqrstuvwxyz';
  const radixIdxs = num.split('').map(x => radixes.indexOf(x));
  const highestRadix = Math.max.apply(null, radixIdxs) + 1;
  return highestRadix + 1;
}

const inputs = ['1', '21', 'ab3', 'ff'];
inputs.forEach(x => {
  const base = highestBase(x);
  const asDecimal = parseInt(x, base);
  console.log(base.toString() + ' => ' + asDecimal.toString());
});
