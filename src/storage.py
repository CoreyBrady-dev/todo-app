import json
import os

#loads tasks from JSON file
def load_tasks():
    file_path = os.path.join('data', 'data.json')

    if not os.path.exists(file_path):
        return []
    
    try:
        with open(file_path, 'r') as file:
            tasks = json.load(file)
            return tasks
    except (json.JSONDecodeError, FileNotFoundError):
        return []

#save data to JSON file
def save_tasks(tasks):
    pass
