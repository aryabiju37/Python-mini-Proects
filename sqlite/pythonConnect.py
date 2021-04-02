import sqlite3

conn = sqlite3.connect("my_friends.db") 
#connect the cursor to the 
c = conn.cursor()
# c.execute("CREATE TABLE Friends (first_name TEXT,last_name TEXT,closeness INTEGER)")
# insert_query = '''INSERT INTO friends(first_name,last_name,closeness)
#                     VALUES ("Balamurali","Krishnan",9)'''


#insert from csv and all
# data = ("Monty","Python",10)
# query = '''INSERT INTO friends VALUES(?,?,?)'''
# c.execute(query,data)
#Bulk Insert
people=[
    ("Jake","Peralta",4),
    ("John","Blasphemy",3),
    ("Joseph","Gordon-lewitt",8),
    ("Angela","Merkel",10),
    ("Angela","The Cat",0)
]
# c.executemany("INSERT INTO Friends VALUES(?,?,?)",people)

#if you want to do something with the tabular data during insert, do this:
sum_close=0
for person in people:
    c.execute("INSERT INTO Friends VALUES(?,?,?)",person)
    sum_close += person[2]
    average = sum_close/len(people)
print(f"average closeness: {average}")

conn.commit()
conn.close()