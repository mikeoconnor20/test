#!C:\Users\moconnor\.virtualenvs\test-YVpzeIj4\Scripts\python.exe

import pymysql

#try:
#	print("Content-type: text/html\n")
#	print("<html><head>")
#	print("<body>")
#	print("<h1>connencting to mysql</h1>")
#conn = pymysql.connect(user="mikeo", passwd="Deca2121")
#	cur = con.cursor()
#	print("<h2>connection succeeded</h2>")
#	print("</body></html>")
#except:
#	print("oops.. there is an error, connection failed")
#mydb = mysql.connector.connect(host="localhost", user="root",passwd="Deca2121")

# Open database connection
db = pymysql.connect("localhost","mikeo","Deca2121","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()