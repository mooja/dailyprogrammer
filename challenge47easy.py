#!/usr/bin/env python
# encoding: utf-8

#######################################################################
#                  challenge 47 easy - Ceaser Cypher                  #
#######################################################################

from string import lowercase
from string import uppercase
from string import maketrans


def ceasar_cypher(offset, message):
    def shift_alphabet(offset, alphabet_string):
        wrapped = alphabet_string[offset:]
        rest = alphabet_string[:offset]
        return wrapped + rest

    shifted_lowercase = shift_alphabet(offset, lowercase)
    shifted_uppercase = shift_alphabet(offset, uppercase)
    translation_table = maketrans(lowercase+uppercase,
                                  shifted_lowercase+shifted_uppercase)

    return message.translate(translation_table)


def rot13(message):
    return ceasar_cypher(13, message)


if __name__ == '__main__':
    cypher = '''
    Spzalu - zayhunl dvtlu sfpun pu wvukz kpzaypibapun zdvykz pz uv ihzpz mvy h 
    zfzalt vm nvclyutlua.  Zbwyltl leljbapcl wvdly klypclz myvt h thukhal myvt aol 
    thzzlz, uva myvt zvtl mhyjpjhs hxbhapj jlyltvuf. Fvb jhu'a lewlja av dplsk 
    zbwyltl leljbapcl wvdly qbza 'jhbzl zvtl dhalyf ahya aoyld h zdvyk ha fvb! P 
    tlhu, pm P dlua hyvbuk zhfpu' P dhz hu ltwlylyvy qbza iljhbzl zvtl tvpzalulk 
    ipua ohk sviilk h zjptpahy ha tl aolf'k wba tl hdhf!... Ho, huk uvd dl zll aol 
    cpvslujl puolylua pu aol zfzalt! Jvtl zll aol cpvslujl puolylua pu aol zfzalt! 
    Olsw! Olsw! P't ilpun ylwylzzlk!'''

    for i in range(1, 27):
        step = raw_input('Try translating using rot{}'.format(i))
        print ceasar_cypher(i, cypher).strip()
        print
