#!/usr/bin/env node

// Daily Programmer Challenge 252 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/43ouxy/20160201_challenge_252_easy_sailors_and_monkeys/

// 30 June 2016

function satisfies(sailors, nuts) {
    for (let i=0; i<sailors; i++) {
      if ((nuts % sailors) !== 1)
        return false
      nuts = nuts - Math.floor(nuts / sailors) - 1;
    }
    return (nuts % sailors) === 0
}

function findPileSize(nsailors) {
  for (let pileSize = 1; ; pileSize++) {
    if (satisfies(nsailors, pileSize))
        return pileSize;
  }
}

console.log(findPileSize(5));
