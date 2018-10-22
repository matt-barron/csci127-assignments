import random

prompt = 'This is the <adjective> <noun> that we have to <adverb> <verb>'
verbList = ['eat', 'truncate', 'defile', 'sabotage', 'slap', 'lick']
nounList = ['heron', 'dog', 'troglodyte', 'roommate', 'pet', 'murderer']
adjectiveList = ['loquacious', 'brooding', 'large', 'smooth', 'bumpy']
adverbList = ['smoothly', 'irritably']

def madLib (prompt):
    wordList = prompt.split()
    newList = []
    blankSpace = ' '
    for item in wordList:
        if item == '<verb>':
            newList.append(verbList[random.randrange(len(verbList))])
            newList.append(blankSpace)
        else:
            if item == '<noun>':
                newList.append(nounList[random.randrange(len(nounList))])
                newList.append(blankSpace)
            else:
                if item == '<adjective>':
                    newList.append(adjectiveList[random.randrange(len(adjectiveList))])
                    newList.append(blankSpace)
                else:
                    if item == '<adverb>':
                        newList.append(adverbList[random.randrange(len(adverbList))])
                        newList.append(blankSpace)
                    else:
                        newList.append(item)
                        newList.append(blankSpace)
    return ''.join(newList)

print(madLib(prompt))
