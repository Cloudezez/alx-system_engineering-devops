#!/usr/bin/python3
"""
A script that gathers data from a REST API for a given employee ID and exports
the TODO list progress for that employee to a JSON file.
"""

import json
import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
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
    employee_name = user.get('username', 'Unknown')

    # Fetch TODO list data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Failed to fetch TODO list.")
        return
    todos = todos_response.json()

    # Filter tasks for the given employee ID
    employee_tasks = [task for task in todos if task.get('userId') == employee_id]

    # Prepare the data for JSON export
    tasks_list = []
    for task in employee_tasks:
        task_info = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        }
        tasks_list.append(task_info)

    data = {str(employee_id): tasks_list}

    # JSON filename
    filename = '{}.json'.format(employee_id)

    # Write to JSON file
    with open(filename, mode='w') as jsonfile:
        json.dump(data, jsonfile)

if __name__ == "__main__":
    main()

