import requests


url = "http://www.google.com"
response = requests.get(url)
print("your request to {url} came back w/ the status code {sta}".format(url = url,sta = response.status_code))