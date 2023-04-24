#!/usr/bin/python3

"""
Fetches information about an employee and exports it to a CSV file.

API: https://jsonplaceholder.typicode.com/
"""
import requests
import sys

API = "https://jsonplaceholder.typicode.com"


def main(employee_id):
    """main function"""
    # get employee details
    response = requests.get(f"{API}/users/{employee_id}")
    if not response.ok:
        return 1
    employee_details = response.json()

    # get employee todos
    response = requests.get(f"{API}/todos?userId={employee_id}")
    if not response.ok:
        return 2
    employee_todos = response.json()

    # store details in variables
    username = employee_details.get('username')

    CSV = ""
    for todo in employee_todos:
        title = todo.get('title')
        status = todo.get('completed')
        CSV += '"{}","{}","{}","{}"\n'.format(
            employee_id, username, status, title
        )

    with open(f"{employee_id}.csv", 'w') as csv_file:
        csv_file.write(CSV)


if __name__ == "__main__":
    employee_id = sys.argv[1]

    sys.exit(main(employee_id))
