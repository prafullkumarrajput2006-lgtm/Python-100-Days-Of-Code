# # Access Specifier/Modifiers in Python... 



# Acess specifiers or access modifiers in Python programming are used to limit the access of class variables and class methods outsode of class while implementing the concepts of inheritance...




# Type of Acess Specifier/Modifiers...


# 1. Public Acess Specifier/Modifiers
# 2. Private Acess Specifier/Modifiers
# 3. Protected Acess Specifier/Modifiers









# # *** Public Access Modifier... 


# All the variables and methods(member function) in Python are by default public. Any instance variable in a class followed by the 'self' keyword ie. self.var_name are public accessed...




# class Employee:
#     def __init__(self):
#         self.name = "Prafull Rajput"

# a = Employee()
# print(a.name)        



#        #OR


# class Employee:
#     def __init__(self, name):
#         self.name = name

# a = Employee("Prafull")
# print(a.name)  









# # *** Private Access Modifier...   



# Prive members of a class(variable and methods) are those members which are only accessible inside the class. We cannot use rivate member outside the class.

# In python, there is not strict concept of "private" access modifiers like in soe other programming languages. However, a conventional has been established to indicate that a varibel of method should be considered private by prefixing its name with a double underscore(_). This is known as a "weak internal use indicator" and it is a convention only nt a strict rule. Code outside the class can still access "private" variable and methods, but it is generally understand that they should not be accessed or modified...    







# class Employee:
#     def __init__(self):
#         self.__name = "Prafull Kumar Rajput"
        
# a = Employee()
# # print(a.__name)                   # Cannot be accessed directly       
# print(a._Employee__name)            # Can be accessed indirectly by using name mangling...

# print(a.__dir__())









# # *** Protected Access Modifier... 



# In OOPs the term "Protected" is used to describe a member(method or attribute) of a class that is intended to be accessed only by the class itself and its subclass. In Python, the convention for indicating that a member is protected is to prefix its name with a sngle underscore(_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclass.print

# It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. The syntax we followed by a single underscore(_).  









# class Student:
#     def __init__(self):
#         self._name = "Prafull"

#     def _funName(self):                         # Protected Method
#         return "CodeWithPrafull" 
    
# class Subject(Student):                         # Inherited Class
#     pass


# obj = Student()
# obj1 = Subject()   
 
# print(obj.__dir__())
# print(obj1.__dir__())


# # Calling by object of Student class

# print(obj._name)
# print(obj._funName())   


# # Calling by object of Subject class

# print(obj1._name)
# print(obj1._funName())