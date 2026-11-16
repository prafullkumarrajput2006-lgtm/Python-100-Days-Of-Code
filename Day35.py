# loops with else in Python... 




# *** FOR LOOP... 





# # *** 1. In normal COndition... 



# for i in range(11):
#     print(i)

# else:
#     print("sorry")   









# # *** 2. Where else statement will execute... 



# for i in range(6):
#     print(i)
#     if i == 4:
#         continue

# else:
#     print("sorry") 









# # *** 3. Here else statement will not excecute...      Because here loop becomes break not complete loop executing...


# for i in range (6):
#     print(i)   
#     if i == 4:
#         break
    
# else:
#     print("Sorry")    







# *** WHILE LOOP... 




# # *** 1.  Here else will execute... 


# i = 0
# while i <= 7:
#     print(i)
#     i+=1
    
#     if i == 4:
#         continue
    
# else:
#     print("Sorry")    









# # *** 2. Here else will not execute... 




# i = 0
# while i <= 7:
#     print(i)
#     i+=1
    
#     if i == 4:
#         break
    
# else:
#     print("Sorry")    