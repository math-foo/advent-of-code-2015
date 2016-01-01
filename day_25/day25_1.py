#!/usr/bin/python

instructions = open('input.txt', 'r').read().split(' ')

row = int(instructions[-3].strip(','))
col = int(instructions[-1].strip('.\n'))

def sum_1_to_n(n):
  return ((n+1) * n)/2

row_col_steps = sum_1_to_n(col + row - 1) - row

value = 20151125
mult_value = 252533
div_value = 33554393


for i in xrange(0,row_col_steps):
  value *= mult_value
  value %= div_value

print value 
