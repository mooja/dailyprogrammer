#!/usr/bin/env node

// Daily Programmer Challenge 233 Eas

// https://www.reddit.com/r/dailyprogrammer/comments/3ltee2/20150921_challenge_233_easy_the_house_that_ascii/

// 10 June 2016

_ = require('lodash');

const WIDTH_UNIT_CHARS = 5; 
const HEIGHT_UNIT_CHARS=3;

const raw_input1 = 
`
   *
  ***
******
`

const raw_input2 = 
`
 *
***
***
***
***
***
***
`

const raw_input3 = 
`
***                    ***
***     **  ***  **    ***
***   ***************  ***
***   ***************  ***
***   ***************  ***
**************************
**************************
`

class Building {

  constructor (blueprint) {
    // build up a columns array-like object. 
    // column[0] = size of the first column, etc
    let columns = {}
    let lines = blueprint.split('\n');
    for (let line of lines) 
      for(let col_idx = 0; col_idx < line.length; col_idx++) 
        if (line[col_idx] === '*')
          columns[col_idx] = (columns[col_idx] || 0) + 1;

    let longest_line = _.max(lines.map(l => l.length))
    let column_heights = [];
    for (let i = 0; i < longest_line; i++)
      column_heights.push(columns[i.toString()]);

    let boxes = [];
    let prev_height = -1;
    let pos = 0; // position on the x axis
    for ( let column_height of column_heights ) {
      let box = {}
      if (column_height === prev_height) {
        box = boxes.pop() 
        box['unit_width'] += 1;
      } else {
        box['unit_width'] = 1;
        box['unit_height'] = column_height;
        prev_height = column_height;
      }

      box['width'] = box['unit_width'] * WIDTH_UNIT_CHARS;
      box['height'] = box['unit_height'] * HEIGHT_UNIT_CHARS;
      box['roof_height'] = box['height'] + Math.floor((box['width'] - 3) / 2) + 1;
      
      boxes.push(box);
    } // end create boxes

    this.boxes = boxes;
  } // end constructor

  toString() {
    let nboxes = this.boxes.length;
    let grid_width = _.sum(this.boxes.map(b => b.width)) - nboxes + 1;
    let grid_height = _.max(this.boxes.map(b => b.roof_height));
    let grid = _.range(grid_height)
      .map(() => 
        ' '.repeat(grid_width)
           .split(''));

    // draw  boxes ----------------------
    let box_pos = 0;
    for (let box of this.boxes) {
      for (let y of _.range(box.height)) {
        for (let x of _.range(box.width)) {
          let is_horizontal_wall = (y === 0 || y === box.height - 1);
          let is_vertical_wall = (x === 0 || x === box.width - 1);
          let is_corner = is_horizontal_wall && is_vertical_wall;

          let grid_ch = grid[y][x+box_pos];

          if (is_corner && grid_ch === '+')
            grid[y][x+box_pos] = '-';
          else if (is_corner)
            grid[y][x+box_pos] = '+';
          else if (is_vertical_wall && grid_ch === '+')
            grid[y][x+box_pos] = '+';
          else if (is_vertical_wall && grid_ch === '|')
            grid[y][x+box_pos] = ' ';
          else if (is_vertical_wall)
            grid[y][x+box_pos] = '|';
          else if (is_horizontal_wall)
            grid[y][x+box_pos] = '-';

        }
      } // end for (let y of _.range(box.height))

      box_pos += box.width - 1
    } // end for (let box of this.boxes)


    // draw roofs ----------------------
    box_pos = 0;
    for (let box of this.boxes) {
      let x = box_pos + 1; 
      let y = box.height;
      let roof_side_length = Math.floor((box.width - 3) / 2)

      // left side
      for(let i = 0; i < roof_side_length; i++) {
        grid[y][x] = '/';
        x++;
        y++;
      }

      // top
      grid[y][x] = 'A';
      x++;
      y--;

      // right side
      for(let i = 0; i < roof_side_length; i++) {
        grid[y][x] = '\\';
        x++;
        y--;
      }

      box_pos += box.width - 1;
    }

    return grid.map(chars => chars.join('')).reverse().join('\n');
  }

}

// main --

let b1 = new Building(raw_input1);
console.log(b1.toString());

let b2 = new Building(raw_input2);
console.log(b2.toString());

let b3 = new Building(raw_input3);
console.log(b3.toString());
