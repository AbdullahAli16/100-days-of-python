# Day: 89(Requests module)

''' The Requests module is an HTTP library that enables developers to send HTTP requests in python.
    It enables you to send HTTP requests using python code and makes it possible to interact with
    APIs and web services '''

import requests

# GET method is used to retrieve something from the server
response=requests.get("http://www.google.com")      

print(response.status_code) # 200 means OK or failed (404,500 etc)
print(response.text)        # Raw text response
print(response.json())      # Parsed JSON (if applicable)


data = {"name": "Bob", "age": 30}

# POST method is used to send something to the server
response = requests.post("https://httpbin.org/post",json=data)

print(response.status_code)
print(response.json())  # See what the server got from us