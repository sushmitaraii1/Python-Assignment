# 13. Write a function to write a comma-separated value (CSV) file. It should accept a filename and a list of tuples
# as parameters. The tuples should have a name, address, and age. The file should create a header row followed by a
# row for each tuple. If the following list of tuples was passed in: [('George', '4312 Abbey Road', 22), ('John',
# '54 Love Ave', 21)]
# it should write the following in the file:
# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21

import csv

data = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]

with open('file.csv', 'w') as file:
    csv_out = csv.writer(file)
    csv_out.writerow(['name', 'address', 'age'])
    for row in data:
        csv_out.writerow(row)

with open('file.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)