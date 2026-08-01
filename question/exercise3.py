def odd_even(number): 
    if number % 2 == 0: 
        return "Even" 
    else: 
        return "Odd"

odd_even(5)  # this will return "Odd" because 5 is an odd number.
odd_even(4)  # this will return "Even" because 4 is an even number.

print (odd_even(5) , odd_even(4))  # this will print "Odd Even" because 5 is an odd number and 4 is an even number.

    #  

def count_vowels(string): 
    vowels = "aeiouAEIOU" 
    count = 0 
    for char in string: 
        if char in vowels: 
            count += 1 
    return count
count_vowels("Hello World")  # this will return the number of vowels in the string "Hello World" which is 3.
print(count_vowels("Hello World"))  # this will print the number of vowels in the string "Hello World" which is 3.