#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 187 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2l6dll/11032014_challenge_187_easy_a_flagon_of_flags/
#
# 25.April.2016

def parse_flag_abbrs(lines):
    short_long_map = {}
    for line in lines:
        s, l = line.split(':')
        short_long_map[s] = l
    return short_long_map


def parse_cmd(definition_lines, cmd_line):
    """
    >>> parse_cmd(['a:all', 'f:force', 'n:networking', 'N:numerical-list'], '-aN 12 --verbose 192.168.0.44')
    'flag: all\\nflag: numerical-list\\nparameter: 12\\nflag: verbose\\nparameter: 192.168.0.44'
    """

    short_long_mapping = {}
    for line in definition_lines:
        s, l = line.split(':')
        short_long_mapping[s] = l

    output_lines = []
    for token in cmd_line.split():
        if token.startswith('--'):
            output_lines.append('flag: ' + token[2:])
        elif token.startswith('-'):
            for flag in token[1:]:
                if flag in short_long_mapping:
                    output_lines.append('flag: ' + short_long_mapping[flag])
                else:
                    output_lines.append('unknown short flag: ' + flag)
        else:
            output_lines.append('parameter: ' + token)
    return '\n'.join(output_lines)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
