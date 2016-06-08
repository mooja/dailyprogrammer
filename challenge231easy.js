#!/usr/bin/env node

// Daily Programmer Challenge 231 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3jz8tt/20150907_challenge_213_easy_cellular_automata/

// 08 June 2016


function rule60(a, b, c) {
    a = Number(a);
    c = Number(c);
    return (a ^ c).toString();
}

function apply_rule_60(cells) {
    let successor_state = [];
    for(let i = 0; i < cells.length; i++) {
        let a = i != 0 ? cells[i-1] : '0';
        let b = cells[i];
        let c = i != cells.length-1 ? cells[i+1] : '0';
        successor_state.push(rule60(a, b, c));
    }
    return successor_state.join('');
}

function* automata_gen(initial_state, steps=25){
    let state = initial_state;
    for(let i = 0; i < steps + 1; i++) {
        yield state.replace(/0/g, ' ').replace(/1/g, 'X');
        state = apply_rule_60(state);
    }
}

for(let s of automata_gen('00000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000'))
    console.log(s)
