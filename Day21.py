# # Functions Arguments in Python... 

# 1. Default Arguments
# 2. Keyword Arguments
# 3. Variable Length Arguments 
# 4. Requirement Argument 









# # *** Default Arguments


# def average(a = 8, b = 5):
#     print("The Average is :", (a+b)/2)
    
# average(1.5)    









# # *** Keyword Argument... Can change the order of argumenets


# def average(a = 8, b = 5):
#     print("The Average is :", (a+b)/2)
    
# average(b = 34, a = 89)    









# # ***Requirement Argument... Necessary to provide the value... 


# def average(a, b, c = 1):
#     print("The Average is :", (a+b+c)/3)
    
# average(5,6)                       #Here the value of a and b must to provide  









# # ***Variable Length Arguments   


# def average(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     # print("The Average is : ", sum/len(numbers))
#     return sum / len(numbers)
    
# # average(5,8,7,9,56)

# c = average(5,8,4,6,1,1)
# print(c)


