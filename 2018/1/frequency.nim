import math
import sequtils
import strutils
import future
import tables

proc floorDiv*[T: SomeInteger](x, y: T): T =
  ## Floor division is conceptually defined as ``floor(x / y)``.
  ## This is different from the ``div`` operator, which is defined
  ## as ``trunc(x / y)``. That is, ``div`` rounds towards ``0`` and ``floorDiv``
  ## rounds down.
  result = x div y
  let r = x mod y
  if (r > 0 and y < 0) or (r < 0 and y > 0): result.dec 1
  
var input = split(readFile("input.txt"))
let data = lc[parseInt(i) | (i <- input[0..^2]), int]

let n = sum(data)
let l = len(data)

var sums = newSeq[int]()
var sums_mod = newSeq[int]()
var sum = 0

var repeats = initTable[int, int]()
var fracs = initTable[int, int]()
var min_index = l*l
var min_sum: int

for idx, val in data:
  sum += val
  if (sum%%n) in sums_mod:
    if (l*floorDiv(sum,n)+repeats[sum mod n]-l*fracs[sum mod n] < min_index):
      min_index = l*floorDiv(sum,n)+repeats[sum mod n]-l*fracs[sum mod n]
      min_sum = sum
  else:
    sums.add(sum)
    sums_mod.add(sum mod n)
    repeats[sum mod n] = idx
    fracs[sum mod n] = floorDiv(sum,n)

echo "Total sum = ",n
echo "First repeat = ",min_sum
