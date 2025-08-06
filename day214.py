'''Write a program, which will find all such numbers between 1000 and 3000 (both included)
   such that each digit of the number is an even number. The numbers obtained should be 
   printed in a space-separated sequence on a single line.'''


for i in range(1000,3001):
    j=str(i)
    if int(j[0])%2==0 and int(j[1])%2==0 and int(j[2])%2==0 and int(j[3])%2==0:
        print(int(j),end=" ")