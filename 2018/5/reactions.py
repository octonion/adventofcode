from string import ascii_lowercase
from operator import itemgetter

data = [i.strip() for i in open("input.txt").readlines()][0]

copy = data

i = 0
while i<len(data)-1:
    if (data[i].upper()==data[i+1].upper()) and not(data[i]==data[i+1]):
        data = data[:i]+data[i+2:]
        i = max(0,i-1)
    else:
        i += 1
print(len(data))

results = []
for l in ascii_lowercase:
    data = copy.replace(l,"").replace(l.upper(),"")
    i = 0
    while i<len(data)-1:
        if (data[i].upper()==data[i+1].upper()) and not(data[i]==data[i+1]):
            data = data[:i]+data[i+2:]
            i = max(0,i-1)
        else:
            i += 1
    results.append([l,len(data)])

ranked = sorted(results, key=itemgetter(1))

print(ranked[0])
