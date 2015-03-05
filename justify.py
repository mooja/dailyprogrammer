#!/usr/bin/env python
# encoding: utf-8

# Codewars Kata
#
# http://www.codewars.com/kata/537e18b6147aa838f600001b/train/python
#
# March.05.2015

def words2jline(width, words):
    """
    >>> words2jline(10, ['one', 'two'])
    'one    two'

    >>> words2jline(14, ['one', 'two', 'three'])
    'one  two three'

    >>> words2jline(15, ['one', 'two', 'three'])
    'one  two  three'

    >>> words2jline(16, ['one', 'two', 'three'])
    'one   two  three'

    >>> words2jline(17, ['one', 'two', 'three'])
    'one   two   three'
    """
    nwords = len(words)
    if nwords == 1:
        return words[0]

    lenwords = sum(len(w) for w in words)
    lenspaces = width - lenwords
    space = ' '*(lenspaces / (nwords-1))

    remainder = lenspaces % (nwords-1)
    for i in range(remainder):
        words[i] = words[i] + ' '

    line = space.join(words)
    return line


def justify(text, width):
    r"""
    >>> justify('123 45 6', 7)
    '123  45\n6'
    """

    lines = []
    words = text.strip().split()

    current_line_words = []
    for w in words:
        total_width = (len(w) + 1 +  # current word + space
                       len(current_line_words) +  # at least once space between words
                       sum(len(x) for x in current_line_words)  # length of each word + 1 space
                       - 1)  # last word doesn't need a space
        if total_width > width:
            lines.append(words2jline(width, current_line_words))
            current_line_words = []
        current_line_words.append(w)

    # don't justify the last line if there is a remainder
    if current_line_words:
        lines.append(' '.join(current_line_words))

    return '\n'.join(lines)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    loremtext = "Consectetur modi eum assumenda commodi dolor velit deserunt facilis. Facilis nulla saepe quo nulla assumenda consequatur. Tempora ex culpa officiis repellendus iure obcaecati! Nobis sapiente aspernatur ratione vel quaerat. Libero reiciendis fugit vel enim dolores? Sunt harum officiis similique ipsam eius. Debitis debitis est reprehenderit velit quasi. Vitae eum saepe quas cupiditate quia! Ratione maxime magnam iure voluptas incidunt soluta, sint eos ullam vitae! Provident dolores maiores doloremque eius obcaecati dignissimos non. Obcaecati repellendus commodi ullam perferendis ab illo? Eius nobis exercitationem deserunt laudantium voluptatum quam autem rem. Ad voluptatibus magnam sequi incidunt ullam sit quas. Voluptate blanditiis tenetur sit."
    print justify(loremtext, 30)
