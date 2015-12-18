#!/usr/bin/python


def say_n_see(numbers):
  d = numbers[0]
  count = 1
  new_numbers = ""

  for n in numbers[1:]:
    if d == n:
      count += 1
    else:
      new_numbers += str(count)
      new_numbers += str(d)
      d = n
      count = 1

  new_numbers += str(count)
  new_numbers += str(d)

  return new_numbers

numbers = "1113222113"


for i in xrange(50):
  numbers = say_n_see(numbers)

print len(numbers)
