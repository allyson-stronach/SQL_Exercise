s = 'new_project Databases "Stuff and things" 20'
# s = s + " "
l = []
word = ""
inquotes = False
for char in s + " ":
    if char == '"' and inquotes == False:
        inquotes = True
    elif inquotes == True and char == '"':
        l.append(word)
        print "the appended word:", word
        word = ""
        inquotes = False
    elif char == " " and inquotes == False:
        if word:
            l.append(word)
        word = ""
    else:
        word += char
    print "char:" , char
    print "word:", word

print [word for word in l if word]
print l
