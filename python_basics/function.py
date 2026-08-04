# price = 100 
# new_price = (price * 0.18  )  
# print (new_price)  # this will print the value of new_price which is 18.0   no redundency needed to use 18.0 directly because it is better to calculate the value of new_price based on the value of price in case the value of price changes in the future.

# def sum(a, b):  # this will define a function sum which takes two parameters a and b and returns their sum. we can also use the return statement to return the value of the sum of a and b.
#     print(a + b)  # this will print the sum of a and b.

# sum (11, 22)  # this will call the function sum with the arguments 11 and 22 and print the value of their sum which is 33.

                                                                        
def cal_gst(price) :   # parameter price is passed to the function cal_gst which will calculate the gst of the price and print the new price after adding gst to the original price.
    new_price = (price + price * 0.18  )
    print (new_price)  # this will print the value of new_price which is 18.0   no redundency needed to use 18.0 directly because it is better to calculate the value of new_price based on the value of price in case the value of price changes in the future.
cal_gst(100)  # this will call the function cal_gst with the argument 100 and print the value of new_price which is 118.0. this is call argument