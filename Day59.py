# # Decorators in Python... 


# Python decorators are a powerful and versatile tool that allow you to modify the behaviour of function and methods. They are a way to extend the functionality of a function or method without modifying its source code.

# A decorator is a function that takes another function as an argument and returns a new function that modified the behaviur of the origin=onal fucntion is often referred as a "decorator" function. The basic syntax for using decorator is the following...



# @decorator_function
# def my_function():
#     pass









# # *** Without Decorator... Like normal Function... 


# def hello():
#     print("Hello Python")

# hello()    









# *** With Decorator... 



# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using this function")
#     return mfx


# @greet

# def hello():
#     print("Hello Python")
    
# hello()    

# def add(a, b):
#     print(a+b)  
    
# add(5,8)   









def greet(fx):

    def mfx(*args, **kwargs):

        print("Good Morning")

        fx(*args, **kwargs)

        print("Thanks for using this function")

    return mfx


@greet
def hello():
    print("Hello Python")


@greet
def add(a, b):
    print(a + b)
    
    
@greet
def mul(a,b):
    print(a*b)    


hello() 
add(5,8)
mul(5,5)
      

    