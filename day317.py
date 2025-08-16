"""Take a alphanumeric string input and print the sum and average of the digits that appear in 
the string, ignoring all other characters.
Input:

hel123O4every093

Output:

Sum: 22
Avg: 2.75"""

s=input("please enter an alpha numeric string: ")
sum=0
counter=0

for i in s:
    if i.isdigit():
        sum+=int(i)
        counter+=1

print("sum=",sum,"average=",sum/counter)