class Rectangle:
    def __init__(self, x1, y1, x2, y2, id):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.id = set(id)
        
data = open("input.txt").readlines()

input = []
for row in data:
    a = row.split()
    id = int(a[0].strip('#'))
    x,y = [int(i) for i in a[2].strip(':').split(',')]
    m,n = [int(i) for i in a[3].split('x')]
    input.append(Rectangle(x,y,x+m,y+n,[id]))

n = len(input)
output = [] #set({})
for i in range(0,n):
    r = input[i]
    for s in output:
        # r and s overlap
        if not((r.x2 <= s.x1 or s.x2 <= r.x1) or
            (r.y2 <= s.y1 or s.y2 <= r.y1)):
            
            # Split r and s into 1, 2, 3, 4, 5 pieces
            # Delete s from output
            # Add pieces to output
            input[i].id = input[i].id.union(s.id)
            s.id = s.id.union(r.id)
            
    output.append(input[i])

for i in output:
    if len(i.id)==1:
        print(list(i.id)[0])
            
