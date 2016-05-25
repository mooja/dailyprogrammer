#!/usr/bin/env node

_ = require("underscore");

// input
let side_length = 12;
let add_logs_count = 10000;
let logs_data = `
  9 15 16 18 16  2 20  2 10 12 15 13 
 20  6  4 15 20 16 13  6  7 12 12 18 
 11 11  7 12  5  7  2 14 17 18  7 19 
  7 14  4 19  8  6  4 11 14 13  1  4 
  3  8  3 12  3  6 15  8 15  2 11  9 
 16 13  3  9  8  9  8  9 18 13  4  5 
  6  4 18  1  2 14  8 19 20 11 14  2 
  4  7 12  8  5  2 19  4  1 10 10 14 
  7  8  3 11 15 11  2 11  4 17  6 18 
 19  8 18 18 15 12 20 11 10  9  3 16 
  3 12  3  3  1  2  9  9 13 11 18 13 
  9  2 12 18 11 13 18 15 14 20 18 10 
`

// helpers
let min = arr => arr.reduce((p1, p2) => p1 < p2 ? p1 : p2);
let max = arr => arr.reduce((p1, p2) => p1 > p2 ? p1 : p2);
let swidth = (w, s) => (' '.repeat(w) + s).slice(-w);

class LogGrid {
    constructor (side_len, data) {
        this.side_len = side_len;
        this.piles = data.trim().split(/\s+/).map(x => parseInt(x));
        this.smallest_pile_size = min(this.piles);
    }

    add_logs(n=1) {
        for(let i of _.range(n)) {
            let next_smallest_idx = this.piles.indexOf(this.smallest_pile_size);
            while(next_smallest_idx == -1) {
                this.smallest_pile_size += 1;
                next_smallest_idx = this.piles.indexOf(this.smallest_pile_size);
            }
            this.piles[next_smallest_idx] += 1;
        }
    }

    str() {
        let max_len = max(this.piles).toString().length;
        let lines = [];
        for(let i of _.range(this.side_len)) {
            let line = [];
            for(let j of _.range(this.side_len)) {
                let pile_idx = this.side_len*i + j;
                line.push(swidth(max_len, this.piles[pile_idx].toString()));
            }
            lines.push(line.join(' '));
        }
        return lines.join('\n');
    }
}

let grid = new LogGrid(side_length, logs_data);
grid.add_logs(add_logs_count);
console.log(grid.str());
