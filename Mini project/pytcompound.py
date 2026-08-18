# python compound interest  

principle = 0 
rate  = 0 
time = 0 

# while principle <= 0 :
#     principle = float(input("Enter the principle amount: "))
#     if principle <=  0 :
#         print("Principle amount cannot be negative. Please enter a valid amount.")
# while rate  <= 0 :
#     rate = float(input("Enter the rate of interest: "))
#     if rate <=  0 :
#         print("Rate of interest cannot be negative. Please enter a valid amount.")

# while time <= 0 :
#     time = int(input("Enter the time in years: "))
#     if time <=  0 :
#         print("Time cannot be negative. Please enter a valid amount.")

# total = principle * (1 + rate / 100) ** time


# print(f"balanced after {time} years is: $ {total:.2f}")  # this will print the total amount after the time period with 2 decimal places.



while True:
    principle = float(input("Enter the principle amount: "))
    if principle <=  0 :
        print("Principle amount cannot be negative. Please enter a valid amount.")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest: "))
    if rate <=  0 :
        print("Rate of interest cannot be negative. Please enter a valid amount.")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time <=  0 :
        print("Time cannot be negative. Please enter a valid amount.")
    else:
        break

total = principle * (1 + rate / 100) ** time


print(f"balanced after {time} years is: $ {total:.2f}")  # this will print the total amount after the time period with 2 decimal places.