import time 
import random
list = []
for i in range(100):
    list.append(random.randrange(1,11))
print(list)

def max(l):
    p = []
    li = 0
    for i in range(1, len(list)):
        if list[i] > list[li]:
            li = i
    return li

def freq(l,val):
    f = 0
    for i in l:
        if i == val:
            f = f + 1
    return f


def mode(l):
    li=0
    a=l[0]
    msf=freq(l, l[0])
    for i in range(len(l)):
        test_freq=freq(l,l[i])
        if test_freq>msf:
            a=l[i]
            li=i
            msf=test_freq
    return "mode:", a

print(max(list))
print (freq(list, 6))
print(freq([1,2,2,2,2,3,4,5], 2))
print(mode([1,2,2,2,3,4,5]))
print(mode([1,1,1,1,2,4]))
