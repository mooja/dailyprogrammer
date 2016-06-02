#!/usr/bin/env node

// Daily Programmer Challenge 224 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3e0hmh/20150720_challenge_224_easy_shuffling_a_list/

// 01 June 2016

// random using current time + linear congruent generator
// weak + breaks on big numbers, don't use in poker

function lcg_factory(
    seed, 
    modulus=Math.pow(2, 24), // returns random 3 bytes
    a=1140671485, // taken from visual basic
    c=2531011)    // taken from visual basic
{
    let state = seed;
    function lgc() {
        state = (state*a + c) % modulus;
        return state
    }
    return lgc;
}

Array.prototype.swap = function(i, j) 
{
    let temp = this[i];
    this[i] = this[j];
    this[j] = temp;
}

// Fisher Yates Shuffle
Array.prototype.shuffle = function() 
{
    let rand = lcg_factory((new Date().getTime()));
    for(let i = this.length-1; i > 0; i--) {
        let r = rand() % i;
        this.swap(i, r)
    }
    return this;
}

let set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(set.shuffle());

let rand_range = lcg_factory((new Date().getTime()));
for(let i=0; i < 10; i++)
    console.log(rand_range())
