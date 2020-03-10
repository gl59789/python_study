#!/usr/bin/env python3
import csv
import datetime
import requests

FILE_URL="http://marga.com.ar/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)


def get_file_sorted_contents(url, start_date):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)

    # Decode all lines into strings
    lines = []
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))

    reader = csv.reader(lines[1:])

    list_row = []
    for row in reader:
        list_row.append(row)

    new_list = sorted(list_row, key=lambda x: x[3])
    index = 0

    for item in new_list:
        item_date = datetime.datetime.strptime(item[3], '%Y-%m-%d')
        if item_date <= start_date:
            index = index + 1
        if item_date > start_date:
            break

    return new_list[index:]



def list_newer(final_list):
    for item in final_list:
        start_date, employees_firstname, employees_lastname = item[3], item[1], item[0]
        print("Started on {}: {} {}".format(start_date, employees_firstname, employees_lastname))


def main():
    start_date = get_start_date()
    sorted_list = get_file_sorted_contents(FILE_URL, start_date)
    list_newer(sorted_list)


if __name__ == "__main__":
    main()