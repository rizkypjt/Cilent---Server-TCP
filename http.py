import requests
url = "http://192.168.10.95/"
req = requests.get(url)
print("HTTP status code :") + str(req.status_code)
print(req.content)
