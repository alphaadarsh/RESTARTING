# roll_num = [ 101 , 15 , 102  , 101 , 101 , 108 , 105 , 110 ]
# unique_roll_num = set(roll_num)  # this will create a set unique_roll_num with the elements of roll_num and remove the duplicate elements from the list.

records = [
    (101, "Alice", 50000),
    (102, "Bob", 65000),
    (103, "Charlie", 45000) ,
    (104, "David", 70000),
    (105, "Eve", 60000),
    (106, "Frank", 55000) , 
]
emp_id = int (input("Enter employee ID: "))
for employee in records:
    if employee[0] == emp_id:
     print (employee)
#         print(employee[1], "has a salary of", employee[2])
#         break
# else:
#     print("Employee not found.")
