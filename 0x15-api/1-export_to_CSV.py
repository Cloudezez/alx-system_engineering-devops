#!/usr/bin/python3
import csv
import requests
import sys
import traceback

def export_to_csv(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()
    
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'ID', 'TITLE', 'COMPLETED']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for todo in todos:
            writer.writerow({
                'USER_ID': todo['userId'],
                'ID': todo['id'],
                'TITLE': todo['title'],
                'COMPLETED': todo['completed']
            })
    print(f"CSV file '{filename}' created.")

if __name__ == "__main__":
    try:
        employee_id = sys.argv[1]
        export_to_csv(employee_id)
    except Exception as e:
        print(f"Error occurred: {str(e)}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)

