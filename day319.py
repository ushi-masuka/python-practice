'''Word location in String.
Statement: Find a location of a word in a given sentence.

Example 1:

Input:

Sentence: We can learn data science through campusx mentorship program.

word: campusx
Output:

Location of the word is 7.
Note- Don't use index/find functions'''

s=input("please enter a string: ")\

s=s.split()

w=input("please enter the word to search for: ")

for i in range(len(s)):
    if s[i]==w:
        print(i+1)