# python weight converter 
weight = float(input("Enter weight: "))
unit = input("KIlogram or Pound (K/P): ")

if unit =="K":
    converted_weight = weight * 2.205
    unit = "Pounds"
    print (f"The converted weight is: {converted_weight:.2f} {unit}") 
elif unit == "p" or unit =="P":
    converted_weight = weight / 2.205
    unit = "Kilograms"
    print (f"The converted weight is: {converted_weight:.2f} {unit}") 
else:

    print(f"Invalid {unit}. Please enter 'K' for Kilogram or 'P' for Pound.")
   
# print (f"The converted weight is: {converted_weight:.2f} {unit}") 
