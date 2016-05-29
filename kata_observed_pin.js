#!/usr/bin/env node

// javascript kata
// kata url: http://www.codewars.com/kata/5263c6999e0f40dee200059d/train/javascript

let nmap = {
  '1': ['1', '2', '4'],
  '2': ['1', '2', '3', '5'],
  '3': ['2', '3', '6'],
  '4': ['1', '4', '5', '7'],
  '5': ['2', '4', '5', '6', '8'],
  '6': ['3', '5', '6', '9'],
  '7': ['4', '7', '8', '8'],
  '8': ['5', '7', '8', '9', '0'],
  '9': ['6', '8', '9'],
  '0': ['0', '8'],
}

function dotProduct(a, b) {
  if (a.length === 0) return b;
  if (b.length === 0) return a;

  let result = [];
  for(let a_idx = 0; a_idx < a.length; a_idx++) 
    for(let b_idx = 0; b_idx < b.length; b_idx++) 
      result.push(a[a_idx] + b[b_idx]);
  return result

}

function set(arr) {
  let result = [];
  for(let i = 0; i < arr.length; i++)
    if (result.indexOf(arr[i]) === -1) 
      result.push(arr[i]);
  return result;
}

function getPINs(observed) {
  let possibilities = observed
    .split('')
    .map(x => nmap[x]);
  return set(possibilities.reduce(dotProduct, []));
}

console.log(getPINs('0'));
