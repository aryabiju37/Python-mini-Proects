import sqlite3
import requests
from bs4 import BeautifulSoup
def scrape_books(url):
    #Request URL
    response = requests.get(url)
    #Initialize BS
    #Extract the data we want
    soup=BeautifulSoup(response.text,"html.parser")
    books = soup.find_all("article")
    all_books=[]
    for book in books:
        book_data=(get_title(book),get_price(book),get_rating(book))
        all_books.append(book_data)       
        
    save_books(all_books)     
    
#Save the data to the DB
def save_books(all_books):
    conn = sqlite3.Connection("books.db")
    c = conn.cursor()
    # c.execute('''CREATE TABLE Books
    #         (Title TEXT,Price REAL,Rating INTEGER)''')
    c.executemany("INSERT INTO Books VALUES(?,?,?)",all_books)
    # c.execute('Select * from Books')
    conn.commit()
    conn.close()
   

def get_title(book):
    return book.find("h3").find("a")["title"]

def get_price(book):
    signed_price=book.select(".price_color")[0].get_text()
    return float(signed_price.replace("Â","").replace("£",""))

def get_rating(book):
    ratings = {"One":1,
                "Two":2,
                "Three":3,
                "Four":4,
                "Five":5
            }
    paragraph = book.select(".star-rating")[0]
    rating = paragraph.get_attribute_list("class")[-1]
    return ratings[rating]

print(scrape_books("http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"))

    





