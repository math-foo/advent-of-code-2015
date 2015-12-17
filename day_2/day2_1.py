#!/usr/bin/python

boxes = open('input.txt', 'r').readlines()

paper = 0

for box in boxes:
  sides = [int(side) for side in box.split('x')]
  sides.sort()
  paper += 3*sides[0] * sides[1] + 2 * sides[1] * sides[2] + 2 * sides [0] * sides[2]

print paper
