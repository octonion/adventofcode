data = [int(i) for i in open("input.txt").readlines()]

n = sum(data)
l = len(data)

sums = set([])
sums_mod = set([])
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
        sums.add(sum)
        sums_mod.add(sum%n)
        repeats[sum%n] = idx
        fracs[sum%n] = floor(sum/n)

print("Total sum = %s" %n)
print("First repeat = %s" %min_sum)
