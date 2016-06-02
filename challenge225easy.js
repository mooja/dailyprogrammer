#!/usr/bin/env node

// Daily Programmer Challenge 225 Easy

// https://www.reddit.com/r/dailyprogrammer/comments/3esrkm/20150727_challenge_225_easyintermediate/

// 02 June 2016

const input_data = 
`
+----------------+ Lorem ipsum dolor sit amet,
|                | consectetur adipiscing elit,
|  Aha, now you  | sed do eiusmod tempor incid-
|  are stumped!! | idunt ut labore et dolore
|                | magna aliqua. Ut enim ad mi-
|       +--------+ nim veniam, quis nostrud ex-
|  top  |          ercitation ullamco laboris
|  kek  | nisi ut aliquip ex.
|       |                       +-------------+
+-------+ Duis aute irure dolor |             |
in repre-henderit in voluptate  | Nothing to  |
velit esse cillum dolore eu fu- |  see here.  |
giat nulla pariatur. Excepteur  |             |
sint occaecat cupidatat non     +-------------+
proident, sunt in culpa qui of-
ficia deserunt mollit anim id est laborum.
`

function decolumnize(text) {
    // remove feature boxes
    text = text
        .split('\n')
        .map(line => 
             line.replace(/([+|])[^\1]+?\1/g, '')
                 .replace(/\|/g, '')) // trailing |'s in case of "| +---+"
        .join('\n');

    // join hyphenated words
    text = text.replace(/(\w+)-\ *\n\ *(\w+)/g, '$1$2');

    // split paragraphs
    let paragraphs = text.split(/\n\ +\n/);

    // remove paragraph newlines and trim
    paragraphs = paragraphs
        .map(p => 
             p.replace(/\s+/g, ' ')
              .trim());

    return paragraphs.join('\n');
}

console.log(decolumnize(input_data.trim()))
