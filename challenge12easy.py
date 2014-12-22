import argparse


from itertools import permutations

p = argparse.ArgumentParser()
p.add_argument('word', help='word to permutate')
args = p.parse_args()
w = args.word

print "Permutations:"
for i in permutations(w):
    print ''.join(i)
