def compress_word(w):
    """
    W is a parameter representing a word that is a string. This
    function should remove the letters " A, E, I, O, U" from a word.
    """
    newword = " "
    vowels= ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in range(len(w)):
        if w[i] not in vowels :
            newword= w[i] + newword
                       
    return newword[::-1]
    

print(compress_word("hello"))
print(compress_word("apple"))
def sentence(line):
   linelist= line.split()
   news=[]
   for i in range(len(linelist)):
       news.append(compress_word(linelist[i]))
    
   return "".join(news)
print(sentence("i like apple pies"))