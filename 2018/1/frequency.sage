import numpy as np

data = np.loadtxt(open('input.txt', 'rb'), dtype='int')

n = sum(data)
l = len(data)

sums = []
sums_mod = []
sum = 0

repeats = {}
fracs = {}
min_index = l*l
min_sum = None
for idx, val in enumerate(data):
    sum += val
    if (sum%n) in sums_mod:
        if (l*floor(sum/n)+repeats[sum%n]-l*fracs[sum%n] < min_index):
            min_index = l*floor(sum/n)+repeats[sum%n]-l*fracs[sum%n]
            min_sum = sum
    else:
        sums.append(sum)
        sums_mod.append(sum%n)
        repeats[sum%n] = idx
        fracs[sum%n] = floor(sum/n)

print("Total sum = %s" %n)
print("First repeat = %s" %min_sum)
