#!/usr/bin/python

instructions = open('input.txt', 'r').read()

current_floor = 0
position = 1

for i in instructions:
  if i == '(':
    current_floor += 1
  elif i == ')':
    current_floor -= 1
  else:
    continue

  if current_floor == -1:
    print position
    break

  position += 1


print current_floor
