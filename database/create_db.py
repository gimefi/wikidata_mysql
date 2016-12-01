#-------------------------------------------------------------------------------
# Name:        creat_db
# Purpose:
#
# Author:      zhx
#
# Created:     21/11/2016
# Copyright:   (c) zhx 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import MySQLdb
import QAsystem
import table1
import table2
import index
import csv

def line_to_value(line):
    line = line.strip('\n')
    line = line.split('\t')
    for i in xrange(len(line)):
        if(line[i]=='null' or line[i]=='NULL' or line[i]=='Null'):
            line[i]=None
    line = tuple(line)
    return line


def line_to_entity(line):
    res = [1,2,3,4,5,6]
    res[0] = line['ID']
    res[1] = line['en name']
    res[2] = line['zh-hans name']
    res[3] = line['aliases']
    res[4] = line['instance of']
    res[5] = line['subclass of']
    for r in xrange(6):
        if res[r] =='':
            res[r]=None
    res = tuple(res)
    return res

def line_to_stmt(line):
    res = [1,2,3,4,5]
    res[0] = line['ID']
    res[1] = line['property']
    res[2] = line['value']
    res[3] = line['qualifiers']
    res[4] = line['references']
    for r in xrange(5):
        if res[r] =='':
            res[r]=None
    res = tuple(res)
    return res
#def main():
db = MySQLdb.connect("localhost","root","your_mysql_passwd","your_database")
cursor = db.cursor()
#cursor.execute("DROP TABLE IF EXISTS table2")
#cursor.execute("DROP TABLE IF EXISTS table1")
# create tables
table1.create_tb1(cursor)
table2.create_tb2(cursor)

# insert into tables
if (True):
    total = 0
    file1 = open('entity_table1.csv')
    reader = csv.DictReader(file1)
    for line in reader:
        #print line
        total +=1
        line = line_to_entity(line)
        table1.insert_into_tb1(db,cursor,line)
    table1.record_num(db,cursor)
    print 'total = ',total
    index.creat_index_tb1(db,cursor)
if (True):
    total =0
    file2 = open('statement_table1.csv')
    reader = csv.DictReader(file2)
    for line in reader:
        total+=1
        #print line
        line = line_to_stmt(line)
        table2.insert_into_tb2(db,cursor,line)
    table2.record_num(db,cursor)
    print 'total = ',total


# create index

# query and answer system
#query_name = input('the name you want to query: ')
#QAsystem.name_to_entity(db,cursor,query_name)
#query_id = input('the entity id you input:')
##query_name = 'cHINa'
##query_property = 'area'
###QAsystem.entity_stmt_entity(db,cursor,query_id)
###QAsystem.entity_to_statements(db,cursor,query_id)
##QAsystem.what_is_A_of_B(db,cursor,query_property,query_name)
##db.close()


