#-------------------------------------------------------------------------------
# Name:        table2 = statements
# Purpose:
#
# Author:      zhx
#
# Created:     22/11/2016
# Copyright:   (c) zhx 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def create_tb2(cursor):
    #cursor.execute("DROP TABLE IF EXISTS table2")
    sql = """create table table2(
	id char(100) not null,
	property char(100) not null,
	value char(100) not null,
	qualifier char(200),
	reference char(200),
	primary key(id,property,value,qualifier),
	foreign key(id) references table1(id)
	)"""
    cursor.execute(sql)

def insert_into_tb2(db,cursor,values ):
    sql ="insert into table2 \
        values('%s' , '%s', '%s', '%s', '%s')" % \
        values
    try:
        #print 'insert'
        cursor.execute(sql)
        #print values
        db.commit()
    except:
        db.rollback()
        #print 'not load success '

def record_num(db,cursor):
    sql = "select count(*)\
           from table2"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        num = row[0]
        print num