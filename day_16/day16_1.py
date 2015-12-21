#!/usr/bin/python

aunts = open('input.txt', 'r').readlines()

sues = {}

for aunt in aunts:
  elems = aunt.split(' ')
  sue_info = {}
  for i in xrange(2,len(elems),2):
    key = elems[i].strip(':')
    value = int(elems[i+1].strip(','))
    sue_info[key] = value
  sues[elems[1].strip(':')] = sue_info

known_info = {'children': 3,
              'cats': 7,
              'samoyeds': 2,
              'pomeranians': 3,
              'akitas': 0,
              'vizslas': 0,
              'goldfish': 5,
              'trees': 3,
              'cars': 2,
              'perfumes': 1}


for sue in sues:
  sue_info = sues[sue]
  match = True
  for key in sue_info:
    if sue_info[key] != known_info[key]:
      match = False
      break

  if match:
    print sue
    break
