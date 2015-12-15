#!/usr/bin/python

instructions = open('input.txt', 'r').read()

current_floor = 0

for i in instructions:
  if i == '(':
    current_floor += 1
  elif i == ')':
    current_floor -= 1
  else:
    continue


print current_floor
