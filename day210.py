'''Find the factorial of a given number.
Write a program to use the loop to find the factorial of a given number.'''

num=int(input("please type the number: "))
factorial=1

for i in range(num,0,-1):
    factorial=factorial*(i)

print(num,"! =",factorial)