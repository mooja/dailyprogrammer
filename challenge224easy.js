#!/usr/bin/env node

// Daily Programmer Challenge 224 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3e0hmh/20150720_challenge_224_easy_shuffling_a_list/

// 01 June 2016

// random using current time + linear congruent generator
// weak + breaks on big numbers, don't use in poker
function rand_range(lo, hi) {
    let now = (new Date().getTime());
    let modulus = hi - lo;
    let pseudo_random_num = (5 * now + 2) % modulus;
    return lo + pseudo_random_num;
}

Array.prototype.swap = function(i, j) {
    let temp = this[i];
    this[i] = this[j];
    this[j] = temp;
}

// Fisher Yates Shuffle
Array.prototype.shuffle = function() {
    for(let i = this.length-1; i > 0; i--) {
        let r = rand_range(0, i);
        this.swap(i, r)
    }
    return this;
}

var set = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(set.shuffle())
