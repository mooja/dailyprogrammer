#!/usr/bin/env node

// Daily Programmer Challenge 236 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3ofsyb/20151012_challenge_236_easy_random_bag_system/

// 14 June 2016

var _ = require("lodash");

function randomBag(seq) {
    return _.shuffle(seq);
}

function* tetronimo_gen(npieces=50) {
    let i = 0;
    let bag = randomBag('OISZLJT'.split(''));
    while (i < npieces) {
        yield bag.pop();
        i++;
        if (bag.length === 0)
            bag = randomBag('OISZLJT'.split(''));
    }
}

let output = [];
for (let piece of tetronimo_gen(50))
    output.push(piece)
console.log(output.join(''));
