#!C:\Users\moconnor\.virtualenvs\test-YVpzeIj4\Scripts\python.exe

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","Deca2121","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create user
sql = """CREATE USER 'mike'@'localhost'
  IDENTIFIED BY 'password';
GRANT ALL
  ON *.*
  TO 'mike'@'localhost'
  WITH GRANT OPTION;"""

cursor.execute(sql)

# disconnect from server
db.close()