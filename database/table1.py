#-------------------------------------------------------------------------
# Name:        create_table1
# Purpose:
#
# Author:      zhx
#
# Created:     21/11/2016
# Copyright:   (c) zhx 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------
import MySQLdb


def create_tb1(cursor):
    #cursor.execute("DROP TABLE IF EXISTS table1")
    sql = """CREATE TABLE table1 (
         id char(100) not null,
         en_name char(100) not null,
         cn_name  char(100) not null,
         aliases char(200),
         instance_of char(100),
         subclass_of char(100),
         primary key(id))"""
    cursor.execute(sql)


def insert_into_tb1(db, cursor, values):
    sql = "insert into table1 \
        values('%s' , '%s', '%s','%s' , '%s', '%s')" % \
        values
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        #print values, ' not load success '


def record_num(db, cursor):
    sql = "select count(*)\
           from table1"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        num = row[0]
        print num
