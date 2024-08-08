#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to your Flask server running on your local machine!"

if __name__ == "__main__":
    # Run the Flask server on port 5000, accessible on the local machine
    app.run(host="0.0.0.0", port=5000, debug=True)

