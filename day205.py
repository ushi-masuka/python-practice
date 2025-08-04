'''Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
Salary(Lakhs) : Tax(%)

Below 5 : 0%
5-10 : 10%
10-20 : 20%
aboove 20 : 30%'''

salary=int(input("please enter your salary in numbers: "))
SalAfterDed=salary-salary*0.1 -salary*0.05 -salary*0.03

if SalAfterDed<500000:
    inhand=SalAfterDed
    print(inhand)
elif SalAfterDed<1000000:
    inhand=(SalAfterDed-500000)*0.9 + (500000)
elif SalAfterDed<2000000:
    inhand=(SalAfterDed-1000000)*0.8 + (SalAfterDed-500000)*0.9 + (500000)
else:
    inhand=(SalAfterDed-2000000)*0.7 + (SalAfterDed-1000000)*0.8 + (SalAfterDed-500000)*0.9 + (500000)

print(inhand)

