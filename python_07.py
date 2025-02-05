#GaussianRandomNumbers

import math
import random

u = random.random()
v = random.random()

print (u, v)

w = math.sin(2*math.pi*v)*(-2*math.log(u))**0.5

print("the gaussian value is: ", w)