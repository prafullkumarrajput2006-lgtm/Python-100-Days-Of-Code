# seek(), tell(), and other Functions... File Handling Functions...


# In python, the seek() and tell() functions are used to work with the object and their positions within a file. These functions are part of the built-in to module, which provides a consistent interface for reading and writing to various file like object, such as files, pipes and in memory buffers... 







# # SEEK()Functions ... 

# this function allows you to move the current position within a file to a specific point, The position is specified and you can move either forward or backward from the currecnt position. 









# # 1. Seek Function()... 



# with open('myfile.txt', 'r') as f :
#     print(type(f))
    
#     #Moov to the 10th byte in the file...
    
#     f.seek(10)


#     #Read the next  bytes

#     data = f.read(5)
#     print(data)









# # TELL()Functions ...


# This function returns the current position within the file, in bytes. This can be useful for keeping track of your location. Within the file or for seeking to a specific position relative to the currecnt position... 









# # 2. Tell Function()... 



# with open('myfile.txt', 'r') as f:
#     print(type(f))

#     f.seek(10)

#     print(f.tell())









# # TRUNCATE Function... 


# When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the node as 'w' or 'a' the file is opened in write mode and you can write to the file. However, if you want to truncate the file to a specific size, you can use the truncate function... 
    





# 3. Truncate Function... 


with open('myfile.txt', 'w') as f:
    
    f.write("Hello World")
    print(f)
    
    f.truncate(7)
    
    
  

    
