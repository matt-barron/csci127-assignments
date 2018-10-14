def filterodd(l):
    i=0
    oddl=[]
    while i <= len(l)-1:
        if l[i]%2 != 0:
            oddl.append(l[i])
        i+=1
    return oddl
print(filterodd([1,2,3,4,5,6]))
print(filterodd([11,231,14,50,23,12]))
def mapsquare(l):
    i=0
    sq=[]
    while i<= len(l)-1:
        sq.append(l[i]**2)
        i+=1
    return sq
print(mapsquare([2,5,6]))
print(mapsquare([3,9,10]))