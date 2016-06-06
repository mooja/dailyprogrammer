#!/usr/bin/env node

// Daily Programmer Challenge 229 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3i99w8/20150824_challenge_229_easy_the_dottie_number/

// 06 June 2016

const SIGMA = 0.000001; // significant figures

function* cos_generator(seed) {
    while (true) {
        seed = Math.cos(seed);
        yield seed;
    }
}

function dottie_number(seed) {
    let previous = seed;
    for (let n of cos_generator(seed)) {
        if (Math.abs(n - previous) < SIGMA)
            return n;
        previous = n;
    }
}

console.log(dottie_number(1000000));
