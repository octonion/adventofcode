data = [i.strip() for i in open("input.txt").readlines()]

class Code():
    def __init__(self,val):
        self.val = val
    def __mul__(self,other):
        dot = 0
        right = ''
        for i in range(0,len(self.val)):
            if self.val[i]==other.val[i]:
                dot += 1
                right += self.val[i]
        return(dot,right)

n = len(data)
inner = []
max = 0
max_right = ''
matches = []
for i in range(0,n):
    for j in range(0,i):
        c = Code(data[i])
        d = Code(data[j])
        dot,right = c*d
        if dot > max:
            max = dot
            max_right = right
            matches = [c,d]
print(max,max_right)

        
        
