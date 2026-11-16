# # Method Overriding in Pyhton... 



# Method OVerriding is a powerful feature in OOPs that allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When you crwate an instance of the derived class and call the overridden method, the version of the method int he derived class is executed, ather than the version in the base class...

# In Python, the method overriding is a way to customize the behaviour of a class based on its specific needs. For example, consider the following base class...








class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
        
# Overriding...Yahan Circle class ne parent class ke area() method ko same name se dobara define kiya hai, lekin calculation alag hai.       
        
    def area(self):                                    
        return 3.14 * self.radius * self.radius   
            
            
        
square = Shape(5, 5)
print("The area of the square is :",square.area())

circle = Circle(5)
print("The area of the Circle is :",circle.area())