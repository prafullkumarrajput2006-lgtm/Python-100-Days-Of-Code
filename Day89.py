# # Request Module in Python... 


# The Python request Module is an HTTP library that enables developers to send HTTP requests in Python. This module enables you to send HTTP request using Python code and makes it possible to interact with APIs and web services 




import requests

response = requests.get("https://www.google.com")
print(response.text)