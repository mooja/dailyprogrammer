#!/usr/bin/env node

// Daily Programmer Challenge 238 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3q9vpn/20151026_challenge_238_easy_consonants_and_vowels/

// 16 June 2016

const _ = require('lodash');
const readline = require('readline');

const consonants = 'bcdfghjklmnpqrstvwxyz';
const vowels = 'aeiou';

function choice(seq) {
    return seq[_.random(seq.length-1)];
}

function generate_word(blueprint) {
    let word = blueprint
        .split('')
        .map(ch => {
            let random_ch = null;
            if (ch.toLowerCase() === 'c')
                random_ch = choice(consonants);
            else
                random_ch = choice(vowels);
            if (ch === 'C' || ch === 'V')
                random_ch = random_ch.toUpperCase();
            return random_ch;
        })
        .join('');
    return word;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let lines = [];
rl.on('line', line => lines.push(line.trim()))
rl.on('close', () => {
    lines = lines
        .filter(line => /^[cv]+$/i.test(line));
    let words = lines.map(generate_word);
    for (let word of words)
        console.log(word);
});
