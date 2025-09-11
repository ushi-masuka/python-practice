'''Write a program to print whether a given number is a prime number or not'''

n= int(input("please enter the number that needs to be checked: "))

if n<=1:
    print("It is not prime")
elif n==2:
    print("it is prime.")
elif n%2==0 and n!=2:
    print("it is not prime")

else:
    for i in range(3,int((n**(0.5))+1),2):
        if n%i==0:
            print("it is not prime")
            break
    else:
        print("it is prime")
        
       