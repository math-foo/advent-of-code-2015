#!/usr/bin/python

limit = 34000000

primes = [2,3,5,7]

for i in xrange(10, limit/10):
  is_prime = True
  for p in primes:
    if i%p == 0:
      is_prime = False
      break
    if p**2 > i:
      break

  if is_prime:
    primes.append(i)
    
def sum_factors(n):
  global primes
  result = 1
  for p in primes:
    if n%p == 0:
      m = 1
      p_a = 1
      while n%p == 0:
        p_a *= p
        m += p_a
        n /= p
      result *= m
    if p > n:
      break
      
  return result


for i in xrange(500000, limit):
  result = sum_factors(i)

  if result*10 >= limit:
    print i
    break
