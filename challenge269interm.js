#!/usr/bin/env node

// Daily Programmer Challenge 269 Intermediate

// https://www.reddit.com/r/dailyprogrammer/comments/4m3ddb/20160601_challenge_269_intermediate_mirror/

// 18 August 2016


class Grid {
  constructor() {
    let grid = [];

    // top header
    grid.push(' abcdefghijklm'.split(''));

    // body 
    const left = 'ABCDEFGHIJKLM';
    const right = 'nopqrstuvwxyz';
    for (let i=0; i<left.length; i++) {
      const row = [left[i], ...(' '.repeat(13)), right[i]];
      grid.push(row)
    }

    // bottom header
    grid.push(' NOPQRSTUVWXYZ'.split(''));

    this.grid = grid;
  }

  addMirrors(lines) {
    for(let row = 0; row < lines.length; row++) {
      for(let col = 0; col < lines[row].length; col++) {
        this.grid[row+1][col+1] = lines[row][col];
      }
    }
  }

  getCoords(ch) {
    for(let row = 0; row < this.grid.length; row++)
      for(let col = 0; col < this.grid[row].length; col++)
        if (this.grid[row][col] === ch)
          return [row, col];
  }

  getReflection(ch) {
    // determine starting location
    let [row, col] = this.getCoords(ch);

    // determine initial direction
    let direction = null;
    if (row === 0)
      direction = 'down';
    else if (row === this.grid.length-1)
      direction = 'up';
    else if (col === 0)
      direction = 'right';
    else
      direction = 'left';

    const turnsTable = {
      '/': {
        'right': 'up',
        'left': 'down',
        'up': 'right',
        'down': 'left'
      },
      '\\': {
        'right': 'down',
        'left': 'up',
        'up': 'left',
        'down': 'right'
      },
    }

    // travel in direction until we meet a mirror or a char
    while (true) {
      switch (direction) {
        case 'down':
          row++; 
          break;
        case 'up':
          row--;
          break;
        case 'left':
          col--;
          break;
        case 'right':
          col++;
      }

      switch (this.grid[row][col]) {
        case '/':
          direction = turnsTable['/'][direction];
          break;
        case '\\':
          direction = turnsTable['\\'][direction];
          break;
        case ' ':
          continue;
          break;
        default:
          return this.grid[row][col];
      }
    }

    return this.grid[row][col];
  }

  decode(s) {
    return s.split('')
      .map(ch => this.getReflection(ch))
      .join('');
  }

  display() {
    for(let row = 0; row < this.grid.length; row++)
        console.log(this.grid[row].join(''))
  }
}

const mirrors = String.raw`   \\  /\    
            \
   /         
      \     \
    \        
  /      /   
\  /      \  
     \       
\/           
/            
          \  
    \/       
   /       /`.split('\n');

let g = new Grid();
g.addMirrors(mirrors);
console.log(g.decode('TpnQSjdmZdpoohd'));
