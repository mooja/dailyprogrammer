#!/usr/bin/env node

// Daily Programmer Challenge 256 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/48a4pu/20160229_challenge_256_easy_oblique_and_deoblique/

// 06 July 2016

"use strict;"

const input = `0 1 2 3 4 5
6  7  8  9 10 11
12 13 14 15 16 17
18 19 20 21 22 23
24 25 26 27 28 29
30 31 32 33 34 35`;

main();

function main() {
  const input_matrix = input
    .split(/\n/)
    .map(line =>
      line
        .split(/\s+/)
        .map(x =>Number(x))
    );

  for (let slice of oblique(input_matrix)) {
    console.log(slice.join(' '));
  }

  console.log();

  for (let row of de_oblique(oblique(input_matrix)))
    console.log(row.join(' '));
}

function* oblique(matrix) {
  let slice = [];
  for (let pos of diagonal_positions(matrix)) {
    slice.push(matrix[pos.row][pos.col]);
    if (pos.col === 0 || pos.row == matrix.length-1) {
      yield slice;
      slice = [];
    }
  }
}

function de_oblique(slices) {
  slices = Array.from(slices);
  let obliq_elements = [].concat.apply([], slices);

  const width = Math.max.apply(null,
    slices.map(slice => slice.length)
  )

  let matrix = new Array(width);
  for (let i = 0; i < matrix.length; i++)
    matrix[i] = new Array(width).fill(null);

  for (let pos of diagonal_positions(matrix)) {
    matrix[pos.row][pos.col] = obliq_elements.shift();
  }

  return matrix;
}

function* diagonal_positions(matrix) {
  const width = matrix[0].length;
  const height = matrix.length;

  for(let col = 0; col < width; col++) {
    let r = 0;
    for(let c=col; c >= 0; c--) {
      p = {'col': c, 'row': r};
      yield p;
      r++;
    }
  }

  for(let row = 1; row < height; row++) {
    let c = width-1;
    for(let r=row; r < height; r++) {
      p = {'col': c, 'row': r};
      yield p;
      c--;
    }
  }
}
