''' Write a program that can remove all the duplicate characters from a string. 
User will provide the input.'''

s=input("please enter the string with duplicates: ")

l=''

for i in s:
    if i not in l:
        l=l+i

print(l)