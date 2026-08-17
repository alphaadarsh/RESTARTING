import time 

time.sleep(1)

my_time = int(input("Enter the time in seconds: "))  # this will take the input from the user for the time in seconds.

for x in range(my_time, 0, -1):  # this will create a loop that will run from the value of my_time to 0 in reverse order.
    seconds = x % 60  # this will calculate the number of seconds remaining after dividing x by 60.
    minutes = x // 60  # this will calculate the number of minutes remaining after dividing x by 60.
    hours = x // 3600  # this will calculate the number of hours remaining after dividing x by 3600.
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time.sleep(1)   
print("Time's up!")  # this will print "Time's up!" after the loop has finished running.23