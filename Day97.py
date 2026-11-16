# # Multithreading in Python... 



# Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process. In Python, we can use the threading module to implement multithreading. In this tutorial, we will take a closer at the threading module and its various functions and how they can be used in Python... 









# # *** Without Multithreading... 


import threading
import time


# time1 = time.perf_counter()

# def func(seconds):
#     print(f"Sleepping for {seconds} seconds")
#     time.sleep(seconds)
    
# func(4)    
# func(2)
# func(1)

# time2 = time.perf_counter()
# print(time2 - time1)









# # *** With Multithreading...



# time1 = time.perf_counter()

# def func(seconds):
#     print(f"Sleepping for {seconds} seconds")
#     time.sleep(seconds)


# t1 = threading.Thread(target=func, args=[4])
# t2 = threading.Thread(target=func, args=[2])
# t3 = threading.Thread(target=func, args=[1])



# t1.start()
# t2.start()
# t3.start()



# # t1.join()
# # t2.join()
# # t3.join()


# time2 = time.perf_counter()
# print("\nThe total time taken is :", time2 - time1)

