#!C:\Users\moconnor\.virtualenvs\test-YVpzeIj4\Scripts\python.exe

import mysql.connector
def connection():
    conn = mysql.connector.connect(host = "localhost",
                  user = 'root',
                  password = 'Deca2121',
                  database = 'login_page',
                  auth_plugin='mysql_native_password')

    c = conn.cursor()
    return c , conn