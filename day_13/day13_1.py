#!/usr/bin/python

import itertools

happiness = open('input.txt', 'r').readlines()

people = {}
couple_dict = {}

for h in happiness:
  elements = h.split(' ')
  couple = [elements[0], elements[-1].strip().strip('.')]
  for person in couple:
    if person not in people:
      people[person] = True
  person_code = couple[0] + '_' + couple[1]
  value = int(elements[3])
  if elements[2] == 'lose':
    value *= -1
  couple_dict[person_code] = value


max_happy = 0
n = len(people.keys())

# BRUTE FORCE
for seating in list(itertools.permutations(people.keys())):
  result = 0
  for i in xrange(0, len(seating)):
    person = seating[i]
    left = seating[(i-1) % n]
    right = seating[(i+1) % n]
    left_pair = person + '_' + left
    right_pair = person + '_' + right
    left_value = couple_dict[left_pair]
    right_value = couple_dict[right_pair]
    result += left_value + right_value

  if result > max_happy:
    max_happy = result

print max_happy
