def addline(d, line):
    lowerline= line.lower()
    lowerlinelist= lowerline.split()
    for i in lowerlinelist:
        if i[0] in d:
            d[i[0]]= d[i[0]] + [i]
        else:
            d[i[0]] = [i]
    return d
dict= {}
print(addline(dict, "Hello world"))
print(addline(dict, "what bird"))
print(addline(dict, "fellow"))
print(addline(dict, "cat"))
print(addline(dict, "turtle"))
def spellcheck(d, word):
    lowerword= word.lower()
    if word[0] in d:
        if word in d[word[0]]:
            return True
        else:
            return False
print(spellcheck(dict, "turtle"))
    