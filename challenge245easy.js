#!/usr/bin/env node

// Daily Programmer Challenge 245 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3wshp7/20151214_challenge_245_easy_date_dilemma/

// 22 June 2016

"use strict;"

function zfill(max_width, n) {
    n = n.toString();
    if (n.length > max_width)
        return n;

    let zeroes = '0'.repeat(max_width);
    return ('0'+n).slice(-max_width);
}

function parseEntry(entry) {
    let columns = entry.split(/\D/g);
    let day, month, year;
    if (columns[0].length === 4) {
        year = columns[0];
        month = zfill(2, columns[1]);
        day = zfill(2, columns[2]);
    } else {
        year = columns[2];
        if (columns[2].length === 2)
            year = '20' + columns[2];
        month = zfill(2, columns[0]);
        day = zfill(2, columns[1]);
    }
    return `${year}-${month}-${day}`;
}


let input = `
2/13/15
1-31-10
5 10 2015
2012 3 17
2001-01-01
2008/01/07
`;

let entries = input.trim().split('\n');
console.log(entries.map(s => parseEntry(s)).join('\n'));
