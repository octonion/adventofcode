import future
import strutils
import tables

var data = readFile("input.txt").strip()

let backup = data

var i = 0
var stack: seq[char]
stack = @[]

while i<len(data):
    if len(stack)==0:
      stack.add(char(data[i]))
    elif (stack[^1].toUpperAscii()==data[i].toUpperAscii()) and not(stack[^1]==data[i]):
      discard stack.pop()
    else:
      stack.add(data[i])
    i += 1
echo(len(stack))

var results = initTable[char,int]()
let letters = {'a'..'z'}
              
for letter in letters:
  data = backup
  data = data.replace($letter)
  data = data.replace($letter.toUpperAscii())
  i = 0
  stack = @[]
  while i<len(data):
    if len(stack)==0:
      stack.add(data[i])
    elif (stack[^1].toUpperAscii()==data[i].toUpperAscii()) and not(stack[^1]==data[i]):
      discard stack.pop()
    else:
      stack.add(data[i])
    i += 1
  results[letter] = len(stack)

var m = len(backup)
for i,v in results:
  if v<m:
    m = v
echo m
