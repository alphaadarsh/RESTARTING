price_1 = float(input("Enter the price of the first item: "))
price_2 = float(input("Enter the price of the second item: "))
price_3 = float(input("Enter the price of the third item: "))

total_price = price_1 + price_2 + price_3
# print("The total price of the three items is: $" + str(total_price))
# print("The total average price of the three items is: $" + str(total_price / 3))

average_price = total_price / 3

# hero_name = input("Enter the name of your favorite superhero: ")
# print("The hero's name contains the letter 's': " + str('s' in hero_name))

print("The total price of the three items is: $" , total_price)
print("The total average price of the three items is: $" , average_price)

#  part 2 

hero_name = input("Enter the name of your favorite superhero: ")

if hero_name.startswith("S"):
    print("The hero's name starts with the letter 'S'.")
else: 
    print("The hero's name does not start with the letter 'S'.")