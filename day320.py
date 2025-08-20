''' Check whether the string is Symmetrical.
Statement: Given a string. the task is to check if the string is symmetrical or not. 
A string is said to be symmetrical if both the halves of the string are the same.

Example 1:

Input

khokho
Output

The entered string is symmetrical'''

s=input("please enter the string: ")
if(len(s)%2==0):
    if s[:((len(s))//2)]==s[((len(s))//2):len(s)]: 
        print("The entered string is symmetrical")
    else:
        print("not symmetrical")
else:
    if s[:((len(s))//2)]==s[((len(s))//2)+1:len(s)]: 
        print("The entered string is symmetrical")
    else:
        print("not symmetrical")

