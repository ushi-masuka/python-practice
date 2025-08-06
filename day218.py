'''Calculate the angle between the hour hand and minute hand.
Note: There can be two angles between hands; we need to print a minimum of two. 
Also, we need to print the floor of the final result angle. For example, if the final 
angle is 10.61, we need to print 10.

Input:
H = 9 , M = 0
Output:
90
Explanation:
The minimum angle between hour and minute hand when the time is 9 is 90 degress.'''


H=int(input("please enter the Hour: "))
M=int(input("please enter the minutes: "))

angle=H*(30) + M*(0.5) - M*(6)

if angle>180:
    print(int(360-angle))
else:
    print(int(angle))