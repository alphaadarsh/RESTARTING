# a = int(input('a: '))
# print(a)
# b = int(input('b: '))
# print(b)
# import math 
# c = math.sqrt(a**2 + b**2)1

# print('c: ', c)

side_a = int(input('Enter the length of side a: '))
side_b = int(input('Enter the length of side b: '))
# Calculate the length of side c using the Pythagorean theorem
hypotenuse = (side_a ** 2 + pow(side_b , 2)) ** 0.5
print('The length of the hypotenuse is:', round(hypotenuse, 2))