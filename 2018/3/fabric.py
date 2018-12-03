import numpy as np

data = open("input.txt").readlines()

fabric = np.zeros((1001,1001),dtype=int)

input = []
for row in data:
    a = row.split()
    id = a[0]
    x,y = [int(i) for i in a[2].strip(':').split(',')]
    m,n = [int(i) for i in a[3].split('x')]
    input.append([id,x,y,m,n])
    for i in range(x,x+m):
        for j in range(y,y+n):
            fabric[i][j] += 1

for i in range(0,1001):
    for j in range(0,1001):
        if fabric[i][j]==1:
            fabric[i][j]=0
        if fabric[i][j]>1:
            fabric[i][j]=1

print(sum(sum(fabric)))

for id,x,y,m,n in input:
    overlap = False
    for i in range(x,x+m):
        for j in range(y,y+n):
            if fabric[i][j]==1:
                overlap = True
                break
    if not(overlap):
        print(id)
        break
