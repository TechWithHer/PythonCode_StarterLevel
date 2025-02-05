#GreatCircle

import math

x1 = float(input("Enter the latitude of the first point: "))
y1 = float(input("Enter the longitude of the first point: "))
x2 = float(input("Enter the latitude of the second point: "))
y2 = float(input("Enter the longitude of the second point: "))

x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

distance = 6371.01 * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

print("The distance between the two points is", distance, "km")


