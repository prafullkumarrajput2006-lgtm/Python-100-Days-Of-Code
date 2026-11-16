# # Excercise 2... Question...




# Greeting According to the time... 




# # 1. Method 1... 



# time = int(input("Enter the Current Time (24 Hours Format) : "))
# print("The time is : ", time)

# if time > 5 and time < 12 :
#     print("Good Morning Sir")
# elif time > 12 and time < 17 :
#     print("Good After Noon Sir")
# elif time > 17 and time < 19  :
#     print("Good Evening Sir")
# else:
#     print("Good Night Sir")
    
    







# 2. Method 2... 


import time

timestamp = time.strftime('%H:%M:%S')

print(timestamp)

timestamp_Hour = int(time.strftime('%H'))
timestamp_Minute = int(time.strftime('%M'))
timestamp_Second = int(time.strftime('%S'))

print("Hours:", timestamp_Hour)
print("Minutes:", timestamp_Minute)
print("Seconds:", timestamp_Second)

if timestamp_Hour >= 5 and timestamp_Hour < 12:
    print("Good Morning Sir")

elif timestamp_Hour >= 12 and timestamp_Hour < 17:
    print("Good Afternoon Sir")

elif timestamp_Hour >= 17 and timestamp_Hour < 20:
    print("Good Evening Sir")

else:
    print("Good Night Sir")








