'''Print the following pattern.
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*'''

n=int(input("please enter the max num: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

for i in range(n-1,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()