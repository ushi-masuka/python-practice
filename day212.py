'''Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible
   by 5, then skip that number. And if the sum is greater than 300, don't need to calculate
   the sum further more. Print the final result. And don't use for loop to solve this
   problem.
Example 1:

Input:

30
Output:

276'''

N=int(input("please enter the number: "))
sum=0
i=1

while sum<=(300-i) and i<=N:
    if i%5!=0:
        sum+=i
        i+=1
    else:
        i+=1

print(sum)


