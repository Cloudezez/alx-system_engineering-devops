#!/usr/bin/python3
"""
This script gathers data from a REST API and displays
the TODO list progress for a given employee ID.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if an employee ID was passed as an argument
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetch employee data
    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user = requests.get(url_user).json()

    # Fetch employee's TODO list
    url_todos = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos = requests.get(url_todos).json()

    # Calculate completed tasks
    completed_tasks = [task['title'] for task in todos if task['completed']]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    # Print the result
    print(f"Employee {user.get('name')} is done with tasks({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

