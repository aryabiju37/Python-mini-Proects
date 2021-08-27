import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT exists store(item TEXT,quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()

def insert_table(item,qty,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,qty,price))
    conn.commit()
    conn.close()

# insert_table("Wine Glass",8,24.5)
# insert_table("Water Bottle",9,10.5)
# insert_table("Books",10,2)
# insert_table("Birds",2,35)
# insert_table("Dogs",1,250)

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def update(price,qty,item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET price = ?,quantity=? WHERE item = ?",(price,qty,item))
    conn.commit()
    conn.close()

update(23,12,"Water Bottle")

