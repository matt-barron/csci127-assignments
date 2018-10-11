import random

def build_random_list(size,max_value):
    """
    Parameters:
      size : the number of elements in the lsit
      max_value : the max random value to put in the list
    """
    l = [] # start with an empty list

    # make a loop that counts up to size
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        # we could have written this instead of the above line:
        # l = l + [random.randrange(0,max_value)]
        i = i + 1
    return l
print(build_random_list(10,99))

def locate(l,value):
    if value in l:
        return l.index(value)
    else:
        return "-1"
print(locate([1,2,3,3,4,5,6],4))
print(locate([12,42,"pi",88],14))

def count(l,value):
    i = 0
    a=0
    while i <= len(l)-1:
        if l[i] == value:
            a= a+1
        i= i+1
    return a
print(count([12,3,3,3,5,6,6],3))
def reverse(l):
    i=0
    a=-1
    b=[]
    while i<= len(l)-1:
        b.append(l[a])
        i+=1
        a-=1
    return b
print(reverse([4,2,2,1]))
print(reverse([1, 2, 3, 4, 50]))
def pal(l):
    i=0
    a=-1
    b=[]
    while i<= len(l)-1:
        b.append(l[a])
        i+=1
        a-=1
    if l == b:
        return "true"
    else:
        return "false"      
print(pal([4,2,2,4]))
def increasing(l):
    i=0
    a=0
    b=a+1
    while i <= len(l)-1:
        a+=1       
        if l[b]>l[a]:
            return "increasing"  
print(increasing([1,9,1,1]))