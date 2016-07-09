#!/usr/bin/env node

// Daily Programmer Challenge 259 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/4bc3el/20160321_challenge_259_easy_clarence_the_slow/<F8>

// 09 July 2016


// Build key coordinates
let key_coordinates = new Map();
for (let i = 0; i < 9; i++) {
  let row = Math.floor(i / 3);
  let col = i % 3;
  key_coordinates.set(i+1, [row, col]);
}
key_coordinates.set('.', [3, 0]);
key_coordinates.set(0, [3, 1]);

const keyDistance = distance.bind(null, key_coordinates);
function distance(coordinates, digit1, digit2) {
  const [x1, y1] = coordinates.get(digit1);
  const [x2, y2] = coordinates.get(digit2);
  return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2))
}

function ipTypingDistance(ipAddr) {
  // parse keys
  const keys = ipAddr.split('')
    .map(k => k === '.' ? k : Number(k));

  // calculate distances
  const distances = [];
  for (let i = 0; i < keys.length-1; i++)
    distances.push(keyDistance(keys[i], keys[i+1]));

  return distances
    .reduce((a, b) => a + b) // sum
    .toFixed(2); // round to 2 decimals
}

console.log(ipTypingDistance('219.45.143.143'));
