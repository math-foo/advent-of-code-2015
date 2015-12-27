#!/usr/bin/python

raw_hp, raw_damage= open('input.txt', 'r').readlines()

enemy_hp =  int(raw_hp.split(' ')[-1].strip())
enemy_damage =  int(raw_damage.split(' ')[-1].strip())


magic_missile = {'c': 53, 'd': 4}
drain = {'c': 73, 'd': 2, 'h': 2}
shield = {'c': 113, 'a' : 7, 't': 6}
poison = {'c': 173, 'd': 3, 't': 6}
recharge = {'c': 229, 'm': 101, 't': 5}

spells = [magic_missile, drain, shield, poison, recharge]

min_mana_win = 10000

# So many gross magic numbers.
def play(you, enemy, spell, spell_costs, shield_left, poison_left, recharge_left):
  cost = 'c'
  damage = 'd'
  armor = 'a'
  hp = 'h'
  turns = 't'
  mana = 'm'
  global min_mana_win
  global spells

  if spell_costs > min_mana_win:
    return

  if shield_left > 0:
    shield_left -= 1
  if poison_left > 0:
    enemy[hp] -= 3
    poison_left -= 1
  if recharge_left > 0:
    you[mana] += 101
    recharge_left -= 1

  if enemy[hp] < 1:
    if spell_costs < min_mana_win:
      min_mana_win = spell_costs
    return

  # above or below possible wins before casting?
  if spell[cost] > you[mana]:
    return

  if spell[cost] == 113:
    if shield_left > 0:
      return
    shield_left = 6
  if spell[cost] == 173:
    if poison_left > 0:
      return
    poison_left = 6
  if spell[cost] == 229:
    if recharge_left > 0:
      return
    recharge_left = 5
  if spell[cost] == 53:
    enemy[hp] -= 4
  if spell[cost] == 73:
    enemy[hp] -= 2
    you[hp] += 2

  spell_costs += spell[cost]
  you[mana] -= spell[cost]

  if enemy[hp] < 1:
    if spell_costs < min_mana_win:
      min_mana_win = spell_costs
    return 

  current_armor = 0
  if shield_left > 0:
    shield_left -= 1
    current_armor = 7
  if poison_left > 0:
    enemy[hp] -= 3
    poison_left -= 1
  if recharge_left > 0:
    you[mana] += 101
    recharge_left -= 1

  if enemy[hp] < 1:
    if spell_costs < min_mana_win:
      min_mana_win = spell_costs
    return

  damage_done = max(1, enemy[damage] - current_armor)
  you[hp] -= damage_done

  if you[hp] < 1:
    return

  for s in spells:
    new_you = you.copy()
    new_enemy = enemy.copy()
    play(new_you, new_enemy, s, spell_costs, shield_left, poison_left, recharge_left)

for spell in spells:
    you = {'h': 50, 'm': 500}
    enemy = {'h': enemy_hp, 'd': enemy_damage}
    play(you, enemy, spell, 0, 0, 0, 0)

print min_mana_win
