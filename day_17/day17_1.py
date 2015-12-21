#!/usr/bin/python

from itertools import chain
from itertools import combinations

buckets = [int(x) for x in open('input.txt', 'r').readlines()]

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


count = 0

for entry in powerset(buckets):
  if sum(entry) == 150:
    count += 1

print count
