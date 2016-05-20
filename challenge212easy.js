#!/usr/bin/env node

// Daily Programmer Challenge 212 Easy
//
// https://www.reddit.com/r/dailyprogrammer/comments/341c03/20150427_challenge_212_easy_r%C3%B6varspr%C3%A5ket/
//
// 19 May 2016


var consonants = 'bcdfghjklmnpqrstvwxyz';
var consonants_re = new RegExp("([" + consonants + "])", 'ig');
var decode_re = new RegExp("([" + consonants + "])o\\1", 'ig');

var encode = t => t.replace(consonants_re, '$1o$1');
var decode = t => t.replace(decode_re, '$1');

console.log(encode('Hello World!'));
console.log(decode(encode('Hello World!')));
