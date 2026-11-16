# File IO in Python... File Handling... 




# # 1. Create a file ... 


# f = open("myfile.txt", "w")

# f.close()









# # # 2. Open the file in read mode... 

# # r mode : open the file in read mode and gives an error when file doesn't exists... 



# f = open('myfile.txt', 'r')

# text = f.read()

# print(text)

# f.close()









# # 3. Open the file in write mode... and write something...

# *** It removes all the previous written content ... 



# f = open('myfile.txt', 'w')

# text = f.write("I'm Good bro. ")

# print(text)

# f.close()









# # 4. Open the file in append mode... Add the content at the end of the previous content.


# f = open('myfile.txt', 'a')

# text = f.write("What about you ?")

# print(text)

# f.close()









# 5. OPERATIONS BY SIMPLE METHOD AND WITHOUT USING CLOSE() STATEMENT... 


with open('myfile.txt', 'a') as f:
    f.write("Hey I'm inside with")










