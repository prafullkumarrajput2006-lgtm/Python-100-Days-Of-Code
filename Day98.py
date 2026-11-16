# # Multiprocessing in Python... 



# Multiprocessing is a Python module that provides a simple way to run multiple processes in parallel. It allows you to take advantage of multiple cores or processors on your system and can significantly improve the performance of your code. In the repl, we'll take a closer look at the multiprocessing module and its variour function and how they can be used in Python...







import multiprocessing

def my_func():
    print("Hello From Process", multiprocessing.current_process().name)
    
    process = multiprocessing.Process(target=my_func)
    process.start()
    process.join()