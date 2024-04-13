'''Write a program which prompts a user to enter the radius of a circle.
If the radius is greater than zero then calculate and print the area and
circumference of the circle'''
from math import pi
Radius=eval(input("Enter radius of Circle: "))
if Radius>0:
    Area=Radius*Radius*pi
    print("Area of circle is = ", format(Area, ".2f"))
    Circumference=2*pi*Radius
    print("Circumference of circle is = ", format(Circumference,".2f"))