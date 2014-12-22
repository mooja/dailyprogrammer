import math


from decimal import *
from fractions import Fraction
from math import factorial as fact

def get_nth_decimal_digit_of_pi(i):
    quotient = i * (2**i) * (fact(i)**2)
    denominator = fact(2*i)
    return Fraction(quotient, denominator)

digits = [get_nth_decimal_digit_of_pi(d) for d in range(1, 11)]
s = sum(digits)
