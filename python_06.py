#Cartesian to PolarCoordinates
import math

def cartesian_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta


x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
print(cartesian_to_polar(x, y))
