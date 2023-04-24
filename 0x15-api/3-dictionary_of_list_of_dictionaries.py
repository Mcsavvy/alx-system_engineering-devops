#!/usr/bin/python3

"""
Fetches information about an employee and exports it to a JSON file.

API: https://jsonplaceholder.typicode.com/
"""
import json
import requests
import sys

API = "https://jsonplaceholder.typicode.com"


def main():
    """main function"""
    # get employees details
    response = requests.get(f"{API}/users/")
    if not response.ok:
        return 1
    employees = response.json()

    data = {}

    # get employee todos
    for employee in employees:
        response = requests.get(f"{API}/todos?userId={employee.get('id')}")
        if not response.ok:
            return 2
        employee_todos = response.json()

        # store details in variables
        username = employee.get('username')

        todos = []
        for todo in employee_todos:
            todos.append({
                "username": username,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            })
        data[f"{employee.get('id')}"] = todos
    
    with open(f"todo_all_employees.json", 'w') as json_file:
        json_file.write(json.dumps(data))


if __name__ == "__main__":
    sys.exit(main())
