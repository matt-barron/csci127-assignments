def makeacronym(w):
    x= w.split()
    b=[]
    for i in x:
        b.append(i[0].lower())
    return "".join(b)
print(makeacronym("laugh Out Loud"))
print(makeacronym("In my opinion"))
print(makeacronym("READ THE FINE MANUAL"))