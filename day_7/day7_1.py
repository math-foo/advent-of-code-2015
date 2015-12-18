#!/usr/bin/python

instructions_raw = open('input.txt', 'r').readlines()


instructions = [i.split(' ') for i in instructions_raw]
wires = {}

# extract constant wires
run = []
for i in instructions:
  if len(i) == 3 and i[0].isdigit():
    wire = i[2].strip()
    wires[wire] = int(i[0])
    run.append(i)

for r in run:
  instructions.remove(r)

while 'a' not in wires:
  run = []
  for i in instructions:
    if i[1] == 'RSHIFT':
      if i[0] in wires:
        value = wires[i[0]] >> int(i[2])
        wires[i[4].strip()] = value
        run.append(i)
      else:
        continue
    elif i[1] == 'LSHIFT':
      if i[0] in wires:
        value = wires[i[0]] << int(i[2])
        wires[i[4].strip()] = value
        run.append(i)
      else:
        continue
    elif i[1] == 'OR':
      if (i[0] in wires or i[0].isdigit()) and (i[2] in wires or i[2].isdigit()):
        lvalue = wires[i[0]] if i[0] in wires else int(i[0])
        rvalue = wires[i[2]] if i[2] in wires else int(i[2])
        value = lvalue | rvalue
        wires[i[4].strip()] = value
        run.append(i)
      else:
        continue
    elif i[1] == 'AND':
      if (i[0] in wires or i[0].isdigit()) and (i[2] in wires or i[2].isdigit()):
        lvalue = wires[i[0]] if i[0] in wires else int(i[0])
        rvalue = wires[i[2]] if i[2] in wires else int(i[2])
        value = lvalue & rvalue
        wires[i[4].strip()] = value
        run.append(i)
      else:
        continue
    elif i[1] == '->':
      if i[0] in wires:
        value = wires[i[0]]
        wires[i[2].strip()] = value
        run.append(i)
      else:
        continue 

    elif i[0] == 'NOT':
      if i[1] in wires:
        value = ~wires[i[1]]
        wires[i[3].strip()] = value
        run.append(i)
      else:
        continue 

  for r in run:
    instructions.remove(r)

print wires['a']
