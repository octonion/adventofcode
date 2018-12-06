import csv
import numpy as np

csv_input = open('input.txt')
input = csv.reader(csv_input)

data = [[int(x),int(y)] for (x,y) in input]

x1 = min(p[0] for p in data)
y1 = min(p[1] for p in data)
x2 = max(p[0] for p in data)
y2 = max(p[1] for p in data)

closest = {}
for i in range(x1,x2+1):
    for j in range(y1,y2+1):
        nearest = []
        min_d = x2+y2+2
        for n in range(0,len(data)):
            p = data[n]
            d = abs(p[0]-i)+abs(p[1]-j)
            if d < min_d:
                min_d = d
                nearest = [n]
            elif d == min_d:
                nearest.append(n)
        if len(nearest)==1:
            closest[str(i)+','+str(j)]=nearest[0]
        else:
            closest[str(i)+','+str(j)]=None

infinite = set({})
for j in range(y1,y2+1):
    infinite.add(closest[str(x1)+','+str(j)])
    infinite.add(closest[str(x2)+','+str(j)])
for i in range(x1,x2+1):
    infinite.add(closest[str(i)+','+str(y1)])
    infinite.add(closest[str(i)+','+str(y2)])

totals = {}
for m in range(0,len(data)):
    if not(m in infinite):
        totals[m] = sum(1 for n in closest.values() if m==n)

print(max(totals.values()))

###

distance = {}
for i in range(0,x2+1):
    for j in range(0,y2+1):
        td = 0
        for n in range(0,len(data)):
            p = data[n]
            d = abs(p[0]-i)+abs(p[1]-j)
            td += d
        distance[str(i)+','+str(j)]=td

print(sum(1 for d in distance.values() if d<10000))
