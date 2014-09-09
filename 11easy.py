import argparse
from datetime import date


parser = argparse.ArgumentParser()
parser.add_argument("day", help="day [0-12]", type=int)
parser.add_argument("month", help="month [0-12]", type=int)
parser.add_argument("year", help="year", type=int)
args = parser.parse_args()

mapping = {0: 'monday', 1: 'tuesday',
           2: 'wednesday', 3: 'thursday',
           4: 'friday', 5: 'saturday',
           6: 'sunday'}

day, month, year = args.day, args.month, args.year
d = date(year, month, day)

print mapping[d.weekday()]
