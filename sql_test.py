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


if connection is None:
    sys.exit(3)

sql = "SELECT database();"

with connection.cursor() as cursor:
    cursor.execute(sql)

    data = cursor.fetchone()
    print ("Database version : %s " % data)

connection.close()