import numpy as np

data = open("input.txt").readlines()

locations = []
velocities = []
for row in data:
    a = row.strip().replace('>','').split(' velocity=<')
    x,y = [float(i) for i in a[0].replace('position=<','').split(',')]
    u,v = [float(i) for i in a[1].split(',')]
    locations.append(np.array([x,y]))
    velocities.append(np.array([u,v]))

n = len(locations)
ml = mean(locations)
mv = mean(velocities)

var('t')
variance = sum(((locations[i]+t*velocities[i]-ml-t*mv)**2 for i in range(0,n)))

root = diff(variance[0],t).roots(multiplicities=False,ring=RR)
time = round(root[0])

p = np.array([locations[i]+time*velocities[i] for i in range(0,n)],dtype=int).min(0)
q = np.array([locations[i]+time*velocities[i] for i in range(0,n)],dtype=int).max(0)

x1,y1 = p
x2,y2 = q

array = np.zeros((x2+1,y2+1),dtype=int)
for i in range(0,n):
    x = int(locations[i][0]+time*velocities[i][0])
    y = int(locations[i][1]+time*velocities[i][1])
    array[x,y] = 1

for j in range(y1-1,y2+1):
    for i in range(x1-1,x2+1):
        if array[i,j]==0:
            sys.stdout.write(' ')
        else:
            sys.stdout.write('*')
    print
print

print(time)
