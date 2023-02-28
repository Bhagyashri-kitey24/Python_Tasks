import urllib.response
response= urllib.request.urlopen("https://www.python.org/")
print(response)
print(response.status)
print(response.headers)