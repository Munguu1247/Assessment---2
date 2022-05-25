import csv
file = open("employees.csv", 'r')
try:
    csv_reader = csv.reader(file)
    for row in csv_reader:


finally:
    file.close()




