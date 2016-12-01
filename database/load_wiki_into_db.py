#-------------------------------------------------------------------------------
# Name:  load_wiki_into_mysql
# Purpose:
#
# Author:      zhx
#
# Created:     21/11/2016
# Copyright:   (c) zhx 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import MySQLdb

db = MySQLdb.connect("localhost","root","zhxsql2016","lesson")
cursor =db.cursor()
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)

db.close()

def load_into_db(db_name,table_name,values):
    db=MySQLdb.connect("localhost","root","zhxsql2016",db_name)
    cursor = db.cursor()
