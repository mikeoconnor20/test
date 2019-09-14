#!C:\Users\moconnor\.virtualenvs\test-YVpzeIj4\Scripts\python.exe
import pymysql
import sys

def get_mysql_connection(read_default_file):
    try:
        connection = pymysql.connect(read_default_file="~/my.cnf")

        return connection
    except pymysql.err.OperationalError as e:
        print(str(e), file=sys.stderr)
        return
#Add this to main function in your Python script:
connection = get_mysql_connection('--login-path=local_mike')

# prepare a cursor object using cursor() method
cursor = connection.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT database()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

if connection is None:
	sys.exit(3)

connection.close()

