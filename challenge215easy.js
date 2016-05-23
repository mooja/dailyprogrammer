#!/usr/bin/env node

// # Daily Programmer Challenge 215 Easy
// #
// # https://www.reddit.com/r/dailyprogrammer/comments/36cyxf/20150518_challenge_215_easy_sad_cycles/
// #
// # 23 May 2016


// helper functions
var sum = l => l.reduce((a, b) => a + b, 0);
var parseInt10 = x => parseInt(x, 10);

// digits powers sum function
function sum_digit_powers(n, p) {
    var digits = n.toString().split('').map(parseInt10);
    var digit_powers = digits.map(d => Math.pow(d, p));
    return sum(digit_powers);
};

// digits powers sum generator
function* sdp_seq(start, p) {
    while (true) {
        yield start;
        start = sum_digit_powers(start, p);
    }
}

// sad cycle detector
function sdp_cycle(start, p) {
    var cycle = [];
    for (var i of sdp_seq(start, p)) {
        var have_seen_i = cycle.indexOf(i) != -1;
        if (have_seen_i)
            return cycle.slice(cycle.indexOf(i))
        cycle.push(i);
    }
}

console.log(sdp_cycle(2, 6).join(', '));
