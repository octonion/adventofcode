data = [i.strip() for i in open("input.txt").readlines()]

two = 0
three = 0
for code in data:
    counts = {}
    for i in range(0,len(code)):
        if code[i] in counts.keys():
            counts[code[i]] += 1
        else:
            counts[code[i]] = 1
    print(counts)
    if (2 in counts.values()):
        two += 1
    if (3 in counts.values()):
        three += 1
        
print(two*three)
