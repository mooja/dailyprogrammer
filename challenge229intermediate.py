#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 229 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/3iimw3/20150826_challenge_229_intermediate_reverse_fizz/
#
# 06 June 2016

import sys

from itertools import count
from itertools import islice
from itertools import permutations
from functools import lru_cache
from string import ascii_lowercase


# generates fizzbuz according to the arguments
@lru_cache(1024)
def fizz_buzz(*fb_integers):
    for n in count(1):
        output = []
        for fb_int_idx, fb_int in enumerate(fb_integers):
            if n % fb_int == 0:
                output.append(ascii_lowercase[fb_int_idx])
        if output:
            yield ''.join(output)

# generate successively higher permutations of arguments for the fizzbuz()
# function and until we find the target output. O(n!) time complexity!
def reverse_fizz_buzz(text):
    target_output = '\n'.join(text.strip().split())
    num_fizzbuzz_args = ascii_lowercase.index(max(target_output)) + 1
    num_fizzbuzz_lines = len(target_output.split('\n'))

    num_range_start = 1
    num_range_end = 2

    while True:
        for perm in permutations(range(num_range_start, num_range_end),
                                 r=num_fizzbuzz_args):
            fizzbuzz_output = '\n'.join(islice(fizz_buzz(*perm), num_fizzbuzz_lines))
            if fizzbuzz_output == target_output:
                return ' '.join(str(i) for i in perm)
        num_range_end += 1

if __name__ == "__main__":
    input_1 = "a b a a b a" 
    input_2 = "b be ab be b abe b"
    input_3 = "a b c d a ab"
    input_challenge = "i b d i f b j i d b i a f e d i b j i d b f i d b i a j f i e b d i b d j f i h b i a d i c b f e j d i b i f d b i a j i d b f i e b d i j b f i a d i b d j f i b e i h d b i a f j d b i i c b f d i e j b d i a f b i d i j b f i d b e g i a d b j f i i d b h i f b j d i a e b i d f i b j d i c b f i a d e b i j f d i b i b d j f i a b d i e b i f h d j i b i d a f b i j d e b i f i d b i j a c b"

    print(reverse_fizz_buzz(input_1))
    print(reverse_fizz_buzz(input_2))
    print(reverse_fizz_buzz(input_3))
    # print(reverse_fizz_buzz(input_challenge))
