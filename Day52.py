# # Lambda Function... 


# A lambda function is a small anonymous fuction without a name. It is defined using the lambda keyword and has the following syntax...

# lambda arguments: expression









# # Without Lambda function... 


# def double(x):
#     return x * 2

# print(double(5))









# # With Lambda Function... 


# double = lambda x: x*2
# cube = lambda x: x*x*x
# square = lambda x: x*x
# avg = lambda x, y: (x+y)/2


# print("Double is",double(5))
# print("Cube is",cube(5))
# print("Square is",square(5))
# print("The sum is", avg(5,8))









# # Function is passing by the another function... 


# def apply(fx, value):
#     return 6 + fx(value)

# cube = lambda x: x*x*x

# print("The cube is", cube(5))

# print(apply(cube, 2))                         # Gives output 14
# print(apply(lambda x: x*x, 2))                # Gives Output 10
