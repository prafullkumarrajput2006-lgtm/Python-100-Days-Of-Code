# # AsyncIO in Python... 


# Asynchronous I/O or Async for short is a programming pattern that allows for high performance I/O operations in a concurrent and non-blocking manner. In Python async programmin is achieved through the use of the asyncio module and asynchronous functions...









# *** Method 1... 



import time
import asyncio

# async def function1():
#     await asyncio.sleep(1)
#     # time.sleep(3)
#     print("func 1")
    
    
# async def function2():
#     await asyncio.sleep(1)
#     # time.sleep(3)
#     print("func 2")
    

# async def function3():
#     await asyncio.sleep(4)
#     # time.sleep(3)
#     print("func 3")     
    

# async def main():
#     task = asyncio.create_task(function1())
#     # await function1()
#     await function2()
#     await function3()     
         
    
# asyncio.run(main())









# *** Method 2... 



async def function1():
    await asyncio.sleep(1)
    # time.sleep(3)
    print("func 1")
    
    
async def function2():
    await asyncio.sleep(1)
    # time.sleep(3)
    print("func 2")
    

async def function3():
    await asyncio.sleep(4)
    # time.sleep(3)
    print("func 3")
    
    
async def main():
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )   
    
    print(L)          
