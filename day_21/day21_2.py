#!/usr/bin/python

import math

raw_hp, raw_damage, raw_armor = open('input.txt', 'r').readlines()

e_hp =  int(raw_hp.split(' ')[-1].strip())
e_damage =  int(raw_damage.split(' ')[-1].strip())
e_armor =  int(raw_armor.split(' ')[-1].strip())

weapons = { 4: 8, 5: 10, 6: 25, 7: 40, 8: 74}
armors = {1: 13, 2: 31, 3: 53, 4: 75, 5: 102, 0: 0}

rings = {25: [1,0], 50: [2,0], 100: [3,0], 20: [0,1], 40: [0,2], 80: [0,3]}

max_cost = 0

for w in weapons:
  for a in armors:
    rounds_survive = math.ceil(100/max(1, e_damage - a))
    rounds_e_survive = math.ceil(100/max(1, w - e_armor))
    if rounds_survive < rounds_e_survive:
      cost = weapons[w] + armors[a]
      if cost > max_cost:
        max_cost = cost
      for r in rings:
        r_w, r_a = rings[r]
        rounds_survive = math.ceil(100/max(1, e_damage - (a+r_a)))
        rounds_e_survive = math.ceil(100/max(1, (w+r_w) - e_armor))
        if rounds_survive < rounds_e_survive:
          cost = weapons[w] + armors[a] + r
          if cost > max_cost:
            max_cost = cost
          for r2 in rings:
            if r == r2:
              continue    
            r2_w, r2_a = rings[r2]
            rounds_survive = math.ceil(100/max(1, e_damage - (a+r_a+r2_a)))
            rounds_e_survive = math.ceil(100/max(1, (w+r_w+r2_w) - e_armor))
            if rounds_survive < rounds_e_survive:
              cost = weapons[w] + armors[a] + r + r2
              if cost > max_cost:
                max_cost = cost
       
print max_cost
