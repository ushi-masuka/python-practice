#guess the number game

import random 

jackpot=random.randint(1,101)


n=int(input("please enter a guess between 1 and 100: "))

i=1

while n!=jackpot:
    print("Womp! Womp!")
    if n>jackpot:
        n=int(input("please guess lower: "))
        i+=1
    else:
        n=int(input("please guess higher: "))
        i+=1
else:
    print("wow man, Thats absolutely correct, what are you a god? \n Only took you like", i , "attemps.")