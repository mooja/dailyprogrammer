#!/usr/bin/env node

// Daily Programmer Challenge 276 Intermediate

// https://www.reddit.com/r/dailyprogrammer/comments/4tqy5c/20160720_challenge_276_intermediate_key_function/

// 05 August 2016


function key(elements, keys, func) {
  let uniqueKeys = [];
  for (let key of keys) 
    if (uniqueKeys.indexOf(key) === -1)
      uniqueKeys.push(key);

  let rvs = [];
  for (let key of uniqueKeys) {
    let keyElements = [];
    for(let i=0; i < elements.length; i++) 
      if(keys[i] === key) 
        keyElements.push(elements[i]);
    rvs.push(func(keyElements));
  }
  return rvs;
}

function histogram(values) {
  let uniqueKeys = [];
  for (let key of values) 
    if (uniqueKeys.indexOf(key) === -1)
      uniqueKeys.push(key);

  const count = x => x.length;
  const keyVals = key(values, values, count);

  let output = '';
  for (let i = 0; i < uniqueKeys.length; i++)
    output += `${uniqueKeys[i]} ${keyVals[i]}\n`;
  return output;
}

function groupedSum(records) {
  const keys = records.map(record => record[0]);
  const values = records.map(record => record[1]);

  let uniqueKeys = [];
  for (let key of keys) 
    if (uniqueKeys.indexOf(key) === -1)
      uniqueKeys.push(key);

  const keyVals = key(values, keys, sum);
  let output = '';
  for (let i = 0; i < uniqueKeys.length; i++)
    output += `${uniqueKeys[i]} ${keyVals[i]}\n`;
  return output;
}

function nub(records) {
  const keys = records.map(record => record[0]);
  const values = records.map(record => record[1]);

  let uniqueKeys = [];
  for (let key of keys) 
    if (uniqueKeys.indexOf(key) === -1)
      uniqueKeys.push(key);

  const func = elems => elems[0];
  const keyVals = key(values, keys, func);

  let output = '';
  for (let i = 0; i < uniqueKeys.length; i++)
    output += `${uniqueKeys[i]} ${keyVals[i]}\n`;
  return output;
}

function sum(elements) {
  return elements.reduce((a, b) => a + b);
}

function main() {
  // key() test
  const key_rv = key([3, 4, 5, 6], [2, 0, 1, 2], sum);
  console.log("key([3, 4, 5, 6], [2, 0, 1, 2]) returned: ", key_rv);

  // histogram() test
  const histogram_vals = '5 3 5 2 2 9 7 0 7 5 9 2 9 1 9 9 6 6 8 5 1 1 4 8 5 0 3 5 8 2 3 8 3 4 6 4 9 3 4 3 4 5 9 9 9 7 7 1 9 3 4 6 6 8 8 0 4 0 6 3 2 6 3 2 3 5 7 4 2 6 7 3 9 5 7 8 9 5 6 5 6 8 3 1 8 4 6 5 6 4 8 9 5 7 8 4 4 9 2 6 10'
    .split(' ')
    .map(x => Number(x));
  const histogram_rv = histogram(histogram_vals);
  console.log(histogram_rv);

  // grouped_sum test
  const grouped_sum_records = 'a 14,b 21,c 82,d 85,a 54,b 96,c 9 ,d 61,a 43,b 49,c 16,d 34,a 73,b 59,c 36,d 24,a 45,b 89,c 77,d 68'
    .split(',')
    .map(str => [str.split(' ')[0], Number(str.split(' ')[1])]);
  const grouped_sum_rv = groupedSum(grouped_sum_records);
  console.log(grouped_sum_rv);

  // nub test
  const nub_records = 'a 14,b 21,c 82,d 85,a 54,b 96,c 9 ,d 61,a 43,b 49,c 16,d 34,a 73,b 59,c 36,d 24,a 45,b 89,c 77,d 68'
    .split(',')
    .map(str => [str.split(' ')[0], Number(str.split(' ')[1])]);
  const nub_rv = nub(nub_records);
  console.log(nub_rv);

}

main();
