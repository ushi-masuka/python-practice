'''Given two rectangles, find if the given two rectangles overlap or not. A rectangle 
is denoted by providing the x and y coordinates of two points: the left top corner and 
the right bottom corner of the rectangle. Two rectangles sharing a side are considered 
overlapping. (L1 and R1 are the extreme points of the first rectangle and L2 and R2 are 
the extreme points of the second rectangle).
Note: It may be assumed that the rectangles are parallel to the coordinate axis.

'''

lx1=int(input("please enter the x coordinate of l1: "))
ly1=int(input("please enter the y coordinate of l1: "))
rx1=int(input("please enter the x coordinate of r1: "))
ry1=int(input("please enter the y coordinate of r1: "))

lx2=int(input("please enter the x coordinate of l2: "))
ly2=int(input("please enter the y coordinate of l2: "))
rx2=int(input("please enter the x coordinate of r2: "))
ry2=int(input("please enter the y coordinate of r2: "))

rect1left=min(lx1,rx1)
rect1right=max(lx1,rx1)
rect1top=max(ly1,ry1)
rect1bottom=min(ly1,ry1)

rect2left=min(lx2,rx2)
rect2right=max(lx2,rx2)
rect2top=max(ly2,ry2)
rect2bottom=min(ly2,ry2)

#to check if one rectangle is above the other
if rect1bottom>rect2top or rect2bottom>rect1top:
    print("they dont overlap")
#to check if one rectanle is to the left of other
elif rect1right<rect2left or rect2right<rect1left:
    print("they dont overlap")
else:
    print("they overlap")