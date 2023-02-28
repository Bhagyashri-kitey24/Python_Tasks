# SQL using python SQLITE3
import sqlite3
connection=sqlite3.connect('Chapter 50/accounting.db')
crsr= connection.cursor()
sql_command=""" 
Creat TABLE employee(
    id INTEGER PRIMARY KEY,
    f_name VARCHAR (20)
    l_name VARCHAR (20)
    gender CHAR(1)
    joining_date DATE
)
"""
crsr.execute(sql_command)

sql_command=""" 
    INSERT INTO employee VALUE (01,"anayka","gupta","F",02/5/2001)
"""
crsr.execute(sql_command)

sql_command=""" 
    INSERT INTO employee VALUE (02,"anaya","vanjare","F",02/8/2002)
"""
crsr.execute(sql_command)

sql_command=""" 
    INSERT INTO employee VALUE (03,"Arohi","sharma","F",08/5/2000)
"""
crsr.execute(sql_command)

sql_command=""" 
    INSERT INTO employee VALUE (04,"nayan","mishra","M",08/5/2001)
"""
crsr.execute(sql_command)

sql_command=""" 
    INSERT INTO employee VALUE (05,"Ram","Bhagat","M",11/7/2001)
"""
crsr.execute(sql_command)

sql_command=""" 
    INSERT INTO employee VALUE (06,"Tejas","Birla","M",12/12/2000)
"""
crsr.execute(sql_command)

#saving changes using commit() method
connection.commit()

#closing the connection
connection.close()


