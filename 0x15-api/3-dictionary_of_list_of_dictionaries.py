#!/usr/bin/pthon3
import json

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None

def main():
    data = load_data('data.json')
    if data is not None:
        print(json.dumps(data, indent=4))  # Format JSON with an indentation of 4 spaces

if __name__ == "__main__":
    main()

