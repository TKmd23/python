# import urllib.request
#
# opener = urllib.request.build_opener()
# response = opener.open("https://httpbin.org/")
# print(response.read())
# -----------------------------------
# import requests
#
# response = requests.get("https://httpbin.org/get")
# print(response.content)
# print(f"Datatype - {type(response.content)}")
# print(response.text)
# print(f"Datatype - {type(response.text)}")
# --------------------------------------
import requests

response = requests.post("https://httpbin.org/post", data="Test data", headers={"h1": "Test title"})
print(response.text)
