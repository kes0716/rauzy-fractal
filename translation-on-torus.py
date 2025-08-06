import numpy as np
import matplotlib.pyplot as plt

################################################################
rules = [
    [[1],[2],[0, 2]],    #0, 01, 0102, (-1) + (-2) + (-3)
    [[0,1], [2], [0]],    #0, 01, 012, (-1) + (-3)
    [[1,2], [2], [0]],    #0, 12, 20, (-3) + (-2)
    [[1], [2], [2,1,0]],  #0, 1, 2, (-1) + (-2) + (-3)
    [[1], [2], [0,1]],    #0, 1, 2, (-3) + (-2)
    [[0,1], [2], [0,0]],  #0, 01, 012, (-1) + (-3) + (-3)
    [[2,0], [0], [0,1]]   #0, 20, 0120, (-2) + (-1) + (-3)
]
n = 50
dot_size = 4
dot_count_limit = 21557
basis = [ [1,0], [-1, 1] ]  #alpha, alpha^2
assert(abs(basis[0][0] * basis[1][1] - basis[0][1] * basis[1][0]) == 1)
################################################################

for rule in rules:
  mat = [[rule[j].count(i) for j in range(3)] for i in range(3)]
  eigvals = np.linalg.eig(np.array(mat))[0]
  dorm = None
  flag = False
  for v in eigvals:
    if abs(v) >= 1:
      if dorm is not None or np.imag(v) > 1:
        print("Not a Pisot substitution")
        flag = True
        break
      else:
        dorm = v
  if flag:
    continue
  alpha = float(1 / dorm)
  print(rule)
  print(alpha)
  l = [0]
  for i in range(n):
    tl = []
    for x in l:
      tl.extend(rule[x])
    if len(tl) > dot_count_limit:
      break
    l = tl
  x = 0
  y = 0
  colors = ['r', 'g', 'b']
  fig = plt.figure(figsize=(12, 12))
  plt.xlim(0, 1.0)
  plt.ylim(0, 1.0)
  for c in l:
    plt.plot(x%1.0, y%1.0, f"{colors[c]}o", markersize = dot_size)
    x += basis[0][0] * alpha + basis[0][1] * alpha ** 2
    y += basis[1][0] * alpha + basis[1][1] * alpha ** 2
  plt.show()
