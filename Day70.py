# # Class Method as Alternative Constructor in Python...Use for giving the output of the different data format 


# It works as a constructor and the motive of it's also same but the difference is that here we don't need to identify the parameter and it is used for performing the action on a perticular type of data...they use class methods as alternative constructors...









# # Example 1... 




# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
        
#     @classmethod
#     def fromStr(cls, string):
#         return cls(string.split("-")[0], int(string.split("-")[1]))
        
        
# e1 = Employee("Prafull", 10000000)
# print(e1.name)
# print(e1.salary)

# string = "John-10000"                              # Alternative Constructor... 
# e2 = Employee.fromStr(string)
# print(e2.name)
# print(e2.salary)
       
       
       
       
       
       
       
       
       
# # Example 2... 



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     @classmethod
#     def from_string(cls, string):
#         # name, age = string.split(',')
#         # return cls(name, int(age))  
#         return cls(string.split(",")[0], int(string.split(",")[1]))
    
    
# Person = Person.from_string("Prafull Rajput, 21")             
# print(Person.name, Person.age)









# # Example 3... 



# class Employee:
#     def __init__(self, name, department):
#         self.name = name
#         self.department = department
        
#     @classmethod
#     def from_String(cls, string):
#         return cls(string.split("_")[0], string.split("_")[1])    

# Employee = Employee.from_String("Prafull Rajput_AI Engineer")        
# print(Employee.name, Employee.department)