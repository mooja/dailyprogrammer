#!/usr/bin/env python
# encoding: utf-8

# array inversion sort using merge sort style divide and conquer approach


def inv_count(seq, sslice=None):
    if sslice is None:
        sslice = slice(0, len(seq))
    if sslice.stop - sslice.start <= 1:
        return 0

    split_pos = sslice.start + ((sslice.stop - sslice.start) / 2)
    left_slice = slice(sslice.start, split_pos)
    right_slice = slice(split_pos, sslice.stop)

    # these recursive calls have sideffects of sorting sub slices
    left_count = inv_count(seq, left_slice)
    right_count = inv_count(seq, right_slice)
    count = left_count + right_count
    # subslices are now sorted

    sorted_seq = []
    j = left_slice.start
    k = right_slice.start
    while j < left_slice.stop and k < right_slice.stop:
        if seq[j] < seq[k]:
            sorted_seq.append(seq[j])
            j += 1
        else:
            count += left_slice.stop - j
            sorted_seq.append(seq[k])
            k += 1

    sorted_seq.extend(seq[j:left_slice.stop])
    sorted_seq.extend(seq[k:right_slice.stop])
    seq[sslice.start:sslice.stop] = sorted_seq[:]

    return count


if __name__ == '__main__':
    with open("IntegerArray.txt") as f:
        seq = f.readlines()
        seq = [int(e.strip()) for e in seq]
        invs = inv_count(seq)

        print "Counter {} inversions".format(invs)
