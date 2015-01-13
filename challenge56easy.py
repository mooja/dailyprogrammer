#!/usr/bin/env python
# encoding: utf-8

from string import ascii_lowercase


def file_window_iter(fh, startpos=0, endpos=None, buffsize=1):
    tmp = fh.tell()
    if endpos is None:
        fh.seek(0, 2)
        endpos = fh.tell()
    fh.seek(tmp)

    if (endpos - startpos) and (endpos - startpos) < buffsize:
        buffsize = endpos - startpos

    for pos in range(startpos, endpos, buffsize):
        tmp = fh.tell()

        fh.seek(pos)
        if pos + buffsize > endpos:
            buffer = fh.read(endpos % buffsize)
        else:
            buffer = fh.read(buffsize)

        fh.seek(tmp)
        yield buffer

    raise StopIteration


def add_letter(fh, letter):
    fh.seek(0, 2)
    endpos = fh.tell()
    contents = file_window_iter(fh=fh, endpos=endpos, buffsize=2024)

    fh.write(letter)
    for buffer in contents:
        fh.write(buffer)
    fh.seek(0)

    return fh


def write_seq(fh, ending_letter):
    ending_index = ascii_lowercase.index(ending_letter.lower())
    ending_index += 1

    for letter in ascii_lowercase[:ending_index]:
        fh = add_letter(fh, letter)

    return fh


def main(endwith='z'):
    with open('sequence.txt', 'w+') as fh:
        fh = write_seq(fh, endwith)


if __name__ == '__main__':
    main('z')
