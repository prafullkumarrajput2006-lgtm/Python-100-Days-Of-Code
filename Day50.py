# read(), readlines() and other methods of FIle Handling...  
    



# # 1. Simple use case of readline()... 



# f = open('myfile.txt', 'r')

# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         break









# # 2. Print the marks of the students using readline()... 



# f = open('myfile.txt', 'r')
# i = 0

# while True:
#     i += 1
#     line = f.readline()

#     if not line:
#         break
    
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
    
#     print(f"Marks of student {i} in Math is : {m1}")
#     print(f"Marks of student {i} in English is : {m2}")
#     print(f"Marks of student {i} in G.K. is : {m3}")
    
#     print(line)









# # 3. Writeline... 



# f = open('myfile.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# print(lines)
# f.close()






