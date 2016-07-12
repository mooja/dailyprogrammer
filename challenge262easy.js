#!/usr/bin/env node

// Daily Programmer Challenge 262 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/4eaeff/20160411_challenge_262_easy_maybenumeric/

// 12 July 2016

function isNumeric(s) {
  numberRe = /^\-?(\d+)?(\.\d+)?(e-?\d+)?$/;
  return numberRe.test(s.trim());
}

function main() {
  const inputs = [
    '123',
    '44.234',
    '0x123',
    '.2345',
    '3.32e10',
    '2.0e-10',
    '0',
    '-100',
    '1234.234.234'
  ];
  inputs.forEach(s => {
    const verdict = isNumeric(s) ? '(number)' : '(string)';
    console.log(s, verdict);
  });
}

main();
