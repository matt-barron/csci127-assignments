def capitalize(name):
     """
    input: name --> a string in the form "first last"
    output: returns a string with each of the two words capitalized
    """
     return name.title()

print(capitalize("matthew barron"))

def init(name):
    """
    Input: name --> a string in the form "first last"
    Returns: a string in the form "F. Last" where it's a capitalized first inital 
    and capitalized last name
    """
    space_index = name.find(" ")
    first = name[0:space_index];
    last = name[space_index:]
    initials = first[0].title() + "." + last.title()
    
    return initials

print(init("matthew barron"))

def part_pig_latin(name):
    """
    Input: A string that is a single lower case word
    Returns: that string in fake pig latin -> move the first letter of the word to the end and add "ay"
    so: "hello" --> "ellohay"
    """
    word = name.lower()
    firstl = word[0]
    pig_latin = word[1:]+firstl+"ay"
    if firstl = "a", "e", "i", "o", "u":
        pig_latin = word+"ay"
    return pig_latin

print(part_pig_latin("pig"))

def make_out_word(out, word):
    return out[:2] + word + out[2:]

print(make_out_word('<<>>', 'matt'))

def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"

print(make_tags('i', 'brown'))
print(part_pig_latin(apple