#!/usr/bin/python3

import requests as req

try:
    response = req.get('https://api.github.com/events')
except req.exceptions.RequestException as e:
    raise SystemExit(e)

# Response code
print("Response code -> r")
print(response) # <Response [200]>

# Response Content
print("\nResponse content -> r.text")
with open("text_response.txt", "w") as writer:
    print("writing response with r.text ...")
    writer.write(response.text)


# find out the econding Requests is using
print("\nfind out the econding, Requests is using with -> r.encoding")
print(response.encoding)

# Access the response body as bytes
print("\nAccess the response body as bytes -> r.content")
with open("bytes_response.txt", "w") as writer:
    print("writing response in bytes ...")
    writer.write(str(response.content))

# Json Response
print("\nJson Response -> r.json()")
with open("json_response.txt", "w") as writer:
    print("writing response in Json ...")
    writer.write(str(response.json()))

# Json Response raise status
print("\nJson Response raise status -> r.raise_for_status()")
print(response.raise_for_status())

# Check for status code
print("\nCheck status code -> r.status_code")
print(response.status_code)

# check for response status
print("\nCheck for status ok with -> r.ok")
print(response.ok)
