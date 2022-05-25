# Assessment 2
# Programming solution: solve a real-life scenario using coding knowledge and skills

def greeting(title, name):
    print(f"Hello,", title, name)

greeting("Mr", "Binayak")


def my(part, first_name, last_name, student_id):
    print(" This is ", part, '\n',
          "Student name:", first_name, last_name,
          '\n',"Student ID:", student_id)

my("Assessment 2", "Mungunchimeg", "Batbayar", "s4662982")


# 1. The average salary of staff whose employees types is "Manager"
# 2. The full name of the staff member who has the lowest salary
# Install the package (import csv)
import csv
file = open("employees.csv", 'r')
try:
    csv_reader = csv.reader(file)
    total_salary = 0
    line_count = 0
    min_salary = 0

    for row in csv_reader:
        if line_count == 0:
            print()
        else:
            if row[3] == "Manager":
                total_salary += int(row[2])
        line_count += 1
    print("The average salary of managers is "+ str(int(total_salary/len(row))) + " dollars.")

    if row in csv_reader:
        min_salary = min(row)
    print("The lowest salary is ", min_salary)

finally:
    file.close()



