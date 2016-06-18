#!/usr/bin/env node

// Daily Programmer Challenge 240 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3s4nyq/20151109_challenge_240_easy_typoglycemia/

// 18 June 2016

const _ = require('lodash');


function punctuationLocs(word) {
    let locs = [];
    word.split('').forEach((ch, idx) => {
        let isPunctuatoin = /\W/.test(ch);
        if (isPunctuatoin)
            locs.push(idx);
    });
    return locs;
}

function mangleWord(word) {
    if (word.length < 4)
        return word;

    let chars = word.split('').filter(w =>/\w/.test(w));
    let body_chars = chars.slice(1, -1);
    body_chars = _.shuffle(body_chars);
    chars = [chars[0], ...body_chars, chars[chars.length-1]];

    // insert punctuation in the original word locations
    let punctuationLocations = punctuationLocs(word);
    let punctuationChars = word.split('').filter(w => /\W/.test(w));
    punctuationLocations.forEach((loc, idx) => {
        chars.splice(loc, 0, punctuationChars[idx]);
    });

    return chars.join('');
}

function main(data) {
    return data.replace(/\w+/g, w => mangleWord(w));
}

let input = `According to a research team at Cambridge University, it doesn't matter in what order the letters in a word are, the only important thing is that the first and last letter be in the right place.  The rest can be a total mess and you can still read it without a problem.  This is because the human mind does not read every letter by itself, but the word as a whole.  Such a condition is appropriately called Typoglycemia.`

console.log(main(input));
