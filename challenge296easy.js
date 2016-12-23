#!/usr/bin/env node

let days = [
  "first",
  "second",
  "third",
  "fourth",
  "fifth",
  "sixth",
  "seventh",
  "eighth",
  "ninth",
  "tenth", 
  "eleventh",
  "twelfth"
];

let gifts = [
  "one Partridge in a Pear Tree",
  "two Turtle Doves",
  "three French Hens",
  "four Calling Birds",
  "five Golden Rings",
  "six Geese a Laying",
  "seven Swans a Swimming",
  "eight Maids a Milking",
  "nine Ladies Dancing",
  "ten Lords a Leaping",
  "eleven Pipers Piping",
  "twelve Drummers Drumming"
];


for (var i = 0, len = days.length; i < len; i++) {
  console.log(`On the ${days[i]} day of Christmas`);
  console.log(`my true love sent to me:`);
  for (var k = i; k >= 0; k--) {
    console.log(gifts[k]);
  }
  console.log('\n');
}
