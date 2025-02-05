#WindChill Checking
import math
v=float(input("Enter the value of wind speed v: "))
t=float(input("Enter the value of temperature in fahrenheit: "))
w=0
if(t<50 and v>3 and v<120):
 w= 35.74 + 0.6215*t + (0.4275*t - 35.75) * math.pow(v, 0.16)
 print("The wind chill is: ", w)
else:
    print("The values are not in the range and value cannot be computed")
