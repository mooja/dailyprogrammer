#!/usr/bin/env node

// Daily Programmer Challenge 265 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/4hhiu8/20160502_challenge_265_easy_permutations_and/

// 15 July 2016

"use strict;"

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

// TODO
function* combinations(seq) {
}

console.log(nthPermutation(3, [0, 1, 2]));
console.log(nthPermutation(240, [0, 1, 2, 3, 4, 5]));
console.log(nthPermutation(3240, [0, 1, 2, 3, 4, 5, 6]));
