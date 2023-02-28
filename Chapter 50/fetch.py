import sqlite3
connection=sqlite3.connect('Chapter 50/accounting.db')
crsr= connection.cursor()
crsr.execute("SELECT * FROM employee")

data= crsr.fetchall()
print(data)