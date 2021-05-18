#!/usr/bin/python3



import requests as req
 
response = req.get('https://api.github.com/events')

# Response code
print("Response code -> r")
print(response) # <Response [200]>

# Response Content
print("\nResponse content -> r.text")
print(response.text)


# find out the econding Requests is using
print("\nfind out the econding Requests is using -> r.encoding")
print(response.encoding)

# Access the response body as bytes
print("\nAccess the response body as bytes -> r.content")
print(response.content)

# Json Response
print("\nJson Response -> r.json()")
print(response.json())

# Json Response raise status
print("\nJson Response raise status -> r.raise_for_status()")
print(response.raise_for_status())

# Check for status code
print("\n Check status code -> r.status_code")
print(response.status_code)
