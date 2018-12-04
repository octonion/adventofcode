import numpy as np
from datetime import datetime as dt
from operator import itemgetter

data = [i.strip() for i in open("input.txt").readlines()]

data.sort()

guards = {}
times = {}
id = None
start = None
for row in data:
    tags = row.split(']')
    dtime = dt.strptime(tags[0].strip('['),'%Y-%m-%d %H:%M')
    words = tags[1].split()
    if 'begins' in words:
        id = next(int(x.strip('#')) for x in words if '#' in x)
    elif 'falls' in words:
        start = dtime
    elif 'wakes' in words:
        end = dtime
        if id in guards.keys():
            guards[id] += end-start
            start_m = start.hour*60+start.minute
            end_m = end.hour*60+end.minute
            times[id][start_m:end_m] += 1
        else:
            guards[id] = end-start
            times[id] = np.zeros(24*60, dtype=int)
            start_m = start.hour*60+start.minute
            end_m = end.hour*60+end.minute
            times[id][start_m:end_m] += 1
            
sleep = sorted(guards.items(), key=lambda kv: kv[1], reverse=True)

id = sleep[0][0]
time = sleep[0][1]
minute = np.argmax(times[id])

print(id,time)
print(minute)

print(id*minute)

most = [[id,np.argmax(times[id]),np.max(times[id])] for id in times.keys()]
likely = sorted(most, key=itemgetter(2), reverse=True)

print(likely[0][0]*likely[0][1])
