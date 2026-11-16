# # Single Inheritance in Python... 



# Single inheritance is a type of inheritance where a class inherits properties and behaviour from a single parent class. This is the simplest and most common form of inheritance... 

# The Syntax for single inheritance in Python is strightforward and easy to understand. To create a new class that inherits from a parent class simply specify the parent class in the class defination, insaide the parenthesis...


# class childClass(ParentClass):









# # Example 1... 




# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def make_sound(self):
#         print("Sound made by the Animal")    

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def make_sound(self):
#         print("Bark!")            

        
# d = Dog("Jacku", "Desi")        
# d.make_sound()
# print(d.name, d.species, d.breed)

# a = Animal("Jacson", "Premium Dog")
# a.make_sound()
# print(a.name, a.species)









# # Example 2... 




# class Animal:
#     def __init__(self, name, category):
#         self.name = name
#         self.category = category
        
#     def make_sound(self):
#         print("Sound by the Animal")    

#     def size(self):
#         print("Size of the Animal")    

# class Cat(Animal):
#     def __init__(self, name, food):
#         Animal.__init__(self, name, category= "Lion Category")
#         self.food = food
        
#     def make_sound(self):    
#         print("Meaw!")


# c = Cat("Pussy", "Milk")        
# c.make_sound()
# print(c.name, c.food, c.category)
        
        
# l = Animal("Sheru", "Lion")        
# l.make_sound()
# print(l.name, l.category)