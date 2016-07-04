#!/usr/bin/env node

// Daily Programmer Challenge 254 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/45w6ad/20160216_challenge_254_easy_atbash_cipher/

// 03 July 2016


const alphabet = 'abcdefghijklmnopqrstuvwxyz';
const reverseAlphabet = alphabet
  .split('')
  .reverse()
  .join('');

let substitutions = new Map();
// lowercase mapping
alphabet.split('').forEach((ch, idx) => {
  substitutions.set(ch, reverseAlphabet[idx]);
});

// uppercase mapping
alphabet.split('').forEach((ch, idx) => {
  substitutions.set(
    ch.toUpperCase(), 
    reverseAlphabet[idx].toUpperCase()
  );
});

function encrypt(text) {
  let ciphertext = '';
  for(let ch of text) {
    if(substitutions.get(ch)) 
      ciphertext += substitutions.get(ch);
    else
      ciphertext += ch;
  }
  return ciphertext;
}

let input = `
foobar
wizard
/r/dailyprogrammer
gsrh rh zm vcznkov lu gsv zgyzhs xrksvi
upperCaseString
`;

input.trim().split('\n').forEach(line => {
  console.log(encrypt(line));
});
