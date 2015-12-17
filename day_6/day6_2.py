#!/usr/bin/python

instructions = open('input.txt', 'r').readlines()

lights = {}

count = 0

for i in instructions:
  if i[0:6] == 'toggle':
    a = i[6:]
    action = 'tog'
  if i[0:7] == 'turn on':
    a = i[7:]
    action = 'on'
  if i[0:8] == 'turn off':
    a = i[8:]
    action = 'off'

  a = a.split('through')
  a = [x.split(',') for x in a]
  lil_x = int(a[0][0])
  lil_y = int(a[0][1])
  big_x = int(a[1][0])
  big_y = int(a[1][1])

  for x in xrange(lil_x, big_x+1):
    for y in xrange(lil_y, big_y+1):
      cord = str(x) + '_' + str(y)
      if cord not in lights:
        lights[cord] = 0

      if action == 'on':
        lights[cord] += 1
      elif action == 'off':
        if lights[cord] > 0:
          lights[cord] -= 1
      elif action == 'tog':
        lights[cord] += 2


on = sum(lights.values())
print on
