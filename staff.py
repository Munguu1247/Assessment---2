# Assessment 2
# Programming solution: solve a real-life scenario using coding knowledge and skills

def greeting(title, name):
    print(f"Hello,", title, name)

greeting("Mr", "Binayak")
print(" ")


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
    person_with_min_salary = []

    for row in csv_reader:

        if line_count == 0:

            print()

        elif line_count == 1:
            min_salary = int(row[2])
            person_with_min_salary = (row[0], row[1])
            if row[3] == "Manager":
                total_salary += int(row[2])

        else:

            if min_salary > int(row[2]):
                min_salary = int(row[2])

                person_with_min_salary = (row[0], row[1])

            if row[3] == "Manager":
                total_salary += int(row[2])
        line_count += 1


    print(f'The average salary of managers is {int(total_salary / len(row)):>5,d} dollars.')

    print(f"{' '.join(person_with_min_salary)} has the lowest salary $({format(float(min_salary), '.2f')}).")

finally:
    file.close()


