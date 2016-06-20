#!/usr/bin/env node

// Daily Programmer Challenge 243 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3uuhdk/20151130_challenge_243_easy_abundant_and/

// 20 June 2016

const _ = require("lodash");


let input = `111  112 220 69 134 85`;
main(input.trim().split(/\s+/).map(x => Number(x)));

function divisors(n) {
    let candidates = _.range(1, n+1);
    return candidates.filter(divCandidate => n % divCandidate === 0);
}

function deficiency(n) {
    return _.sum(divisors(n)) - 2*n;
}

function main(ns) {
    for (let n of ns) {
        let def = deficiency(n);
        if (def > 0) 
            console.log(n+' abundant by '+def);
        else if (def === 0)
            console.log(n+' ~~niether~~ deficient');
        else
            console.log(n+' deficient');
    }
}
