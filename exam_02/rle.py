def encode(s):
    count1= 0
    slist= list(s)
    count = []
    newl= []
    for i in range(len(slist)-1):
        if slist[i] == slist[i+1] or slist[i] == slist[i-1]:
               count1 += 1
        count.append([slist[i],count1])
    return count
print(encode("abbaaacddaaa"))