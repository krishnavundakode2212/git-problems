import xml

highest_salary = 0
employee = "  "

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader 1 :
        salary = int(row["Salary"])
        if salary > highest_salary:
            highest_salary = salary
            employee = row["Name"]
            date=new[DDMMYYYY]

print(f"Highest Salary: {employee} - {highest_salary}") saikrishna harekrishna hare

