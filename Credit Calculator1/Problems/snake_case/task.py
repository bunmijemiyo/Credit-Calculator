word = input()

modify = []

if word.islower():
    print(word)

else:
    for letter in word:
        if letter.isupper():
            modify = word.replace(letter, "_" + letter.lower())
    print(modify)