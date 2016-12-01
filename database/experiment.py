import MySQLdb
import csv
import time
import datetime

def line_to_pty(line):
    res = [1,]
    res[0] = line['property']
    for r in xrange(1):
        if res[r] == '':
           res[r]=None
    res = tuple(res)
    return res

def test(db,cursor,property):
    sql = "select  max(value)\
            from table2 \
            group by property\
            having property = '%s'" % \
        	(property)
    cursor.execute(sql)

def main():
	db = MySQLdb.connect("localhost","root","mysql","wikitest")
	cursor = db.cursor()
	file = open('test_dataset.csv')
	reader = csv.DictReader(file)
	st = datetime.datetime.now()
	for line in reader:
        #print line
		line = line_to_pty(line)
		test(db,cursor,line)
	ed = datetime.datetime.now()
	print 'index:on, time = ',(ed-st)

main()


