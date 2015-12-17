#!/usr/bin/python

instructions = open('input.txt', 'r').read()

current_x = 0
current_y = 0

robo_x = 0
robo_y = 0
santa_x = 0
santa_y = 0

place_dict = {}

houses = 0

santa = True

for i in instructions:
  if santa:
    current_x = santa_x
    current_y = santa_y
  else:
    current_x = robo_x
    current_y = robo_y

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

  if santa:
    santa_x = current_x  
    santa_y = current_y
  else:
    robo_x = current_x  
    robo_y = current_y

  santa = not santa


print houses
