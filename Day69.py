# # Class Method in Python... Like Static Method...Day65



# In Python, classes are a way to define custom data type that can store data and define functions that can manipulate that data. One type of function that can be defined within a class is called a "method". In this blog post, we will explore what Python class methods are, why they are useful and how to use them...









# # *** Without class Method... 



# class Employee:
    
#     company = "Apple"
    
#     def show(self):
#         print(f"The name is {self.name} and the company is {self.company}")
        
#     def changeCompany(cls, newCompany):
#         cls.company = newCompany
        
        
# e1 = Employee()
# e1.name = "Prafull" 
# e1.show()
# e1.changeCompany("Samsung")           
# e1.show()
# print(Employee.company)                       # Gives the output "Apple"









# *** With Class Method... 




class Employee:
    
    company = "Apple"
    
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")
    
    @classmethod    
    def changeCompany(cls, newCompany):
        cls.company = newCompany
        
        
e1 = Employee()
e1.name = "Prafull" 
e1.show()
e1.changeCompany("Samsung")           
e1.show()
print(Employee.company)                       # Gives the output "Samsung"