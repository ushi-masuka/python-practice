#Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

principle=float(input("please enter the priunciple: "))
roi=float(input("please enter the raet of interest (in %): "))
time=float(input("please enter the time period: "))

sinterest=principle*roi*time/100
amount=principle+sinterest
print(sinterest , amount)