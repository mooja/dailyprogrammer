#!/usr/bin/env node

// Daily Programmer Challenge 253 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/44qzj5/20160208_challenge_253_easy_unconditional_loan/

// 03 July 2016

const _ = require('lodash');


let interestRate = 0.02;
let annualLoanAmount = 15000;
let startAge = 18;
let clawbackBalanceTrigger = 100000;
let royaltyRateUnder65 = .2;
let royaltyRateOver65 = .4;
let income_stream = '0 0 30 30 30 30 30 30 30 30 30 30 40 40 40 40 40 40 40 40 40 40 50 50 50 50 50 50 50 50 50 50 60 60 60 60 60 60 60 60 60 60 100 120 140 160 200 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10';


let overall_loans = _.sum(income_stream
  .split(/\s+/)
  .map(x => Number(x))
);
console.log('overall loans: ', overall_loans)
