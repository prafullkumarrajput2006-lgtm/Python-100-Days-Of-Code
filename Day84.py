# # Time Module in Python...



# The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formating, and time conversion.This module is part the Python Standard Library and is available in all Python installations, making it a convenient and essential tool for a wide range of applications. In this day 84 tutorial, we'll explore the time module in Python and see how it can be used in different scenarios... 



# # time.time()...

# The time.time() function returns the current time as a floating-point number, representing the number of seconds since the spoch (the point in time when the time module was initialized). The returned value is based on the computer's system clock and is affected by time adjustments made by the operating system, such as daylight saving...









# # *** time.time()...



import time

# def usingWhile():
#     i = 0
#     while i < 500:
#         i = i+1
#         print("While Loop",i)


# def usingFor():
#     for i in range (500):
#         print("For Loop",i)
        
        
# init = time.time()
# usingFor()
# print(time.time() - init)



# init = time.time()
# usingWhile()
# print(time.time() - init)









# # *** time.sleep()... 


# The time.sleep() function suspends the execution of the current thread for a specified number of seconds. The function can be used to pause the program for a certain period of time, allowing other parts of the program to run, ot to synchronize the execution of multiple threads. Here's an example...






# print(4)
# time.sleep(3)
# print("This is printed after 3 seconds")









# *** time.strftime()... 




t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)