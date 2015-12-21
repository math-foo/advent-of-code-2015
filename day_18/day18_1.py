#!/usr/bin/python

import copy

raw_lights = open('input.txt', 'r').readlines()

lights = []

def light(x):
  if x == '#':
    return 1
  else:
    return 0

for row in raw_lights:
  b_row = [light(x) for x in row]
  lights.append(b_row)

for step in xrange(0,100):
  new_lights = copy.deepcopy(lights)
  for i in xrange(0,100):
    for j in range(0,100):
      nbrs_on = 0
      if i > 0:
        nbrs_on += lights[i-1][j]
        if j > 0:
          nbrs_on += lights[i-1][j-1] 
        if j < 99:
          nbrs_on += lights[i-1][j+1]

      if i < 99:
        nbrs_on += lights[i+1][j]
        if j > 0:
          nbrs_on += lights[i+1][j-1] 
        if j < 99:
          nbrs_on += lights[i+1][j+1]
 
      if j > 0:
        nbrs_on += lights[i][j-1]
 
      if j < 99:
        nbrs_on += lights[i][j+1]

      if nbrs_on == 3:
        new_lights[i][j] = 1
      elif nbrs_on != 2:
        new_lights[i][j] = 0
        
  lights = new_lights

print sum([sum(x) for x in lights])

