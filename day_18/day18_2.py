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

lights[0][0] = 1
lights[0][99] = 1
lights[99][0] = 1
lights[99][99] = 1

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
  lights[0][0] = 1
  lights[0][99] = 1
  lights[99][0] = 1
  lights[99][99] = 1

print sum([sum(x) for x in lights])

