import numpy as np

data = open("input.txt").readlines()

input = []
for id,row in enumerate(data):
    a = row.strip().replace('>','').split(' velocity=<')
    x,y = [int(i) for i in a[0].replace('position=<','').split(',')]
    u,v = [int(i) for i in a[1].split(',')]
    input.append([id,x,y,u,v])

t = 0
id1,x1,y1,u1,v1 = input[0]
n = 0.0
for id2,x2,y2,u2,v2 in input:
    if (u2==u1 and v2==v1):
        continue
    t += -((u2-u1)*(x2-x1)+(v2-v1)*(y2-y1))/((u2-u1)**2+(v2-v1)**2)
    n += 1

t = int(np.floor(t/n))

x1 = 1000
y1 = 1000
x2 = 0
y2 = 0
for id,x0,y0,u,v in input:
    x = int(x0+t*u)
    y = int(y0+t*v)
    x1 = min(x,x1)
    y1 = min(y,y1)
    x2 = max(x,x2)
    y2 = max(y,y2)

m = max(x2,y2)+1
array = np.zeros((m,m),dtype=int)
for id,x0,y0,u,v in input:
    x = int(x0+t*u)
    y = int(y0+t*v)
    array[x,y] = 1

for j in range(y1-1,y2+1):
    for i in range(x1-1,x2+1):
        if array[i,j]==0:
            print(' ',end='')
        else:
            print('*',end='')
    print()
print()

print(t)
