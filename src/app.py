from flask import Flask, render_template, request, redirect, url_for
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "..", "data", "tasks.json")
app = Flask(__name__, static_folder='static', template_folder='templates')

app = Flask(__name__)

tasks = []

# create tasks
@app.route("/", methods=["GET", "POST"])
def home():
    tasks = load_tasks()

    if request.method == "POST":
        title = request.form.get("title")
        priority = request.form.get("priority")
        description = request.form.get("description")

        if title and priority and description:
            tasks.append({"title": title, "priority": priority, "description": description})
            save_tasks(tasks)
        return redirect(url_for("home"))
    
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    tasks.sort(key=lambda task: priority_order.get(task["priority"], 4))

    return render_template("index.html", tasks=tasks)

# utility functions
def load_tasks():
    try:
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open(JSON_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# delete tasks
@app.route("/delete/<int:index>")
def delete_task(index):
    tasks = load_tasks()        
    if 0 <= index < len(tasks): 
        tasks.pop(index)        
        save_tasks(tasks)       
    return redirect(url_for("home"))  
