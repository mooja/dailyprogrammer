#!/usr/bin/env node

// Daily Programmer Challenge 275 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/4savyr/20160711_challenge_275_easy_splurthian_chemistry/

// 27 July 2016


function followsRules(element, sym) {
  if (sym.length !== 2)
    return false;

  const regex = new RegExp(String.raw`^\w*${sym[0]}\w*${sym[1]}\w*$`, 'i');
  if (!regex.test(element))
    return false;

  return true;
}


console.log(followsRules('Spenglerium', 'Ee'), true)
console.log(followsRules('Zeddemorium', 'Zr'), true)
console.log(followsRules('Venkmine', 'Kn'), true)
console.log(followsRules('Stantzon', 'Zt'), false)
console.log(followsRules('Melintzum', 'Nn'), false)
console.log(followsRules('Tullium', 'Ty'), false)
