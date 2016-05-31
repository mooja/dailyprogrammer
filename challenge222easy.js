#!/usr/bin/env node

// Daily Programmer Challenge 222 Easy
//
// https://www.reddit.com/r/dailyprogrammer/comments/3c9a9h/20150706_challenge_222_easy_balancing_words/
//
// 30 May 2016

_ = require("underscore")

// input
const input_data = `
STEAD
CONSUBSTANTIATION
WRONGHEADED
UNINTELLIGIBILITY
SUPERGLUE
`;

// helpers
let alphabet_pos = x => 1 + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.indexOf(x);
Array.prototype.sum = function() {
    return this.reduce((a, b) => a + b, 0);
}

function get_weight(word) {
    let weight_from_right = (ch, idx) =>
        (word.length - idx) * alphabet_pos(ch);
    return word
        .split('')
        .map((ch, idx) => weight_from_right(ch, idx))
        .sum();
}

// weight of 0 means balanced
function get_balanced_weight(word, pos) {
    let weight_from_position = (ch, idx) =>
        (pos - idx) * alphabet_pos(ch)
    return word
        .split('')
        .map((ch, idx) => weight_from_position(ch, idx))
        .sum();
}

function find_balance_pos(word) {
    for(let i = 0; i < word.length; i++)
        if (get_balanced_weight(word, i) === 0) return i;
    return -1;
}

function main(data) {
    let words = data.trim().split(/\s+/);
    words.forEach(word => {
        let balance_pos = find_balance_pos(word);
        if (balance_pos === -1)
            console.log(`${word} DOES NOT BALANCE`);
        else {
            let left_side = word.slice(0, balance_pos);
            let right_side = word.slice(balance_pos+1);
            let side_weight = get_weight(left_side);
            console.log([
                left_side,
                word[balance_pos],
                right_side,
                side_weight
            ].join(' ')
            );
        }
    });
}

main(input_data);
