#!/usr/bin/python

import numpy as np

ingrdnts = open('input.txt', 'r').readlines()

array_elems = []
calories = []

for i in ingrdnts:
  elems = i.split(' ')
  calories.append(int(elems[10]))
  array_elems.append([int(x.strip(',')) for x in [elems[2], elems[4], elems[6], elems[8]]])

props = np.array(array_elems)
calories = np.array(calories)

max_score = 0

# I *should* be partitioning 100 and then rearranging it; but I am lazy
for a in xrange(0,101):
  if a * calories[0] > 500:
    break
  for b in xrange(0,101):
    if a + b > 100:
      break

    if a * calories[0] + b * calories[1] > 500:
      break
   
    for c in xrange(0,101):
      if a + b + c > 100:
        break
   

      d = 100 - a - b - c
      
      vec = np.array([a, b, c, d])
      total_calories = vec.dot(calories)
      if total_calories != 500:
        continue

      result = vec.dot(props)
      value = np.prod([max(0, r) for r in result])
      if value > max_score:
        max_score = value

print max_score
      
