def noUnhappy(b):
   alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
   happy=False
   for i in range(len(b)):
        if b[i] not in alpha and b[i] == "_":
            happy= True
        else:
            happy=False
   return happy
def adjacentcell(b):
    adjacent= False
    for i in range(len(b)):
        if i == 0:
           if b[i] == b[i+1]:
               adjacent = True
           else:
                adjacent = False
                break
        elif i == (len(b)-1):
            if b[i-1] == b[i]:
                adjacent = True
            else:
                adjacent = False
                break
        elif b[i] == b[i+1] or b[i] == b[i-1]:
          adjacent = True
    return adjacent

def underscore(b):
    for i in b:
        if i == "_":
            return True        
    return False
        
        
def twoplus(b):
    happybug = False
    for i in b:
        if i != "_":
            count = 0
            for c in b:
                if i == c:
                    count += 1
            if count >= 2:
                happybug = True
            else:
                happybug = False
                break
    return happybug

    return two
def happyLadybugs(b):
    alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if b == "":
        return "NO"
    if  noUnhappy(b):
        return "YES"
    if adjacentcell(b):
        return "YES"
    elif underscore(b):
        if twoplus(b):
            return "YES"
        else:
            return "NO"
    return "NO"

    
    
print(happyLadybugs("__"))
print(happyLadybugs("AABB"))
print(happyLadybugs("X_Y__X"))
print(happyLadybugs("B_RRBR"))
'''no spaces
no happy configuration
range should be range(len(b-1))
if "_" in b
need at least two ladybugs of each color and at least one empty cell
'''

