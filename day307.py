'''The natural logarithm can be approximated by the following series.
temp.jpg

If x is input through the keyboard, write a program to calculate the sum of the first seven
terms of this series.'''

x=int(input("please enter the x: "))
n=int(input("please enter the n: "))
lnx1=(x-1)/x
lnx=lnx1
for i in range(2,n+1):
    lnx+=(lnx1**i)/i
    print(lnx)

