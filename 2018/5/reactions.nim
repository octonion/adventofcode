import future
import strutils
import tables

var data = readFile("input.txt").strip()

let backup = data

var i = 0
while i<len(data)-1:
  if (data[i].toUpperAscii()==data[i+1].toUpperAscii()) and not(data[i]==data[i+1]):
    data = data[ .. (i-1)] & data[(i+2) .. ^1]
    i = max(0,i-1)
  else:
    i += 1
echo len(data)

var results = initTable[char,int]()
let letters = {'a'..'z'}

for letter in letters:
  data = backup
  data = data.replace($letter).replace($letter.toUpperAscii())
  i = 0
  while i<len(data)-1:
    if (data[i].toUpperAscii()==data[i+1].toUpperAscii()) and not(data[i]==data[i+1]):
      data = data[ .. (i-1)] & data[(i+2) .. ^1]
      i = max(0,i-1)
    else:
      i += 1
  results[letter] = len(data)

var m = len(backup)
for i,v in results:
  if v<m:
    m = v
echo m
