#!/usr/bin/python3
"""
A script that gathers data from a REST API for a given employee ID and exports
the TODO list progress for that employee to a CSV file.
"""

import csv
import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
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

    # CSV filename
    filename = '{}.csv'.format(employee_id)

    # Write to CSV file
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in employee_tasks:
            writer.writerow([employee_id, employee_name, task.get('completed'), task.get('title')])

if __name__ == "__main__":
    main()

