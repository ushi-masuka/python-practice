'''Print all the Armstrong numbers in a given range.
Range will be provided by the user
Armstrong number is a number that is equal to the sum of cubes of its digits. 
For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.'''

rangeS=int(input("please enter the range starting: "))
rangeE=int(input("please enter the range ending(inclusive): "))

for number in range(rangeS,rangeE+1):
    n=str(number)
    sum=0
    for i in range(len(n)):
        sum+=(int(n[i]))**3
    if sum==number:
        print(number)
        