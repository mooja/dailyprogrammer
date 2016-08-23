#!/usr/bin/env node

// Daily Programmer Challenge 280 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/4z04vj/20160822_challenge_280_easy_0_to_100_real_quick/

// 23 August 2016


function rightHandTotal(fingers) {
  // convert string to an array of ints
  fingers = fingers.split('')
    .map(x => Number(x));

  let total =  0;
  // thumb counts as five
  if (fingers[0])
    total += 5;

  // add sum of the four other
  total += fingers
    .slice(1) 
    .reduce((a, b) => a + b); 

  return total;
}


function leftHandTotal(fingers) {
  fingers = fingers.split('')
    .map(x => Number(x));

  let total = 0;

  if(fingers[4])
    total += 50;

  total += fingers.slice(0, 4)
    .map(x => x*10)
    .reduce((a, b) => a + b);
  return total;
}


function parseHand(fingers) {
  const leftHandFingers = fingers.slice(0, 5);
  const rightHandfingers = fingers.slice(5); 
  return leftHandTotal(leftHandFingers) + rightHandTotal(rightHandfingers);
}


function isValid(fingers) {
  const leftHandFour = fingers
    .slice(0, 4);
  const rightHandFour = fingers
    .slice(6);

  if (!leftHandFour.match(/^0*1*$/))
    return false;
  if (!rightHandFour.match(/^1*0*$/))
    return false;
  return true;
}


console.log(parseHand('0111011100'), isValid('0111011100'));
console.log(parseHand('1010010000'), isValid('1010010000'));
console.log(parseHand('0011101110'), isValid('0011101110'));
console.log(parseHand('0000110000'), isValid('0000110000'));
