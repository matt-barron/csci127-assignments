def canMakeWord(letters, word):
    letterslist = list(letters)
    for i in word:
        if i in letterslist:
            letterslist.remove(i)
        else:
            return False
    return True
print(canMakeWord("ladilmy", "daily"))
print(canMakeWord("eerriin", "eerie"))
print(canMakeWord("orrpgma", "program"))
print(canMakeWord("orppgma", "program"))
def withWild(letters, word):
     letterslist = list(letters)
     for i in word:
        if i in letterslist:
            letterslist.remove(i)
        elif "?" in letterslist:
            letterslist.remove("?")
        else:
            return False
     return True
print(withWild("ladilm?", "daily"))