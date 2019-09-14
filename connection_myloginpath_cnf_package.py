#!C:\Users\moconnor\.virtualenvs\test-YVpzeIj4\Scripts\python.exe

import pymysql
import sys
import configparser
import myloginpath
from configparser import RawConfigParser
from os import getenv


conf = myloginpath.parse('client')

print(**conf)

#_____________________________________________________________________________________
db = pymysql.connect(**conf, host='localhost', db='testdb')
#--------------

#--------------
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT database()")


# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database: %s " % data)

# disconnect from server
db.close()