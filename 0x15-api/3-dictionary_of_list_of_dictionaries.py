import json
import requests

def fetch_data():
    # URL to fetch data (example URL, adjust if needed)
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    return response.json()

def transform_data(data):
    transformed = []
    for item in data:
        transformed_item = {
            'id': item.get('id', 'N/A'),
            'username': item.get('username', 'N/A'),  # Use .get() to avoid KeyError
            'email': item.get('email', 'N/A'),
            'address': item.get('address', 'N/A'),
            'phone': item.get('phone', 'N/A')
        }
        transformed.append(transformed_item)
    return transformed


def main():
    data = fetch_data()
    transformed_data = transform_data(data)
    
    with open('todo_all_employees.json', 'w') as file:
        json.dump(transformed_data, file, indent=4)
    
    print("Data exported to todo_all_employees.json")

if __name__ == "__main__":
    main()

