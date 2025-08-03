#Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.

point1x=float(input("please enter 1st x coordinate:"))
point1y=float(input("please enter 1st y coordinate:"))
point2x=float(input("please enter 2nd x coordinate:"))
point2y=float(input("please enter 2nd y coordinate:"))
print("point1:(",point1x,",",point1y,"),point2:(",point2x,",",point2y,")")

distance=((point1x-point2x)**2 + (point1y-point2y)**2)**(1/2)

print("eaclidean distance: ", distance)