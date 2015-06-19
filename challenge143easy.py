#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 142 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1s061q/120313_challenge_143_easy_braille/
#
# June.18.2015


braille2alpha = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z'
}


def main():
    lines = []
    for i in range(3):
        lines.append(raw_input().strip())

    braille_letters = ['' for _ in range(len(lines[0].split()))]
    for line in lines:
        for idx, chars in enumerate(line.split()):
            braille_letters[idx] = braille_letters[idx] + chars

    result = bytearray()
    for bletter in braille_letters:
        result += braille2alpha[bletter]

    print result


if __name__ == '__main__':
    main()
