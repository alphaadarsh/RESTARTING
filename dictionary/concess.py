menu = {
    "pizza": 10,
    "burger": 5,
    "pasta": 7,
    "salad": 8 , 
    "popcorn": 3,

}
cart   = []
total = 0
print("------------------------------------")
for key, value in menu.items():
      print(f"{key:10} : $ {value:.2f}")  # this will print the key and value of the dictionary item.  and also we can use index to get the value of the dictionary.
print("________________________________")

while True:
    food = input("select an item (q to quit): ").lower()
    if food == "q":
         break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart: 
    total += menu.get(food)
    print(food , end = " ")
print()
print(f"Total: $ {total:.2f}")