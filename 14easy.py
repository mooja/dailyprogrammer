def reverse_blocks(l, k):
    m = list()
    for i in xrange(0, len(l), k):
        m.extend(reversed(l[i:i+k]))
    return m

l = range(10)
m = reverse_blocks(l, 3)
print(m)
