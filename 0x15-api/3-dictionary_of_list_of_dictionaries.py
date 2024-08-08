#!/usr/bin/python3
import json
import requests
import sys
import traceback

def dictionary_of_list_of_dictionaries():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()
    
    user_dict = {}
    for user in users:
        user_dict[user['id']] = {
            'name': user['name'],
            'username': user['username'],
            'email': user['email']
        }
    
    filename = "user_data.json"
    with open(filename, 'w') as jsonfile:
        json.dump(user_dict, jsonfile)
    print(f"Dictionary of lists of dictionaries file '{filename}' created.")

if __name__ == "__main__":
    try:
        dictionary_of_list_of_dictionaries()
    except Exception as e:
        print(f"Error occurred: {str(e)}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)

