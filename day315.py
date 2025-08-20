'''Find uncommon words from two Strings.
Statement: Given two sentences as strings A and B. The task is to return a list of all 
uncommon words. A word is uncommon if it appears exactly once in any one of the sentences, 
and does not appear in the other sentence. Note: A sentence is a string of space-separated words. 
Each word consists only of lowercase letters.

Example 1:

Input:

A = "apple banana mango" 
B = "banana fruits mango"
Output:

['apple', 'fruits']'''

a=input("please enter string A: ")
b=input("please enter String B: ")
c=[]

for i in a.split():
    if i not in b.split():
        c.append(i)
        

for i in b.split():
    if i not in a.split():
        c.append(i)

print(c)