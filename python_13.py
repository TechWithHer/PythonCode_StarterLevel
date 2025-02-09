def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32

def fahrenheit_to_celsius(fahrenheit):
    return (5/9) * (fahrenheit - 32)

def tempcheck():
    if fahrenheit  >=100 and fahrenheit<=150:
        print("Its warm and cosy")
    elif fahrenheit<100:
        print("Its cold")
    else:
        print("Its hot. Be safe")

while True:
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    
    choice = input("Choose an option (1/2/3): ")
    
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is {fahrenheit:.2f}°F")
        tempcheck()
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is {celsius:.2f}°C")
        tempcheck()
    elif choice == "3":
        print("Exiting the converter.")
        break
    else:
        print("Invalid option, please choose 1, 2, or 3.")
