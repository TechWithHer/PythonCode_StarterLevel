
#Task1 From CHAPTER 1
x=1
print("Hello, World!")
name =  input ("What is youur name?")
city = input("which City?")
age = input("Enter your age")

print(f"Hello {name}! You are {age} years old and live in {city}.")

#Task2 From CHAPTER 1

	length = float(input ("Enter the length of the rectangle: "))
	width = float(input("Enter the width of the rectangle: "))

	area = length * width

	print (f"the area of the rectangle is {area}")

#Task3 From CHAPTER 1

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit is {fahrenheit}.")


#Task4 From CHAPTER 1

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    result = "Invalid operation"

print(f"Result: {result}")

#Task5 From CHAPTER 1

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
