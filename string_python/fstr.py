name = "Alice"
age = 30
# Using f-string to format the output
print(name , "is" ,  age , "years  old ")  # Output: Alice is age 30 years old

# but now using f-string
print(f"{name} is {age} years old.")  # Output: Alice is 30 years old.

name  =  "bob"
age = 25 

print(f"{name} is {age} years old.")  # Output: bob is 25 years old. and f means here fetch the value inside the variable and print it in the output. 

sub1 = 90
sub2 = 80
sub3 = 70
print(f"Subject 1: {sub1}, Subject 2: {sub2}, Subject 3: {sub3}")