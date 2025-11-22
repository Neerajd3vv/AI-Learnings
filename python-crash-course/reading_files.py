

employee_file = open("employees.txt", "r")


print(employee_file.readable()) # check if file is readable
# print(employee_file.read()) # read entire file

# print(employee_file.readline())  # read first line
# print(employee_file.readline())  # read second line

# print(employee_file.readlines()[0])  # readlines returns a list of lines

for employee in employee_file.readlines():
    print(employee)

employee_file.close()  # close the file
