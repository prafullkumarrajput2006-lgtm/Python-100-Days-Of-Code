# # Multilevel Inheritance in Python... 



# Multilevel Inheritance is a type of Inheritance in OOPs where a derived class inherits from another derived class. This type of inheritaance allows you to build a hierarchy of classes where one class builds upon another, leading to a more specilized class.

# Inpython, multilevel inheritance is achieved using the class hierarchy. The syntax form multilevel inheritance is quite simple and follows the same syntax as single inheritance 




# Syntax...  



# class BaseClass:
#     # Code...
    
# class DerivedClass1(BaseClass):
#     # Derived class 1 code          
    
# class
# DerivedClass2(DerivedClass1):
#     # Derived class 2 code 








class Animal:
    def __init__(self, name, species):                 
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name : {self.name}")  
        print(f"Species : {self.species}")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed : {self.breed}")        
        
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f"Color : {self.color}")
        
        
        

o = GoldenRetriever("Tomy", "Black")        
o.show_details()
print(GoldenRetriever.mro())

p = Dog("Jacku", "Desi")
p.show_details()
print(Dog.mro())

q = Animal("Sultan", "Dog")
q.show_details()
print(Animal.mro())



