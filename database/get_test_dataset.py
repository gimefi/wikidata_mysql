import csv
import MySQLdb


def main():

	db = MySQLdb.connect("localhost","root","mysql","wikitest")
	cursor = db.cursor()
	sql = "select DISTINCT property\
	from table2"
	cursor.execute(sql)
	result = cursor.fetchall()
	test_dateset = file('test_dataset.csv','wb')
	writer = csv.writer(test_dateset)
	writer.writerow(['property'])
	for row in result:
		tmp =[]
		tmp.append(row[0])
		writer.writerow(tmp)
	test_dateset.close()

#main()