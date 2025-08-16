'''Write a program that will take a decimal number as input and prints out the binary 
equivalent of the number'''


n=int(input("please enter the number: "))
r=""
if n==0:
    print("0")
while n>0:
    r+=str(n%2)
    n=n//2

print(r[::-1])

    
