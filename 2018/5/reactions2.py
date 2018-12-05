from string import ascii_lowercase
from operator import itemgetter

data = [i.strip() for i in open("input.txt").readlines()][0]

copy = data

i = 0
stack = []
while i<len(data):
    if len(stack)==0:
        stack.append(data[i])
    elif (stack[-1].upper()==data[i].upper()) and not(stack[-1]==data[i]):
        stack.pop()
    else:
        stack.append(data[i])
    i += 1
print(len(stack))

results = []
for letter in ascii_lowercase:
    data = copy.replace(letter,"").replace(letter.upper(),"")
    i = 0
    stack = []
    while i<len(data):
        if len(stack)==0:
            stack.append(data[i])
        elif (stack[-1].upper()==data[i].upper()) and not(stack[-1]==data[i]):
            stack.pop()
        else:
            stack.append(data[i])
        i += 1
    results.append([letter,len(stack)])

ranked = sorted(results, key=itemgetter(1))

print(ranked[0][1])
