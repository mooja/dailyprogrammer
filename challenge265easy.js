#!/usr/bin/env node

// Daily Programmer Challenge 265 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/4hhiu8/20160502_challenge_265_easy_permutations_and/

// 15 July 2016

"use strict;"

const _ = require("lodash");

fact = _.memoize(_fact);
function _fact(n) {
  if (n === 1)
    return 1;
  return n * _fact(n-1);
}

function* permutations(seq) {
  if (seq.length === 1)
    yield seq;
  for (let i=0; i < seq.length; i++) {
    let first = seq[i];
    let rest = [...seq.slice(0, i), ...seq.slice(i+1)];
    for (let sub_perm of permutations(rest))
      yield [first, ...sub_perm]
  }
}

function nthPermutation(n, seq) {
  let counter = 0;
  for (let perm of permutations(seq)) {
    if (counter === n-1)
      return perm;
    counter++;
  }
}

function* combinations(seq, r) {
  let seen = [];
  for (let perm of permutations(seq)) {
    let combination_candidate = perm.slice(0, r).sort();
    let has_been_seen = false;
    for (let seen_comb of seen)
      if (_.isEqual(combination_candidate, seen_comb))
        has_been_seen = true;
    if (has_been_seen)
      continue;
    seen.push(combination_candidate);
    yield combination_candidate;
  }
}

function nthCombination(n, seq, r) {
  let counter = 0;
  for (let comb of combinations(seq, r)) {
    if (counter === n-1)
      return comb;
    counter++;
  }
}

console.log(nthPermutation(3,    [0, 1, 2]));
console.log(nthPermutation(240,  [0, 1, 2, 3, 4, 5]));
console.log(nthPermutation(3240, [0, 1, 2, 3, 4, 5, 6]));
console.log(nthCombination(24,   [0, 1, 2, 3, 4, 5, 6, 7], 3));
console.log(nthCombination(112,  [0, 1, 2, 3, 4, 5, 6, 7, 8], 4));
