# shopping cart program

item = input("Enter the item you want to add to the shopping cart: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: ")) 

total_cost = price * quantity
print(f"the total costof {quantity} x {item}(s) is: ${total_cost:.2f}")
