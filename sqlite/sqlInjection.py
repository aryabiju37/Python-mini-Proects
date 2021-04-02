import sqlite3

conn = sqlite3.connect("users.db")

# users_lst=[
#     ("Colty","punmaster101"),
#     ("Manu","manusree"),
#     ("Jacky","kennedy")
# ]
# c = conn.cursor()
# c.executemany("INSERT INTO users Values(?,?)",users_lst)
# c.execute("INSERT into users(user_name,passwors) values('Blie','meow')")
u = input("Insert User Name:")
p=input("Insert pwd:")
query=f"SELECT * FROM users WHERE user_name='{u}' AND passwors='{p}'"
c = conn.cursor()
result=c.execute(query)
if result:
    print(f"Welcome back {u}")
else:
    print("Incorrect User Name and Password")
conn.commit()
conn.close()

#in input password put in ' or 1==1 --