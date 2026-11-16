# Map, Filter & Reduce... 




# *** Map... 
 
# The map function applies a function to each element in a sequence and returns a new sequenece containg the transdormed elements. The map function has the following syntax... 

# map(function, iterable)









# # Without Map function... 


# def cube(x):
#     return x*x*x

# print(cube(2))

# list_1 = [1,2,3,4,5,6]

# new_list_1 = []

# for i in list_1:
#     new_list_1.append(cube(i))

# print(new_list_1)    









# # With Map Function... 



# def cube(x):
#     return x*x*x

# print(cube(2))

# list_1 = [1,2,3,4,5,6]

# new_list_1 = list(map(cube, list_1))

# print(new_list_1)









# # Map function using lambda Function...    Here, there is no need to define a function outside... 


# list_1 = [1, 2, 3, 4, 5, 6]

# new_list_1 = list(map(lambda x: x*x*x, list_1))

# print(new_list_1)









# # *** Filter... 

# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new swquence containg only the elements that meet the predicate. The flter function has the following syntax... 

# filter(predicate, iterable)









# # Use of Filter... 



# def filter_function(a):
    
#     return a > 3

# list_1 = [2, 4, 8, 3, 1, 6, 9]
# print(list_1)

# new_list_1 = list(filter(filter_function, list_1))

# print(new_list_1)









# # Filter function using lambda Function...       Here, there is no need to define any function outside... 



# list_1 = [2, 4, 8, 3, 1, 6, 9]

# new_list_1 = list(filter(lambda x: x > 3 and x < 8, list_1))

# print(new_list_1)
# print(list_1)









# # *** Reduce... 

# The Reduce function is a higher order function that applies function to a sequence and returns a single value. Is is a part of the functions module in Python and has the following Syntax...

# reduce(function, Iterable)









# # Use of Reduce with normal function... 



from functools import reduce

# def my_sum(x, y):
#     return x + y

# numbers = [1, 2, 3, 4, 5, 6]

# sum = reduce(my_sum, numbers)

# print(sum)









# Use of Reduce with the help of Lambda Function... 



numbers = [1, 2, 3, 4, 5, 6]

sum = reduce(lambda x, y: x + y, numbers)

print(numbers)
print("The Sum of the Numbers :", sum)

