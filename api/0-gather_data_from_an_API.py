#!/usr/bin/python3
"""Script for fetching and showing Employee progress using his employee ID"""

import requests
import sys

"""1. get employee todo progress from API for the employee ID"""
def get_employee_progress(employee_id):
    url = "https://jsonplaceholder.typicode.com"

    usr = requests.get(f"{url}/users/{employee_id}").json()
    todo = requests.get(f"{url}/users/{employee_id}/todos").json()

    completed = [i for i in todo if i["completed"]]
    total = len(todo)
    done = len(completed)

    print(f"Employee {usr['name']} is done with ({done}/{total}) ")
    for task in completed:
        print(f"\t {task['title']}")

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Usage: 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        """gets user through integer specifiying in the function-runner under the function runner"""
        employee_id = int(sys.argv[1])
        get_employee_progress(employee_id)

    except  ValueError:
        print("Error not employee id use an integer")
        sys.exit(1)


