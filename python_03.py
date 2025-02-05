import math 

a=float (input("enter the value of a:"))
a_rad = math.radians(a) #converts the angle to radians
cosine=math.cos(a)
sine=math.sin(a)
print("cosine of a is:",cosine)
print("sine of a is:",sine)

print("the calculated value of cos^2(a) + sin^2(a) is:",cosine**2+sine**2)


# Possible Error: Type Error 
# A radian is a unit of angular measure used in mathematics and engineering. 
# It is the standard unit for measuring angles in trigonometry and calculus.