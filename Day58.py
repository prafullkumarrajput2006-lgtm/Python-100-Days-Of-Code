# # Constructors in Pyhton...    It helps to create an object


# A constructor is a special method in a class used to create and initiaize an object of a class.There are different types of constructors. It is invoked automatically when an object of a class is created.Person

# A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. it connot return any value other than none.



# 1. Parameterized Constructor
# 2. Default constructor









# # *** Normal use of class and Objects... 


# class Person:
#     name = "Prafull"
#     occupation = "AI Engineer"

#     def info(self):
#         print(f"{self.name} is a {self.occupation}")


# a = Person()
# # print(a.name, a.occupation)
# a.info()









# # *** Parameterized constructor...



# class Person():
    
#     def __init__(self, name, occupation):                              # Parameterized Constructor...
#         print("Hey I am a person")
#         self.name = name
#         self.occupation = occupation
        
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")    
        


# a = Person("Prafull", "AI Engineer")
# b = Person("Piyush", "Labour")
# c = Person(1, 2)

# a.info()
# b.info()
# c.info()









# # *** Default Constructors... 


# class Person:
#     def __init__(self):
#         print("Hey, I'm a Person")


# a = Person()    












# ********** In Simple Words **********




# # *** Without constructor...     




# class Employee:
#     pass


# e1 = Employee()
# e1.name = "Prafull"
# e1.id = 101

# e2 = Employee()
# e2.name = "Rahul"
# e2.id = 102









# # *** With constructor... 




# class Employee:

#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def show(self):
#         print(f"Name: {self.name}, ID: {self.id}")


# e1 = Employee("Prafull", 101)
# e2 = Employee("Rahul", 102)

# e1.show()
# e2.show()

