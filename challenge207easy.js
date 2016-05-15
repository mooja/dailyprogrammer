#!/usr/bin/env node

// Daily Programmer Challenge 207 Easy
//
// https://www.reddit.com/r/dailyprogrammer/comments/2zyipu/20150323_challenge_207_easy_bioinformatics_1_dna/
//
// 15 May 2016


const readline = require('readline');
const rl = readline.createInterface(process.stdin, process.stdout);

var opposite = (ch) => {
    const opposites = {
        ' ': ' ',
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    };
    return opposites[ch];
};

rl.on('line', (line) => {
    line = line.replace(/\n$/, '');
    opp_line = line.split('').map(opposite).join('');
    console.log(line);
    console.log(opp_line);
});
