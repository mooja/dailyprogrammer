// Daily Programmer Challenge 239 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/

// 17 June 2016

function gameOfThrees(num) {
  while(num > 1) {
    let remainder = num % 3;
    if (remainder == 2)
      remainder = -1;
    console.log('%d %d', num, Math.round(remainder*(-1)));
    num = Math.round((num - remainder) / 3)
  }
  console.log(1);
}

let input = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', (chunk) => input += chunk);
process.stdin.on('end', () => {
  gameOfThrees(Number(input.trim()));
});

// $ echo 100 | node challenge239easy.js
// 100 -1
// 33 0
// 11 1
// 4 -1
// 1
