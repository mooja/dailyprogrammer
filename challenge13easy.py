def day(m, d):
    month_seq = map(int, "31 28 31 30 31 30 31 31 30 31 30 31".split())
    return sum(month_seq[:m]) + d

import ipdb; ipdb.set_trace()
ipdb.pm()
day(0, 1)
day(11, 31)
