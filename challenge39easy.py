#!/usr/bin/python3
# encoding: utf-8

#######################################################################
#                        Challenge 39 FizzBuzz                        #
#######################################################################


def fizz_buzz(n):
    for i in range(1, n+1):
        if (i % 3 == 0) or (i % 5 == 0):
            if i % 3 == 0:
                print "Fizz",
            if i % 5 == 0:
                print "Buzz",
            print
        else:
            print i

if __name__ == '__main__':
    fizz_buzz(15)
