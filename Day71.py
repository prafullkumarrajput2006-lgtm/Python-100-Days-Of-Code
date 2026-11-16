# # dir, __dict__, help method in Python... 


# We must look into dir(), __dir__() and help() attribute/methods in Python. They make it easy for us to understand how classes resolve various functions and executes code. In python, there are three built-in functions that are commonly used to get the information about objects: dir(), dict() and help(). Let's take a look at each of them... 









# 1. *** dir() Method...


# dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object...





# # *** List***


# x = [1, 2, 3]
# print(dir(x))
# print(x.__add__)





# # *** Tuple ***


# x = (1, 2, 3)
# print(dir(x))
# print(x.__add__)









# # 2. *** __dict__ attribute... 



# __dict__: The __dict__ attribute returns a doctionary representation of an object's attributes. It is a useful for introspection...





# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.version = 1
        
        
# p = Person("Prafull Rajput", 21)        
# print(p.__dict__)









# # 3. *** help() method... 



# help(): The help() method is used to get help documentation for an bject, including a description of its attributes and methods...






# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.version = 1
        
        
# p = Person("Prafull Rajput", 21)        
# print(p.__dict__)

# print(help(Person))
