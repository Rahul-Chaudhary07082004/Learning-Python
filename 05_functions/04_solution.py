# Function returning multiple values 
# Create a function that returns both the area and circumference of a circle given its radius

import math 

def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle(4)
print("Area:", round(a, 2), "circumference:", round(c, 2))