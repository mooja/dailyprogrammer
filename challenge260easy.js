#!/usr/bin/env node

// Daily Programmer Challenge 260 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/4cb7eh/20160328_challenge_260_easy_garage_door_opener/

// 10 July 2016

function main() {
  // b = button clicked, c = cycle complete
  const inputs = ['b', 'c', 'b', 'b', 'b', 'b', 'b', 'c'];
  const FSM = [
    ['CLOSED',  'b', 'OPENING'],
    ['OPEN',    'b', 'CLOSING'],
    ['OPENING', 'c', 'OPEN'],
    ['OPENING', 'b', 'STOPPED_WHILE_OPENING'],
    ['CLOSING', 'c', 'CLOSED'],
    ['CLOSING', 'b', 'STOPPED_WHILE_CLOSING'],
    ['STOPPED_WHILE_OPENING', 'b', 'CLOSING'],
    ['STOPPED_WHILE_OPENING', 'c', 'STOPPED_WHILE_OPENING'],
    ['STOPPED_WHILE_CLOSING', 'b', 'OPENING'],
    ['STOPPED_WHILE_CLOSING', 'c', 'STOPPED_WHILE_OPENING'],
  ];

  let state = 'CLOSED';
  console.log('Door: ', state);
  for (let input of inputs) {
    console.log(input == 'b' ? '> Button clicked.' : '> Cycle complete.');
    for (let [s, i, newState] of FSM) {
      if(s === state && i === input) {
        state = newState;
        break;
      }
    }
    console.log('Door: ', state);
  }
}

main();
