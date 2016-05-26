#!/usr/bin/env node

_ = require("underscore");

// input
var test_input = `
123
286
196196871
`


// memoize since it will be often twice with the same args
_.memoize(reversed_int);
function reversed_int(x) { 
    return Number(x.toString().split('').reverse().join(''));
}

function is_palindrome(x) { return  x === reversed_int(x); }

function get_palindromic(seed, steps_limit=1000) {
    let steps = 0, n = seed;
    while(!is_palindrome(n) && steps < steps_limit) {
        n = n + reversed_int(n);
        steps += 1;
    }

    if(steps >= steps_limit) n = -1; // Lychrel number
    return [n, steps];
}

function main(input) {
    let seeds = input.trim().split(/\s+/).map(Number);
    let output_lines = seeds.map(seed => {
        let [palindrome, steps] = get_palindromic(seed);
        if(palindrome == -1) 
            return `${seed} did not converge on a palindrome after ${steps} steps.`
        return `${seed} gets palindromic after ${steps} steps: ${palindrome}.`;
    });
    console.log(output_lines.join('\n'));
}

// see which numbers 1-1000 yield identical palindromes
function main_extra() {
    let pmap = {}; // palindrome map
    for(let n = 0; n < 1001; n += 1) {
        let [p, s] = get_palindromic(n);
        if(p !== -1)
            pmap[p] = (pmap[p] || []).concat(n);
    }

    let entries = Object.keys(pmap).map(k => [k, pmap[k]])
    entries.sort((a, b) => b[1].length - a[1].length);
    let lines = entries.slice(0, 10)
        .map(entry => `Palindrome: ${entry[0]}, seeds: ${entry[1].join(', ')}`);
    console.log(lines.join('\n'));
}

main(test_input);
console.log('------');
main_extra();
