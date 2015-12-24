#!/usr/bin/python

import copy

raw_transforms = open('input.txt', 'r').readlines()

molecule = raw_transforms.pop(-1).strip()

#removing the blank line
raw_transforms.pop(-1)

transforms = {}

for transform in raw_transforms:
  base, _, rule = transform.split(' ')
  rule = rule.strip()
  if not base in transforms:
    transforms[base] = []

  transforms[base].append(rule)

molecules_seen = {}

for base in transforms:
  i = 0
  while molecule.find(base, i) >= 0:
    j = molecule.find(base, i)
    k = j + len(base)
    for rule in transforms[base]:
      new_molecule = molecule[:j] + rule + molecule[k:]
      molecules_seen[new_molecule] = True
    i = j+1

print len(molecules_seen)
