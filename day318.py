"""Removal of all characters from a string except integers
Given:

str1 = 'I am 25 years and 10 months old'
Expected Output:

2510"""

s=input("please enter the string: ")

for i in s:
    if i.isnumeric():
        print(i,end="")