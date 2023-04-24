#!/usr/bin/python3

"""
Fetches and displays information about an employee

API: https://jsonplaceholder.typicode.com/
"""

API = "https://jsonplaceholder.typicode.com"


def main(employee_id):
    """main function"""
    import requests

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
    name = employee_details['name']
    num_of_todos = len(employee_todos)
    completed_todos = tuple(
            todo for todo in employee_todos if todo['completed'])

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(completed_todos), num_of_todos
    ))
    for todo in completed_todos:
        print(f"\t {todo['title']}")


if __name__ == "__main__":
    import sys

    employee_id = int(sys.argv[1])

    sys.exit(main(employee_id))
