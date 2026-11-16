# # Multiple Inheritance... 



# Multiple Inheritance is a powerful featurs in OOPs that follows a class to inherit attribute and methods from multiple parent classes. This can be useful in situation where a class needs to inherit functionality form multiple sources... 

# Syntax...


# class childClass(ParentClass1, ParentClass2, ParentClass3):









class Employee:
    def __init__(self, name):
        self.name = name
        
    def show(self):
        print(f"The name is {self.name}")   
         


class Dancer:
    def __init__(self, dance):
        self.dance = dance
        
    def show(self):
        print(f"The dance is {self.dance}")  
          
        

class DancerEmployee(Employee, Dancer):             # If we put dance first and then call show method then "Kathak will be print not "Shivani
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance
        

DE = DancerEmployee("Shivani", "Kathak")        
print(DE.name, DE.dance)
DE.show()                                           #  SHivani will print because in class DancerClass the first parameter is Employee 


E = Employee("Pankaj")
print(E.name)
E.show()


D = Dancer("Neha")
print(D.dance)
D.show()
