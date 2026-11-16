# Finally Keyword in Python... The code which is inside the finally that will be always execute... 




# # *** SImple Use of FInally... 


# try:
#     l = [1,5,4,9,7]

#     i = int(input("Enter the index : "))
#     print(f"The value of index {i} is ",l[i])

# except:
#     print("Some Error Occur")    

# finally:
#     print("I'm always Executed")









# *** Main use of the Finally in Function... 


def func1():
    try:
        l = [1,5,8,9,4]

        i = int(input("Enter the index : "))
        print(f"The value of index {i} is : ", l[i])
        return 1
    
    except:
        print("Some Error Occured")
        return 0
    
    finally:
        print("I'm always Ececuted")


x = func1()
print(x)        

