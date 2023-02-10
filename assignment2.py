#Write a Python program that accepts a word from the user and reverse it.
a = input("Input a word to get reverse of it: ")

for i in range(len(a) - 1, -1, -1):
    print(a[i], end="")
