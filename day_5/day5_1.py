#!/usr/bin/python

strings = open('input.txt', 'r').readlines()


def nice(s):
  prev = '#'

  double = False
  vowel_count = 0
  vowels = {'a': 0, 'e': 0, 'i':0, 'o': 0, 'u': 0}
  bad_letters = {'b' : 0, 'd': 0, 'q': 0, 'y' : 0}

  for c in s:
    if c == prev:
      double = True

    if c in vowels:
      vowel_count += 1

    if ord(c) - ord(prev) == 1:
      if c in bad_letters:
        return False

    prev = c

  return (double and vowel_count > 2)

i = 0

for s in strings:
  if nice(s):
    i += 1

print i
