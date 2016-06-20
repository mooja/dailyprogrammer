#!/usr/bin/env node

// Daily Programmer Challenge 242 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3twuwf/20151123_challenge_242_easy_funny_plant/

// 19 June 2016

const _ = require('lodash');

function harvest(plantsSeq) {
    let total = 0;
    for(let nfruits of plantsSeq)
        total += nfruits;
    return total;
}

function nextWeek(plantsSeq) {
    let newPlantsNum = 0
    plantsSeq = plantsSeq.map(nfruits => {
        newPlantsNum += nfruits + 1;
        return nfruits += 1;
    });
    for (let i=0; i < newPlantsNum; i++)
        plantsSeq.push(0);
    return plantsSeq;
}

function nWeeksToSustain(npeople, nplants) {
    let plants = _.range(nplants).map(() => 0);
    let nweeks = 1;
    while (harvest(plants) < npeople) {
        plants = nextWeek(plants);
        nweeks += 1;
    }
    return nweeks;
}

console.log(nWeeksToSustain(250, 15));
console.log(nWeeksToSustain(50000, 1));
console.log(nWeeksToSustain(150000, 250));
