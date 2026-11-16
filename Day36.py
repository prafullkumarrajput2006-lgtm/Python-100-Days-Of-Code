# Error Handling in Python... 




# # ***Normal Table print of any number... 



# a = int(input("Enter the number : "))
# print("The table of", a, "is :")
# for i in range(1, 11):
    
#     print(a, "*", i, "=", a * i)









# *** Exception Handling...



# # 1. Method 1... Difference on the position of the try...



# a = (input("Enter the number : "))
# print(f"Multiplication table of {a} is : ")

# try:
#     for i in range(1, 11):
#         print(f"{a} X {i} = {int(a) * i}")        
# except :
#     print("Sorry Error Occur")        
    

# print("End of program")









# # 2. Method 2... 



# try:
#     a = int(input("Enter the number : "))
#     print(f"The multiplication table of {a} is :")

#     for i in range(1,11):
#         print(f"{a} X {i} = ", a*i)
        
# except :
#     print("Invalid Input")        


# print("End of the Program")    









# # 3. Specific Type of error handling... ValueError


# try:
#     n = int(input("Enter an Integer: "))
    
#     print(f"The number which you have entered is {n}.")
    
#     a = [6,5,8,3,5,2,7,9,2,1]
#     print(a[n])
    
#     print(n, f"is present in the list of an Integer at place of {a(n)}")
    
# except ValueError:
#     print("Number entered is not an integer.")
    
# except IndexError:
#     print("Index Error")    
    
# print("Hello Python")    









# # 4. Much Complex... 



# try:
#     n = int(input("Enter an Integer: "))

#     a = [6, 5, 8, 3, 5, 2, 7, 9, 2, 1]

#     print(f"The number you entered is {n}.")

#     print(f"The number {n} is present at index {a.index(n)}.")

# except ValueError:
#     try:
#         int(n)
#     except NameError:
#         print("Please enter a valid integer.")
#     else:
#         print(f"The given number {n} is not present in the list.")

# print("Hello Python")



