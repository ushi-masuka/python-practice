'''Write a program to pring the following pattern
    *
  * * *
* * * * *
'''

n=int(input("please enter the number of rows: "))
l=1
for i in range(1,n):
  l+=2

for i in range(1,l+1,2):
  print(" "*(n-i//2),"*"*i,sep="")


