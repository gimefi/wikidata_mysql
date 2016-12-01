
import csv
csvfile = open('statement_table1.csv')

reader = csv.DictReader(csvfile)
# file1.readline()
i = 1
for line in reader:
    i += 1
    if i == 10:
        break
    print line
    print '|||||||||||||||||||||\n'
