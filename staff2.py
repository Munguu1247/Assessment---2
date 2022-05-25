import csv
file = open("employees.csv", 'r')
try:
    csv_reader = csv.reader(file)
    min_salary = 0
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(row[2])
        else:
            if row[2] >=0:
                min_salary -= int(row[2])
        line_count += 1
    print("The average salary of managers is "+ str(min_salary) + " dollars.")
finally:
    file.close()



