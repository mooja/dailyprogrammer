#!/usr/bin/env node

// Daily Programmer Challenge 207 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/307m27/20150325_challenge_207_intermediate/

// 15 May 2016


const readline = require('readline');
const rl = readline.createInterface(process.stdin, process.stdout);

const opposites = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'A', ' ': ' '}

rl.on('line', (line) => {
    line = line.replace(/\n$/, '');
    opp_line = line.split('')
       .map(s => opposites[s])
       .join('');
    console.log(line);
    console.log(opp_line);
});
