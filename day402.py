L1=[1,2,3,4]
L2=['a','b','c','d']


l3=[[i,j] for i in L1 for j in L2 ]
l4=list(zip(L1,L2))

print(l3)
print(l4)
