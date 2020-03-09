"""import csv

hosts = [["workstation.local", "192.168.1.1"], ["webserver.cloud", "192.168.0.1"]]

with open("example.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
"""

"""

import os
import csv

# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename, "r") as flower_csv:
    # Read the rows of the file
        flower_csv.readline()
        rows = csv.reader(flower_csv)

    # Process each row
        for row in rows:
            name, color, type = row
        # Format the return string for data rows only

            return_string += "a {} {} is {}\n".format(color, name, type)
    return return_string

#Call the function
print(contents_of_file("flowers.csv"))

"""


import csv

def read_employees(csv_file_location):
    """
    Args:
        csv_file_location:
    """
    employee_list = []
    empDialect = csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_csv = csv.DictReader(open(csv_file_location), dialect='empDialect')

    for data in employee_csv:
        employee_list.append(data)

    return employee_list

def process_data(employee_list):
    """
    Args:
        employee_list:
    """
    department_list = []
    department_data = {}
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)

    return department_data

def write_report(dictionary, report_file):
    """
    Args:
        dictionary:
        report_file:
    """
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()


employee_list = read_employees("employee.csv")
write_report(process_data(employee_list), 'report.txt')




