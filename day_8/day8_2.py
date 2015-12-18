#!/usr/bin/python

lines = open('input.txt', 'r').readlines()

original = 0
new = 0


for line in lines:
  original += len(line)

  n = 2
  for l in line:
    n += 1
    if l == '\\' or l == '"':
      n += 1
 
  new += n

print new - original

