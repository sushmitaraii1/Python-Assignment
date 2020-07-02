# 14. Write a function that reads a CSV file. It should return a list of dictionaries, using the first row as key
# names, and each subsequent row as values for those keys. For the data in the previous example it would return: [{
# 'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name': 'John', 'address': '54 Love Ave', 'age': 21}]
import csv

with open('file.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    list_of_dict = []
    for row in reader:
        list_of_dict.append(dict(row))
    print(list_of_dict)