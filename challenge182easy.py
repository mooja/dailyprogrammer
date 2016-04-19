#!/usr/bin/env python3
# encoding: utf-8


# Daily Programmer Challenge 182 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2hssx6/29092014_challenge_182_easy_the_column_conundrum/
#
# 19.April.2016


def mk_column(colwidth, text):
    """ 
    >>> mk_column(3, 'abcdefgh')
    'abc\\ndef\\ngh'
    >>> mk_column(3, 'ab\\ncd\\nefgh')
    'ab\\ncd\\nefg\\nh'
    """
    
    output_lines = []
    text_lines = text.split('\n')
    for line in text_lines:
        for i in range(0, len(line), colwidth):
            output_lines.append(line[i:i+colwidth])
    return '\n'.join(output_lines)

def columnize(ncols, colwidth, spacewidth, text):
    """
    >>> columnize(2, 2, 1, 'abcdef')
    'ab ef\\ncd'
    """
    column_text = mk_column(colwidth, text)
    column_lines = column_text.split('\n')
    nrows = (len(column_lines)+1) // ncols

    lines_dict = {}
    for i, line in enumerate(column_lines):
        i = i % nrows
        if not i in lines_dict:
            lines_dict[i] = [line]
        else:
            lines_dict[i].append(line)
    
    output_lines = ((' '*spacewidth).join(lines_dict[i])
                   for i in sorted(lines_dict.keys()))
    return '\n'.join(l for l in output_lines)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    text = 'Sit fugiat nihil porro eius quos quia saepe at? Voluptate doloribus assumenda perspiciatis ullam aut minus odio quis officia ea in distinctio magnam eveniet obcaecati, maxime cum. Laborum exercitationem dicta culpa culpa veritatis. Officiis animi excepturi maiores provident omnis repellendus eum suscipit molestiae! Adipisci sit eveniet dolorum distinctio deleniti excepturi laboriosam corrupti provident praesentium placeat aliquam amet? Ad optio inventore quae eaque quas. Nostrum odit quasi ad beatae pariatur. Saepe voluptatibus praesentium omnis voluptatum ratione tenetur? Modi fuga beatae sint nam maxime. Ab doloremque vero explicabo placeat ipsam! Fuga quisquam dolor reiciendis animi sint, quam incidunt veritatis. Impedit in veritatis.'
    print(columnize(3, 20, 2, text))
