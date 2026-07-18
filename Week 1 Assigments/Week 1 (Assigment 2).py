# 1. Write a program to create a new string made of an input string’s first,
# middle, and last character.

text = input("Enter a string: ")

first = text[1]
middle = text[len(text) // 2]
last = text[-1]

new_string = first + middle + last

print("New String", new_string)


# 2. Write a program to count occurrences of all characters within a string
# Given.

text1 = input("Enter a String: ")

for char in set (text1):
    print(char, ":", text1.count(char))


# 3. Reverse a given string

text2 = input("Enter a string: ")

result = text2[::-1]

print("New String", result)
