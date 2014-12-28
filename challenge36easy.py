#!/usr/bin/env python
# encoding: utf-8

from math import ceil
# lockers problem from challenge 35 easy

# 1000 Lockers Problem.

# In an imaginary high school there exist 1000 lockers labelled 1, 2, ..., 1000.
# All of them are closed. 1000 students are to "toggle" a locker's state. 
# * The # first student toggles all of them 
# * The second one toggles every other one (i.e, 2, 4, 6, ...)
# * The third one toggles the multiples of 3 (3, 6, 9, ...)
# and so on until all students have finished.
# 
# To toggle means to close the locker if it is open, and to open it if it's
# closed.  How many and which lockers are open in the end?

if __name__ == '__main__':
    lockers = [False for i in range(1000)]

    for n in range(1, 1001):
        for i in range(len(lockers)):
            if (i+1) % n == 0:
                lockers[i] = (not lockers[i])

    num_open = len([1 for lock in lockers if lock])
    print("Result: {:>3d} locks remained opened in the end".format(num_open))
    print("First 25 lockers: ")

    # just trying out printing output in columns
    ncolumns = int(ceil(25 / 10.0))
    columns = [[] for i in range(ncolumns)]
    for i in range(25):
        if lockers[i]:
            columns[i/10].append("{:>2d}: [ ]".format(i+1))
        else:
            columns[i/10].append("{:>2d}: [x]".format(i+1))

    for r in range(10):
        output = ''
        for c in range(3):
            if r < len(columns[c]):
                output += columns[c][r].ljust(12)
        print(output)
