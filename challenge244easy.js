#!/usr/bin/env node

// Daily Programmer Challenge 244 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3wdm0w/20151209_challenge_244_easyer_array_language_part/

// 21 June 2016


function ForkString(f_name, g_name, h_name) {
    return `${g_name}(${f_name}(y, x), ${h_name}(y, x))`;
}

function ForkFactory(f, g, h) {
    let composition = (y, x) => g(f(y,x), h(y, x));
    return composition;
}

function sum(arg, y=0) {
    return arg.reduce((a, b) => a + b);
}

function divide(a, b) { 
    return (a / b);
}

function count(arg, x=0) {
   return arg.length;
}

const mean = ForkFactory(sum, divide, count);
console.log(ForkString('sum', 'divide', 'count'));
console.log(mean([1, 2, 3, 4, 5, 6, 7]));
