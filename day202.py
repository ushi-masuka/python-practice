#max of 3 numbers


a=int(input("please enter a number: "))
b=int(input("please enter a number: "))
c=int(input("please enter a number: "))

if a>b and a>c:
    print(a, "is the biggest")
elif b>c:
    print(b, "is the biggest")
else:
    print(c, "is the biggest")