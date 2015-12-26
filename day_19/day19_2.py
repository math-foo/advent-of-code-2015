#!/usr/bin/python

import copy

raw_transforms = open('input.txt', 'r').readlines()

molecule = raw_transforms.pop(-1).strip()
atoms = []

while len(molecule) > 0:
  atom = molecule[0]
  if len(molecule) > 1 and molecule[1].islower():
    atom = molecule[0:2]
    molecule = molecule[2:]
  else:
    molecule = molecule[1:]

  atoms.append(atom)

#removing the blank line
raw_transforms.pop(-1)

transforms = {}

start = 'Rn'
end = 'Ar'
spacer = 'Y'

steps = 0

while end in atoms:
  j = atoms.index(end) + 1
  i = j -  atoms[:j][::-1].index(start) - 2
  x = len(atoms[i:j])
  steps += (x - 3 - 2 * atoms[i:j].count(spacer)) # each additional Y adds 2 to len of step
  atoms = atoms[:i] + ['X'] + atoms[j:]


steps += (len(atoms) - 1)
print steps

