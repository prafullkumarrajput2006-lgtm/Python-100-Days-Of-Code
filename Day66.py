# Instance Variable VS Class Variable... 



# In Pyhton, variables can be defined at the class level or at the instance level. Understanding the difference between these types of variables is crucial for writing efficient and maintainable code...  









# # *** Class Variable... 


# Class variable are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is comman to all instance of the class. For example a class variable can be used to store the number of instance of a class that have been created... 










# # *** Instance Variable... 


# Instance variable are defined at the instance level and are unique to each instance of the class. They are defined inside that init method and are usually used to store information that is specific to each instance of the class. For example, an instance variable can be used to store the name of an employee in a class that represnets an employee...









# Use of Class variable and Instance Variable... 




class Employee:
    
    companyName = "Apple"                            # Class Variable... These will be same for all the Entities
    NoOfEmployee = 0
      
    def __init__(self, name):
        self.name = name                             # Instance Variable... These will be vary for all the Entities
        self.raise_amount = 0.02                     # Instance Variable... These will be vary for all the Entities
        Employee.NoOfEmployee += 1
        
    def showDetials(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.NoOfEmployee} sized company {self.companyName} is  {self.raise_amount}")    




emp1 = Employee("Prafull")
emp1.raise_amount = 0.3                             # Instance Variable... These will be vary for all the Entities

# Here it gives the priority to the Instance Variable if it is present, if it is not present if will provide the default value of class Variable

emp1.companyName = "Apple India"                    
emp1.showDetials()                                  #OR... Employee.showDetials(emp1)   
    
emp2 = Employee("Piyush")    
emp2.showDetials()
      
