#!/usr/bin/env node

// Daily Programmer Challenge 208 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/30ubcl/20150330_challenge_208_easy_culling_numbers/

// 16 May 2016

const readline = require('readline');
const rl = readline.createInterface(process.stdin, process.stdout);

rl.on('line', line => {
    var nums = line.replace(/\n$/, '').split(' ');
    var culled_nums = [];
    var visited = {};
    nums.forEach(n => {
        if(!(n in visited)) {
            culled_nums.push(n);
            visited[n] = true;
        }
    });
    console.log(culled_nums.join(' '));
});
