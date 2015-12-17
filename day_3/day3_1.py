#!/usr/bin/python

instructions = open('input.txt', 'r').read()

current_x = 0
current_y = 0

place_dict = {}

houses = 0

for i in instructions:
  if i == '<':
    current_x -= 1
  elif i == '>':
    current_x += 1
  elif i == 'v':
    current_y -= 1
  elif i == '^':
    current_y += 1
  else:
    continue

  current_code = str(current_x) + '_' + str(current_y)

  if current_code not in place_dict:
    place_dict[current_code] = 1
    houses += 1


print houses
