# Assessment 2
# Programming solution: solve a real-life scenario using coding knowledge and skills

def greeting(title, name):
    print(f"Hello,", title, name)

greeting("Mr", "Binayak")


def my(part, first_name, last_name, student_id):
    print(" This is ", part, '\n',
          "Student name: ", first_name, last_name,
          '\n',"Student ID: ", student_id)

my("Assessment 2", "Mungunchimeg", "Batbayar", "s4662982")


# 1. The average salary of staff whose employees types is "Manager"
# Install the package (import csv)
import csv
file = open("employees.csv", 'r')
try:
    csv_reader = csv.reader(file)
    average_salary = 0
    for row in csv_reader:
        if row[3] == "Manager":
            print(row)

finally:
   file.close()







