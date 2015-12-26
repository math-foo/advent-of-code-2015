#!/usr/bin/python

limit = 34000000

def sum_factors(n):
  x = max(1,n/50)
  count = 0
  for i in xrange(x, n+1):
    if n%i == 0 and n/i < 50:
      count += i

  return count

lowest = limit
max_result = 0

for i in xrange(786240, limit):
  result = sum_factors(i)

  if result > max_result:
    max_result = result

  if i % 1000 == 0:
    print i, max_result

  if result*11 >= limit:
    print i
    exit(0)

