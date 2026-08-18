# letys make a shopping cart program using python and tkinter. we will create a class called shoppingcart which will have the following methods:
# 1. add_item: this method will take the item name and price as input and add the item to the cart.
# 2. remove_item: this method will take the item name as input and remove the item from the cart.
# 3. view_cart: this method will display the items in the cart along with their prices and the total price of the items in the cart.
# 4. checkout: this method will display the total price of the items in the cart

foods = []
prices = []
total = 0

while True :
    food = input("Enter the food item you want to add to the cart (q to quit):  ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the {food}:  "))
        foods.append(food)
        prices.append(price)

print("------ Shopping Cart ---")
for food in foods: 
    print(food , end = " , " )
print()  # Print a newline after the list of foods

for price in prices:
    print(f"${price:.2f}", end = " + ") 

print()  # Print a newline after the list of prices

for price in prices:
    total += price

print(f"total price is ${total:.2f}")  # this will print the total price of the items in the cart.

print()  # Print a newline at the endp
