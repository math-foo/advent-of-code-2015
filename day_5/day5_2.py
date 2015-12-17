#!/usr/bin/python

strings = open('input.txt', 'r').readlines()


def nice(s):
  prev = '#'
  prev_prev = '#'
  pairs = {}

  repeated_pair = False
  repeated_one = False
  
  p = 0

  for c in s:
    if c == prev_prev:
      repeated_one = True

    new_pair = prev + c
    if new_pair in pairs:
      if p - pairs[new_pair] >= 2:
        repeated_pair = True
    else:
      pairs[new_pair] = p

    p += 1
    prev_prev = prev
    prev = c


  return (repeated_pair and repeated_one)

i = 0

for s in strings:
  if nice(s):
    i += 1

print i
