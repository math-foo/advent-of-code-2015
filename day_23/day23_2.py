#!/usr/bin/python

program = open('input.txt', 'r').readlines()

program = [[instr.strip(',') for instr in line.strip().split(' ')] for line in program]


a = 1
b = 0
i = 0

while i >= 0 and i < len(program):
  line = program[i]
#  print a, b, i, line
  if line[0] == 'jio': # jump if one
    value = a if line[1] == 'a' else b
    if value == 1:
      jump_value = int(line[2][1:])
      if line[2][0] == '+':
        i += jump_value
      else:
        i -= jump_value
    else:
      i += 1
      continue
  elif line[0] == 'jie': # jump if even
    value = a if line[1] == 'a' else b
    if value % 2 == 0:
      jump_value = int(line[2][1:])
      if line[2][0] == '+':
        i += jump_value
      else:
        i -= jump_value
    else:
      i += 1
      continue
  elif line[0] == 'jmp': # jump
    value = int(line[1][1:])
    if line[1][0] == '+':
      i += value
    else:
      i -= value
    continue
  elif line[0] == 'inc': # increment
    if line[1] == 'a':
      a += 1
    else:
      b += 1
    i += 1
    continue
  elif line[0] == 'tpl': # triple
    if line[1] == 'a':
      a *= 3
    else:
      b *= 3
    i += 1
    continue
  elif line[0] == 'hlf': # halve
    if line[1] == 'a':
      a /= 2
    else:
      b /= 2
    i += 1
    continue
  else:
    print line
    exit(0)

print b
