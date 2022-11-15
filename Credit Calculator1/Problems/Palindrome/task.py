# checking for palindrome words
word = input()
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")