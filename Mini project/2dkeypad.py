num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:  # this will iterate through the 2d tuple num_pad and print each row of the tuple.
    for num in row :  #
        print(num, end=" ")  # this will print each number in the 2d tuple num_pad. and also we can use index to get the value of the 2d tuple.
    print()
    # print(row)  # this will print each row of the 2d tuple num_pad. and also we can use index to get the value of the 2d tuple./