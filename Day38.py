# Raising Custom Error in Python... 




# a = int(input("Enter the value between 1 and 10 : "))
# print("Correct Value Entered")

# if (a < 1 or a > 10):
#     raise ValueError(f"Your value is {a} but you havo to enter the value between 1 and 10")









# # Custom Error Generate... By using own Keywords...



# class AreYouBlind(Exception):
#     pass

# a = int(input("Enter the value between 1 and 10 : "))

# if (a < 1 or a > 10):
#     raise AreYouBlind(f"Your value is {a} but you have to choose the value between 1 and 10")

# print("Correct Value Entered")









# # Quiz... Code should not give the error when we enter the value 'quit' but the value datatype in int. for any other datatype it acts as normal...


# try:
#     n = (input("Enter the number or 'quit' to exit : "))
    
#     if n.lower() == "quit":
#         print("You successfully exit from the program")
#     else:
#         n = int(n)
#         print(f"Your number is {n}")

# except ValueError:
#     print("Please enter a valid number or type 'quit' to exit from the program")

# print("Thank You")