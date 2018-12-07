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

order = ''

while len(steps)>0:
    possible = [x for x in steps if not(x in before.keys())]
    possible.sort()
    next = possible[0]
    order += next
    keys = before.keys()
    for k in keys:
        if next in before[k]:
            before[k].remove(next)
    before = {k: v for k, v in before.items() if len(v)>0}
    steps.remove(next)

print(order)
