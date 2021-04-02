import requests

resp = requests.get("https://www.ycombinator.com")
print(resp.headers)