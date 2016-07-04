#!/usr/bin/env node

// Daily Programmer Challenge 255 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/46zm8m/20160222_challenge_255_easy_playing_with_light/

// 04 July 2016

const input = `1000
616 293
344 942
27 524
716 291
860 284
74 928
970 594
832 772
343 301
194 882
948 912
533 654
242 792
408 34
162 249
852 693
526 365
869 303
7 992
200 487
961 885
678 828
441 152
394 453`;


function main(data) {
    const parsedNumbers = data
        .split(/\s+/)
        .map(x => Number(x));

    const numBulbs = parsedNumbers[0];
    let bulbs = new Array(numBulbs).fill(false);

    // parse slices
    let slices = [];
    for (let i = 1; i < parsedNumbers.length; i += 2) {
        const slice = [parsedNumbers[i], parsedNumbers[i+1]]
          .sort();
        slices.push(slice);
    }

    // apply slices
    for (let slice of slices) 
      for(let i=slice[0]; i <= slice[1]; i++)
          bulbs[i] = !bulbs[i];

    console.log(bulbs.filter(Boolean).length);
}

main(input);
