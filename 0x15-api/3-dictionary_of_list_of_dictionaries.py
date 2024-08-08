import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    # Fetch user data
    user = requests.get(user_url).json()
    username = user.get("username")

    # Fetch tasks data
    todos = requests.get(todos_url).json()

    # Prepare the list of dictionaries
    tasks = [{"task": todo.get("title"),
              "completed": todo.get("completed"),
              "username": username} for todo in todos]

    # Wrap the list in a dictionary with the user_id as the key
    data = {user_id: tasks}

    # Export the data to a JSON file
    filename = f"{user_id}.json"
    with open(filename, mode='w') as file:
        json.dump(data, file)

