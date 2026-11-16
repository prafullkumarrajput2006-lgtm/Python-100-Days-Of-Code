# # Magic/Dunder Methods in Python... 




# These are special methods that you can define in your classes, and invoked, they give you a powerful way to manipulate objects and their behaviour.

# Magic methods, also known as "dunders" from the double underscore surrounding their names, are powerful tools that allow you to cutomize the behaviour of your classes. They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptions and properties.









# # *** Method 1 ... Unfamiliar




# class Employee:
#     name = "Harry"
    
#     def __len__(self):
#         i = 0
#         for c in self.name:
#             i = i + 1
#         return i

# e = Employee()
# print(e.name)
# print(len(e))                      # We have define the function with __len__ but we call the function with only (len) that's why magic fun









# # *** Method 2... Familiar Method




class Employee:
    def __init__(self, name):
        self.name = name
        
    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return i
    
    def __str__(self):
        return (f"The name of the Employee is {self.name} str")                # For magic method we havo to return not print...
    



# # Here it will print only str method but if str method is not present  then only it will print otherwise not             
    
    
#     def __repr__(self):
#         return (f"The name of the Employee is {self.name} repr")    
   
    
e = Employee("Prafull")        
print(e.name)
print(len(e))
print(e)
