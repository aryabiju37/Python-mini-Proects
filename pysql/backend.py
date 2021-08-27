import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE book(id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor() 
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    # print("chck insert")
    conn.commit()
    conn.close()
# insert(" P vs NP review","Scott Aaronson",1988,904250952489)
# insert(" The Algorithm Design","Steven Skiena",1932,234252392489)
# insert(" Grokking algorithms","Dick Anderson",2003,320328952489)
# insert(" Engineering a Compiler 2nd Ed","Cooper & Torczon ",1923,2389023432)
# insert(" Introduction to the Theory of Computation","Michael Sipser ",1938,1209324439)
# insert(" C# in depth","John Skeet",2005,8327983202)

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor() 
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author =? OR year=? or isbn=? ",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET  title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

# insert("Machine Learning","Bishop",1998,1923832898398))

# update(8,"Machine Learning a Probablistic Perspective","Murphy",2003,23987896398)
# print(view())    