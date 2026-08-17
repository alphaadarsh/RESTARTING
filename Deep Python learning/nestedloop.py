# outer loop 
#       inner loop 
#               loop under loop  
#                         and soo  onnn
 
for x in range(3) : 
    for y in range(1,10): 
        print(y , end = " ")  # this will print the value of y in each iteration of the inner loop and will not move to the next line after each iteration.
    print()  # this will move to the next line after each iteration of the outer loop.



rows =  int(input("Enter the number of rows: "))     # this will take the input from the user for the number of rows in the pattern.
columns =  int(input("Enter the number of columns: "))  # this will take the input from the user for the number of columns in the pattern.

symbol = input("Enter the symbol to use: ")  # this will take the input from the user for the symbol to use in the pattern.

 
for x in range(rows) : 
    for y in range(columns) : 
        print(symbol, end = " ")  # this will print the value of y in each iteration of the inner loop and will not move to the next line after each iteration.
    print()  # this will move to the next line after each iteration of the outer loop.