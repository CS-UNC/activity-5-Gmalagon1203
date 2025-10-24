'''
# open takes two arguments: the first argument is the path to the file 
# to read as a string. The second argument is a string indicating what 
# mode the file is to opened in (options being 'w' for writing, 'r' for 
# reading and 'a` for appending to the file)
words_file = open('CROSSWD.txt','r')
type(words_file)
# The expression below is what is called a `list comprehension`. 
# In Python, you can 'select' values in a list that satisfy a criteria
# (the if condition at the end). You can see that this looks similar to
# the for loop, just a bit more elegant
print([x for x in dir(words_file) if '_' != x[0]])
print(words_file.readline())
print(word.strip())
for line in words_file:
    ## We decode each line from the file and strip the special characters.
    word = line.decode('utf-8').strip()
    print(word)
'''


#Function #1:
def twenty_or_more(file):
    words_over_20 = []
    with open(CROSSWD.txt, 'r'):
        for line in data:
            for words in line.split():
                if len(word.strip()) > 20:
                    words_over_20.append(word.strip())
    return words_over_20


#Function #2:

def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True
    


#Function #3:

def uses_only(word, letters):
    for x in word:
        if x not in letters:
            return False
    return True


#Function #4:

def all_uses_only(file, letters):
    valid_words = []
    with open('CROSSWD.txt', 'r') as x:
        for line in x:
            words = line.split()
            for word in words:
                if uses_only(word, letters):
                    valid_words.append(word)
    return valid_words