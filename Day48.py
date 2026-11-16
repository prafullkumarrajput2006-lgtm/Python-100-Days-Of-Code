# Local vs Global Variable... 


# 1. Local Variable... That type of variable which is defined within a function and use in only that function where it defined that is called local Variable...

# 2. Global Variable... That type of variable which is defined outside of a function and it can be used inside and outside of the function that is called global variable... 









# # In Normal condition... 



# x = 4
# print(x)

# def hello():
#     x = 5
#     print(f"The local variable x is {x}")                # Local Variable...
#     print("Hello Prafull")

# print(f"The global variable x is {x}")                   # Global Variable 

# hello()

# print(f"The global variable x is :  {x}")                # GLobal Variable









# # *** Change the global variable ...



# x = 4
# print(x)

# def hello():
#     x = 5
#     print(f"The local variable x is {x}")                
#     print("Hello Prafull")

# print(f"The global variable x is {x}")                   

# hello()
# x = 5

# print(f"The global variable x is :  {x}")                









# # *** Check the condition of global and local variable ... and change the value of global variable inside the function



# x = 10

# def my_function():
    
#     global x 
#     x = 5
    
#     y = 12
#     print(y)
    

# print(f"1st print {x}")    
# my_function()
# print(f"Second print {x}")
# # # print(y)                          # This will cause an error because y is a local variable and is not accessible outside of the function...


