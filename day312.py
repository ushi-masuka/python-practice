'''Write a program that will take 2 numbers as input and prints the LCM and HCF of 
those 2 numbers'''


a=int(input('please enter a num: '))
b=int(input("please enter the other number: "))

if a>b:
    num1=a
    num2=b
else:
    num1=b
    num2=a

rem=-1

rem=num1%num2

while rem!=0;
    