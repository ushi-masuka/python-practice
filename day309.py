'''Write a program to print all the unique combinations of 1,2,3 and 4
Output:

1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 1 3 4
2 1 4 3
2 3 1 4
2 3 4 1
2 4 1 3
.
.
and so on'''


n=int(input("please enter n: "))

for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):
            for d in range(1,n+1):
                print(a,b,c,d)
print("those with no number common:")

for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):
            for d in range(1,n+1):
                if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
                    print(a,b,c,d)