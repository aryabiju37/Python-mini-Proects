import sqlite3
conn = sqlite3.connect("users.db")
u = input("Insert user name..")
p = input("Insert password..")
query="SELECT * FROM users WHERE user_name=? AND passwors=?"
c = conn.cursor()
c.execute(query,(u,p))
result = c.fetchone()
if result:
    print(f"welcome back ! {u}")
else:
    print("Incorrect Credentials!")