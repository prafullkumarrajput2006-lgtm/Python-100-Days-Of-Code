# Solution of Exercise 2... Day15




# Greeting According to the time... 




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
