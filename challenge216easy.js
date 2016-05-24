#!/usr/bin/env node

var _ = require('underscore');

// input
var nplayers = 3;

// build a shuffled deck
var ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'].map(String);
var suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades'];
var deck = suits
  .map(s => ranks.map(r => ({r, s})))
  .reduce((a, b) => a.concat(b), []);
deck = _.shuffle(deck);

// distribute cards
var hands = new Map();
['Your Hand']
  .concat(_.range(1, nplayers).map(d => `CPU ${d} Hand`))
  .forEach(hn => hands.set(hn, _.range(2).map(i => deck.pop())));
var flop = _.range(3).map(i => deck.pop());
var turn = deck.pop();
var river = deck.pop();

// display the cards
var output_lines = [];
hands.forEach((cards, name) => {
    var cards_text = cards.map(card => `${card.r} of ${card.s}`).join(', ');
    output_lines.push(`${name}: ${cards_text}`);
});
output_lines.push('');
output_lines.push('Flop: '+flop.map(card => `${card.r} of ${card.s}`).join(', '));
output_lines.push(`Turn: ${turn.r} of ${turn.s}`);
output_lines.push(`River: ${river.r} of ${river.s}`);
console.log(output_lines.join('\n'));
