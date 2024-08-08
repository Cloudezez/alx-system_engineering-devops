#!/usr/bin/python3
"""
A script that gathers data from a REST API for a given employee ID and displays
the TODO list progress for that employee.
"""

import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        return

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        return

    # API URLs
    users_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    # Fetch user data
    user_response = requests.get(users_url)
    if user_response.status_code != 200:
        print("User not found.")
        return
    user = user_response.json()
    employee_name = user.get('name', 'Unknown')

    # Fetch TODO list data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Failed to fetch TODO list.")
        return
    todos = todos_response.json()

    # Filter tasks for the given employee ID
    employee_tasks = [task for task in todos if task.get('userId') == employee_id]

    total_tasks = len(employee_tasks)
    done_tasks = sum(1 for task in employee_tasks if task.get('completed'))

    # Display the result
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in employee_tasks:
        if task.get('completed'):
            print(f"\t {task.get('title')}")

if __name__ == "__main__":
    main()

