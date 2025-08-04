'''Write a program that take a user input of three angles and will find out whether it can form a triangle or not.'''

angle1=int(input("please enter the angle1: "))
angle2=int(input("please enter the angle2: "))
angle3=int(input("please enter the angle3: "))

angles=[angle1,angle2,angle3]
sum=0

for i in angles:
    sum+=i

if sum==180:
    print(True)
else:
    print(False)