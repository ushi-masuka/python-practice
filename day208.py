'''Problem 4: Write a menu-driven program -
1. cm to ft
2. km to miles
3. USD to INR
4. exit'''
 
print("what do you want:\n1. cm to ft \n2. km to miles \n3. USD to INR \n4. exit ")

option=int(input("please choose: "))
while option!=4:
    value=int(input("enter the value: "))

    if option==1:
        print(value/30.48)
    elif option==2:
        print(value*0.62137)
    elif option==3:
        print(value*87.67)
    else:
        print("bro choose a valid number!")
    
    option=int(input("please choose: "))



