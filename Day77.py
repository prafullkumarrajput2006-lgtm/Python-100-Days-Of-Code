# # Operator Overloading in Python... 




# Operator Overloading is a feature in Python that allows developers to redefine the behaviour of mathematical and comparison operators for custom data types. THis means that you can use the standard mathematical operators (+, -, *, /, etc) and comparison operators (>, <, ==, etc) in your own classes, just as you would for built-in data types like int, float, and str...









# # *** Why do we need Operator Overloading... 



# Operator oveloading allow you to create more readable and intuitive code. For instance, consider a custom class that represents a point in 2D space. You could define a method called 'add' to ass two points together, but using the + operator makes the code more concise and readable... 









class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
        
    def __str__(self):
        return (f"{self.i}i + {self.j}j + {self.k}k") 
    
    
    
# Tumne + operator ka default behaviour apni Vector class ke according customize kar diya.. yehi h operator overloading kyuki yaha humne + operator ka use apne according krwaya h yaha + ka use i se i ko, j se j ko and k se k ko add krne ke liye use kiya gya h   
    
    def __add__(self, x):
        # return (f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k")        # It will give the output in STRING... 
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)
    
v1 = Vector(2, 5, 9)            
print(v1)

v2 = Vector(5, 9, 6)
print(v2)

print("The sum of the vectors is :", v1 + v2)
print(type(v1 + v2))
        