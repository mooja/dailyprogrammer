#!/usr/bin/env node

// Daily Programmer Challenge 232 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3kx6oh/20150914_challenge_232_easy_palindromes/

// 08 June 2016

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function isPalindrome(s) {
  let letters = s
    .replace(/\W/g, '')
    .toLowerCase()
  let reversed_letters = letters
    .split('')
    .reverse()
    .join('');
  return letters === reversed_letters;
}

let lines = [];
rl.on('line', line => lines.push(line));
rl.on('close', () => {
  let text = lines.join('\n');
  if (isPalindrome(text))
    console.log('Palindrome');
  else
    console.log('Not a palindrome');
})
