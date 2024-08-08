#!/usr/bin/python3
import json
import requests
import sys
import traceback

def export_to_json(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()
    
    filename = f"{employee_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(todos, jsonfile)
    print(f"JSON file '{filename}' created.")

if __name__ == "__main__":
    try:
        employee_id = sys.argv[1]
        export_to_json(employee_id)
    except Exception as e:
        print(f"Error occurred: {str(e)}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)

