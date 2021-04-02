# https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
from csv import  writer

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text,"html.parser")
#html - article tag
#<article id="blig-post">..</article>
articles = soup.find_all("article")
with open("ScrapedBlog.csv","w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Title","Title URL","Date"])
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        title_url = a_tag["href"]
        date = article.find("time")["datetime"]
        csv_writer.writerow([title,title_url,date])


    
    


