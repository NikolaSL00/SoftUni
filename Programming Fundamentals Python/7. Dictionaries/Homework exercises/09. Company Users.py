# Write a program that keeps information about companies and their employees.
# You will be receiving a company name and an employee's id, until you receive the command "End" command. Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# When you finish reading the data, order the companies by the name in ascending order.
# Print the company name and each employee's id in the following format:
# {companyName}
# -- {id1}
# -- {id2}
# -- {idN}
# Input / Constraints
# Until you receive the "End" command, you will be receiving input in the format: "{companyName} -> {employeeId}".
# The input always will be valid.

# INPUT:
# SoftUni -> AA12345
# SoftUni -> BB12345
# Microsoft -> CC12345
# HP -> BB12345
# End

# OUTPUT:
# HP
# -- BB12345
# Microsoft
# -- CC12345
# SoftUni
# -- AA12345
# -- BB12345

# INPUT:
# SoftUni -> AA12345
# SoftUni -> CC12344
# Lenovo -> XX23456
# SoftUni -> AA12345
# Movement -> DD11111
# End

# OUTPUT:
# Lenovo
# -- XX23456
# Movement
# -- DD11111
# SoftUni
# -- AA12345
# -- CC12344

command = input()
dictionary_with_company_users = {}

while command != "End":
    company, employee_id = command.split(" -> ")

    if company not in dictionary_with_company_users.keys():
        dictionary_with_company_users[company] = []
        dictionary_with_company_users[company].append(employee_id)
    else:
        if employee_id not in dictionary_with_company_users[company]:
            dictionary_with_company_users[company].append(employee_id)

    command = input()

for company, employees in sorted(dictionary_with_company_users.items(), key=lambda kvp: kvp[0]):
    print(company)
    for el in employees:
        print(f"-- {el}")
