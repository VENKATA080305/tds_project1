'''

import os
import requests
from flask import Flask, jsonify, request
from src.file_handler import read_file as file_reader
from src.task_executor import execute_task as task_runner

app = Flask(__name__)

# Fetch the AIPROXY_TOKEN from environment variables
AIPROXY_TOKEN = os.environ.get("AIPROXY_TOKEN")
if not AIPROXY_TOKEN:
    print("Error: AIPROXY_TOKEN not found.")
    exit(1)  # Exit if the token is missing


@app.post("/run")
def run_task():
    task = request.args.get("task")  # Extract 'task' from query params
    if not task:
        return jsonify({"status": "error", "result": "Task description required"}), 400

    try:
        result = task_runner(task)  # Use task_executor to process the task
        return jsonify({"status": "success", "result": result}), 200
    except ValueError as ve:
        return jsonify({"status": "error", "result": str(ve)}), 400
    except Exception as e:
        return jsonify({"status": "error", "result": str(e)}), 500


@app.get("/read")
def read_file():
    path = request.args.get("path")  # Extract 'path' from query params
    if not path:
        return jsonify({"status": "error", "result": "File path required"}), 400

    try:
        content = file_reader(path)  # Use file_handler to read the file
        return jsonify({"status": "success", "result": content}), 200
    except FileNotFoundError:
        return jsonify({"status": "error", "result": "File not found"}), 404
    except Exception as e:
        return jsonify({"status": "error", "result": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
'''