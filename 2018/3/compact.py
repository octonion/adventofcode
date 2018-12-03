import numpy as np
import re

input = open("input.txt").readlines()

fabric = np.zeros((1000,1000),dtype=int)

data = map(lambda s: map(int, re.findall(r'-?\d+', s)), input)

claims = []
for (id, x, y, m, n) in data:
    claims.append([id,x,y,m,n])
    fabric[x:x+m,y:y+n] += 1

print(np.sum(fabric > 1))

for (id, x, y, m, n) in claims:
    if (np.sum(fabric[x:x+m,y:y+n])==m*n):
        print(id)
