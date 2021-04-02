import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text,"html.parser")
pagination = soup.find_all("nav")
print(pagination)
for page in pagination:
    print(page.find("a"))
# for page in pagination:
#     print(page.find("span"))

# print(articles.find(class_="pagination"))