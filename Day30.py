# Recursion in Python... When function called itself again and again...



# # 1.   Method 1... 



# def factorial(n):
#     if (n == 0) or (n == 1):
#         return 1
#     else:
#         result =  n * factorial(n-1)
    
#     print("The factorial of", n, "=", result)
#     return result

# factorial(7)









# # Method 2... 



# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else :
#         return n * factorial(n-1)
    
# print("The Factorial of", 5, "=", factorial(5))    











# *** Fibonacci Series... 




# n = int(input("Enter the number up to which you want to print the fibonacci series : "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")  

#     c = a + b
#     a = b 
#     b = c    







# def fibonacci(n):
#     if n <= 1:
#         return n

#     return fibonacci(n - 1) + fibonacci(n - 2)


# n = int(input("Enter the number of terms: "))

# for i in range(n):
#     print(fibonacci(i), end=" ")












