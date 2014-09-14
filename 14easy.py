def reverse_blocks(l, k):
    m = list()
    for i in range(len(l) // k):
        start_pos = i*k
        end_pos = (i+1)*k
        m += reversed(l[start_pos:end_pos])
    return m

l = range(10)
m = reverse_blocks(l, 3)
print(m)
