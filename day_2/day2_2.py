#!/usr/bin/python

boxes = open('input.txt', 'r').readlines()

ribbon = 0

for box in boxes:
  sides = [int(side) for side in box.split('x')]
  sides.sort()
  ribbon += 2 * sides[0] + 2 * sides[1] + sides[0] * sides[1] * sides [2]

print ribbon
