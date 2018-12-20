def countPlurals(line):
    count = 0
    linelist= line.split()
    for i in linelist:
        if i[-1] == "s":
            count
    return count, linelist
print(countPlurals("dogs and cats"))
print(countPlurals("snakes and ladders snake"))
def notPossessive(line):
    count = 0
    linelist= line.split()
    for i in linelist:
        if i[-1] == "s" and i[-2] != "'" :
            count +=1
        
    return count
print(notPossessive("gorillas gorilla's cats"))