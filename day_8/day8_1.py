#!/usr/bin/python

lines = open('input.txt', 'r').readlines()

code = 0
memory = 0


for line in lines:
  escaped = False
  hex_chars = 0

  code += len(line)

  m = 0
  for l in line:
    if escaped:
      if l == 'x':
        hex_chars = 2
      escaped = False
    elif hex_chars > 0:
      hex_chars -= 1
    elif l == '"':
      continue
    else:
      m += 1
      if l == '\\':
       escaped = True    
 
  memory += m

print code - memory

