#!/usr/bin/python3
from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/run_script/<script_name>', methods=['GET'])
def run_script(script_name):
    script_path = os.path.join(os.path.dirname(__file__), f"{script_name}.py")
    args = request.args.getlist('args')
    
    print(f"Running script: {script_path} with arguments: {args}")
    
    try:
        result = subprocess.run(
            ["python3", script_path] + args, 
            capture_output=True, text=True, check=True
        )
        output = result.stdout
        errors = result.stderr
        if output:
            print(f"Output of {script_name}: {output}")
        if errors:
            print(f"Errors of {script_name}: {errors}")
        return jsonify({"output": output, "errors": errors}), 200
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running script {script_name}: {str(e)}")
        return jsonify({"error": str(e), "output": e.output, "errors": e.stderr}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

