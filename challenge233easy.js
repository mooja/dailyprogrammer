#!/usr/bin/env node

// Daily Programmer Challenge 233 Eas

// https://www.reddit.com/r/dailyprogrammer/comments/3ltee2/20150921_challenge_233_easy_the_house_that_ascii/

// 10 June 2016

_ = require('lodash');

const WIDTH_UNIT_CHARS = 5; 
const HEIGHT_UNIT_CHARS=3;

const raw_input = 
`
   *
  ***
******
`

function get_column_heights( input ) {
  let lines = input.split('\n');
  let line_lengths = lines.map(l => l.length);
  let longest_line = _.max(line_lengths);

  // build up a columns array-like object. 
  // column[0] = size of the first column, etc
  let columns = {}
  for (let line of lines) {
    for(let col_idx = 0; col_idx < line.length; col_idx++) {
      if (line[col_idx] === '*')
        columns[col_idx] = (columns[col_idx] || 0) + 1
    }
  }

  // convert culumns object to a Array object so that we have a .length
  // property
  let column_heights = [];
  for (let i = 0; i < longest_line; i++) {
    column_heights.push(columns[i.toString()]);
  }

  return column_heights;
}

function get_boxes_from_colheights( column_heights ) {
  let boxes = [];
  let prev_height = -1;
  for ( let column_height of column_heights ) {
    let box = {}
    if (column_height === prev_height) {
      box = boxes.pop() 
      box.width += 1;
    } else {
      box['width'] = 1;
      box['height'] = column_height;
      prev_height = column_height;
    }
    boxes.push(box);
  }
  return boxes;
}

function draw_box(box) {
  let height_chars = box.height * HEIGHT_UNIT_CHARS;
  let width_chars = box.width * WIDTH_UNIT_CHARS;

  let box_lines = [];
  for(let row of _.range(height_chars)) {
    let line = [];

    for(let col of _.range(width_chars)) {
      let is_horizontal_wall = (row === 0 || row === height_chars-1)
      let is_vertical_wall = (col === 0 || col === width_chars-1)
      let is_corner = is_horizontal_wall && is_vertical_wall;

      if (is_corner)
        line.push('+');
      else if (is_vertical_wall)
        line.push('|');
      else if (is_horizontal_wall)
        line.push('-');
      else
        line.push(' ');

    } // end for cols

    box_lines.push(line.join(''));
  } // end for rows

  return box_lines.join('\n');
}

// "image" = a string of a drawn box
function combine_box_images(img1, img2) {
  let img_height = img => img.split('\n').length;
  let img_width = img => img.split('\n')[0].length;

  // construct a two-dimentional matrix
  let combined_width = img_width(img1) + img_width(img2);
  let combined_height = _.max([img_height(img1), img_height(img2)]);
  let combined_grid = [];
  for(let row of _.range(combined_height)) {
    combined_grid.push(' '.repeat(combined_width).split(''))
  }

  // add first image to the grid
  let img1lines = img1.split('\n');
  for (let row of _.range(img_height(img1))) {
    for (let col of _.range(img_width(img1))) {
      combined_grid[row][col] = img1lines[row][col];
    }
  }

  // add second image to the grid
  let img2lines = img2.split('\n');
  let img2offset = {row: 0, 
                    col: img_width(img1) - 1}

  for (let row of _.range(img_height(img2))) {
    for (let col of _.range(img_width(img2))) {
      let grid_row = row + img2offset.row;
      let grid_col = col + img2offset.col

      let img2_ch = img2lines[row][col];
      let grid_ch = combined_grid[grid_row][grid_col];

      let is_overlapping_corner = (img2_ch === '+' || grid_ch === '+');
      let is_overlapping_wall = (img2_ch === '|' && grid_ch === '|');

      if (is_overlapping_corner) {
        combined_grid[grid_row][grid_col] = '+';
      } else if (is_overlapping_wall) {
        combined_grid[grid_row][grid_col] = ' ';
      } else {
        combined_grid[grid_row][grid_col] = img2_ch;
      }
    }
  }

  let combined_grid_lines = combined_grid.map(arr => arr.join(''));
  // combined_grid_lines.reverse();
  return combined_grid_lines.join('\n');

} // end combine_box_images

// main --

let col_heights  = get_column_heights(raw_input);
console.log(col_heights);

let boxes = get_boxes_from_colheights(col_heights);
console.log(boxes);

let drawn_boxes = boxes.map(draw_box);
for (let drawn_box of drawn_boxes) 
  console.log(drawn_box);

let combined_boxes = drawn_boxes.reduce(combine_box_images);
console.log(combined_boxes);
