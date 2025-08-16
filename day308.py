'''Write a program to calculate the sum of series up to n term. For example, if n =5 the 
series will become 2 + 22 + 222 + 2222 + 22222 = 24690. Take the user input and then calculate. 
And the output style should match which is given in the example.

Example 1:

Input:

5
Output:

2+22+222+2222+22222
Sum of above series is: 24690'''


n=int(input("please enter the n: "))
sum=0

for i in range(1,n+1):
    sum+=int('2'*i)
    print("2"*i,"+",sep="",end="")

print()    

print("Sum of above series is:",sum)