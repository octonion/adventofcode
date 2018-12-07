data = [[i.strip().split()[1],i.strip().split()[7]] for i in open("input.txt").readlines()]

data.sort()

before = {}
steps = set({})
for x,y in data:
    steps.add(x)
    steps.add(y)
    if y not in before.keys():
        before[y] = set({x})
    else:
        before[y].add(x)

workers = 5
total = 0
inactive = 5
active = {}

while len(steps)>0:

    # Add assisgnments

    possible = [x for x in steps if not(x in before.keys()) and not(x in active.keys())]
    possible.sort(reverse=True)

    # Assign possibles to inactive workers
    
    while len(possible)>0 and inactive>0:
        next = possible.pop()
        active[next] = ord(next)-ord('A')+1+60
        inactive -= 1

    print(active)
    # Determine next steps to finish
        
    change = min(active.values())
    total += change
    for k in active.keys():
        active[k] -= change
        
    done = set([k for k in active.keys() if active[k]==0])

    # Remove steps in done from active, before and steps

    inactive += len(done)

    active = {k: v for k, v in active.items() if v>0}

    for k in before.keys():
        before[k] = before[k].difference(done)
            
    before = {k: v for k, v in before.items() if len(v)>0}
    steps = steps.difference(done)

print(total)
