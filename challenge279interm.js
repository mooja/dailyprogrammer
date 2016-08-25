#!/usr/bin/env node

// Daily Programmer Challenge 279 Interm

// https://www.reddit.com/r/dailyprogrammer/comments/4ybbcz/20160818_challenge_279_intermediate_text_reflow/

// 25 August 2016


function wrap(text, width) {
  const paragraphs = text.split('\n\n');
  let output = '';

  for (let p of paragraphs) {
    let column = 0;
    const words = p.split(/\s+/g);
    for (let word of words) {
      const newCol = column + word.length + 1;
      if (column === 0) {
        output += word
        column += word.length;
      }
      else if (newCol <= width) {
        output += ' ' + word;
        column += word.length + 1;
      } 
      else {
        output += '\n' + word;
        column = word.length;
      }
    }
    output += '\n\n';
  }

  return output.trim();
}

const text = `In the beginning God created the heavens and the earth. Now the earth was 
formless and empty, darkness was over the surface of the deep, and the Spirit of
God was hovering over the waters.

And God said, "Let there be light," and there was light. God saw that the light
was good, and he separated the light from the darkness. God called the light
"day," and the darkness he called "night." And there was evening, and there was
morning - the first day.`

console.log(wrap(text, 40));
