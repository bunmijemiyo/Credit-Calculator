n = input()
vowels = ["a", "e", "i", "o", "u"]

for letters in n:
    if letters.isalpha():
        if letters in vowels:
            print("vowel")
        else:
            print("consonant")
    else:
        break