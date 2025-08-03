#print the sum of digits entered by the user

a=int(input("please enter a 3 digit number"))

onesd=a%10
tensd=(a//10)%10
hunsd=(a//100)
print(onesd,tensd,hunsd, "+=", onesd+tensd+hunsd)