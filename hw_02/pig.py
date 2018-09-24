#Matthew Barron/Emily Fang
def part_pig_latin(name):
    word = name.lower()
    firstl = word[0]
 
    if firstl in "aeiou":
        result = word + "ay"
    else:
        pig_latin = word[1:]+firstl+"ay"
    
    return pig_latin
    
print(part_pig_latin("eggs"))
print(part_pig_latin("apple"))
print(part_pig_latin("under"))
print(part_pig_latin("tree"))
