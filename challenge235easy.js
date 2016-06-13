#!/usr/bin/env node

// Daily Programmer Challenge 235 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3nkanm/20151005_challenge_235_easy_ruthaaron_pairs/

// 13 June 2016


function factorize(n) {
    let factors = [];
    for(let i = 2; i <= n; i++) {
        if (n % i === 0) {
            factors.push(i)
            while(n % i === 0) 
                n /= i;
        }
    }
    return factors;
}

function are_ruth_aaron_pairs(a, b) {
    let sum_a = factorize(a).reduce((x, y) => x + y);
    let sum_b = factorize(b).reduce((x, y) => x + y);
    return sum_a === sum_b;
}


const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});


let lines = [];
rl.on('line', line => lines.push(line.trim()))
rl.on('close', () => {
    for (let line of lines.slice(1)) {
        line = line.replace(/[\(\)]/g, '');
        let numbers = line.split(',').map(Number);
        let verdict = null;
        if (are_ruth_aaron_pairs(...numbers))
            verdict = 'VALID';
        else
            verdict = 'NOT VALID';
        console.log(`(${numbers[0]},${numbers[1]}) ${verdict}`);
    }
});
