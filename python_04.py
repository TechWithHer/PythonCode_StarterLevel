#Calculating the compound interest

import math 

def compound_interest(principal, rate, time):
    return principal * math.pow((1 + rate/100), time)

principal=float(input("Enter the principal amount: "))
rate=float(input("Enter the rate of interest: "))
time=float(input("Enter the time in years: "))
result=compound_interest(principal, rate, time)
print("The compound interest is: ", result)


#Note: the above calculation is for the compound interest. The formula for compound interest is given by: A = P(1 + r/n)^(nt) where A is the amount, P is the principal amount, r is the rate of interest, n is the number of times that interest is compounded per year, and t is the time in years.

#In the next one, we will calculate the continuous compound interest.

def continuous_compound_interest(principal, rate, time):
    return principal * math.exp(rate * time)
    
result_1=continuous_compound_interest(principal, rate, time)
print("The continuous compound interest is: ", result_1)