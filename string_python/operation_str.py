#  lets learn operation on string 

s1  = "hello python is fun "
s2  = " lets learn operation on string "
print (s1+s2)  # Output: hello python is fun  lets learn operation on string

s3  = "hello python is fun "
print (s3*3)  # Output: hello python is fun hello python is fun

#   membrship operator in python is used to check if a substring is present in the string or not.
s4  = "hello python is fun "
print("python" in s4)  # Output: True
print("Java" in s4)  # Output: False

# lets see in not in operator
print("python" not in s4)  # Output: False  
print("Java" not in s4)  # Output: True

#  comparison operator in python is used to compare two strings and return a boolean value.

print ("pyTHon" == "python")  # Output: False
print ("python" == "python")  # Output: True

#  removing spaces from the string using strip() method
s5  = "   hello python is fun   "
print(s5)  # Output:    hello python is fun
print(s5.strip())  # Output: hello python is fun
# print(s5.lstrip())  # Output: hello python is fun
# print(s5.rstrip())  # Output:    hello python is fun
print(s5.replace("python", "Java"))  # Output:    hello Java is fun    

# counting the number of occurrences of a substring in a string using count() method
# s6  = "hello python is fun python is fun"
# print(s6.count("python"))  # Output: \
# print(f"Occu")

s6 = "hello python is fun python is fun"
s7 = "python"

# Counting the number of occurrences of a substring in a string using count() method
print(f"Occurrences of {s7} is {s6.count(s7)}")  # Output: Occurrences of 'python' in 'hello python is fun python is fun': 2
