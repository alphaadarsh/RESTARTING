#  or   

# temp  = 20 
# is_raining = True

# if temp > 25 or is_raining:
#     print("It's either hot or raining.")

# temp2  = 20 
# is_sunny = True

# if temp2 > 28 and is_sunny: 
#     print("It's hot and sunny.")
#     print("Enjoy the weather!😊")
# elif temp2 > 28 and is_sunny:
#     print("It's hot but not sunny.")
#     print("Stay hydrated!💧")
# elif 12 < temp2 <= 0:
#     print("It's cold.")
#     print("Bundle up!🧥")
# else:
#     print("The weather is moderate.")
#     print("Have a great day!🌤️")



temp2  = 32
is_sunny = False

if temp2 > 28 and not is_sunny: 
    print("It's hot and sunny.")
    print("Enjoy the weather!😊")
elif temp2 > 28 and not is_sunny:
    print("It's hot but not sunny.")
    print("Stay hydrated!💧")
elif 12 < temp2 <= 0:
    print("It's cold.")
    print("Bundle up!🧥")
else:
    print("The weather is moderate.")
    print("Have a great day!🌤️")