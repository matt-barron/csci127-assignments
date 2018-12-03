def encode(s):
    count = 1
    list=[]
    for i in range(1, len(s) + 1):
        if i == len(s):
            list.append([s[i - 1], str(count)])
            break
        else:
           if s[i - 1] == s[i]:
                count += 1
           else:
              list.append([s[i - 1], str(count)])
              count = 1
    return list
print(encode("abbaa"))
print(encode("abbaaacddaaa"))