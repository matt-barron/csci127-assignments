def no_letters(b):
    alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    happy=False
    for i in range(len(b)):
         if b[i] not in alpha and b[i] == "_":
             happy= True
         else:
             happy=False
    return happy
def adjacent(b):
    adjacent = False
    for i in range(len(b)):
        if b[i] != "_":
            if i != 0 and i != len(b)-1:
                if b[i] == b[i+1] or b[i] == b[i-1]:
                    adjacent = True
                else:
                    adjacent = False
    return adjacent
def rr(b):
    rr= False
    dict= {}
    for i in b:
        if i !="_":
            dict[i]=0
            for c in b:
                if i == c:
                    dict[i]+=1
            if dict[i] >=2 and "_" in b:
                rr= True
            else:
                rr= False
                break
    return rr
def happyLadybugs(b):
    if no_letters(b):
        return "Yes"
    elif adjacent(b):
        return "Yes"
    elif rr(b):
        return "Yes"
    else:
        return "No"
    return "No"
print(happyLadybugs("__"))
print(happyLadybugs("AABBB"))
print(happyLadybugs("X_Y__X"))
print(happyLadybugs("B_RRBR"))
