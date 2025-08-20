

import copy

L1=[1,2,3,4,[5,6]]
L2=L1
L3=L1.copy()
L4=copy.deepcopy(L1)
print(id(L1),id(L2),id(L3),id(L4))

L1.append(7)
L4.append(100)
L3[4][1]=200
L4[4][0]=300
L2[4][0]=400

print(L1)
print(L2)
print(L3)
print(L4)