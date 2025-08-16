'''Append second string in the middle of first string
Input:

campusx
data
Output:

camdatapusx'''

s1=input("please enter the 1st string: ")
s2=input("please enter the 2nd string: ")
s3=s1[:(len(s1))//2] + s2 + s1[(len(s1))//2:]

print(s3)