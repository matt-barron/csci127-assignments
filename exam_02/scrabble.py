def score(w):
    scores= {}
    scores[1]= "AEIOULNRSTaeioulnrst"
    scores[2]= "DGdg"
    scores[3]= "BCMPbcmp"
    scores[4]= "FHVWYfhvwy"
    scores[5]= "Kk"
    scores[8]= "JXjx"
    scores[10]= "QZqz"
    wlist= list(w)
    score = 0
    for i in wlist:
        if i in scores[1]:
            score = score + 1
        elif i in scores[2]:
            score = score + 2
        elif i in scores[3]:
            score = score + 3
        elif i in scores[4]:
            score = score + 4
        elif i in scores[5]:
            score = score + 5
        elif i in scores[8]:
            score = score + 8
        elif i in scores[10]:
            score = score + 10
    return score
print(score("hello"))
print(score("Amazing"))
print(score("HeLLo"))