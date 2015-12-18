#!/usr/bin/python

import itertools

distances = open('input.txt', 'r').readlines()

cities = {}
dist_dict = {}

for d in distances:
  elements = d.split(' ')
  city_pair = [elements[0], elements[2]]
  for city in city_pair:
    if city not in cities:
      cities[city] = True
  city_pair.sort()
  distance = int(elements[-1])
  city_code1 = city_pair[0] + '_' + city_pair[1]
  city_code2 = city_pair[1] + '_' + city_pair[0]
  dist_dict[city_code1] = distance
  dist_dict[city_code2] = distance


max_travel = 0

# BRUTE FORCE
for travel in list(itertools.permutations(cities.keys())):
  result = 0
  for i in xrange(0, len(travel)-1):
    code = travel[i] + '_' + travel[i+1]
    result += dist_dict[code]

  if result > max_travel:
    max_travel = result

print max_travel
