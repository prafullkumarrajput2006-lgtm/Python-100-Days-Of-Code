# # Walrus Operator in Python... 


# The walrus operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a  loop, but don't want to repeat the calculation...

# he walrus operator is represented by the ":=" syntax and can be used in a variety of contexts including while loops and if statements...








# # *** Without using Walrus Operator... 



# a = True
# print(a = False)









# # *** Using Walrus Operator... 



# a = True
# print(a := False)






# happy = False
# print(happy)

# print(happy := True)









# # *** Example of Walrus Operator... 



# numbers = [25, 78, 58, 96, 23, 12, 45] 

# while (n := len(numbers)) > 0:
#     print("The poped item is : ",numbers.pop())
#     print(numbers)









# # *** Without using Walrus Operator... 



# foods = list()
# while True:
#     food = input("What food do you like ?:")
#     if food == "quit":
#         break
#     food.append(food)









# *** Using Walrus Operator... 



foods = list()

while (food := input("What food do you like ? : ")) != "quit":
    foods.append(food)
    