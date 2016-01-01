#!/usr/bin/python

from itertools import chain
from itertools import combinations
from operator import mul
from copy import deepcopy

packages = [int(x) for x in open('input.txt', 'r').readlines()]

total = sum(packages)
target = total/4

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


set_size = -1

possible_sets = []

for package_set in powerset(packages):
  if sum(package_set) == target:
    if set_size < 0:
      set_size = len(package_set)

    if len(package_set) > set_size:
      break
    
    possible_sets.append(package_set)

def product(a_list):
  return reduce(mul, a_list)

possible_sets.sort(key=product)

for a_set in possible_sets:
  packages_copy = deepcopy(packages)
  for package in a_set:
    packages_copy.remove(package)

  is_valid = False

  for package_set in powerset(packages_copy):
    if sum(package_set) == target:
      is_subset_valid = False
      packages_copy_copy = deepcopy(packages_copy)
      for package in package_set:
        packages_copy_copy.remove(package)

      for other_package_set in powerset(packages_copy_copy):
        if sum(other_package_set) == target:
          is_subset_valid = True
          break

      if is_subset_valid:       
        is_valid = True
        break


  if is_valid:
    print product(a_set)
    break
