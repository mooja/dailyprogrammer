#!/usr/bin/env node

// Daily Programmer Challenge 237 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3pcb3i/20151019_challenge_237_easy_broken_keyboard/

// 15 June 2016


var fs = require('fs');
var _ = require('lodash');

function find_words(letters) {
    fs.readFile('enable1.txt', 'utf8', (err, data) => {
        if (err) throw err;
        let words = data.split(/\s+/);
        found_words = words.filter(w => {
            for(let ch of w)
                if (!letters.includes(ch))
                    return false;
            return true;
        });
        let biggest_word = found_words.reduce((a, b) => {
            if (a.length >= b.length)
                return a;
            return b;
        });
        console.log(letters, ' = ', biggest_word);
    });
}

var chunks = [];
process.stdin.setEncoding('utf8');
process.stdin.on('readable', () => {
    let chunk = process.stdin.read();
    if (chunk !== null)
        chunks.push(chunk);
});

process.stdin.on('end', () => {
    let data = chunks.join('');
    let lines = data.split('\n').filter(l => /[a-z]+/.test(l));
    for (let line of lines)
        find_words(line.trim());
});
