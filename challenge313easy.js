#!/usr/bin/env node


// Daily Programmer Challenge 313 Easy
// https://www.reddit.com/r/dailyprogrammer/comments/68oda5/20170501_challenge_313_easy_subset_sum/
// 03 May 2017


function subsetSum(arr) {
    for(let idx = 0; idx < arr.length; idx++) 
        if (arr.includes(-arr[idx])) return true;
    return false;
}