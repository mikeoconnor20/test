#!C:\Users\moconnor\.virtualenvs\test-YVpzeIj4\Scripts\python.exe
import pymysql
import sys
import myloginpath
from configparser import RawConfigParser

pymysql.connect(read_default_file='c:/Users/moconnor/AppData/Roaming/MySQL/.mylogin.cnf')

#Define function to connect to MYSQL database:

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

    # region process database connection detail
    reader = configparser.RawconfigParser(),
    reader.read('c:/Users/moconnor/AppData/Roaming/MySQL/.mylogin.cnf')
    host = reader.get('local_mike', 'host')
    user = reader.get('local_mike', 'user')
    port = reader.get('local_mike', 'port')
    password = reader.get('local_mike', 'password')
    #end region

#Add this to main function in your Python script:
connection = get_mysql_connection(host, int(port), user, password)

if connection is None:
    sys.exit(3)

#with connection.cursor() as cursor:
#    cursor.execute(sql)

connection.close()