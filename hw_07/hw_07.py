import random
dict1 = {}
dict2 = {}
dict1['nouns'] = ['heron', 'dog', 'troglodyte', 'roommate', 'pet', 'murderer']
dict1['verbs'] = ['eat', 'truncate', 'defile', 'sabotage', 'slap', 'lick']
dict1['adjectives']= ['smelly', 'imposing', 'large', 'tiny']
dict1['adverbs']=  ['smoothly', 'irritably']
dict2['nouns'] = ['teacher', 'doctor', 'king', 'firefighter', 'police officer']
dict2['verbs'] = ['eat', 'kick', 'duel']
dict2['adjectives']= ['terrible', 'loud', 'strange']
dict2['adverbs']= ['quietly', "joyfully", "sadly", "quickly"]
prompt = 'This is the <adjective> <noun> that we have to <adverb> <verb>'
def madLib (prompt,b):
    wordList = prompt.split()
    newList = []
    blankSpace = ' '
    for i in wordList:
         if i == '<verb>':
            newList.append(b['verbs'][random.randrange(len(b['verbs']))])
            newList.append(blankSpace)
         else:
             if i == '<noun>':
                 newList.append(b['nouns'][random.randrange(len(b['nouns']))])
                 newList.append(blankSpace)
             else:
                 if i == '<adjective>':
                     newList.append(b['adjectives'][random.randrange(len(b['adjectives']))])
                     newList.append(blankSpace)
                 else:
                     if i == '<adverb>':
                         newList.append(b['adverbs'][random.randrange(len(b['adverbs']))])
                         newList.append(blankSpace)
                     else:
                         newList.append(i)
                         newList.append(blankSpace)
    return ''.join(newList)



print(madLib(prompt,dict1))
print(madLib(prompt,dict2))