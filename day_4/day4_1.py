#!/usr/bin/python

import hashlib


found = False
i = 1
secret = 'iwrupvqb'

while not found:
  s = secret + str(i)
  m = hashlib.md5()
  m.update(s)
  result = m.hexdigest()

  if result[0:5] == '00000':
    print i, result
    found = True

  i += 1
