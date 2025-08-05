import numpy as np
import matplotlib.pyplot as plt

################################################################
rule = [[1,2], [2], [0]]
n = 50
dot_size = 4
dot_count_limit = 21557
################################################################

mat = [[rule[j].count(i) for j in range(3)] for i in range(3)]
alpha = float(1 / np.max(np.linalg.eig(np.array(mat))[0]))
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
  x += alpha
  y += alpha ** 2
plt.show()
