#Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.

num1=int(input("please enter the 1st number: "))
num2=int(input("please enter the 2st number: "))
n=int(input("please enter the n: "))
d=num2-num1
numn=num1 +(n-1)*d
print(numn)