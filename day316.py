"""Given string contains a combination of the lower and upper case letters. Write a program to arrange
 the characters of a string so that all lowercase letters should come first.
Given:

str1 = PyNaTive

Expected Output:

yaivePNT"""

s=input("please enter the string: ")
a=''
b=''

for i in s:
    if i.islower():
        a+=i
    else:
        b+=i

print(a+b)
