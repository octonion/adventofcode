from string import ascii_lowercase
from operator import itemgetter

data = open("input.txt").read().strip()

F.<a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z> = FreeGroup()

product = ''
for ii in range(0,len(data)):
    letter = data[ii]
    if letter.isupper():
        product += '*'+letter.lower()+'**-1'
    else:
        product += '*'+letter

result = eval(product[1:])
print(len(result.Tietze()))

results = []
for letter in ascii_lowercase:
    #G = F/[eval(letter),eval(letter+'**2')]
    #G = F/[eval(letter),eval(letter+'*'+letter)]
    G = F/[eval(letter),eval(letter+'**-1')]
    R = G.rewriting_system()
    reduced = R.reduce(result)
    results.append([letter,len(reduced.Tietze())])

ranked = sorted(results, key=itemgetter(1))
print(ranked[0])

# Slower

#results = []
#for letter in ascii_lowercase:
#    reduced = eval(product[1:].replace(letter,'F.one()'))
#    results.append([letter,len(reduced.Tietze())])

#ranked = sorted(results, key=itemgetter(1))
#print(ranked[0])
