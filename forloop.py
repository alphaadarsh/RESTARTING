#  for loop =>  repeatedly execute a block of code for a fixed number of times. In python, we have two types of loops: for loop and while loop. and used most of times  

# lets talk about for loop in python. for loop is used to repeatedly execute a block of code for a fixed number of times. the syntax of a for loop is as follows:

# num =  range (10)  # this will create a range object that represents the numbers from 0 to 9.
for i in range(1 , 10):  # this will iterate over the range object and assign the value of each element in the range to the variable i.
    print(i)  # this will print the value of i in each iteration of the loop.ckea

print ("new code")  # this will print the string "Hello, World!" after the for loop has completed.

 # LETS PRINT ONLY EVEN NUMBER  
for j in range(1 ,11):  # this will iterate over the range object and assign the value of each element in the range to the variable j.
        if  j % 2 == 0:  # this will print the value of i multiplied by j in each iteration of the loop.
            print(j)

for k in range (2 , 11 , 2) :  # this will iterate over the range object and assign the value of each element in the range to the variable k.
    print(k)  # this will print the value of k in each iteration of the loop.

 #  LETS PRINT MULTIPLE OF 3 IF 21 THAN STOP 
for l in range(1, 50):
    if (l == 21):  # this will check if the value of l is equal to 21 in each iteration of the loop.
        # break  # this will break the loop if the condition is true.
        continue  # this will skip the current iteration of the loop if the condition is true and continue with the next iteration of the loop.
    if l % 3 == 0:
        print(l)  # this will print the value of l in each iteration of the loop.