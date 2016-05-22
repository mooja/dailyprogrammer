#!/usr/bin/env node

// Daily Programmer Challenge 214 Easy
//
// https://www.reddit.com/r/dailyprogrammer/comments/35l5eo/20150511_challenge_214_easy_calculating_the/
//
// 22 May 2016


var input_dataset = [5, 6, 11, 13, 19, 20, 25, 26, 28, 37]

var sum = list => list.reduce((a, b) => a + b, 0);

function std_dev(dataset) {
  var mean = sum(dataset) / dataset.length
  var squared_deviations = dataset.map(a => Math.pow((a - mean), 2));
  var variance = sum(squared_deviations) / dataset.length
  var std_dev = Math.sqrt(variance);
  return parseFloat(std_dev.toFixed(4));
}

console.log(std_dev(input_dataset));
