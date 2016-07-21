#!/usr/bin/env node

// Daily Programmer Challenge 272 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/4oylbo/20160620_challenge_272_easy_whats_in_the_bag/

// 21 July 2016

const DISTRIBUTION_DATA = `A	9, B	2, C	2, D	4, E	12, F	2, G	3, H	2, I
  9, J	1, K 1, L	4, M	2, N	6, O	8, P	2, Q	1	, R	6, S	4, T	6, U	4, V	2,
  W	2, X 1, Y 2, Z	1, _ 2`;
const INPUT0 = 'AEERTYOXMCNB_S';
const INPUT1 = 'PQAREIOURSTHGWIOAE_';
const INPUT2 = 'LQTOONOEFFJZT';
const INPUT3 = 'AXHDRUIOR_XHJZUQEE';


function leftInBag(input) {
  let m = new Map();
  for (let row of DISTRIBUTION_DATA.split(',')) {
    const key = row.trim().split(/\s+/)[0];
    const count = Number(row.trim().split(/\s+/)[1]);
    m.set(key, count);
  }

  for (let ch of input) {
    if (m.get(ch) == 0) {
      console.log(`More ${m.get(ch)}'s have been taken from the bag than possible.`);
      process.exit(1);
    }
    m.set(ch, m.get(ch) - 1);
  }

  let byCount = new Map();
  for (let [key, count] of m.entries()) {
    if(byCount.has(count))
      byCount.get(count).push(key);
    else
      byCount.set(count, [key]);
  }

  const sortedKeys = Array.from(byCount.keys())
    .sort((a, b) => b - a)
  for (let count of sortedKeys)
    console.log(`${count}: ${byCount.get(count).join(', ')}`);
}

leftInBag(INPUT0);
console.log('---');

leftInBag(INPUT1);
console.log('---');

leftInBag(INPUT2);
console.log('---');

leftInBag(INPUT3);
console.log('---');
