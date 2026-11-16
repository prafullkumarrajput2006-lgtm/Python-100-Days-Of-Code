# Getters & Setters in Python... 



# # Getters... 


# Getters in Python are methods that are used to access the value of an ibject's properties. They are used to retrun value of a specific, and are typically defined using the @property decorator. Here is an example of a simple class with a getter method...









# # *** Without Getter...



# class Myclass:
#     def __init__(self, value):
#         self._value = value
        
#     def show(self):
#         print(f"Value is {self._value}")    

# @property
# def value(self):
#     return self._value

# obj = Myclass(10)
# obj.show()









# # *** With Getter... 


# class MyClass:
#     def __init__(self, value):
#         self.value = value
        
#     def show(self):
#         print(f"The value is {self.value}")    

#     @property
#     def ten_value(self):                      # Getter
#         return 10 * self.value    

# obj =  MyClass(10)  
# print(obj.ten_value)      
# obj.show()









# # Setter...



# It is important to note that the getters do not take any parameter ans we cannot set the value through getter method. For that we need setter method which can be added by decorating method with @property_name.setter 









# With Setter... 



class MyClass:
    def __init__(self, value):
        self.value = value
        
    def show(self):
        print(f"The value is {self.value}")    

    @property
    def ten_value(self):
        return 10 * self.value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self.value = new_value/10
        
        
obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()
