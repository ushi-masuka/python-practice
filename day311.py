'''Reverse words in a given String
Statement: We are given a string and we need to reverse words of a given string.

Example 1:

Input:

geeks quiz practice code
Output:

code practice quiz geeks
Example 2:

Input:

my name is laxmi
Output:

laxmi is name my'''

s=input("please enter the string: ")

s=s.split()

print(s[::-1])


for i in range(len(s)-1,-1,-1):
    print(s[i],end=" ")