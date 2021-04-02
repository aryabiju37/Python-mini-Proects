import sqlite3

conn = sqlite3.connect("my_friends.db")
c=conn.cursor()
# c.execute("SELECT * FROM Friends")
# for data in c:
#     print(data)
#fetch all results in a list:
# print(c.fetchall())

#Fetch one result:
# c.execute("SELECT * FROM Friends WHERE first_name IS 'Angela'")
# print(c.fetchone())

c.execute("SELECT * FROM Friends WHERE Closeness > 5 ORDER BY Closeness")
print(c.fetchall())

c.close()