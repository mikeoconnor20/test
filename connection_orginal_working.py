#!C:\Users\moconnor\.virtualenvs\test-YVpzeIj4\Scripts\python.exe

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","Deca2121","TESTDB" )


# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT database()")


# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()
