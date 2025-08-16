'''Create Short Form from initial character
Given a string create short form ofthe string from Initial character. Short form should be 
capitalised.

Example:

Input:

Data science mentorship program
Output:

DSMP'''

s=str(input("please enter the name: "))

s=s.title()
s=s.split()

for i in range(len(s)):
    print((s[i])[0],end="")