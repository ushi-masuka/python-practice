'''Problem 3: Write a program that will take user input of 
   cost price and selling price and determines whether its 
   a loss or a profit.'''

cp=int(input("please enter the cost price: "))
sp=int(input("please enter the selling price: "))

profit=sp-cp

if profit>0:
    print("it was a profit of:",profit)
elif profit<0:
    print("it was a loss of:",profit*-1)
else:
    print("you broke even")