def reverse_blocks(lst, block_length):
    result = list()
    for i in xrange(0, len(list), block_length):
        result.extend(reversed(lst[i:i+block_length]))
    return result

l = range(10)
m = reverse_blocks(l, 3)
print(m)
