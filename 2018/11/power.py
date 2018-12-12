import numpy as np

input = 7165
power = np.zeros((301,301),dtype=int)
for x in range(1,301):
    for y in range(1,301):
        id = x+10
        p = id*y
        p += input
        p *= id
        pl = (int(np.floor(p/100)) % 10)-5
        power[x,y] = pl

mp = 0
for x in range(1,298):
    for y in range(1,298):
        total = np.sum(power[x:x+3,y:y+3])
        if total>mp:
            mx=x
            my=y
            mp=total
print(mx,my,mp)

mp = 0
for s in range(1,301):
    for x in range(1,302-s):
        for y in range(1,302-s):
            total = np.sum(power[x:x+s,y:y+s])
            if total>mp:
                ms=s
                mx=x
                my=y
                mp=total

print(mx,my,ms,mp)                
        
