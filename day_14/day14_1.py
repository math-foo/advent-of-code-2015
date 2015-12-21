#!/usr/bin/python

reindeer = open('input.txt', 'r').readlines()

speeds = {}

for r in reindeer:
  elements = r.split(' ')
  speeds[elements[0]] = [int(elements[3]), int(elements[6]), int(elements[-2])]


time = 2503
winning = 0

for entry in speeds:
  speed, travel_time, rest_time = speeds[entry]
  cycle_time = travel_time + rest_time
  cycle_distance = travel_time * speed
  cycles = time / cycle_time
  distance = cycle_distance * cycles
  remainder = time % cycle_time
  if remainder >= travel_time:
    distance += cycle_distance
  else:
    distance += remainder * speed
  if distance > winning:
    winning = distance

print winning
