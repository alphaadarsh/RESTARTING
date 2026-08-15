unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter temperature: "))

if unit == "C":
    temp = round((9 * temp)/5 + 32, 2)
    print(f"Temperature in Fahrenheit: {temp}°F")
elif unit == "F":
    temp = round(5*(temp-32)/9, 2)
    print(f"Temperature in Celsius: {temp}°C")
else:
    print(f"Invalid {unit}. Please enter 'C' for Celsius or 'F' for Fahrenheit.")