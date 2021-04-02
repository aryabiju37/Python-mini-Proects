import requests

url = "http://www.google.com/"
response = requests.get(url)
print(f"your request to {url} came back w/ status {response.status_code}")