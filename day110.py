#Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.

h_of_carton=float(input("please enter height of box: "))
b_of_carton=float(input("please enter breadth of box: "))
l_of_carton=float(input("please enter length of box: "))
h_of_glass=float(input("please enter height of glass: "))
r_of_glass=float(input("please enter radius of glass: "))

volume_of_milk= h_of_carton*b_of_carton*l_of_carton
volume_of_glass=(22/7*r_of_glass**2)*h_of_glass

num_of_glass=volume_of_milk/volume_of_glass

print(num_of_glass)