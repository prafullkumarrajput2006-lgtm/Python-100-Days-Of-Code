# # Super Keyword in Pyhton... 



# The super() keyword in Pyhton is used to refer to the parent class. It is especially useful when a class inherits from multiple parent and you want to call a method from one of the parent classes...

# When a c;ass inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes you might want to use the parent class method in the child class. This is where the super() keyowrd is handy. 









# # Example 1... 




# class ParentClass:
#     def parent_method(self):
#         print("This is the Parent method")

# class ChildClass(ParentClass):
    
#     def parent_method(self):
#         print("Prafull")
#         super().parent_method()
        

#     def child_method(self):
#         print("This is the child method")
#         super().parent_method()    
                              
        
# child_object = ChildClass()                  # object created named child_object

# child_object.child_method()                  # it Calls the child method

# child_object.parent_method()                 # it calls the parent method









# # Example 2... Without Using Super keyword...




# class Employee:
#     def __init__(self, name, id):
#         self.name = name 
#         self.id = id
        

# class Programmer:
#     def __init__(self, name, id, language):        
#         self.name = name 
#         self.id = id
#         self.language = language
        
        
# Prafull = Employee("Prafull", 101)        
# Piyush = Programmer("Piyush", 102, "C++")     

# print(Prafull.name, Prafull.id)   
# print(Piyush.name, Piyush.id, Piyush.language)
        
        
        
        
        
        
        


# Example 2... With using super keyword... Reuse the code of the parent class...




class Employee:
    def __init__(self, name, id):        
        self.name = name
        self.id = id
        

class Programmer(Employee):
    def __init__(self, name, id, language):
        self.language = language
        super().__init__(name, id)  
        

Prafull = Employee("Prafull", 101)              
Piyush = Programmer("Piyush", 102, "C++")

print(Prafull.name, Prafull.id)
print(Piyush.name, Piyush.id, Piyush.language)



