#!/usr/bin/python

from itertools import chain
from itertools import combinations

buckets = [int(x) for x in open('input.txt', 'r').readlines()]

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


count = 0
min_count = len(buckets)

for entry in powerset(buckets):
  if sum(entry) == 150:
    if len(entry) < min_count:
      min_count = len(entry)
      count = 1
    elif len(entry) == min_count:
      count += 1

print count
