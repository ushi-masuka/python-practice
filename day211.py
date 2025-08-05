'''Reverse a given integer number.'''

num=str(input("please enter the number: "))
rev_num=num[-1]
for i in range(2,len(num)+1):
    rev_num=rev_num + num[-i]
print(rev_num)