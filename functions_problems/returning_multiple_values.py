# create a function that returns both the area and circumference of a circle given its radius.
import math
def circle_status(radius):
    area = math.pi * radius **2
    circumference = 2 * math.pi * radius
    return area,circumference
a,b = circle_status(2)
print("Area : ",a , "circumference :",b)