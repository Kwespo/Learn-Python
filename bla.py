p = 2

pr = 10

e = 1

if pr < p:
  p = p - (pr * e)

elif p == 0:
  pr = pr - ((pr / 3) * e)

elif pr > p:
  dpr = pr - p
  dpr = dpr - ((pr / 3) * e)
  pr = pr - dpr
  p = p - (pr * e)

print(f"{p} : {pr}")

"Expected results:"
"""
e = 1 :: e = 1
p = 10 :: p = 8
pr = 2 :: pr = 2


e = 1 :: e = 1
p = 2 :: p = 0
pr = 10
pr = 
"""