#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 103 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/11erhd/10132012_challenge_103_easydifficult_text/
#
# May.07.2015

from random import random, choice


def make_trans_table(fname='leet_table.txt'):
    """ make_trans_table: create a conversion table {'A': ['4'], 'B': ['8', '6']...
        :fname: filename
        :returns: translation_table
    """
    table = {}
    with open(fname) as f:
        for line in f:
            cols = line.strip().split()
            table[cols[0]] = cols[1:]
    return table

def text2leet(text, table, conv_chance=1.0):
    """ text2leet: transcode text according to a given translation_table,
                   with the conv_chance probability of each letter to be
                   replaced.
        :text: text string
        :table: translation table
        :conv_chance: chance for each letter to be converted. 0 for no conversion, 1.0 
                      for whole conversion.
        :returns: translated text
    """
    output = []
    for char in text.upper():
        if char in table:
            if random() <= conv_chance:
                output.append(choice(table[char]))
            else:
                output.append(char)
        else:
            output.append(char)

    return ''.join(output)


def main():
    l33t_table = make_trans_table("leet_table.txt")
    text = """
    I must not fear.
    Fear is the mind-killer.
    Fear is the little-death that brings total obliteration.
    I will face my fear.
    I will permit it to pass over me and through me.
    And when it has gone past I will turn the inner eye to see its path.
    Where the fear has gone there will be nothing. Only I will remain.
    """
    print text2leet(text, l33t_table, 0.3)



if __name__ == '__main__':
    main()
    # I MUST NOT (=EAR.
    # FEA2 IS TH& emIND-|XIL|_ER.
    # F3AR IS THE Leye+TLE-DEAT|-| THAT B|`INC-es T[]†AL OBL!TERZTIΩN.
    # I WILL |=/\<E MY ʃE4R.
    # 3y3 WI7L P&R/|/|I1 IT TO PA§5 ¤V3R M€ AND THR0UG(-) (\/)E.
    # AND WHE// I7 HAS (_+ohNə PAzT I WI|1 TUR₪ TH€ INNElz EYE TO 5EE |Tes PATH.
    # UU:-:ERE THE ]=E@R HAS GO//\\//[- THERə WILL BE |\|OTHI|\|cj. O~L'/ eye WILL RE44AIN.
