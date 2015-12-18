#!/usr/bin/python



def password_checker(password):
  if 'i' in password or 'o' in password or 'l' in password:
    return False
  
  prev_prev = '#'
  prev = '#'
  pairs_seen = []
  streak = False

  for c in password:
    if c == prev and c not in pairs_seen:
      pairs_seen.append(c)
    if ord(c) == ord(prev)+1 and ord(prev) == ord(prev_prev) +1:
      streak = True

    prev_prev = prev
    prev = c

  return (streak and len(pairs_seen) > 1)


def password_increment(password):
  new_password = list(password)

  z_value = ord('z')

  # does not handle incrementing to a longer string i.e. zz -> aaa
  while not password_checker(new_password):
    incr = True
    ind = -1
    while incr:
      c = new_password[ind]
      d = chr(ord(c) + 1)
      if ord(d) > z_value:
        ind -= 1
        continue
      else:
        incr = False
        if d == 'i' or d == 'l' or d == 'o':
          # will be j, m or p, no need to check not greater than z
          d = chr(ord(c) + 2)
        new_password[ind] = d
        ind += 1
        while ind < 0:
          new_password[ind] = 'a'
          ind += 1

  new_password = ''.join(new_password)
  return new_password

print password_increment('vzbxkghb')
