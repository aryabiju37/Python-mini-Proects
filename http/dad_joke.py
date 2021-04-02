import requests

url = "https://icanhazdadjoke.com/"

#not all websites handles text/plain
#response = requests.get(url,headers={"Accept":"text/plain"})
response = requests.get(url,headers={"Accept":"application/json"})
#print(response.text)

data = response.json()
print(data["joke"])