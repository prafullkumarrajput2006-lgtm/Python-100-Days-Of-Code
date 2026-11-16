# # OS Module in Python... 



# The OS module in Python os a built-in library that provides functions for interacting with the operating system. It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.

# It can delete any file from any folder
# It can create a file or folder in the OS  









# # *** This is the demo of the OS Module in the Another dedicated Folder named... OS Module Introduction Day46




# import os

# if(not os.path.exists("data")):
#     os.mkdir("data")


# for i in range(0, 100):
#     # os.mkdir(f"data/Day{i+1}")
    
#     # os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}")
    
#     # os.rename(f"data/Tutorial{i+1}", f"data/Tutorial {i+1}")
    
#     folders = os.listdir("data")
#     print(folders)
    
    
#     # for folder in folders:
#     #     print(folder)
    
    
#     for folder in folders:
#         print(folder)
#         print(os.listdir(f"data/{folder}"))   

       
# print(os.getcwd())