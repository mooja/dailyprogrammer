#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 113 Intermediate
#
# http://www.reddit.com/r/dailyprogrammer/comments/13hmz5/11202012_challenge_113_intermediate_text_markup/
#
# May.18.2015


import re


def process_bold(text):
    new_text = list(text)
    tag_is_closed = True
    i = 0
    while i < (len(new_text)-1):
        twochars = ''.join(new_text[i:i+2])
        prevchar = new_text[i-1] if i > 0 else None
        if twochars == '**' and prevchar != '\\':
            new_text[i:i+2] = list('<b>') if tag_is_closed else list('</b>')
            tag_is_closed = not tag_is_closed
        i += 1

    if not tag_is_closed:
        new_text.append('</b>')

    return ''.join(new_text)


def process_italics(text):
    new_text = list(text)
    tag_is_closed = True
    i = 0
    while i < len(new_text):
        char = new_text[i]
        prevchar = new_text[i-1] if i > 0 else None
        if char == '*' and prevchar != '\\':
            new_text[i:i+1] = list('<i>') if tag_is_closed else list('</i>')
            tag_is_closed = not tag_is_closed
        i += 1

    if not tag_is_closed:
        new_text.append('</i>')

    return ''.join(new_text)


def process_strikethrough(text):
    new_text = list(text)
    tag_is_closed = True
    i = 0
    while i < (len(new_text)-1):
        twochars = ''.join(new_text[i:i+2])
        prevchar = new_text[i-1] if i > 0 else None
        if twochars == '~~' and prevchar != '\\':
            new_text[i:i+2] = list('<strike>') if tag_is_closed else list('</strike>')
            tag_is_closed = not tag_is_closed
        i += 1

    if not tag_is_closed:
        new_text.append('</strike>')

    return ''.join(new_text)


def process_superscript(text):
    new_text = list(text)
    tag_is_closed = True
    i = 0
    while i < len(new_text):
        char = new_text[i]
        prevchar = new_text[i-1] if i > 0 else None

        if char == '^' and prevchar != '\\':
            new_text[i:i+1] = list('<sup>')
            tag_is_closed = not tag_is_closed
        elif char.isspace() and not tag_is_closed:
            new_text[i:i+1] = list('</sup>') + list(char)
            tag_is_closed = True
        i += 1

    if not tag_is_closed:
        new_text.append('</sup>')

    return ''.join(new_text)


def process_links(text):
    regex = re.compile(r'''
                        \[    #  opening  bracket
                        (.+)  #  name of the link
                        \]    #  closing bracket
                        \(    #  opening parenthesis
                        (.+)  # link itself
                        \)    # closing parenthesis
                        ''', re.X)
    return re.sub(regex, r'<a href="\2">\1</a>''', text)


def process_preformatted(text):
    pass



def process_markdown(text):
    text = process_superscript(text)
    text = process_bold(text)
    text = process_italics(text)
    text = process_strikethrough(text)
    text = process_links(text)
    return text



if __name__ == '__main__':
    msg = '**welcome   *to* \\*the world of **real\\* and ~~ **super^script ~~\n\n [reddit!](http://reddit.com)'
    print 'Text: {}'.format(msg)
    print 'Processed: ', process_markdown(msg)
