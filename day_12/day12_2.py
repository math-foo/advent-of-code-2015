#!/usr/bin/python

import json

data = open('input.txt', 'r')

parsed_data = json.load(data)

total = 0

def extract_num(data):
  global total
  if isinstance(data, list):
    for elem in data:
      extract_num(elem)
  elif isinstance(data, dict):
    if 'red' in data or 'red' in data.values():
      return

    for elem in data.keys():
      extract_num(data[elem])
  elif isinstance(data, int):
    total += int(data)
    return

extract_num(parsed_data)
print total
