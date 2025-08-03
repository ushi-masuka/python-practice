#Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.

num1=int(input("please enter the numerator 1: "))
den1=int(input("please enter the denominator 1: "))
num2=int(input("please enter the numerator 2: "))
den2=int(input("please enter the denominator 2: "))
numsum=num1*den2 +num2*den1 
densum=den1*den2

print("sum=",numsum,"/",densum)