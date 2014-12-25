#!/usr/bin/env python
# encoding: utf-8


if __name__ == '__main__':
    with open('qa.txt', 'r') as f:
        lines = f.readlines()

    quest2answer = dict()
    for line in lines:
        q = line.split(';')[0].strip()
        a = line.split(';')[1].strip()
        quest2answer[q] = a

    for q in quest2answer:
        print q
        answer = raw_input('> ')
        if answer.lower() == 'exit':
            print "Exiting."
            break
        if answer.lower() != quest2answer[q].lower():
            print "Incorrect. Correct answer was '{}'".format(quest2answer[q])
