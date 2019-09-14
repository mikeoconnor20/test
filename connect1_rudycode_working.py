#!C:\Users\moconnor\.virtualenvs\test-YVpzeIj4\Scripts\python.exe
import pymysql
import sys

def get_mysql_connection(host, port, user, password, db):
    try:
        connection = pymysql.connect(host=host,
                                     port=port,
                                     user=user,
                                     password=password,
                                     db=db,
                                     charset='utf8mb4')

        return connection
    except pymysql.err.OperationalError as e:
        print(str(e), file=sys.stderr)
        return
#Add this to main function in your Python script:
connection = get_mysql_connection('localhost', 3306, 'mike', 'Deca2121', 'testdb')

# prepare a cursor object using cursor() method
cursor = connection.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT database()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database : %s " % data)

if connection is None:
    sys.exit(3)

connection.close()