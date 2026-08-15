# python weight converter 
weight = float(input("Enter weight: "))
unit = input("KIlogram or Pound (K/P): ")

if unit == "k" or unit =="K":
    converted_weight = weight * 2.205
    unit = "Pounds"
elif unit == "p" or unit =="P":
    converted_weight = weight / 2.205
    unit = "Kilograms"
else:
    print("Invalid unit. Please enter 'K' for Kilogram or 'P' for Pound.")
    exit()
print (f"The converted weight is: {converted_weight:.2f} {unit}") 