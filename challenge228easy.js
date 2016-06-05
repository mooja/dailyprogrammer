#!/usr/bin/env node

// Daily Programmer Challenge 228 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3h9pde/20150817_challenge_228_easy_letters_in/

// 05 June 2016

function in_order(word) {
    for(let i=0; i < word.length-1; i++)
        if(word[i] > word[i+1])
            return false
    return true
}

function in_reversed_order(word) {
    return in_order(word.split('').reverse());
}

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', (line) => {
    word = line.trim()
    if (in_order(word)) 
        console.log(word, 'IN ORDER')
    else if (in_reversed_order(word))
        console.log(word, 'REVERSE ORDER');
    else
        console.log(word, 'NOT IN ORDER');
    
})
