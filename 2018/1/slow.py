import numpy as np

data = np.loadtxt(open('input.txt', 'rb'), dtype='int')

sums = []
sum = 0
found = False
while not(found):
    for val in data:
        sum += val
        if sum in sums:
            print(sum)
            found = True
            break
        else:
            sums.append(sum)
