import sqlite3 as sql

con = sql.connect("database.db")
cur = con.cursor()

adminUsername = "admin"
adminPassword = "sup3r_s3cret_p@@sw0rd"

cur.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username varchar(20) NOT NULL, password varchar(100) NOT NULL)''')
cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (adminUsername,adminPassword))
con.commit()
con.close()
